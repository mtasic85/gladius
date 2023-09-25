# CHANGELOG

## v0.1.4

Added:
    - Component: Added `TextContentComponent` for components that have text content in constructor.
    - HTML5: H1, H2, H3, H4, P, BlockQuote, Figure, FigCaption, Strong, Em, Code.
    - HTML5: Pre, Ol, Ul, Li, Table, THead, Tr, Th, Td, Img, Video, Source, Hr.
    - HTML5: Button.
    - DaisyUI: Hero, HeroContent.
    - DaisyUI: Indicator, IndicatorItem.
    - DaisyUI: Stack.
    - DaisyUI: Toast, Alert.
    - Examples: Layout.

Changed:
    - Tailwind Plugins: forms, typography, aspect-ratio, line-clamp.
    - DaisyUI: Button, support for text label in constructor.
    - HTML5: Span is subclass of TextContentComponent.
    - Component: `Component` go all features from `TextContentComponent`.

Removed:
    - Examples: Artboard, Divider, Footer.

## v0.1.3

Added:
    - Component: `add_class`, `remove_class`, `has_class` methods.
    - DaisyUI: NavbarButton, Artboard, Divider, Footer, FooterTitle components.
    - HTML5: A, Footer, Nav, Header.

Changed:
    - Examples, rename `dui` to `d`.
    - Rename `prop{s}` to `attr{s}` because of HTML convention.
    - Rename attr `sf_id` to be `sf-id`.
    - Renamed `EventRequest` to `Event`.
    - Updated DaisyUI from `2.6.0` to `3.7.7`.
    - DaisyUI: `Join` component adds default class `join-item` to its children.

Fixed:
    - Component registration of ComponentLibrary's sub-classes.
    - Read `event: Event` from HTTP headers, and pass to callback.

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
