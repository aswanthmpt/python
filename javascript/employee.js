function asd(e)
{
    e.preventDefault();
    let eid=document.getElementById('eid').value;
    let ename=document.getElementById('enm').value;
    let slry=document.getElementById('slry').value;
    let exp=document.getElementById('exp').value;
    let img=document.getElementById('img').value;
    console.log(eid,ename,slry,exp,img)

    if(!(eid&&ename&&slry&&exp&&img))
        {
            alert("fields are empty")
        }
        else{
            alert('succesfully submitted')
        }
}