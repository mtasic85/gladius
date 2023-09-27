# CHANGELOG

## v0.1.8

Added:
* Gladius: `SF-Session-ID` header.
* Component: `sf-session-id` attr on `html` element.
* Html5: use `idiomorph` library as the swapping mechanism in `htmx`.

Changed:
* Gladius: Redefined `Event` to allow future definition of `Web Event`.
* DaisyUI: `Navbar` based on `html5.Div`, with custom `add` method.
* Html5: Swap only body on any event and optimize DOM update using `idiomorph`.
* Html5: Rename `sf_id` to `g_id`.
* Html5: Rename `sf_session_id` to `g_session_id`.
* Html5: Rename `SF-Session-ID` to `G-Session-ID`.
* HTML5, DaisyUI: Rename `default_tag` to `tag`.
* HTML5, DaisyUI: moved `htmx` scripts from DaisyUI to Html5.

Removed:
* consts: `_ontextchanged`, `_ontablechanged`.

## v0.1.7

Added:
* Component: `remove` child method.
* Component: `clone` method, with support for shallow and deep cloning.

Changed:
* DaisyUI: Upgraded from version `3.7.7` to `3.8.0`.
* Component: Simplified `Component.__init__` using `set_attr`.

Fixed:
* Component: `set_attr`, takes care of `class` and `id` attrs.
* CHANGELOG: fixed list markdown.

## v0.1.6

Added:
* HTML5: `set_attr`, `set_attr`, `del_attr`, `has_attr` methods.
* HTML5: High-level `Page` component.
* Example: `hello_world_2.py`.

Changed:
* DaisyUI: `Page` extends `html5.Page`.

Fixed:
* Component: do not attach `htmx` attributes for: html, head, meta, title, link, script, body, button, a, input, textarea
* DaisyUI: `NavbarButton` extends `html5.A`.
* DaisyUI: `Text` extends `html5.Span`.
* Html5: `hx-boots` on body.
* DaisyUI: `ht-target` attr added on `Navbar` and `Join` children.

## v0.1.5

Changed:
* Tailwind: Plugin `line-clamp` is included by default from Tailwind v3.3.
* Component: can be triggered now on custom event `_contentchange`.

Removed:
* Component: Removed need for `TextContentComponent`.

## v0.1.4

Added:
* Component: Added `TextContentComponent` for components that have text content in constructor.
* HTML5: H1, H2, H3, H4, P, BlockQuote, Figure, FigCaption, Strong, Em, Code.
* HTML5: Pre, Ol, Ul, Li, Table, THead, Tr, Th, Td, Img, Video, Source, Hr.
* HTML5: Button.
* DaisyUI: Hero, HeroContent.
* DaisyUI: Indicator, IndicatorItem.
* DaisyUI: Stack.
* DaisyUI: Toast, Alert.
* Examples: Layout.

Changed:
* Tailwind Plugins: forms, typography, aspect-ratio, line-clamp.
* DaisyUI: Button, support for text label in constructor.
* HTML5: Span is subclass of TextContentComponent.
* Component: `Component` go all features from `TextContentComponent`.

Removed:
* Examples: Artboard, Divider, Footer.

## v0.1.3

Added:
* Component: `add_class`, `remove_class`, `has_class` methods.
* DaisyUI: NavbarButton, Artboard, Divider, Footer, FooterTitle components.
* HTML5: A, Footer, Nav, Header.

Changed:
* Examples, rename `dui` to `d`.
* Rename `prop{s}` to `attr{s}` because of HTML convention.
* Rename attr `sf_id` to be `sf-id`.
* Renamed `EventRequest` to `Event`.
* Updated DaisyUI from `2.6.0` to `3.7.7`.
* DaisyUI: `Join` component adds default class `join-item` to its children.

Fixed:
* Component registration of ComponentLibrary's sub-classes.
* Read `event: Event` from HTTP headers, and pass to callback.

## v0.1.2

Added:
* HTML5 Components: Html, Head, Meta, Link, Title, Script, Body, Div, Span.
* Added example: hello_world_1.

Changed:
* Component uses `hx-target='[sf_id="ID"]'` instead of `hx-target="#ID"`.
* Moved Html5 Components into independent module `html5`.

Fixed:
* Cyclic reference imports.
* Fixed examples: multi_page_0, hello_world_0.

## v0.1.1

Fixed:
* Text got custom event `_ontextchange`, so it can detect changes.

## v0.1.0

Added:
* Initial version based on aiohttp, uvloop, htmx, TailwindCSS, DaisyUI.
