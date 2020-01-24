"""Transform Pylint information messages as warning messages.
Informational messages (such as useless-suppression) do not cause a
non-zero exit code in Pylint. As such, they don't break builds.
But we want broken builds for most informational messages!
"""

# This is not a real Pylint plugin. We abuse the fact that Pylint will
# call the `register()` before doing much, which lets us monkey-patch
# its code.
def register(linter):
    from pylint import constants

    constants.MSG_TYPES_STATUS["I"] = 1
