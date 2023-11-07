document.addEventListener('DOMContentLoaded', function() {
    // Función para guardar el formulario de nueva planilla
    function guardarPlanilla(event) {
        event.preventDefault(); // Previene el comportamiento predeterminado del formulario

        // Aquí puedes agregar el código para enviar el formulario a tu servidor
        // Por ejemplo:
        // const formulario = event.target;
        // const formData = new FormData(formulario);
        // fetch('/planillas', {
        //     method: 'POST',
        //     body: formData
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log('Respuesta del servidor:', data);
        // })
        // .catch(error => console.error('Error:', error));

        alert('Formulario guardado'); // Simplemente una alerta para demostración
    }

    // Asignar el evento submit al formulario de nueva planilla
    const formularioNuevo = document.querySelector('.form-agg form');
    formularioNuevo.addEventListener('submit', guardarPlanilla);

    // Función para modificar un registro
    function modificarRegistro() {
        alert('Registro modificado'); // Simplemente una alerta para demostración
    }

    // Asignar el evento click a los botones de modificar registro
    const botonesModificar = document.querySelectorAll('.modificarRegistro');
    botonesModificar.forEach(boton => {
        boton.addEventListener('click', modificarRegistro);
    });
});
