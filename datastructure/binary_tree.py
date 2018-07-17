class BinTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        
        
class BinTree():
    def __init__(self, root=None):
        self.root = root
        
    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
    
    def preorder(self, subtree):
        if subtree is not None:
            print(subtree.data, end=' ')
            self.preorder(subtree.left)
            self.preorder(subtree.right)
            
    def midorder(self, subtree):
        if subtree is not None:
            self.midorder(subtree.left)
            print(subtree.data, end=' ')
            self.midorder(subtree.right)
            
    def backorder(self, subtree):
        if subtree is not None:
            self.backorder(subtree.left)
            self.backorder(subtree.right)
            print(subtree.data, end=' ')
        
    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)
              
node_list = [
        {'data':'A', 'left':'B', 'right':'C', 'is_root':True},
        {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
        {'data': 'D', 'left': None, 'right': None, 'is_root': False},
        {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
        {'data': 'H', 'left': None, 'right': None, 'is_root': False},
        {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
        {'data': 'F', 'left': None, 'right': None, 'is_root': False},
        {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
        {'data': 'I', 'left': None, 'right': None, 'is_root': False},
        {'data': 'J', 'left': None, 'right': None, 'is_root': False}
        ]
    
btree = BinTree.build_from(node_list)

btree.preorder(btree.root)
print()
btree.midorder(btree.root)
print()
btree.backorder(btree.root)












