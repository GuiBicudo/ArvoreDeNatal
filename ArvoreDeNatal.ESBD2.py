from abc import ABC, abstractmethod

class AbstractTree(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

class Tree(AbstractTree):
    def description(self) -> str:
        return "Árvore"

class TreeDecorator(AbstractTree):
    _tree: AbstractTree = None

    def __init__(self, tree: AbstractTree):
        self._tree = tree

    def description(self) -> str:
        return self._tree.description()

class Guirlanda(TreeDecorator):
    def description(self) -> str:
        return f"{self._tree.description()}, Guirlanda"

class Bolas(TreeDecorator):
    def description(self) -> str:
        return f"{self._tree.description()}, Bolas"

class Doces(TreeDecorator):
    def description(self) -> str:
        return f"{self._tree.description()}, Doces"

if __name__ == "__main__":

    # Arvore
    base_tree = Tree()
    print(f"Árvore base: {base_tree.description()}") 

    # Arvore e Guirlanda
    tree_with_guirlanda = Guirlanda(base_tree)
    print(f"Árvore com guirlanda: {tree_with_guirlanda.description()}") 

    # Arvore, Guirlanda e Bolas
    tree_with_guirlanda_and_bolas = Bolas(tree_with_guirlanda)
    print(f"Árvore com guirlanda e bolas: {tree_with_guirlanda_and_bolas.description()}") 

    # Arvore, guirlanda, bolas e doces.
    tree_fully_decorated = Doces(tree_with_guirlanda_and_bolas)
    print(f"Árvore completa: {tree_fully_decorated.description()}") 

    # Arvore e bolas
    another_base_tree = Tree()
    tree_only_with_bolas = Bolas(another_base_tree)
    print(f"Outra árvore apenas com bolas: {tree_only_with_bolas.description()}") 

    # Árvore, bolas e guirlanda 
    tree_with_bolas_then_guirlanda = Guirlanda(Bolas(Tree()))
    print(f"Árvore com bolas e depois guirlanda: {tree_with_bolas_then_guirlanda.description()}") 

    # Árvore, doces e guirlanda 
    tree_doces_then_guirlanda = Guirlanda(Doces(Tree()))
    print(f"Árvore com doces e guirlanda: {tree_doces_then_guirlanda.description()}") 
