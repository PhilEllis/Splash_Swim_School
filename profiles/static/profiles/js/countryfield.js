/**
 * Handles the styling of the country selection dropdown in the profile form.
 * 
 * Checks if a country has been selected in the country dropdown 
 * If no country is selected, it sets the dropdown's 
 * text color to a light grey to act as a placeholder style.
 * 
 * It adds a change event listener to the country dropdown. When a change 
 * in selection occurs, it checks if a country is selected. If not, it retains the grey 
 * text color. Otherwise, it changes the text color to a darker shade.
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