document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#increase").onclick = increase;
    document.querySelector("#reset").onclick = reset;
    document.querySelector("h1").innerHTML = count;
})

let count = 0;


function increase() {
    count++;
    if(count % 10 === 0){
        alert(`The count is now ${count}`);
    }
    document.querySelector("h1").innerHTML = count;
}

function reset() {
    count = 0;
    console.log(count);

    document.querySelector("h1").innerHTML = count;
}