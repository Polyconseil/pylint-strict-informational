===========================
Pylint Strict Informational
===========================

   As of pylint 2.9.0, the `fail-on=I configuration option <https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html#fail-on>`_
   can be used instead of this plugin. Therefore, this plugin is deprecated.

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
