from textnode import TextNode
from htmlnode import HTMLNode


def main():
  test_text = TextNode("This is a text node", "bold", "https://www.boot.dev")
  print(test_text)

  test_html = HTMLNode("p", "Boots is a BEAR!", [], {"text-align": "center"})
  print(test_html)


if __name__ == "__main__":
    main()