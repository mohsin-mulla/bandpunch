<!-- Toggle email input box on purchase form -->
$('#id_email').hide();
$('label[for="id_email"]').hide();
$('#id_email_receipt').change(function () {
    $("#id_email").toggle(this.checked);
    $('label[for="id_email"]').toggle();
});

<!-- Used for hover function of artist information -->
$('.thumb').hover(function(){
	$(this).find('.caption').css('opacity','1');
}, function(){
	$(this).find('.caption').css('opacity','0');
});