class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.father = None

class Tree:
    def __init__(self) -> None:
        self.root = None
        
    def get_father(self, node):
        return node.father
    
    def get_left(self, node):
        return node.left
    
    def get_right(self, node):
        return node.right
    
    def get_data(self, node):
        return node.data
        
    def is_left(self, node):
        pai = self.get_father(node)
        if pai == None:
            return False
        if self.get_left(pai) == node:
            return True
        return False

    def is_right(self, node):
        pai = self.get_father(node)
        if pai == None:
            return False
        if self.get_right(pai) == node:
            return True
        return False
    
    def brother(self, node):
        if self.get_father(node) == None:
            return False # Só pode ser irmão se for filho
        if self.is_left(node):
            return self.get_right(self.get_father(node))
        return self.get_left(self.get_father(node))
    
    def read_pre_order(self, node): # Profundidade
        if (node != None):
            print(self.get_data(node))
            self.read_pre_order(self.get_left(node))
            self.read_pre_order(self.get_right(node))
            
    def read_in_order(self, node): # Simetrica
        if (node != None):
            self.read_in_order(self.get_left(node))
            print(self.get_data(node))
            self.read_in_order(self.get_right(node))
            
    def read_pos_order(self, node):
        if (node != None):
            self.read_pos_order(self.get_right(node))
            self.read_pos_order(self.get_left(node))
            print(self.get_data(node))
            
    def tree_search(self, node, pesquisado):
        if node is None:
            return None  # Valor não encontrado
        if pesquisado == node.data:
            return node
        if pesquisado < node.data:
            return self.tree_search(node.left, pesquisado)
        else:
            return self.tree_search(node.right, pesquisado)
    
    def tree_minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def tree_maximum(self, node):
        while node.right != None:
            node = node.right
        return node
    
    def tree_successor(self, node):
        if node.right != None:
            return self.tree_minimum(node.right)
        y = self.get_father(node)
        while y != None and node == y.right:
            node = y
            y = self.get_father(y)
        return y

    def tree_insert(self, Tree, node):
        y = None
        x = Tree.root
        while x is not None:
            y = x
            if node.data < x.data:
                x = self.get_left(x)
            else:
                x = self.get_right(x)
                
        node.father = y
        if y is None:
            Tree.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
    
    def tree_delete(self, T, data):
        node = self.tree_search(T.root, data) 
        if node is None: 
                return None # O nó com o valor especificado não foi encontrado
        if node.left is None or node.right is None:
            y = node
        else:
            y = self.tree_successor(node)
            
        if y.left is not None:
            x = y.left
        else:
            x = y.right
            
        if x is not None:
            x.father = y.father
            
        if y.father is None:
            T.root = x
        elif self.is_left(y):
            y.father.left = x
        else:
            y.father.right = x
            
        if y != node:
            node.data = y.data
        return y

            

arvore = Tree()

inserir = [12,8,2,5,22,11,7]
for i in inserir:
    novo_no = Node(i)
    arvore.tree_insert(arvore, novo_no)
    
print(arvore.get_data(arvore.tree_minimum(arvore.root)))

arvore.tree_delete(arvore, 2)

print(arvore.get_data(arvore.tree_successor(arvore.root)))