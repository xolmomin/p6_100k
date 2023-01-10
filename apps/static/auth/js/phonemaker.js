let element = document.getElementById('phone');
let maskOptions = {
    mask: '+{998}(00)000-00-00',
    lazy: false
}
let mask = new IMask(element, maskOptions);