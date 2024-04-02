class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not Implemented")
    def props_to_html(self):
        if self.props == None:
            return ""
        html = ""
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html
    def __repr__(self):
        print(self.tag)
        print(self.value)
        print(self.children)
        print(self.props)
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is Empty")
        elif self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        elif self.children is None:
            raise ValueError("No children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"       