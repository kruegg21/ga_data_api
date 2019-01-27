# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module level variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import logging

import _send_notification  # pylint: disable=import-error
import _settings_accessor  # pylint: disable=import-error


_SETTINGS = _settings_accessor.SettingsAccessor()
_LOGGER = logging.getLogger(__name__)
_HANDLER = _send_notification.EmailHandler()
_LOGGER.addHandler(_HANDLER)
_LOGGER.setLevel(logging.WARNING)


def main():
    """Main function."""
    _LOGGER.warning('here')


if __name__ == '__main__':
    main()
