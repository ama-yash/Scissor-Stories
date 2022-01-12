function valSp(){
    var a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12;
    var username = document.forms['myform']['username'].value;
    var email = document.forms['myform']['email'].value;   
    var password = document.forms['myform']['password'].value;
    var password1 = document.forms['myform']['password1'].value;
    var firm_name = document.forms['myform']['firm_name'].value;
    var owner_name = document.forms['myform']['owner_name'].value;
    var address = document.forms['myform']['address'].value;
    var contact = document.forms['myform']['contact'].value;
    var image = $('#imagee').val();
    var city = document.forms['myform']['city'].value;
    var state = document.forms['myform']['state'].value;
    var count = 0
    if(username==''){
      var a = document.getElementById('usernull');
      a.style.display='block';
      a1=false;
    }
    else{
      var a = document.getElementById('usernull');
      a.style.display='none';
      a1=true;
    }
    if(email==''){
        var a = document.getElementById('emailnull');
        a.style.display='block'; 
        a2=false; 
      }
      else{
        var a = document.getElementById('emailnull');
        a.style.display='none';   
        a2=true;   
      }
      if(password==''){
        var a = document.getElementById('passnull');
        a.style.display='block';
        a3=false;
      }
      else{
        var a = document.getElementById('passnull');
        a.style.display='none';
        if (password.length<8){
            var a = document.getElementById('passlen')
            a.style.display='block';
            a4=false;
        }
        else{
            var a = document.getElementById('passlen')
            a.style.display='none';
            a4=true;
        }
        a3=true;
      }
      if (password1==''){}
      else{
        if(password==password1){
            var a = document.getElementById('pass1');
            a.style.display='none';
            a5=true;
          }
          else{
              var a = document.getElementById('pass1');
              a.style.display='block';
              a5=false;
          }
      }
      if(firm_name==''){
        var a = document.getElementById('firmnull');
        a.style.display='block';
        a6=false;
      }
      else{
        var a = document.getElementById('firmnull');
        a.style.display='none';
        a6=true;
      }
      if(owner_name==''){
        var a = document.getElementById('ownernull');
        a.style.display='block';
        a7=false;
      }
      else{
        var a = document.getElementById('ownernull');
        a.style.display='none';
        a7=true;
      }
      if(address==''){
        var a = document.getElementById('addressnull');
        a.style.display='block';
        a8=false;
      }
      else{
        var a = document.getElementById('addressnull');
        a.style.display='none';
        a8=true;
      }
      if(contact==''){
        var a = document.getElementById('contactnull');
        a.style.display='block';
        a9=false;
      }
      else{
        var a = document.getElementById('contactnull');
        a.style.display='none';
        if(!contact.match('/\d{10}/') && contact.length<10){
          var a = document.getElementById('contactval');
          a.style.display='block';
          a10=false;
        }
        else{
          var a = document.getElementById('contactval');
          a.style.display='none';
          a10=true;
        }
        a9=true;
      }
      if(state == 0){
        var a = document.getElementById('statenull');
          a.style.display='block';
          a11=false;
      }
      else{
        var a = document.getElementById('statenull');
          a.style.display='none';
          a11=true;
      }
      if(city == 0){
        var a = document.getElementById('citynull');
          a.style.display='block';
          a12=false;
      }
      else{
        var a = document.getElementById('citynull');
          a.style.display='none';
          a12=true;
      }
      if(a1==true && a2==true && a3==true&& a4==true&& a5==true&& a6==true&& a7==true&& a8==true&& a9==true&&a10==true&&a11==true&&a12==true){
        $(document).on('submit','#myform',function(e){
          e.preventDefault();
          $.ajax({
            type:'POST',
            url:'/s-admin/service-provider/validate',
            data:{
              username:username,
              password:password,
              email:email,
              firm_name:firm_name,
              owner_name:owner_name,
              address:address,
              contact:contact,
              city:city,
              state:state,
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
              if(!data.success){
                swal({
                  icon: 'error',
                  text: 'Username already exists!',
                  buttons:false,
                  timer:1500,
                });
              }
              else{
                swal({
                  icon: 'success',
                  text: 'Service Provider added successfully!',
                  buttons:false,
                  timer:1500,
                });
              }
            },
            error:function(){
              alert('Error');
            }
          })
        })
      }
      else{
        return false;
      }
}
function bcity(){
  var sid=$('#state').val();
  $.ajax({
    type:"GET",
    dataType:'JSON',
    url:'/s-admin/service-provider/getcity',
    data:{sid:sid},
    success:function(data){   
      $('#city').empty();
      $('#city').append("<option value=0>--Select City--</option>");
      for(var i =0;i<data.length;i++){
        var id=data.city_id[i];
        var name=data.city_name[i];        
        $('#city').append("<option value="+id+">"+name+"</option>");
      }
    }
  });
}

