class TextNode:
  def __init__(self, text, text_type, url):
    self.text = text
    self.text_type = text_type
    self.url = url

    if not url:
      self.url = None
  
  def __eq__(textnode_1, textnode_2):
    if textnode_1 == textnode_2:  # change to check ALL properties !!
      return True
    
  def __repr__():
    pass
    '''
    returns a string representation of the TextNode object. It should look like this:
    TextNode(TEXT, TEXT_TYPE, URL)

    Where TEXT, TEXT_TYPE, and URL are the values of the text, text_type, and url properties, respectively.
    '''