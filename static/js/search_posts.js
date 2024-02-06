var selectedTags = [];

$(document).ready(function () {
    $(".btn-tag").on("click", function () {
        var tag = $(this).text();

        // Toggle the selection
        if (selectedTags.includes(tag)) {
            selectedTags = selectedTags.filter(function (t) {
                return t !== tag;
            });
            $(this).removeClass("selected-tag");
        } else {
            selectedTags.push(tag);
            $(this).addClass("selected-tag");
        }

        // Update the hidden input value
        $("#selected-tags").val(selectedTags.join(' '));
    });

    // Manually submit the form with selected tags when the search button is clicked
    $("#search-button").on("click", function () {
        $("#search-form").submit();
    });
});