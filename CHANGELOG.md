# CHANGELOG

## v0.1.2

Added:
    - HTML5 Components: Html, Head, Meta, Link, Title, Script, Body, Div, Span.

Changed:
    - Component uses `hx-target='[sf_id="ID"]'` instead of `hx-target="#ID"`.
    - Moved Html5 Components into independent module `html5`.

Fixed:
    - Cyclic reference imports.

## v0.1.1

Fixed:
    - Text got custom event `_ontextchange`, so it can detect changes.

## v0.1.0

Added:
    - Initial version based on aiohttp, uvloop, htmx, TailwindCSS, DaisyUI.
