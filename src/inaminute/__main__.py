"""Get delayed

Usage:
------

    $ inaminute 

    
Version:
--------

- inaminute v1.0.0
"""
# imports
import sys
from inaminute import delay


def main() -> None:
    """Read the Real Python article feed."""
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    text=delay.message()
    if len(args)>0 or len(opts)>0:
        print(text.upper())
    else:
        print(text)

if __name__ == "__main__":
    main()
