/*
window.onload = function () {
    

        var canvas  = document.getElementById("map");
        var context = canvas.getContext('2d');

        
        
        canvas.style.width='100%';


        canvas.height = 3484
        canvas.width = 2457
        var img = new Image();

        img.src = 'Manipulate.svg';
        console.log(img.height)


        img.onload = function(e)
        {

            console.log(img.width)
            context.drawImage(img,0, 0,  canvas.width, canvas.height);
        }
}
*/


window.addEventListener('load', function () {


    const clickable = document.getElementsByClassName('clickable')


    const clickable_array = Array.from(clickable)
    console.log(clickable)

    for (let i = 0; i < clickable_array.length; i++) {

        clickable_array[i].onmouseover = function(){
            basic_opacity = clickable_array[i].style.fillOpacity
            clickable_array[i].style.fillOpacity = 0.2;
            console.log(clickable_array[i]);
            
        }
        clickable_array[i].onmouseout = function(){

            clickable_array[i].style.fillOpacity = basic_opacity;
        }
        
        
    }
});