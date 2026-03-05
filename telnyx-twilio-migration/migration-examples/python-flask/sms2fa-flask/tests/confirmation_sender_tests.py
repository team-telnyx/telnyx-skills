from .base import BaseTest
from flask import session
from sms2fa_flask import confirmation_sender
from mock import patch
from mock import MagicMock


class ConfirmationSenderTest(BaseTest):

    def test_sender_creates_a_message(self):
        # Set Telnyx config for testing
        self.app.config['TELNYX_API_KEY'] = 'test_key'
        self.app.config['TELNYX_PHONE_NUMBER'] = '+15551230987'
        
        confirmation_sender.generate_code = MagicMock(return_value='random_code')
        with patch('sms2fa_flask.confirmation_sender.Telnyx') as mock_telnyx_class:
            mock_client = MagicMock()
            mock_telnyx_class.return_value = mock_client
            mock_client.messages.send.return_value = MagicMock(id='msg_test_id')
            
            confirmation_sender.send_confirmation_code('+15551234321')
            
            mock_client.messages.send.assert_called_once()
            # Verify the call used correct parameters
            call_args = mock_client.messages.send.call_args
            self.assertEqual(call_args[1]['to'], '+15551234321')
            self.assertEqual(call_args[1]['text'], 'random_code')
            self.assertEqual(call_args[1]['from_'], '+15551230987')
            self.assertEqual('random_code', session.get('verification_code'))
