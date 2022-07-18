const offcanvas = document.querySelector('.js-offcanvas')
const valor = document.querySelector('.valor')
const bichow = document.querySelector('.bicho')
function addCanvas() {
    document.querySelector('.js-offcanvas').classList.add('canvas-active')
   
}

function exitCanvas() {
    offcanvas.classList.remove('canvas-active')
    
}
function addbicho(){
    const bichos = [
    "avestruz",
    "aguia"  ,
    "burro" ,
    "borboleta",
    "cachorro" ,
    "cabra" ,
    "carneiro",
    "camelo" ,
    "cobra",
    "coelho" ,
    "cavalo",
    "elefante",
    "galo",
    "gato" ,
    "jacare" ,
    "leao" ,
    "macaco",
    "porco",
    "pavao",
    "peru",
    "touro",
    "tigre" ,
    "urso",
    "viado",
    "vaca" ,
]

 for (let i = 0; i < 25; i++) {
     let ops = document.createElement('option')
     ops.value = i+1
     ops.innerHTML = (i+1) + " - " + bichos[i]
     // ops.setAttribute('name', 'bichos-ops')
     bichow.appendChild(ops)
 }
}



// function addimg() {
//     const valor = document.getElementsByName('bichos-ops')
//     const imagens = ['https://img.quizur.com/f/img5c40b4073ecaa3.57926270.png?lastEdited=1547744354']
//     const img = document.createElement('img')
//     img.src = imagens[0]
//     bichow.parentElement.appendChild(img)
// }
// addimg()
addbicho()