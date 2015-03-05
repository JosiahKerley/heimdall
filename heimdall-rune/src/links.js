$.getJSON("sites.json", function (obj) {
  $.each(obj.users, function (key, value) {
    $("ul").append("<li>" + value.name + "</li>");
  }
);