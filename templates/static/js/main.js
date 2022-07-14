const offcanvas = document.querySelector('.js-offcanvas')
const exitCanva = document.querySelector('.exit')
const valor = document.querySelector('.valor')

function addCanvas() {
    document.querySelector('.js-offcanvas').classList.add('canvas-active')
   
}

function exitCanvas() {
    offcanvas.classList.remove('canvas-active')
    
}


