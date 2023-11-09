document.addEventListener('DOMContentLoaded', function() {
    //  "Book Now" button
    var bookNowButton = document.getElementById('bookNowButton');
    var locationDropdown = document.getElementById('locationDropdown');
    
    // Disable the Book Now button initially
    bookNowButton.disabled = true;
    
    // Listen for changes in location 
    locationDropdown.addEventListener('change', function() {
        // Check if a location is selected
        bookNowButton.disabled = this.value === "";
    });
    
    // Listen for a click on the Book Now button 
    bookNowButton.addEventListener('click', function() {
        // Check if a location is selected
        if (locationDropdown.value === "") {
            // Display a warning message using an alert
            alert("Select a location before booking.");
        }
    });

    // Bootstrap 5 Carousel Initialization
    var heroCarouselElement = document.querySelector('#heroCarousel');
    if (heroCarouselElement) {
        var heroCarousel = new bootstrap.Carousel(heroCarouselElement, {
            interval: 5000,
            ride: 'carousel'
        });
    }

    // AOS Initialization
    AOS.init({
        duration: 1000,
        easing: 'ease-in-out',
        once: true,
        mirror: false
    });

    // PureCounter Initialization
    new PureCounter();
});
