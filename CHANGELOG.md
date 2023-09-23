# CHANGELOG

## v0.1.x

Todo:
    - Fix Text element.
    - Fix Component registration of ComponentLibrary's sub-classes.

## v0.1.2

Added:
    - HTML5 Components: Html, Head, Meta, Link, Title, Script, Body, Div, Span.
    - Added example: hello_world_1.

Changed:
    - Component uses `hx-target='[sf_id="ID"]'` instead of `hx-target="#ID"`.
    - Moved Html5 Components into independent module `html5`.

Fixed:
    - Cyclic reference imports.
    - Fixed examples: multi_page_0, hello_world_0.

## v0.1.1

Fixed:
    - Text got custom event `_ontextchange`, so it can detect changes.

## v0.1.0

Added:
    - Initial version based on aiohttp, uvloop, htmx, TailwindCSS, DaisyUI.
