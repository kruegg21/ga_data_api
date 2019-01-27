# -*- coding: utf-8 -*-
"""Send email alerts.

This module contains classes that create objects for sending email alerts.

Todo:
    * Make classes

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import email
import logging.handlers
import smtplib

import _settings_accessor  # pylint: disable=import-error


_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.StreamHandler())
_LOGGER.setLevel(logging.DEBUG)
_SETTINGS = _settings_accessor.SettingsAccessor()


class EmailHandler(logging.StreamHandler):
    """
    A handler class which allows the cursor to stay on
    one line for selected messages
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
        except smtplib.SMTPAuthenticationError as e:
            _LOGGER.debug(e)
            _LOGGER.debug('Authentication error with your email credentials')
