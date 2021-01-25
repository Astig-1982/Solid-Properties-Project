

$(document).ready(function(){
    $('.navbar').css('background-color', 'rgb(33,0,112)')
    $('.services-container').addClass('detailed-service-bottom')
    $('.select-property').change(function(){
        let bedrooms = $(this).val();
        let servicePrice = $('.service-price').html()
        let servicePriceInt = parseInt(servicePrice)
        let noOfBedrooms = parseInt(bedrooms)
        let totalPrice = servicePriceInt * noOfBedrooms
        $('.total-price').text(`£${totalPrice.toFixed(2)}`)
        console.log(servicePrice)
        console.log(noOfBedrooms)
    })   
});