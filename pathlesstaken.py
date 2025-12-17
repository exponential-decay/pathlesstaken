"""User facing entry point for pathlesstaken for anyone running the
code from the repository and not pypi.
"""

import sys

from src.pathlesstaken import pathlesstaken

sys.dont_write_bytecode = True


def main():
    """Primary entry point for this script."""
    pathlesstaken.main()


if __name__ == "__main__":
    main()
