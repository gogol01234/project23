$(".remove-notes").click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type:"POST",
        url:"/removenotes/",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("Delete")
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})