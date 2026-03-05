/**
 * Telnyx WebRTC Client configuration for the browser-calls-node
 * Migrated from Twilio Client to Telnyx WebRTC SDK
 */

// IMPORTANT: Telnyx WebRTC SDK must be loaded via CDN or bundler
// For CDN: <script src="https://unpkg.com/@telnyx/webrtc@latest/dist/bundle.js"></script>
// When using CDN, use TelnyxWebRTC.TelnyxRTC instead of TelnyxRTC directly

// Store some selectors for elements we'll reuse
var callStatus = $("#call-status");
var answerButton = $(".answer-button");
var callSupportButton = $(".call-support-button");
var hangUpButton = $(".hangup-button");
var callCustomerButtons = $(".call-customer-button");

// Global client and active call
var client = null;
var activeCall = null;

/* Helper function to update the call status bar */
function updateCallStatus(status) {
  callStatus.text(status);
}

console.log("Requesting Telnyx Credentials...");
$(document).ready(function() {
  $.post("/token/generate", {page: window.location.pathname})
    .then(function(data){

      // Setup TelnyxRTC client
      // Note: When loading via CDN, use: new TelnyxWebRTC.TelnyxRTC({...})
      // When using npm/bundler, use: new TelnyxRTC({...})
      client = new TelnyxRTC({
        login_token: data.token,
        // OR use SIP credentials directly:
        // login: data.sip_username,
        // password: data.sip_password
      });

      // Set audio element for remote audio playback
      client.remoteElement = 'remoteAudio';

      // Connect and register the client
      client.connect();

      client.on("telnyx.ready", function() {
        console.log("TelnyxRTC Ready!");
        updateCallStatus("Ready");
      });

      client.on("telnyx.error", function(error) {
        console.log("TelnyxRTC Error: " + error.message);
        updateCallStatus("ERROR: " + error.message);
      });

      client.on("telnyx.notification", function(notification) {
        if (notification.type === 'callUpdate') {
          var call = notification.call;
          activeCall = call;

          // Handle call state changes
          switch (call.state) {
            case 'ringing':
              if (call.direction === 'inbound') {
                // Incoming call
                updateCallStatus("Incoming support call");

                // Set a callback on the answer button and enable it
                answerButton.click(function() {
                  call.answer();
                });
                answerButton.prop("disabled", false);
              } else {
                // Outbound call ringing
                updateCallStatus("Ringing...");
              }
              break;

            case 'active':
              // Call connected
              console.log("Successfully established call!");
              hangUpButton.prop("disabled", false);
              callCustomerButtons.prop("disabled", true);
              callSupportButton.prop("disabled", true);
              answerButton.prop("disabled", true);

              // Determine who we're calling based on direction
              if (call.direction === 'outbound') {
                updateCallStatus("In call");
              } else {
                updateCallStatus("In call with customer");
              }
              break;

            case 'hangup':
            case 'destroy':
              // Call ended
              hangUpButton.prop("disabled", true);
              callCustomerButtons.prop("disabled", false);
              callSupportButton.prop("disabled", false);
              activeCall = null;
              updateCallStatus("Ready");
              break;
          }
        }
      });

    })
    .catch(function(err) {
      console.log(err);
      console.log("Could not get credentials from server!");
    });

  initNewTicketForm();
});

/* Call a customer from a support ticket */
function callCustomer(phoneNumber) {
  updateCallStatus("Calling " + phoneNumber + "...");

  if (client) {
    // Get the Telnyx phone number from a data attribute or config
    var callerNumber = $("#telnyx-phone-number").data('number') || '+15551234567';
    
    activeCall = client.newCall({
      destinationNumber: phoneNumber,
      callerNumber: callerNumber
    });
  }
}

/* Call the support_agent from the home page */
function callSupport() {
  updateCallStatus("Calling support...");

  if (client) {
    var callerNumber = $("#telnyx-phone-number").data('number') || '+15551234567';
    
    // This would dial the support agent's SIP identity
    // For direct dial to a support line, use a PSTN number
    // For browser-to-browser, use sip:identity@subdomain.sip.telnyx.com
    activeCall = client.newCall({
      destinationNumber: 'sip:support_agent@telnyx.sip.telnyx.com',
      callerNumber: callerNumber
    });
  }
}

/* End a call */
function hangUp() {
  if (activeCall) {
    activeCall.hangup();
    activeCall = null;
  }
}

function initNewTicketForm() {
  var formEl = $(".new-ticket");
  var buttonEl = formEl.find(".btn.btn-primary");

  // button handler
  formEl.find("[type='button']").click(function(e) {
    $.ajax({
        url: '/tickets/new',
        type: 'post',
        data: formEl.serialize()
    })
    .done(function(){
      showNotification("Support ticket was created successfully.", "success");
      // clear form
      formEl.find("input[type=text], textarea").val("");
    })
    .fail(function(res) {
      showNotification("Support ticket request failed. " + res.responseText, "danger");
    });
  });
}

function showNotification(text, style) {
  var alertStyle = "alert-"+style;
  var alertEl = $(".alert.ticket-support-notifications");

  if (alertEl.length == 0) {
    alertEl = $("<div class=\"alert ticket-support-notifications\"></div>");
    $("body").before(alertEl);
  }

  alertEl.removeClass (function (index, css) {
    return (css.match (/(^|\s)alert-\S+/g) || []).join(' ');
  });

  alertEl.addClass(alertStyle);
  alertEl.html(text);

  setTimeout(clearNotifications, 4000);
}

function clearNotifications() {
  var alertEl = $(".alert.ticket-support-notifications");
  alertEl.remove();
}
