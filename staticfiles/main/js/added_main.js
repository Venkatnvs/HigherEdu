$(".toggle-password").click(function () {
  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});
window.onload = () =>{
  const allToolTips  = document.querySelectorAll(".nvs-tooltip");
    allToolTips.forEach(tt => {
        new bootstrap.Tooltip(tt)
    });
}