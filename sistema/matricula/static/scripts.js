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
    url = url + `${id}?form_state=open`; 
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
                    document.getElementById(`entry-${id}`).remove();  
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


function toggleEditMode() {
    const fields = document.querySelectorAll('.editable');
    const saveButton = document.getElementById('saveButton');
    fields.forEach(field => {
        field.disabled = !field.disabled;
    });
    saveButton.classList.toggle('hidden');
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
            const inputField = document.querySelector(`#${fieldId}`);
            const value = inputField.value.trim(); 
            if (value) {
                this.selectElement(value); 
                inputField.value = ''; 
            }
        });
        
    }
    
    selectElement(value) {
        if (this.availableElementsList.includes(value)) {
            this.selectedElementsList.push(value);
            this.availableElementsList = this.availableElementsList.filter(element => element !== value); 
            this.updateChips(); 
        }
    }
    updateChips() {
        let chipsSection = document.querySelector(`#${this.chipsSectionId}`); 
        chipsSection.innerHTML = ''; 

        for (let chip of this.selectedElementsList) {
            let chipElement = document.createElement('div');
            chipElement.className = 'chip flex items-center justify-between px-2 py-1 bg-gray-800 text-white rounded-md shadow-sm border border-gray-700 text-xs';
            chipElement.innerHTML = `
                <span class="font-medium">${chip}</span>
                <button
                    class="remove flex items-center justify-center w-4 h-4 ml-1 rounded-full hover:bg-gray-600 focus:outline-none"
                    type="button"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-3 h-3">
                        <path d="M5.28 4.22a.75.75 0 0 0-1.06 1.06L6.94 8l-2.72 2.72a.75.75 0 1 0 1.06 1.06L8 9.06l2.72 2.72a.75.75 0 1 0 1.06-1.06L9.06 8l2.72-2.72a.75.75 0 0 0-1.06-1.06L8 6.94 5.28 4.22Z" />
                    </svg>
                </button>
            `;
            chipsSection.appendChild(chipElement);
            chipElement.querySelector('.remove').addEventListener('click', () => {
                this.removeChip(chip);
            });
        }
            
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