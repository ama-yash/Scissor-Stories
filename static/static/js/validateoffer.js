function valOffer(){
    var a1,a2,a3,a4,a5,a6,a7,a8;
    var off_id=document.forms['myform']['offer_id'].value;
    var off_name=document.forms['myform']['offer_name'].value;
    var off_from=document.forms['myform']['offer_from'].value;
    var off_to=document.forms['myform']['offer_to'].value;
    var disc_rat=document.forms['myform']['disc_ratio'].value;
    var maxamt=document.forms['myform']['maxamount'].value;
    var flag=0;
    var tod= new Date();
    var giv=new Date(off_from);
    if(off_id==''){
        var a = document.getElementById('offernull');
        a.style.display='block';
        a1=false;
    }
    else{
        var a = document.getElementById('offernull');
        a.style.display='none';
        a1=true;
    }
    if(off_name==''){
        var a = document.getElementById('offername');
        a.style.display='block';
        a2=false;
    }
    else{
        var a = document.getElementById('offername');
        a.style.display='none';
        a2=true;
    }
    if(off_from==''){
        var a = document.getElementById('fromnull');
        a.style.display='block';
        a3=false;
    }
    else{
        var a = document.getElementById('fromnull');
        a.style.display='none';
        if(giv < tod){
            var a =document.getElementById('futerr');
            a.style.display='block';
            a4=false;
        }
        else{
            var a =document.getElementById('futerr');
            a.style.display='none';
            a4=true;
        }
        a3=true;
    }
    if(off_to==''){
        var a = document.getElementById('tonull');
        a.style.display='block';
        a5=false;
    }
    else{
        var a = document.getElementById('tonull');
        a.style.display='none';
        
        if (off_from > off_to){
            var a = document.getElementById('dateerr');
            a.style.display='block';
            a6=false;
        }
        else{
            var a = document.getElementById('dateerr');
            a.style.display='none';
            a6=true;
        }
        a5=true;
    }
    if(disc_rat==''){
        var a = document.getElementById('discnull');
        a.style.display='block';
        a7=false;
    }
    else{
        var a = document.getElementById('discnull');
        a.style.display='none';
        a7=true;
    }
    if(maxamt==''){
        var a = document.getElementById('maxnull');
        a.style.display='block';
        a8=false;
    }
    else{
        var a = document.getElementById('maxnull');
        a.style.display='none';
        a8=true;
    }
    if (a1==true && a2==true && a3==true && a4==true && a5==true&& a6==true&& a7==true&& a8==true){
        $(document).on('submit','#myform',function(e){
            e.preventDefault();
                $.ajax({
                  type:'POST',
                  url:'/s-admin/bookings/offers',
                  data:{
                    off_id:off_id,
                    off_name:off_name,
                    off_from:off_from,
                    off_to:off_to,
                    disc_rat:disc_rat,
                    maxamt:maxamt,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
                    },
                  success:function(data){
                    if(data.success){
                        localStorage.setItem('flag1',true);
                        window.location.href="/s-admin/bookings/";                        
                    }
                    else{
                        swal({
                            icon: 'error',
                            text: 'Offer ID already exists!',
                            buttons:false,
                            timer:1500,
                          });
                    }
                  }                
              })
              
          });
    } 
    else{
        return false;
    }
}
function greet1(){
    if (localStorage.getItem('flag1') != null){
        swal({
            position:"top-end",
            text: "Offer Added Successfully!",
            buttons:false,
            timer:2500,
            icon: "success",
          });
        localStorage.removeItem('flag1');
    }
}