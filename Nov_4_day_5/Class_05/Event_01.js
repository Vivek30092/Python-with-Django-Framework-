function f1(){
//    var ref = document.getElementsByTagName("h1");
   var ref = document.getElementsByTagName("img");
    
    // alert(ref); // it's used for temp
    ref[0].height+=50;
    ref[0].width+=50;
}
function f2(){
    var ref = document.getElementsByTagName("img")
    ref[0].height-=50;
    ref[0].width-=50;
    
}