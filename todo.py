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
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        return all(todo.done for todo in self._todos)

    def remove_at(self, idx):
        del self._todos[idx]

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)
        for todo in filter(callback, self._todos):
            new_list.add(todo)

        return new_list

    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.first()

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, title):
        todo = self.find_by_title(title)
        todo.done = True





empty_todo_list = TodoList('Nothing Doing')

def setup():

    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list


def step_8():
    print('--------------------------------- Step 8')
    todo_list = setup()

    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [X] Clean room
    # [ ] Go to gym

    todo_list.mark_all_done()
    print(todo_list)
    # ---- Today's Todos -----
    # [X] Buy milk
    # [X] Clean room
    # [X] Go to gym

    todo_list.mark_all_undone()
    print(todo_list)
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Clean room
    # [ ] Go to gym

step_8()

