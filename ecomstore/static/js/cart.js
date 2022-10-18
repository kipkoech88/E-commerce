var updateBtns=document.getElementsByClassName('update-cart') 

for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product 
        var action = this.dataset.action 
        console.log('productId', productId, 'action', action) 
        console.log('User', user) 
        if (user =='AnonymousUser'){
            console.log("user not authenticated")
        } 
        else{
            console.log("user is logged in, sending data..")
        }
    } 
    )
} 

function UpdateUserOrder(productId, action){
    console.log("User is loged in, sending data..") 
    var url='/update-items/' 
    
    fetch(url, {
        mathod: 'POST' ,
        Headers:{
            'Content-Type':'application/json', 
            'X-CSRFToken': csrftoken,
        }, 
        body: JSON.stringify({'ProductId': productId, 'action' : action})
    }) 
    .then((response)=>{
        return response.json()
    }) 
    .then((data)=>{
        console.log('data', data)
    })
    
}