class Dom:
    def __init__(self, text, siblings):
        self.text = text
        self.siblings = siblings

def dom_visiting(dom):
    print(dom.text)
    if len(dom.siblings) == 0:
        return
    for sibling in dom.siblings:
        dom_visiting(sibling)
