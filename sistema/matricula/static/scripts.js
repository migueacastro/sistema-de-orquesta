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
    constructor(chipsSectionId, fieldId, datalistId, buttonId) {
        this.chipsSectionId = chipsSectionId;
        this.fieldId = fieldId;
        this.selectedElementsList = [];
        this.availableElementsList = [];
        this.datalistId = datalistId;
        this.buttonId = buttonId;

        /*document.querySelector(`#${fieldId}`).addEventListener('input', (event) => {
            
        })*/

        
        document.querySelector(`#${chipsSectionId}`).insertAdjacentHTML('afterend', `
            <input type="text" id="value-${chipsSectionId}" value="" hidden> 
         `);

         this.populateAvailableElementsList()
        // <!-- Codigo magico, no tocar -->
        document.querySelector(`#${fieldId}`).insertAdjacentHTML('afterend', `
           <button type="button" id="${fieldId}-button" value="" class="w-[10%] h-7 bg-gray-800 text-white px-4 py-2 my-2 rounded rounded-l-none flex flex-row items-center justify-center">
                <i class="fas fa-search"></i>
           </button> 
        `);
        document.querySelector(`#${fieldId}-button`).addEventListener('click', (event) => {
            document.querySelector(`#${fieldId}`).value='';
            this.selectElement(document.querySelector(`#${fieldId}`).value);
        });
    }
    
    selectElement(value) {
        if (this.availableElementsList.includes(value)) {
            this.selectedElementsList.push(value);
            this.availableElementsList.filter(element => element != value);
            this.updateChips();
            
        }
    }
    updateChips() {
        let chipsSection = document.querySelector(`#${this.chipsSectionId}`); 
        chipsSection.innerHTML = '';
        for (let chip of this.selectedElementsList) {
            let chipElement = `
                <div class="chip relative rounded-md flex bg-slate-800 py-0.5 pl-2.5 pr-8 border border-transparent text-sm text-white transition-all shadow-sm">
                    <button
                            class="remove flex items-center justify-center transition-all p-1 rounded-md text-white hover:bg-white/10 active:bg-white/10 absolute top-0.5 right-0.5"
                            type="button"
                        >
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
                        <path d="M5.28 4.22a.75.75 0 0 0-1.06 1.06L6.94 8l-2.72 2.72a.75.75 0 1 0 1.06 1.06L8 9.06l2.72 2.72a.75.75 0 1 0 1.06-1.06L9.06 8l2.72-2.72a.75.75 0 0 0-1.06-1.06L8 6.94 5.28 4.22Z" />
                        </svg>
                    </button>
                </div>
            `;
            ;
            chipsSection.insertAdjacentHTML('beforeend', chipElement);
            console.log(chipsSection.querySelector('.remove'));
            chipsSection.querySelector('.remove').addEventListener('click', () => {
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