from data_structures import Stack, reverse_string
from data_structures import Queue


#############
# Stack Tests
#############


def test_create_empty_stack():
    stack = Stack()

    assert stack.size() == 0


def test_create_stack_with_single_item():
    stack = Stack()
    stack.push('a')

    assert stack.size() == 1


def test_peak_at_stack():
    stack = Stack()
    stack.push('a')

    assert stack.peek() == 'a'


def test_stack_pop():
    stack = Stack()
    stack.push('a')
    item = stack.pop()

    assert item == 'a'


def test_stack_is_empty():
    stack = Stack()
    stack.push('a')
    stack.pop()

    assert stack.is_empty() is True


def test_reverse_string():
    my_string = '123'

    assert reverse_string(my_string) == '321'


#############
# Queue Tests
#############

def test_enqueue_item():
    q = Queue()
    q.enqueue(1)

    assert q.is_empty() is False


def test_dequeue_item():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    item = q.dequeue()

    assert item == 1


def test_queue_size():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.size() == 3
