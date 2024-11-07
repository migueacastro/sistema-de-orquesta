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

        title: "Estas seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminalo!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
            title: "Eliminado!",
            text: "Tu registro ha sido eliminado",
            icon: "success"
        });
        let parts = window.location.href.toString().split("/"); 
        let tableName = parts[parts.length-2];
        let url =`/${tableName}/${id}`;
        let csrfToken = document.querySelector('#csrf_token').innerHTML; 
        fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken':csrfToken
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
