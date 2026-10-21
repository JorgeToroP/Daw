const nombre = "Jorge";
const edad = 32;

const saludar = function(){
    console.log(`Hola soy ${nombre} y tengo ${edad} años`);
}

const  tik = function(){
    console.log("tic...");
}

const tak = function(){
    console.log("tak...");
}

setTimeout(saludar, 2000);

const intervalId1 = setInterval(function(){
    tik();
}, 1000);

const intervalId2 =setInterval(function(){
    tak();
}, 2000);

setTimeout(function(){
    clearInterval(intervalId1);
},5000);

