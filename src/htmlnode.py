class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        new_string = ""
        if self.props == None:
            return new_string
        for key, value in self.props.items():
            new_string += f' {key}="{value}"'
        return new_string
    
    def __repr__(self):
        return  f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, value):
        if self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props:
            return True
        return False

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag missing!")
        if self.children == None:
            raise ValueError("Children missing!")
        new_string = ""
        if len(self.children) == 0:
            return f"<{self.tag}>{new_string}</{self.tag}>"
        for child in self.children:
            new_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{new_string}</{self.tag}>"
            
        


