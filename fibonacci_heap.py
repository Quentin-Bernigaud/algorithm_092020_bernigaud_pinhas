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


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value
        self.order = 0

    # Adding element at the end of the tree
    def append(self, item):
        self.children.append(item)
        self.order += 1

class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """
    def __init__(self):
        self.nodes = []
        self.min_node = None
        self.size = 0

    def display(self):
        """
        Display Heap information
        """
        if self.min_node is None:
            print(" - FibonacciHeap is empty")
        else:
            print(" - FibonacciHeap has {:d} nodes, min is {:d}, root nodes are: ".format(self.size, self.find_min()), end='')
            index=1
            # display root nodes values only
            len = self.nodes.__len__()
            for current_node in self.nodes:
                print(current_node.value, end='')
                if index < len:
                    print("-->", end='')
                index += 1
            print("") # end of line


    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """

        # Check value type
        if not isinstance(value, int):
            raise ValueError

        node = Node(value)
        self.nodes.append(node)
        self.size += 1

        self.update_min(node)

    def update_min(self, node):
        """
        Change self.min_node si node.value est plus petit
        """
        if (self.min_node is None or node.value < self.min_node.value):
            self.min_node = node


    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        return  None if self.min_node is None else self.min_node.value

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        if self.min_node is None:
            return None

        min_to_delete = self.min_node
        # before deleting, move children to trees structure
        for child in min_to_delete.children:
            self.nodes.append(child)
        self.nodes.remove(min_to_delete)

        # use first item (if any) as new min
        if self.nodes == []:
            self.min_node = None
        else:
            self.min_node = self.nodes[0]
            # trees have changed, reorganize
            self.consolidate()

        self.size -= 1
        return min_to_delete.value


    # Consolidate the tree
    def consolidate(self):
        new_nodes = (math.frexp(self.size)[1] ) * [None]

        while self.nodes != []:
            x = self.nodes[0]
            order = x.order
            self.nodes.remove(x)
            while new_nodes[order] is not None:
                y = new_nodes[order]
                # swap if needed
                if x.value > y.value:
                    x, y = y, x
                x.append(y)
                new_nodes[order] = None
                order += 1
            new_nodes[order] = x

        self.min_node = None
        for new_node in new_nodes:
            if new_node is not None:
                self.nodes.append(new_node)
                self.update_min(new_node)


    def merge(self, fheap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        if fheap is None:
            return self

        for node in fheap.nodes:
            self.mergeNode(node)

        # optionnaly we could do: self.consolidate()

    def mergeNode(self, node: Node) -> None:
        if node is None:
            return self

        self.insert(node.value)
        for child in node.children:
            self.mergeNode(child)
