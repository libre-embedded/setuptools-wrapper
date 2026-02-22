# =====================================
# generator=datazen
# version=3.2.3
# hash=46e33b13a25a530ae54714c2f0e7b221
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
        "3.13",
        "3.14",
    ],
}
setup(
    pkg_info,
    author_info,
)
