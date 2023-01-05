$(document).ready(function () {
    $('.my-phone-mask').inputmask({
        mask: "+\\9\\98(99) 999-99-99",
        showMaskOnHover: true,
        showMaskOnFocus: true,
        onBeforePaste: function (pastedValue, opts) {
            return pastedValue.replace(/\D/g,'').slice(-9);
        }
    });
    
});
