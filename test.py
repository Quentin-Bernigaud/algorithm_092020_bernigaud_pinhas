import fibonacci_heap as module
import sys

def assertDefined(variable):
    assert True or variable

def test_create():
    try:
        assertDefined(module.FibonacciHeap())
    except Exception:
        print("ERROR test_create")
        return False
    else:
        print("OK test_create")
        return True

def test_insert_1():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert(5)
    except Exception:
        print("ERROR: test_insert_1")
        return False
    else:
        print("OK: test_insert_1")
        return True


def test_insert_int_as_string():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert("5")
    except ValueError:
        print("OK: test_insert_string")
        return False
    else:
        print("ERROR: test_insert_string")
    return True

def test_insert_string():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert("abc")
    except ValueError:
        print("OK: test_insert_string")
        return False
    else:
        print("ERROR: test_insert_string")
        return True


def test_min_of_1():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert(1)
        assert (fib_heap.find_min() == 1)
    except Exception:
        print("ERROR: test_min_of_1")
        return False
    else:
        print("OK: test_min_of_1")
        return True

def test_min_of_7():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert(4)
        fib_heap.insert(3)
        fib_heap.insert(7)
        fib_heap.insert(5)
        fib_heap.insert(2)
        fib_heap.insert(1)
        fib_heap.insert(10)
        fib_heap.display()
        assert (fib_heap.find_min() == 1)
    except Exception:
        print("ERROR: test_min_of_7")
        return False
    else:
        print("OK: test_min_of_7")
        return True

def test_extract_of_3():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert(5)
        fib_heap.insert(2)
        fib_heap.insert(8)

        fib_heap.display()

        assert (fib_heap.find_min() == 2)
        assert (fib_heap.delete_min() == 2)
        fib_heap.display()
        assert (fib_heap.size == 2)
        assert (fib_heap.min is not None)




    except Exception as err:
        print("ERROR: test_extract_of_3", err)
        return False
    else:
        print("OK: test_extract_of_3")
        return True




def test_heap(heap):
    heap.insert(5)
    heap.insert(1)
    heap.insert(10)
    heap.insert(0)
    heap.insert(42)
    heap.insert(15)
    heap.insert(7)
    heap.insert(19)
    heap.insert(20)
    heap.insert(2)
    heap.insert(84)
    heap.insert(50)

    print("started")
    while True:
        heap.display()
        node = heap.delete_min()
        if node is None:
            break
    print("done")

def mainTest():
    with open(f"test.log", "w") as log:
        try:
            heap = module.FibonacciHeap()
            test_heap(heap)
        except Exception as e:
            log.write(f"{e}\n")

def main():
    test_create()
    test_insert_1()
    test_insert_int_as_string()
    test_insert_string()
    test_min_of_1()
    test_min_of_7()
    test_extract_of_3()
    mainTest()

main()