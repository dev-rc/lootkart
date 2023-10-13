$(document).ready(function () {
    // Function to fetch product names from API
    function fetchProductNames() {
        $.ajax({
            url: 'http://127.0.0.1:8000/api/', // Adjust the URL accordingly
            method: 'GET',
            success: function(data) {
                initializeAutocomplete(data.names); // Assuming the API response contains a list of 'names'
            },
            error: function(error) {
                console.error('Error fetching product names:', error);
            }
        });
    }

    // Function to initialize autocomplete
    function initializeAutocomplete(names) {
        $("#searchInput").autocomplete({
            source: names
        });
    }

    // Call the function to fetch product names
    fetchProductNames();
});