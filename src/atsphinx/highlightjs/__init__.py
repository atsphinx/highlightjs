"""Override code-block output for highlight.js."""
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util import logging
from sphinx.util.docutils import SphinxTranslator

__version__ = "0.1.1"

here = Path(__file__).parent
logger = logging.getLogger(__name__)


def register_ext_static(app: Sphinx, config: Config):
    """Use packages' static folder in Sphinx."""
    if not hasattr(config, "html_static_path"):
        config.html_static_path = []
    config.html_static_path += [str(here / "_static")]


def register_highlightjs(app: Sphinx):
    """Append static contents to highlight by highlight.js.

    It works only html-style builder.
    """
    if app.builder.format != "html":
        logger.info("Builder does not generate HTML files. Skip proc of it.")
        return
    app.builder.add_css_file(
        "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/default.min.css"  # noqa: E501
    )
    app.builder.add_css_file("highlight.css")
    app.builder.add_js_file(
        "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js"  # noqa: E501
    )
    app.builder.add_js_file("highlight.js")


def visit_literal_block(
    self: SphinxTranslator, node: nodes.literal_block
):  # noqa: D103
    lang = node["language"]
    code = node.rawsource
    if "hl_lines" in node["highlight_args"]:
        splitted = node.rawsource.split("\n")
        code = "\n".join(
            splitted[line - 1] for line in node["highlight_args"]["hl_lines"]
        )
    self.body.append(f'<pre><code class="language-{lang}">{code}</code></pre>')
    raise nodes.SkipNode


def depart_literal_block(
    self: SphinxTranslator, node: nodes.literal_block
):  # noqa: D103
    pass


def setup(app: Sphinx):  # noqa: D103
    app.connect("config-inited", register_ext_static)
    app.connect("builder-inited", register_highlightjs)
    app.add_node(
        nodes.literal_block,
        override=True,
        html=(visit_literal_block, depart_literal_block),
    )
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
