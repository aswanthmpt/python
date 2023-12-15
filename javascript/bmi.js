function bmi(){
    let x=parseFloat(document.getElementById("hh").value)
    let y=parseFloat(document.getElementById("ww").value)
    let h=x/100
    let b=y/(h*h)
    if (b>=30){
        a="  obesity";

    }
        
    else if (b>=25){
        a="  over weight"

    }
         
    else if (b>=18.5){
        a="  normal weight"

    }
            
    else if (b<18){
        a="  under weight"

    }
        
    document.getElementById("bm").innerHTML=b+a
    // document.getElementById("vv").innerHTML=a

}