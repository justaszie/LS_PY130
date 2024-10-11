import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(len(self.todos), 3)

    def test_to_list(self):
        self.assertEqual(self.todos.to_list(), [self.todo1, self.todo2, self.todo3])

    def test_first(self):
        self.assertEqual(self.todos.first(), self.todo1)

    def test_last(self):
        self.assertEqual(self.todos.last(), self.todo3)

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())
        self.todos.mark_all_undone()

    def test_add_invalid(self):
        # 2 different formats of asserting that exception is raised
        self.assertRaises(TypeError, self.todos.add, 'Todo as a String')

        with self.assertRaises(TypeError):
            self.todos.add(123)

    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(20)

        self.assertIs(self.todos.todo_at(0), self.todo1)

    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(20)

        self.todos.mark_done_at(0)
        self.assertFalse(self.todo2.done)
        self.assertTrue(self.todo1.done)

    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(20)

        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True

        self.assertTrue(self.todo1.done)
        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_mark_all_done(self):
        self.todo1.done, self.todo2.done, self.todo3.done = False, False, False

        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(20)

        self.todos.remove_at(0)
        self.assertNotIn(self.todo1, self.todos.to_list())

    def test_str(self):
        """
        result = f"---- {self.title} -----"
        for todo in self._todos:
            result += f"\n{todo}"

        return result

        o("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")


        Todo str:
        [{Todo.SYMBOL_DONE if self.done
                   else Todo.SYMBOL_NOT_DONE}] {self.title}"
        """
        expected =  "---- Today's Todos ----\n" \
            "[ ] Buy milk\n" \
            "[ ] Clean room\n" \
            "[ ] Go to the gym" \

        actual = str(self.todos)
        self.assertEqual(actual, expected)

    def test_str_done_todo(self):
        self.todo1.done = True

        expected =  "---- Today's Todos ----\n" \
            "[X] Buy milk\n" \
            "[ ] Clean room\n" \
            "[ ] Go to the gym" \

        actual = str(self.todos)
        self.assertEqual(actual, expected)

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()

        expected =  "---- Today's Todos ----\n" \
            "[X] Buy milk\n" \
            "[X] Clean room\n" \
            "[X] Go to the gym" \

        actual = str(self.todos)
        self.assertEqual(actual, expected)

    def test_each(self):
        result = []
        self.todos.each(lambda x: result.append('1.' + x.title))

        self.assertEqual(result, ['1.Buy milk', '1.Clean room', '1.Go to the gym'])


    def test_select(self):
        self.todo1.done = True
        self.todo2.done = True

        new_list = self.todos.select(lambda todo: todo.done)

        self.assertEqual(new_list.to_list(), [self.todo1, self.todo2])



if __name__ == "__main__":
    unittest.main()