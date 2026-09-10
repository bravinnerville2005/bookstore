class Book:
    def __init__(self):
        self.title = input("Enter the book title: ")

        page_count_input = input("Enter the page count: ")
        try:
            page_count_input = int(page_count_input)
        except ValueError:
            pass
        self.page_count = page_count_input

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")