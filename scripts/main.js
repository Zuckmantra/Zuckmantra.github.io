let miImage = document.querySelector('img');

miImage.onclick = function (){
    let miSrc = miImage.getAttribute('src');
    if (miSrc === 'images/moon.jpg'){
        miImage.setAttribute ('src', 'images/moon2.jpg');
    } else {
        miImage.setAttribute ('src', 'images/moon.jpg');
    }
} 

let miBoton = document.querySelector('button');
let miTitulo = document.querySelector ('h1');

function estableceNombreUsuario(){
    let miNombre = prompt('Por favor ingresa tu nombre.');
    if (!miNombre){
        estableceNombreUsuario();
    } else {
    localStorage.setItem('nombre', miNombre);
    miTitulo.textContent = 'Bienvenido a Moon Lounge, ' + miNombre;
    }
}

if(!localStorage.getItem('nombre')){
    estableceNombreUsuario();
} else {
    let nombreAlmacenado = localStorage.getItem('nombre');
    miTitulo.textContent = 'Bienvenido a Moon Lounge, ' + nombreAlmacenado; 
}

 miBoton.onclick = function(){
    estableceNombreUsuario();
}