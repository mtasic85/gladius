
class BaseElement:
    ctx: Gladius | None = None
    tag: str | None = None
    attrs: dict | None = None

    # A void element is an element in HTML that cannot have any child nodes
    # (i.e., nested elements or text nodes).
    # Void elements only have a start tag;
    # end tags must not be specified for void elements.
    # https://developer.mozilla.org/en-US/docs/Glossary/Void_element
    void_element: bool | None = None


class VoidElement(BaseElement):
    void_element: bool = True


class Element(BaseElement):
    void_element: bool | None = False
    children: list[BaseElement] | None = []
