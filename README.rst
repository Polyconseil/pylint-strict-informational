===========================
Pylint Strict Informational
===========================

Pylint plugin to make it fail when an informational message (the "I" category) is found.

Pylint >= 2.4.0 is required (in order for ``pylint.constants`` module to exist).

Usage:

1. Install with ``pip install pylint-strict-informational``.

2. Add the plugin to the pyint configuration file (here in TOML):

   .. code:: toml

       [tool.pylint.MASTER]
       load-plugins = [
           "pylint_strict_informational",
       ]
