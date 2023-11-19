// toast-init.js
document.addEventListener('DOMContentLoaded', function () {
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
        var toast = new bootstrap.Toast(toastEl);
        toast.show();
        return toast;
    });

    // Automatically hide the toast after 5s
    toastList.forEach(function(toast) {
        setTimeout(function() {
            toast.hide();
        }, 5000);
    });
});