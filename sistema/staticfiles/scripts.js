const toggleFormVisibility = () => {
    const formContainer = document.querySelector('#section-form');
    const tableContainer = document.querySelector('#section-table');
    formContainer.classList.remove('hidden'); 
    tableContainer.classList.add('hidden');
}

const checkFormVisibilityByParams = () => {
    const urlObject = window.location.search
    const urlParams = new URLSearchParams(urlObject);
    const formState = urlParams.get('form_state');

    if (formState === 'open') {
        return true;
    }
    return false;
};
const checkDeletedEntryByParams = () => {
    const urlObject = window.location.search
    const urlParams = new URLSearchParams(urlObject);
    const formState = urlParams.get('deleted_entry');

    if (formState === 'success') {
        return true;
    }
    return false;
};

const editEntry = (id) => {
    let url = window.location.href; 
    url = url + id;
    window.location.replace(url); 
};
const deleteEntry = (id) => {
    Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, elíminalo!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "¡Eliminado!",
                text: "Tu registro ha sido eliminado",
                icon: "success"
            });
            let parts = window.location.href.toString().split("/"); 
            let tableName = parts[parts.length - 2];  
            let url = `/${tableName}/${id}`;  
            let csrfToken = document.querySelector('#csrf_token').innerHTML; 
            
            
            fetch(url, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrfToken
                }
            }).then(response => {
                if (response.ok) {
                    if (!isNaN(window.location.href.split('/').slice(-1)[0])) {
                        window.location.href = window.location.href.split('/').slice(0,-1).join('/');
                    } else {
                        document.getElementById(`entry-${id}`).remove();  
                    }
                    
                } else {
                    Swal.fire({
                        title: "Error",
                        text: "Hubo un problema al eliminar el registro",
                        icon: "error"
                    });
                }
                
            });
        }
    });
};

function setFormParams() {
    let url = new URL(window.location.href);
    if (!url.searchParams.has('form_state')) {
        url.searchParams.set('form_state', 'open');
        window.location.href = url.href;
    }
}

function removeFormParams() {
    let url = new URL(window.location.href);
    if (url.searchParams.has('form_state')) {
        url.searchParams.delete('form_state');
        window.location.href = url.href;
    }
}


function toggleEditMode() {
    const fields = document.querySelectorAll('input, select, textarea');
    const saveButton = document.getElementById('save-button');
    const cancelButton = document.getElementById('cancel-button');
    const editButton = document.getElementById('edit-button');
    fields.forEach(field => {
        field.disabled = !field.disabled;
    });
    saveButton.classList.toggle('hidden');
    cancelButton.classList.toggle('hidden');
    editButton.classList.toggle('hidden');

    document.querySelectorAll('.modal-openner').forEach(element => {
        element.classList.toggle('hidden');
    })
}

class ManyToManyField {
    constructor(fieldId) {
        this.chipsSectionId = fieldId+"-field";
        this.fieldId = fieldId;
        this.selectedElementsList = [];
        this.availableElementsList = [];
        let fieldElement = document.querySelector(`#${fieldId}`);

        if (fieldElement.value && fieldElement.value != "") {
            for (let entry of fieldElement.value.split(',')) {
                this.selectElement(entry);
            }
            fieldElement.value = '';
        }
        this.datalistId = fieldElement.parentElement.querySelector('datalist').id;

        fieldElement.insertAdjacentHTML('afterend', `
            <div class="flex flex-row flex-wrap items-center" id="${this.chipsSectionId}"></div>
        `);
        let fieldSection = document.createElement('div');
        fieldSection.className = "flex flex-row items-center";
        let fieldElementClone = fieldElement.cloneNode(true);
        fieldSection.appendChild(fieldElementClone);
        fieldElement.insertAdjacentElement('beforebegin', fieldSection);
        fieldElement.remove();

        document.querySelector(`#${this.chipsSectionId}`).insertAdjacentHTML('afterend', `
            <input type="text" id="values-${this.chipsSectionId}" name="${fieldId}" value="" hidden> 
        `);

        this.populateAvailableElementsList()
        // <!-- Codigo magico, no tocar -->
        fieldSection.insertAdjacentHTML('beforeend', `
        <button type="button" id="${fieldId}-button" value="" class="w-[10%] h-7 bg-gray-800 text-white px-4 py-2 my-2 rounded rounded-l-none flex flex-row items-center justify-center">
                <i class="fas fa-search"></i>
        </button> 
        `);
            
        document.querySelector(`#${fieldId}-button`).addEventListener('click', (event) => {
            this.selectElement(document.querySelector(`#${fieldId}`).value);
            document.querySelector(`#${fieldId}`).value='';
        });
        
    }
    
    selectElement(value) {
        if (this.availableElementsList.includes(value)) {
            this.selectedElementsList.push(value);
            this.availableElementsList = this.availableElementsList.filter(element => element != value);
            this.updateChips();
            
        }
    }
    updateChips() {
        let chipsSection = document.querySelector(`#${this.chipsSectionId}`); 
        chipsSection.innerHTML = '';
        for (let chip of this.selectedElementsList) {
            let chipElement = document.createElement('div');
            chipElement.className = 'chip w-auto mx-2 h-7 bg-gray-800 text-white px-4 py-2 my-2 rounded flex flex-row items-center justify-center'
            chipElement.innerHTML = `
                ${chip}
                <button class="remove" type="button">
                    <i class="fa-solid  fa-x mx-1"></i>
                </button>
            `;
            chipsSection.insertAdjacentElement('beforeend', chipElement);
            console.log(chipElement.querySelector('.remove'));
            chipElement.querySelector('.remove').addEventListener('click', () => {
                this.removeChip(chip);
            }); 

        }
        let datalistElement = document.querySelector(`#${this.datalistId}`)
        for (let option of datalistElement.querySelectorAll('option')) {
            option.disabled = this.selectedElementsList.includes(option.value);
            
        }
        console.log();
        document.querySelector(`#values-${this.chipsSectionId}`).setAttribute('value', Array.from(datalistElement.querySelectorAll('option')).filter(option => option.disabled == true).map(option => option.dataset.id).toString());
    }

