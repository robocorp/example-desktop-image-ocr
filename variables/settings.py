import os
import sys

GNUCASH_EXECUTABLE = {
    "linux": "gnucash",
    "darwin": "/Applications/Gnucash.app/Contents/MacOS/Gnucash",
    "win32": "C:/Program Files (x86)/gnucash/bin/gnucash",
}[sys.platform]

GNUCASH_DATABASE = os.path.join(
    os.getenv("ROBOT_ROOT", ""), "resources", "demo.gnucash"
)

GNUCASH_LOCK_FILE = os.path.join(
    os.getenv("ROBOT_ROOT", ""), "resources", "demo.gnucash.LCK"
)
