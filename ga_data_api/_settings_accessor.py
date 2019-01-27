# -*- coding: utf-8 -*-
"""Settings accessor.

This module contains classes for accessing settings for module. Used to
abstract settings so they can be read from a variety of sources.

Attributes:
    EMAIL_ADDRESS (str): Admin email account (address we want to send alerts
        from).

    EMAIL_PASSWORD (str): Admin email password.

Todo:

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import logging
import os

import hjson

_LOGGER = logging.getLogger(__name__)
_LOGGER.addHandler(logging.StreamHandler())
_LOGGER.setLevel(logging.DEBUG)
_EMAIL_HJSON_PATH = os.path.join(os.path.dirname(__file__), 'settings')
_EMAIL_HJSON_FILE_NAME = 'email.hjson'


def _attempt_read_file(file):
    try:
        with open(file) as f:
            return hjson.load(f)
    except FileNotFoundError as e:
        _LOGGER.error(e)
        _LOGGER.debug('This means WARNING and ERROR emails will not '
                      'be sent to you')


_EMAIL_CONFIG = _attempt_read_file(os.path.join(_EMAIL_HJSON_PATH, _EMAIL_HJSON_FILE_NAME))


def email_config_exists():
    """Check if email config file exists.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    return True if _EMAIL_CONFIG else False


class SettingsAccessor:
    """Settings accessor

    Used to access configuration settings.
    """

    def __init__(self):
        pass

    def __str__(self):
        return '\n'.join([
            'Email Address: {address}'.format(address=self.email_address),
            'Email Password: {password}'.format(password=self.email_password),
        ])

    @property
    def email_address(self):
        """str: string of email address of Admin."""
        return _EMAIL_CONFIG.get('address', None)

    @property
    def email_password(self):
        """str: string of email password of Admin."""
        return _EMAIL_CONFIG.get('password', None)

    @property
    def credentials(self):
        """str: string of email password of Admin."""
        return self.email_address, self.email_password

    @property
    def admin_addresses(self):
        """list: list of email password of Admins."""
        return _EMAIL_CONFIG.get('admin_addresses', None)

    @property
    def email_host(self):
        """list: list of email password of Admins."""
        return _EMAIL_CONFIG.get('host', None)
