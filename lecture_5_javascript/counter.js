if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

function count(){
    let counter = localStorage.getItem('counter')
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);

    /* 
    if(counter % 10 === 0){
        // template literal
        alert(`The counter is now ${counter}`);
    }
    */
}

// considering functions as values is functional programming

//querySelecter is returning NULL value because DOM is not completely loaded
// document.querySelector('button').onclick = count

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // document.querySelector('button').addEventListener('click', count);

    // setInterval(count, 1000);
});