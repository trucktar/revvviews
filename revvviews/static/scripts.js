$(document).ready(() => {
  getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };
  csrfSafeMethod = (method) => {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  };

  var csrftoken = getCookie("csrftoken");
  $.ajaxSetup({
    beforeSend: (xhr, settings) => {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
  });

  var authTabs = $(".modal-header");
  var authForms = $(".modal-body");

  $(".modal-header a").click((e) => {
    e.preventDefault();
    authTabs.toggleClass("d-none", "show");
    authForms.toggleClass("d-none", "show");
  });

  $(".modal-body form").submit((event) => {
    event.preventDefault();
    current_page = window.location.href;
    var form = $(event.target);

    $.post($(form).attr("action"), $(event.target).serialize())
      .done((data) => {
        // Just releod same page after form submission
        window.location.href = current_page;
      })
      .fail((data) => {
        $.each(data.responseJSON, (errName, errList) => {
          console.log(errName, errList);
          var input = $(`[name='${errName}']`);
          if (errList.length > 0) {
            if (errName === "non_field_errors") {
              $(form).before(
                `<div class="alert alert-danger alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert">×</button>${errList[0]}
                </div>`
              );
            }
            for (var i = 0; i < errList.length; i++) {
              input.addClass("is-invalid");
              input.after(`<div class="invalid-feedback">${errList[i]}</div>`);
            }
          }
          input.val("");
        });
      });
  });
});
