from unittest.mock import patch

from mailer import send_report


@patch("mailer.smtplib.SMTP")
def test_send_report(mock_smtp):
    mock_instance = mock_smtp.return_value.__enter__.return_value

    send_report("test@example.com", "report.xlsx")

    mock_instance.login.assert_called_once()
    mock_instance.send_message.assert_called_once()