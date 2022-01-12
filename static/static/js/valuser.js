function valUsername(){
    if(username==''){
        var a = document.getElementById('uerror');
        a.style.display='block';
        return false;
    }
    else{
        if(/\s/.test(username)){
            var a = document.getElementById('uerror1');
            a.style.display='block';
            return false;
        }
        else{
            var a = document.getElementById('uerror1');
            a.style.display='none';
            return true;
        }
        var a = document.getElementById('uerror');
        a.style.display='none';
        return true;
    }
}
function valEmail(){
    if(email==''){
        var a = document.getElementById('eerror');
        a.style.display='block';
        return false;
    }
    else{
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)){
            var a = document.getElementById('eerror1');
            a.style.display='none';
            return true;
        }
        else{
            var a = document.getElementById('eerror1');
            a.style.display='block';
            return false;
        }
        var a = document.getElementById('eerror');
        a.style.display='none';
        return true;
    }
}
function valPass1(){
    if(pass==''){
        var a = document.getElementById('perr');
        a.style.display='block';
        return false;
    }
      else{
        var a = document.getElementById('perr');
        a.style.display='none';
        return true;
        if (pass.length<8){
            var a = document.getElementById('perr1');
            a.style.display='block';
            return false;
        }
        else{
            var a = document.getElementById('perr1');
            a.style.display='none';
            return true;
        }
        
      }
    
}
function valPass2(){
    if(pass==pass1){
        var a = document.getElementById('perr11');
        a.style.display='none';
        return true;
      }
      else{
        var a = document.getElementById('perr11');
        a.style.display='block';
        return false;
      }    
}
function val(){
    if(valUsername() && valEmail() && valPass1() && valPass2()){
        return true;
    }
    else{
        return false;
    }
}
function abc(){ 
    username=document.getElementById('username').value;
    email=document.getElementById('email').value;
    pass=document.getElementById('pass').value;
    pass1=document.getElementById('pass2').value;
    if(val()){
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