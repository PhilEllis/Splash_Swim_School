/**
 * Handles the styling of the country selection dropdown in the profile form.
 * 
 * Checks if a country has been selected in the country dropdown 
 * If no country is selected, it sets the dropdown's 
 * text color to a light grey or dark grey if selected.
 * 
 */
let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#020924');
    }
});