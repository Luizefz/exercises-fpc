class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.rigth = None
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
    
    def read_pre_order(self, node):
        if (node != None):
            print(self.get_data(node))
            self.read_pre_order(self.get_left(node))
            self.read_pre_order(self.get_right(node))
            
    def read_in_order(self, node):
        if (node != None):
            self.read_in_order(self.get_left(node))
            print(self.get_data(node))
            self.read_in_order(self.get_right(node))
            
    def read_pos_order(self, node):
        if (node != node):
            self.read_pos_order(self.get_right(node))
            self.read_pos_order(self.get_left(node))
            print(self.get_data(node))
            
    