import sys

class TreeNode:
    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)

class binaryTree:
    def __init__(self):
        self.root=None
        self.size=0

    def __contains__(self,value):
        pass


    def get(self,value):
        """""Retorna o NÓ correspondente ao value"""
        def search(node,value):
            if not node:
                return None
            elif node.value == value:
                return node
            else:
                return search(node.left,value) or search(node.right,value)
        return  search(self.root,value)
    
        

    def __len__(self):
        return self.size
    
    def dfs(self,node):
        "Depth-First Search (DFS) Recursive"
        ans = []
        def body(node):
            if not node:
                return
            else:
                ans.append(node.value)
                body(node.left)
                body(node.right)
        body(node)
        return ans

    def preOrder(self,node):
        return self.dfs(node)

    def inOrder(self,node):
        pass

    def posOrder(self,node):
        pass

    def tree_height(self,node):
        pass

    def tree_depth(self,root,node):
        pass

    def successor(self,node):
        pass

    def predecessor(self,node):
        pass
    
    def insertRoot(self,value):
        if self.root:
            raise TypeError ('Arvore nao esta vazia')
        self.root = TreeNode(value)
        self.size += 1

    def insertLeft(self,currNode,value):
        if not currNode:
            raise TypeError('Nó nao esta vazia')
        else:
            if currNode.left:
                currNode.left.value = value
            else:
                currNode.left = TreeNode(value)
                self.size += 1

    def insertRight(self,currNode,value):
        if not currNode:
            raise TypeError('N-o corrente é NONE')
        else:
            if currNode.right:
                currNode.right.value = value
            else:
                currNode.right = TreeNode(value)
                self.size +=1
                

    def show(self):
            # adapted from https://www.worldofitech.com/red-black-tree-insertion/
            # Printing the tree
            self._show(self.root, "", True)
            
    def _show(self, node, indent, last):
        # adapted from https://www.worldofitech.com/red-black-tree-insertion/
        if node != None:
            sys.stdout.write(indent)
            if last:
                if node == self.root:
                    sys.stdout.write("Root.")
                else:    
                    sys.stdout.write("R..")
                indent += "   "
            else:
                sys.stdout.write("L..")
                indent += "   "
            print(str(node.value))
            self._show(node.left, indent, False)
            self._show(node.right, indent, True)

if __name__ == '__main__':
        # Example usage:
        # Create a binary tree
        t = binaryTree()
        root = TreeNode(100)
        root.left = TreeNode(20)
        root.right = TreeNode(130)
        root.left.left = TreeNode(10)
        root.left.right = TreeNode(30)
        root.right.right = TreeNode(150)
        root.right.left = TreeNode(110)
        t.root = root
        t.show()
        print('-'*30)
        t1 = binaryTree()
        t1.insertRoot(100)
        t1.insertLeft(t1.root,20)
        t1.insertRight(t1.root,130)
        t1.insertLeft(t1.root.left,10)
        t1.insertRight(t1.root.left,30)
        t1.insertLeft(t1.root.right,110)
        t1.insertRight(t1.root.right,150)
        t1.show()
        print(t1.dfs)


