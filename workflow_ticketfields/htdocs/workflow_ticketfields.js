jQuery(document).ready(function($) {
  $("fieldset#action").on("click", "input[name=action]", function() {
    $(".workflow_ticket_fields").slideUp();
    $(this).closest("div").find(".workflow_ticket_fields").slideDown();
  });
});
