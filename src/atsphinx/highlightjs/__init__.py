"""Override code-block output for highlight.js"""
from pathlib import Path

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.util.docutils import SphinxTranslator

__version__ = "0.0.0"
here = Path(__file__).parent


def register_ext_static(app: Sphinx, config: Config):
    if not hasattr(config, "html_static_path"):
        config.html_static_path = []
    config.html_static_path += [str(here / "_static")]


def register_highlightjs(app: Sphinx):
    """Append static contents to highlight by highlight.js."""
    app.builder.add_css_file("https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/styles/default.min.css")
    app.builder.add_css_file("highlight.css")
    app.builder.add_js_file("https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/highlight.min.js")
    app.builder.add_js_file("highlight.js")


def visit_literal_block(self: SphinxTranslator, node: nodes.literal_block):
    lang = node["language"]
    code = node.rawsource
    if "hl_lines" in node["highlight_args"]:
        splitted = node.rawsource.split("\n")
        code = "\n".join(
            splitted[line-1]
            for line in node["highlight_args"]["hl_lines"]
        )
    self.body.append(f'<pre><code class="language-{lang}">{code}</code></pre>')
    raise nodes.SkipNode


def depart_literal_block(self: SphinxTranslator, node: nodes.literal_block):
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
