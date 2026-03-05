$(document).ready(function() {

  $('#login-form').submit(function(e) {
    e.preventDefault();
    const formData = $(e.currentTarget).serialize();
    attemptOneTouchVerification(formData);
  });

  const attemptOneTouchVerification = function(form) {
    $.post( "/login", form, function(data) {
      $('.form-errors').remove();
      // Check first if we successfully authenticated the username and password
      if (data.hasOwnProperty('error')) {
        $('#login-form').prepend(data.error);
        return;
      }

      if (data.success) {
        $('#authy-modal').modal({backdrop:'static'},'show');
        $('.auth-ot').fadeIn();
        checkForOneTouch();
      } else {
        redirectToTokenForm();
      }
    });
  };

  const checkForOneTouch = function() {
    $.get( "/login/status", function(data) {
      
      if (data === 'approved') {
        window.location.href = "/account";
      } else if (data === 'denied') {
        redirectToTokenForm();
      } else {
        setTimeout(checkForOneTouch, 2000);
      }
    });
  };

  const redirectToTokenForm = function() {
    window.location.href = "/verify";
  };
});
