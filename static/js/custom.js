/**
 * Custom JS to show and hide toast messages 
 * 
 * Custom JS to disable book now button until
 * a radio button has been selected for a course
 * 
 */
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

    // New code to disable/enable the 'Book Now' button using the specific ID
    var bookNowButton = document.getElementById('book-now-btn');
    var radioButtons = document.querySelectorAll('input[type="radio"]');

    // Initially disable the 'Book Now' button
    bookNowButton.disabled = true;

    // Function to check if any radio button is selected
    function updateButtonState() {
        var isAnyRadioButtonChecked = Array.from(radioButtons).some(radio => radio.checked);
        bookNowButton.disabled = !isAnyRadioButtonChecked;
    }

    // Add event listeners to all radio buttons
    radioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', updateButtonState);
    });
});