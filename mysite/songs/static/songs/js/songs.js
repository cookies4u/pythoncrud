$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-song").modal("show");
      },
      success: function (data) {
        $("#modal-song .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#song-table tbody").html(data.html_song_list);
          $("#modal-song").modal("hide");
        }
        else {
          $("#modal-song .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create song
  $(".js-create-song").click(loadForm);
  $("#modal-song").on("submit", ".js-song-create-form", saveForm);

  // Update song
  $("#song-table").on("click", ".js-update-song", loadForm);
  $("#modal-song").on("submit", ".js-song-update-form", saveForm);

  // Delete song
  $("#song-table").on("click", ".js-delete-song", loadForm);
  $("#modal-song").on("submit", ".js-song-delete-form", saveForm);

});
