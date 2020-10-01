import sys
import math

class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """



    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass

class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0 # Degree of the node
        self.mark = 'W'#  Black or white mark of the node
        self.c = 'N' # Flag for assisting in the Find node function


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des données efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """
    def __init__(self):
        # self.nodes = []
        self.size = 0
        self.min = None

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        if not isinstance(value, int):
            raise ValueError

        try:
            new_node = Node(value)
            if self.min is None:
                # first item is min ;)
                self.min = new_node
            else:
                # insertion
                (self.min.left).right = new_node
                new_node.right = self.min
                new_node.left = self.min.left
                self.min.left = new_node
                # min check
                if (new_node.value < self.min.value):
                    self.min = new_node

            self.size += 1
        except Exception :
            print("ERROR: insert value ", sys.exc_info()[0])

        pass

    def display(self):
        """
        Display Heap information
        """
        current = self.min
        if current is None:
            print(" - Empty FibonacciHeap")
        else:
            print(" - FibonacciHeap has {:d} nodes, min is {:d}, root nodes are: ".format(  self.size,  self.find_min()), end='' )
            while True:
                print(current.value, end='')
                current = current.right
                if (current != self.min):
                    print("-->", end='')
                # end of while ?
                if current == self.min or current.right is None:
                    print("") # new line
                    break




    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        return self.min.value


    # // Linking the heap nodes in parent child relationship
    def Fibonnaci_link(self, ptr2: Node,  ptr1: Node):
        ptr2.left.right = ptr2.right
        ptr2.right.left = ptr2.left
        if ptr1.right == ptr1:
            self.min = ptr1
        ptr2.left = ptr2
        ptr2.right = ptr2
        ptr2.parent = ptr1
        if ptr1.child is None:
            ptr1.child = ptr2
        ptr2.right = ptr1.child
        ptr2.left = ptr1.child.left
        ptr1.child.left.right = ptr2
        ptr1.child.left = ptr2
        if ptr2.value < ptr1.child.value:
            ptr1.child = ptr2
        ptr1.degree+=1

    # Consolidating the heap
    def Consolidate(self):
        # temp1
        temp2 = math.log(self.size,2)
        temp3 = math.floor(temp2)

        arr = [None] * (temp3+1)

        ptr1 = self.min
        ptr2 = None
        ptr3 = None
        ptr4 = ptr1

        while True:
            ptr4 = ptr4.right
            temp1 = ptr1.degree
            while arr[temp1] is not None:
                ptr2 = arr[temp1]
                if ptr1.value > ptr2.value:
                    # swap TODO ptr1, ptr2 = ptr2, ptr1
                    ptr3 = ptr1
                    ptr1 = ptr2
                    ptr2 = ptr3

                if ptr2 == self.min:
                    self.min = ptr1

                self.Fibonnaci_link(ptr2, ptr1)
                if ptr1.right == ptr1:
                    self.min = ptr1

                arr[temp1] = None
                temp1+=1 #end while

            arr[temp1] = ptr1
            ptr1 = ptr1.right
            if ptr1 == self.min:
                break # end while True

        self.min = None
        # TODO for arrj in arr
        for j in range (0,  temp3):
            if arr[j] is not None:
                arr[j].left = arr[j]
                arr[j].right = arr[j]
                if self.min is not None:
                    self.min.left.right = arr[j]
                    arr[j].right = self.min
                    arr[j].left = self.min.left
                    self.min.left = arr[j]
                    if arr[j].value < self.min.value:
                        self.min = arr[j]
                else:
                    self.min = arr[j]

                if self.min is None:
                    self.min = arr[j]
                elif arr[j].value < self.min.value:
                        self.min = arr[j]

    # extract_min
    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        if self.min is None:
            print(" - Empty FibonacciHeap")
            return None


        result = self.min.value
        temp = self.min
        pntr = temp
        x = None
        if temp.child is not None:
            x = temp.child
            while True:
                pntr = x.right
                self.min.left.right = x
                x.right = self.min
                x.left = self.min.left
                self.min.left = x
                if x.value < self.min.value:
                    self.min = x
                x.parent = None
                x = pntr
                if pntr == temp.child:
                    break

        temp.left.right = temp.right
        temp.right.left = temp.left
        self.min = temp.right
        if temp == temp.right and temp.child is None:
            self.min = None
        else:
            self.min = temp.right
            self.Consolidate()

        self.size -= 1
        return result



    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        pass