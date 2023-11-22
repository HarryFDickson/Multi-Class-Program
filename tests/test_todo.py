from lib.todo_list import *
from lib.todo_task import *

def test_todo_returns_nothing():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

def test_todo_returns_an_incomplete_task():
    todo_list = TodoList()
    task = Todo("Complete this damn task")
    todo_list.add(task)
    assert todo_list.incomplete() == [task]

def test_todo_complete_returns_all_tasks_after_give_up():
    todo_list = TodoList()
    task = Todo("Complete this damn task")
    todo_list.add(task)
    todo_list.give_up()
    assert todo_list.complete() == [task]

def test_todo_complete_returns_all_tasks_after_mark_complete():
    todo_list = TodoList()
    task = Todo("Complete this damn task")
    task.mark_complete()
    todo_list.add(task.task, task.value)
    assert todo_list.complete() == ["Complete this damn task"]