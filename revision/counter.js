if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

let count = localStorage.getItem('counter');


document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#increase").onclick = increase;
    document.querySelector("#reset").onclick = reset;
    document.querySelector("h1").innerHTML = count;
    setInterval(increase, 1000);
})





function increase() {
    count++;
    document.querySelector("h1").innerHTML = count;
    localStorage.setItem('counter', count);
}

function reset() {
    count = 0;

    document.querySelector("h1").innerHTML = count;
    localStorage.setItem('counter', count);
}