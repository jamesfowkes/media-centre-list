function filter_shows(element) {
    var value = $(element).val().toLowerCase();

    $("#shows_list > li").each(function() {
        if ($(this).text().toLowerCase().search(value) > -1) {
            $(this).show();
        }
        else {
            $(this).hide();
        }
    });
}

function filter_films(element) {
    var value = $(element).val().toLowerCase();

    $("#films_list > li").each(function() {
        if ($(this).text().toLowerCase().search(value) > -1) {
            $(this).show();
        }
        else {
            $(this).hide();
        }
    });
}
