let call = async() =>{
    let response = await fetch("http://localhost:8000/consumables/")
    let data = await response.json()
    console.log(data);
}
call()