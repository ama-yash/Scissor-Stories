function valUser(){
    var a1,a2,a3,a4,a5,a6;
    username=document.getElementById('username').value;
    email=document.getElementById('email').value;
    pass=document.getElementById('pass').value;
    pass1=document.getElementById('pass2').value;
    if(username==''){
        var a = document.getElementById('uerror');
        a.style.display='block';
        a1=false;
    }
    else{
        if(/\s/.test(username)){
            var a = document.getElementById('uerror1');
            a.style.display='block';
            a2=false;
        }
        else{
            var a = document.getElementById('uerror1');
            a.style.display='none';
            a2=true;    
        }
        var a = document.getElementById('uerror');
        a.style.display='none';
        a1=true;
    }
    if(email==''){
        var a = document.getElementById('eerror');
        a.style.display='block';
        a3=false;
    }
    else{
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
            var a = document.getElementById('eerror1');
            a.style.display='none';
            a4=true;
        }
        else{
            var a = document.getElementById('eerror1');
            a.style.display='block';
            a4=false;
        }
        var a = document.getElementById('eerror');
        a.style.display='none';
        a3=true;
    }
    if(pass==''){
        var a = document.getElementById('perr');
        a.style.display='block';
        a4=false;
    }
      else{
        var a = document.getElementById('perr');
        a.style.display='none';
        a4=true;
        if (pass.length<8){
            var a = document.getElementById('perr1');
            a.style.display='block';
            a5=false;
        }
        else{
            var a = document.getElementById('perr1');
            a.style.display='none';
            a5=true;
        }
        
      }
      if(pass==pass1){
        var a = document.getElementById('perr11');
        a.style.display='none';
        a6=true;
      }
      else{
        var a = document.getElementById('perr11');
        a.style.display='block';
        a6=false;
      }
    if(a1 && a2 && a3 && a4 && a5 && a6){
        $(document).on('submit','#register',function(e){
            e.preventDefault();
            $.ajax({
              type:'POST',
              url:'/auth/add',
              data:{
                username:username,
                pass:pass,
                email:email,
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
              },
              success:function(data){
                if(!data.success){                 
                    if(!data.user){
                        var a = document.getElementById('uexist');
                        a.style.display='block';
                        return false;
                    }
                    else{
                        var a = document.getElementById('uexist');
                        a.style.display='none';
                    }
                }
                else{
                  document.location.href=data.url;
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

function valLogin(){
  var a1,a2;
  var user=document.getElementById('logusername').value;
  var pass=document.getElementById('logpassword').value;
  if(user==''){
    var a=document.getElementById('unull');
    a.style.display='block';
    a1=false;
  }
  else{
    var a=document.getElementById('unull');
    a.style.display='none';
    a1=true;
  }
  if(pass==''){
    var a=document.getElementById('pnull');
    a.style.display='block';
    a2=false;
  }
  else{
    var a=document.getElementById('pnull');
    a.style.display='none';
    a2=true;
  }
  if(a1 && a2){
    $(document).on('submit','#login',function(e){
      e.preventDefault();
      $.ajax({
        type:'POST',
        url:'/auth/validate',
        data:{
          username:user,
          password:pass,
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
          if(!data.success){  
              var a = document.getElementById('uex');
              a.style.display='none';
              var b = document.getElementById('perr');
              b.style.display='none';               
              if(!data.user){
                  var c = document.getElementById('uex');
                  c.style.display='block';
                  return false;
              }
              else if(!data.passw){
                var d =document.getElementById('perr');
                d.style.display='block';
              }
          }
          else{
            document.location.href=data.url;
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

function valFor(){
    var a1;
    username=document.getElementById('forusername').value;
    if(username==''){
      var a=document.getElementById('unull');
      a.style.display='block';
      a1=false;
    }
    else{
      var a=document.getElementById('unull');
      a.style.display='none';
      a1=true;
    }
    if(a1){
      $(document).on('submit','#forpass',function(e){
        e.preventDefault();
        $.ajax({
          type:'POST',
          url:'/auth/validate-for-pass',
          data:{
            username:username,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
          },
          success:function(data){
            if(!data.success){  
                var a = document.getElementById('uex');
                a.style.display='block';
            }
            else{
              document.location.href=data.url;
            }
          },
          error:function(){
            alert('Error');
          }
        })
      })
    }
    else{
      return a1;
    }
}
function valPass(){
    var a4,a5,a6;
    pass=document.getElementById('pass1').value;
    pass1=document.getElementById('pass2').value;
    if(pass==''){
      var a = document.getElementById('perr');
      a.style.display='block';
      a4=false;
  }
    else{
      var a = document.getElementById('perr');
      a.style.display='none';
      a4=true;
      if (pass.length<8){
          var a = document.getElementById('perr1');
          a.style.display='block';
          a5=false;
      }
      else{
          var a = document.getElementById('perr1');
          a.style.display='none';
          a5=true;
      }
      
    }
    if(pass==pass1){
      var a = document.getElementById('perr11');
      a.style.display='none';
      a6=true;
    }
    else{
      var a = document.getElementById('perr11');
      a.style.display='block';
      a6=false;
    }
    if(a4 && a5 && a6){
      return true;
    }
    else{
      return false;
    }
}
function ser(){
  date=document.getElementById('dtp').value;
  but=document.getElementById('but').value;
  date1 = new Date(date)
  yyyy= date1.getFullYear();
  mm=date1.getMonth();
  dd=date1.getDate();
  $.ajax
  ({
        type: "POST",
        url: "/service-providers/send",
        data: {yyyy:yyyy,
              mm:mm,
              dd:dd,
              but:but,
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
        success: function(data)
        {
            $('#service').empty()
            $('#service').append('<thead><tr><th scope="col">ID</th><th scope="col">Service</th><th scope="col">From</th><th scope="col">To</th><th scope="col">Attendant</th><th scope="col">Gender</th><th scope="col">Price</th>')
            for(var i=0;i<data.length;i++){
              var id=data.idlist[i];
              var ser=data.serlist[i];
              var from=data.fromlist[i];
              var to=data.tolist[i];
              var att=data.atlist[i];
              var gen=data.genlist[i];
              var price=data.pricelist[i];
              $('#service').append("<tr><th scope='row'>" + id + "</th><td>" + ser + "</td><td>"+ from + "</td><td>" + to + "</td><td>" + att + "</td><td>" + gen + "</td><td>" + price + "</td><td><a href='/appointment/book?id=" + id +"&pro=" + data.pro + "&date=" + data.date + "'>Book Now</a></td>");
            }
        }
   });  
}