function asd(e)
{
    e.preventDefault();
    let uname=document.getElementById('un').value;
    let email=document.getElementById('email').value;
    let pass=document.getElementById('pss').value;
    let cpass=document.getElementById('cpss').value;
    console.log(uname,email,pass,cpass)
    if(pass==cpass)
    {
        if(!(uname&&email&&pass&&cpass))
        {
            alert("fields are empty")
        }
        else{
            alert('succesfully loged in')
        }


    }
    else{
        alert("password not match")
    }
}
