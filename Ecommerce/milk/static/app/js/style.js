$('.plus.cart').click(function(){
    var id=$(this).attr('pid').tostring();
    var em1 = this.parentNode.children[2]
    console.log('pid =',id)
    $.ajax({
        type:'GET',
        url:'/pluscart',
        data:{
            prod_id:id
    },
    success:function(data){
        console.log('data =',data);
        eml.innerText=data.quantity
        document.getElementById('amount').innerText = data.amount
        document.getElementById('totalamount').innerText = data.totalamount

    }
 })
})
$('.minus.cart').click(function(){
    var id=$(this).attr('pid').tostring();
    var em1 = this.parentNode.children[2]
    console.log('pid =',id)
    $.ajax({
        type:'GET',
        url:'/minuscart',
        data:{
            prod_id:id
    },
    success:function(data){
        console.log('data =',data);
        eml.innerText=data.quantity
        document.getElementById('amount').innerText = data.amount
        document.getElementById('totalamount').innerText = data.totalamount
        
    }
 })
})
$('.remove.cart').click(function(){
    var id=$(this).attr('pid').tostring();
    var eml=this
    
    $.ajax({
        type:'GET',
        url:'/removecart',
        data:{
            prod_id:id
        },
        success:function(data){
            console.log('data =',data);
            eml.innerText=data.quantity
            document.getElementById('amount').innerText = data.amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        
    }
 })
})