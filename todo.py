class Todo:
    SYMBOL_DONE = 'X'
    SYMBOL_NOT_DONE = ' '
    def __init__(self, title):
        self._title = title
        self.done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    def __str__(self):

        return f"[{Todo.SYMBOL_DONE if self.done
                   else Todo.SYMBOL_NOT_DONE}] {self.title}"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return self.title == other.title and self.done == other.done
