$(document).ready(function () {
    var searchInput = $('#searchInput');
    var ajaxRequest;

    searchInput.typeahead({
        source: function (query, process) {
            if (ajaxRequest) {
                ajaxRequest.abort();
            }
            
            ajaxRequest = $.ajax({
                url: 'api/products',
                type: 'GET',
                dataType: 'json',
                data: { query: query },
                success: function (data) {
                    var productNames = data.map(function(item) {
                        return item.name;
                    });
                    process(productNames);
                }
            });
        }
    });
});