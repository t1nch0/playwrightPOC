
class BasePage:
    def __init__(self, page):
        self.page=page
    
    def goto(self, url):
        self.page.goto(url)
    
    def clickOn(self,selector):
        self.page.click(selector)
    
    def fill(self, selector, text):
        self.page.fill(selector, text)
    
    def getText(self, selector):
        return self.page.text_content(selector)
    
    def isVisible(self, selector):
        return self.page.is_visible(selector)
    