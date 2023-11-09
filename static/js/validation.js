$(document).ready(function() {
    // Disable the "Book Now" button initially
    $("#bookNowButton").prop("disabled", true);

    // Listen for changes in the location dropdown
    $("#locationDropdown").change(function() {
        // Check if a location is selected
        if ($(this).val() !== "") {
            // Enable the "Book Now" button
            $("#bookNowButton").prop("disabled", false);
        } else {
            // Disable the "Book Now" button
            $("#bookNowButton").prop("disabled", true);
        }
    });

    // Listen for a click on the "Book Now" button
    $("#bookNowButton").click(function() {
        // Check if a location is selected
        if ($("#locationDropdown").val() === "") {
            // Display a warning message using an alert
            alert("Select a location before booking.");
        }
    });
});
