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

