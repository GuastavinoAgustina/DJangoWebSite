var updateBtns = document.getElementsByClassName('update-recital')

for (i=0; i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var recitalId = this.dataset.recital
        var action = this.dataset.action
        updateReserva(recitalId,action)
    })
}

function updateReserva(recitalId,action){
    console.log('recitalId:', recitalId, 'action:',action)

    var url = '/updateitem/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'recitalId':recitalId, 'action:':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log(data)
    })
}