function add(){
    let x=parseInt(document.getElementById('aa').value)
    let y=parseInt(document.getElementById('bb').value)
    let c=x+y
    document.getElementById("ss").innerHTML = c;
}

function sub(){
    let x=parseInt(document.getElementById('aa').value)
    let y=parseInt(document.getElementById('bb').value)
    let c=x-y
    document.getElementById("ss").innerHTML = c;
}

function mul(){
    let x=parseInt(document.getElementById('aa').value)
    let y=parseInt(document.getElementById('bb').value)
    let c=x*y
    document.getElementById("ss").innerHTML = c;
}

function div(){
    let x=parseInt(document.getElementById('aa').value)
    let y=parseInt(document.getElementById('bb').value)
    let c=x/y
    document.getElementById("ss").innerHTML = c;
}