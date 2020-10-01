import fibonacci_heap as module

def test_create():
    try:
        assert module.FibonacciHeap() is not None
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


def test_min_of_0():
    fib_heap = module.FibonacciHeap()
    try:
        assert (fib_heap.find_min() is None)
    except Exception:
        print("ERROR: test_min_of_0")
        return False
    else:
        print("OK: test_min_of_0")
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
        assert (fib_heap.min_node is not None)

    except Exception as err:
        print("ERROR: test_extract_of_3", err)
        return False
    else:
        print("OK: test_extract_of_3")
        return True




def test_heap():
    fib_heap = module.FibonacciHeap()
    try:
        fib_heap.insert(5)
        fib_heap.insert(1)
        fib_heap.insert(10)
        fib_heap.insert(0)
        fib_heap.insert(42)
        fib_heap.insert(15)
        fib_heap.insert(7)
        fib_heap.insert(19)
        fib_heap.insert(20)
        fib_heap.insert(2)
        fib_heap.insert(84)
        fib_heap.insert(50)

        while True:
            fib_heap.display()
            node = fib_heap.delete_min()
            if node is None:
                break
    except Exception as err:
        print("ERROR: test_heap", err)
        return False
    else:
        print("OK: test_heap")
        return True



def test_merge_None():
    fib_heap1 = module.FibonacciHeap()
    try:
        fib_heap1.insert(5)
        fib_heap1.insert(1)
        fib_heap1.insert(10)
        fib_heap1.display()
        fib_heap1.merge(None)

        assert (fib_heap1.size == 3)

    except Exception as err:
        print("ERROR: test_merge_None", err)
        return False
    else:
        print("OK: test_merge_None")
        return True

def test_merge_small():
    fib_heap1 = module.FibonacciHeap()
    fib_heap2 = module.FibonacciHeap()
    try:
        fib_heap1.insert(5)
        fib_heap1.insert(1)
        fib_heap1.insert(10)
        fib_heap1.display()

        fib_heap2.insert(3)
        fib_heap2.display()

        fib_heap2.merge(fib_heap1)
        fib_heap2.display()
        assert (fib_heap2.size == 4)
        assert (fib_heap2.find_min() == 1)

    except Exception as err:
        print("ERROR: test_merge_small", err)
        return False
    else:
        print("OK: test_merge_small")
        return True

def test_merge():
    fib_heapOdd = module.FibonacciHeap()
    fib_heapEven = module.FibonacciHeap()
    try:
        fib_heapOdd.insert(3)
        fib_heapOdd.insert(7)
        fib_heapOdd.insert(1)
        fib_heapOdd.insert(5)
        fib_heapOdd.insert(11)
        fib_heapOdd.display()

        fib_heapEven.insert(8)
        fib_heapEven.insert(2)
        fib_heapEven.insert(4)
        fib_heapEven.display()

        fib_heapEven.merge(fib_heapOdd)
        fib_heapEven.display()
        assert (fib_heapEven.size == 8)
        assert (fib_heapEven.find_min() == 1)

    except Exception as err:
        print("ERROR: test_merge", err)
        return False
    else:
        print("OK: test_merge")
        return True

def test_merge_with_children():
    fib_heapOdd = module.FibonacciHeap()
    fib_heapEven = module.FibonacciHeap()
    try:
        fib_heapOdd.insert(3)
        fib_heapOdd.insert(7)
        fib_heapOdd.insert(1)
        fib_heapOdd.insert(5)
        fib_heapOdd.insert(11)
        # consolidate will create children when needed
        fib_heapOdd.consolidate()
        fib_heapOdd.display()

        fib_heapEven.insert(8)
        fib_heapEven.insert(2)
        fib_heapEven.insert(4)
        # consolidate will create children when needed
        fib_heapEven.consolidate()
        fib_heapEven.display()

        fib_heapEven.merge(fib_heapOdd)
        fib_heapEven.display()
        assert (fib_heapEven.size == 8)
        assert (fib_heapEven.find_min() == 1)

    except Exception as err:
        print("ERROR: test_merge_with_children", err)
        return False
    else:
        print("OK: test_merge_with_children")
        return True



def main():
    test_create()
    test_insert_1()
    test_insert_int_as_string()
    test_insert_string()
    test_min_of_0()
    test_min_of_1()
    test_min_of_7()
    test_extract_of_3()
    test_merge_None()
    test_merge_small()
    test_merge()
    test_merge_with_children()
    test_heap()

main()

