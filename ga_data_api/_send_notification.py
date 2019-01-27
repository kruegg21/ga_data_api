# -*- coding: utf-8 -*-
"""Send email alerts.

This module contains classes that create objects for sending email alerts.

Attributes:
    settings (_settings_accessor.SettingsAccessor): Interfaces with various
        module settings.

    logger (logging.Logger): Logger set to DEBUG level and configured using
        logging.json, if such file exists.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    =

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import email
import logging.config
import smtplib

import _settings_accessor  # pylint: disable=import-error


_SETTINGS = _settings_accessor.SettingsAccessor()
logging.config.dictConfig(_SETTINGS.logging_config)
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class EmailHandler(logging.StreamHandler):
    """Email handler for logging.

    Custom logging handler for sending emails.

    Written because of issues with logging.handlers.SMTPHandler class.

    """

    def emit(self, record):
        try:
            message = self.format(record)
            msg = email.message.EmailMessage()
            msg['From'] = _SETTINGS.email_address
            msg['To'] = ', '.join(_SETTINGS.admin_addresses)
            msg['Subject'] = 'Hello'
            msg.set_content(message)
            smtp = smtplib.SMTP(_SETTINGS.email_host)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(_SETTINGS.email_address, _SETTINGS.email_password)
            smtp.send_message(msg)
            smtp.quit()
            _LOGGER.info('email message sent')
        except smtplib.SMTPServerDisconnected as error_message:
            _LOGGER.debug(error_message)
        except smtplib.SMTPAuthenticationError as error_message:
            _LOGGER.debug(error_message)
        except OSError as error_message:
            _LOGGER.debug(error_message)
            _LOGGER.debug('Poorly formed port number in email credentials')
