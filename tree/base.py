class Node:
    def __init__(self,val):
        self.val=val
        self.lchild=None
        self.rchild=None

class BiTree:
    def __init__(self):
        self.root=None
        self.lchild=None
        self.rchild=None
  
    ###利用队列新建一棵树
    def createTree(self,nums):
        queue=[]
        cur_pos=0
        if self.root==None:
            node=Node(nums[cur_pos])
            self.root=node
            queue.append(node)
            cur_pos+=1
        while queue is not None and cur_pos<len(nums):
            cur_node=queue.pop(0)
            if cur_node.lchild is None and cur_pos<len(nums):
                lnode=Node(nums[cur_pos])
                cur_node.lchild=lnode
                queue.append(lnode)
                cur_pos+=1
            if cur_node.rchild is None and cur_pos<len(nums):
                rnode=Node(nums[cur_pos])
                cur_node.rchild=rnode
                queue.append(rnode)
                cur_pos+=1
    ##层次遍历
    def reverseTree_level(self):
        if self.root==None:
            print('this tree is null')
            return 
        queue=[]
        queue.append(self.root)
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.val)
            if cur_node.lchild:                
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)

    ##先序遍历——递归
    def reverseTree_PreOrder(self,node):
        if node is None:
            return 
        print(node.val)
        if node.lchild:
            self.reverseTree_PreOrder(node.lchild)
        if node.rchild:
            self.reverseTree_PreOrder(node.rchild)

    ##中序遍历——递归
    def reverseTree_InOrder(self,node):
        if node is None:
            return 
        if node.lchild:
            self.reverseTree_InOrder(node.lchild)
            #print(node.lchild.val)
        print(node.val)
        if node.rchild:
            self.reverseTree_InOrder(node.rchild)
            #print(node.rchild.val)
        
    ##后序遍历——递归
    def reverseTree_PostOrder(self,node):
        if node is None:
            return 
        if node.lchild:
            self.reverseTree_PostOrder(node.lchild)        
        if node.rchild:
            self.reverseTree_PostOrder(node.rchild)  
        print(node.val)
    
    ##栈中序遍历
    def reverseTree_InOrder_Stack(self):
        if self.root is None:
            return
        stack=[]
        node=self.root
        while stack or node:
            if node:
                stack.append(node)
                node=node.lchild
            else:
                node=stack.pop()
                print(node.val)
                node=node.rchild
    
    ##栈前序遍历
    def reverseTree_PreOrder_Stack(self):
        if self.root is None:
            return
        stack=[]
        node=self.root
        while stack or node:
            if node:
                print(node.val)
                stack.append(node)               
                node=node.lchild
            else:
                node=stack.pop()
                node=node.rchild

    ##栈后序遍历
    def reverseTree_PostOrder_Stack(self):
        if self.root is None:
            return
        stack=[]
        node=self.root
        visted_node=None
        while stack or node:
            if node:
                stack.append(node)
                node=node.lchild
            else:
                node=stack[-1] ##查看栈顶元素
                ##当目前的节点有右节点，并且没被访问过
                if node.rchild and node.rchild!=visted_node:
                    node=node.rchild
                    stack.append(node)
                    node=node.lchild
                else:
                    node=stack.pop()  
                    print(node.val)
                    visted_node=node
                    node=None
                





if __name__ == "__main__":
    tree=BiTree() 
    tree.createTree([0,1,3,5,6,7,9])
    print('-----levelOrder--------')
    tree.reverseTree_level()
    print('-----PreOrder--------')
    tree.reverseTree_PreOrder(tree.root)
    print('-----InOrder--------')
    tree.reverseTree_InOrder(tree.root)
    print('-----PostOrder--------')
    tree.reverseTree_PostOrder(tree.root)
    print('-----InOrder_Stack--------')
    tree.reverseTree_InOrder_Stack()
    print('-----PreOrder_Stack--------')
    tree.reverseTree_PreOrder_Stack()
    print('-----PostOrder_Stack--------')
    tree.reverseTree_PostOrder_Stack()

            


            

