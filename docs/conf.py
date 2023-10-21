# noqa: D100
from atsphinx.highlightjs import __version__

# -- Project information
project = "atsphinx-highlightjs"
copyright = "2023, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = [
    "atsphinx.highlightjs",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for extensions
