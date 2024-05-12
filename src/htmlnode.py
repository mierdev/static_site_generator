class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props is not None:
      assembled_props = []
      for prop in self.props:
        assembled_props.append(f"{prop}=\"{self.props[prop]}\" ")
      return assembled_props  # FIXME: this returns wrong things, a list instead of a string and no spaces between
    
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"