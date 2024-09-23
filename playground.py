
class Page:

    def click(self):
        print('Clicking')

    def input_text(self, text):
        print(f"Entering text {text}")

    def find_element(self):
        print('Searching for element')

class LoginPage(Page):
    pass

page = Page()
page.input_text('some text')
page.click()


