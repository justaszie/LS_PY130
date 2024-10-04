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

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo_item):
        if not isinstance(todo_item, Todo):
            raise TypeError('The item type should be Todo')

        self._todos.append(todo_item)

    def __str__(self):
        result = f"---- {self.title} -----"
        for todo in self._todos:
            result += f"\n{todo}"

        return result

    def __len__(self):
        return len(self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos.copy()

    def todo_at(self, idx):
        return self._todos[idx]

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True

    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False

    def mark_all_done(self):
        # On purpose not accessing the underlying list directly
        # Going through the public methods instead for better abstraction
        for idx in range(len(self)):
            self.mark_done_at(idx)

    def mark_all_undone(self):
        for idx in range(len(self)):
            self.mark_undone_at(idx)

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, idx):
        del self._todos[idx]
