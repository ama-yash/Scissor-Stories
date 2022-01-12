function valAttendant(){

    var a1,a2,a3,a4,a5,a6,a7,a8;
    var atname=document.getElementById('atname').value;
    var gender=document.getElementById('gender').value;
    var contact=document.getElementById('contact').value;
    if(atname==''){
        var a = document.getElementById('atnull');
        a.style.display='block';
        a1=false;
    } 
    else{
        var a =document.getElementById('atnull');
        a.style.display='none';
        a1=true;
    }
    if(contact==''){
        var a = document.getElementById('connull');
        a.style.display='block';
        a2=false;
      }
    else{
        var a = document.getElementById('connull');
        a.style.display='none';
        if(!contact.match('/\d{10}/') && contact.length<10){
          var a = document.getElementById('conn');
          a.style.display='block';
          a3=false;
        }
        else{
          var a = document.getElementById('conn');
          a.style.display='none';
          a3=true;
        }
        a2=true;
      }
      if(gender==0){
        var a = document.getElementById('gennull');
        a.style.display='block';
        a4=false;
      }
      else{
        var a = document.getElementById('gennull');
        a.style.display='none';
        a4=true;
      }
    if(a1 && a2 && a3 && a4){
       return true;
    }
    else{
        return false;
    }
}

function valService(){
  var a1,a2,a3,a4,a5;  
  var atname=document.getElementsByName('attendant')[0].value;
  var service=document.getElementsByName('service')[0].value;
  var timefrom=document.getElementsByName('timefrom')[0].value;
  var timeto=document.getElementsByName('timeto')[0].value;
  var price=document.getElementsByName('price')[0].value;
  if(atname==0){
    a1=false;
    var a = document.getElementById('att');
    alert("ASDFASF");
    a.style.display='block';
  }
  else{

    var a = document.getElementById('att');
    a.style.display='none';
    a1=true;
  } 
  if(service=='0'){
    a2=false;
    var a = document.getElementById('ser');
    a.style.display='block';
  }
  else{
    var a = document.getElementById('ser');
    a.style.display='none';
    a2=true;
  } 
  if(timefrom==''){
    a3=false;
    var a = document.getElementById('tf');
    a.style.display='block';
  }
  else{
    var a = document.getElementById('tf');
    a.style.display='none';
    a3=true;
  } 
  if(timeto==''){
    a4=false;
    var a = document.getElementById('tt');
    a.style.display='block';
  }
  else{
    var a = document.getElementById('tt');
    a.style.display='none';
    a4=true;
  } 
  if(price==''){
    a5=false;
    var a = document.getElementById('pr');
    a.style.display='block';
  }
  else{
    var a = document.getElementById('pr');
    a.style.display='none';
    a5=true;
  }
  if(a1 && a2 && a3 && a4 && a5){
    return true;
  }
  else{
    return false;
  }
}