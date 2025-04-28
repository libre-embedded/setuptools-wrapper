# =====================================
# generator=datazen
# version=3.2.3
# hash=03ae76005fb2fd1fc4c78694d143fdc7
# =====================================

"""
setuptools-wrapper - Package definition for distribution.
"""

# internal
from setuptools_wrapper import DESCRIPTION, PKG_NAME, VERSION

try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from setuptools_wrapper_bootstrap.setup import setup  # type: ignore

author_info = {
    "name": "Libre Embedded",
    "email": "vaughn@libre-embedded.com",
    "username": "libre-embedded",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.12",
        "3.13",
    ],
}
setup(
    pkg_info,
    author_info,
)
