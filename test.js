let left = 25
let machineLeft = 25
let timer = setInterval(machine, 500);
function machine(){
    $('#box2').animate({left: machineLeft + "px"})
    machineLeft += 25
    if(machineLeft == 1000){
        $('#box1').fadeOut(1000);
        $('#box2').fadeOut(1000);
        $('#res').css('color', 'red');
        res.innerText = "YOU LOSE!"
    }
}
$('#box1').click(function(){
    $('#box1').animate({left: left + "px"});
    left += 25
    if(left == 1000){
    $('#box1').fadeOut(1000);
    $('#box2').fadeOut(1000);
    res.innerText = "YOU WIN!" 
    clearInterval(timer);
    }
});