    removeChip(value) {
        this.availableElementsList.push(value);
        this.selectedElementsList = this.selectedElementsList.filter(chip => chip != value);
        this.updateChips();
    }

    populateAvailableElementsList() {
        let datalistElement = document.querySelector(`#${this.datalistId}`);
        for (let option of datalistElement.options) {
            this.availableElementsList.push(option.value);
        }
        this.updateChips();
    }

}

const saveFormData = () => {
    localStorage.removeItem('formData');
    let formData = new FormData(document.querySelector('#main-form'));
    let innerFormNames = new Set();
    document.querySelector(`#main-form`).querySelectorAll('form').forEach(form => {
        for (const element of form.elements) { 
            innerFormNames.add(element.name);
        }
    })
    for (const [name, value] of formData) { 
        if (innerFormNames.has(name)) { 
            formData.delete(name); 
        } 
    }
    let data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });
    localStorage.setItem('formData', JSON.stringify(data));
}

const loadFormData = () => {
    let data = localStorage.getItem('formData');
    if (data) {
        let formData = JSON.parse(data);
        for (let key in formData) {
            if (formData.hasOwnProperty(key)) {
                let field = document.querySelector(`[name=${key}]`);
                if (field) {
                    field.value = formData[key];
                }     
            }
        }
    }
}

const saveCreateEntry = (formId, buttonId, endpoint) => {
    localStorage.removeItem('formData');
    let formData = new FormData();
    let formElements;
    if (buttonId) {
        formElements = document.querySelector(`#${formId}`).querySelectorAll(':scope > div > div > input, :scope > div > div > select, :scope > div > div > textarea');
        formElements.forEach(element => { 
            if (element.name && element.value) { 
                formData.append(element.name, element.value); 
            } 
        });
    } else {
        formData = new FormData(document.querySelector(`#${formId}`));
    }
    
    // Optionally log the form data to verify 
    for (let [name, value] of formData.entries()) { 
        console.log(name, value); 
    }
    
    fetch(window.location.href.split('/').slice(0,-2).join('/') + '/' + endpoint + '/', { // BUSCAR ENDPOINT
        method: 'POST', 
        body: formData, 
        headers: { 
            'X-CSRFToken': document.querySelector('#csrf_token').innerHTML,
        }
    }).then(response => response.json()).then(data => { 
        // Finishing 
        if (data.success === true) {
            Swal.fire({
                title: "¡Agregado!",
                text: "Tu registro ha sido agregado",
                icon: "success",
                timer: 2000,
                timerProgressBar: false,
                didOpen: () => {
                    Swal.showLoading();
                    const timer = Swal.getPopup().querySelector("b");
                    timerInterval = setInterval(() => {
                    timer.textContent = `${Swal.getTimerLeft()}`;
                    }, 100);
                },
                willClose: () => {
                    clearInterval(timerInterval);
                }
            }).then((result) => {
                if (buttonId && buttonId === "save-button") {
                    window.location.href = window.location.href.split('?').slice(0,-1)[0];
                    console.log(newUrl);
                } else {
                    if (!checkFormVisibilityByParams()) {
                    
                        window.location.href = window.location.href + '?form_state=open'; 
                    }
                    else {
                        window.location.reload();
                    }
                } 
            });
        } else {
            Swal.fire({
                title: "¡Error!",
                text: `${Array.from(Object.keys(data.errors).map(key => `Campo ${key}: ` + data.errors[key])).join('\n')}`,
                icon: "error",
            });
        }
       
    

    });
}

const saveEditEntry = () => {
    localStorage.removeItem('formData');
    let formData = new FormData();
    let formElements = document.querySelector('#main-form').querySelectorAll(':scope > div > div > input, :scope > div > div > select, :scope > div > div > textarea');
    formElements.forEach(element => { 
        if (element.name && element.value) { 
            formData.append(element.name, element.value); 
        } 
    });
    // Optionally log the form data to verify 
    for (let [name, value] of formData.entries()) { 
        console.log(name, value); 
    }

    let url;
    url = window.location.href.split('?')[0];
   

    fetch(url, { // BUSCAR ENDPOINT
        method: 'POST', 
        body: formData, 
        headers: { 
            'X-CSRFToken': document.querySelector('#csrf_token').innerHTML,
        }
    }).then(response => response.json()).then(data => { 
        // Finishing 
        if (data.success === true) {
            Swal.fire({
                title: "¡Editado!",
                text: "Tu registro ha sido editado",
                icon: "success",
                timer: 2000,
                timerProgressBar: false,
                didOpen: () => {
                    Swal.showLoading();
                    const timer = Swal.getPopup().querySelector("b");
                    timerInterval = setInterval(() => {
                    timer.textContent = `${Swal.getTimerLeft()}`;
                    }, 100);
                },
                willClose: () => {
                    clearInterval(timerInterval);
                }
            }).then((result) => {
                window.location.href = url;
            });
        } else {
            Swal.fire({
                title: "¡Error!",
                text: `${Array.from(Object.keys(data.errors).map(key => `Campo ${key}: ` + data.errors[key])).join('\n')}`,
                icon: "error",
            });
        }
       
    

    });
}