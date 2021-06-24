class BSTNode:
    """ An internal node for a Binary Search Tree.  """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def inorder(self, x):
        strtree = ''
        if x:
            strtree = self.inorder(x._leftchild)
            strtree += str(x._element) + ', '
            strtree = strtree + self.inorder(x._rightchild)
        return strtree


    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        if self._element is not None:
            y = '('
            if self._leftchild is not None:
                x = self._leftchild
                y += self._leftchild.inorder(x)[:-2]
            y += ')' + str(self._element) + '('
            if self._rightchild is not None:
                x = self._rightchild
                y += self._rightchild.inorder(x)[:-2]
            y += ')'
            return y


    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    
  
    def search(self, searchitem):
        """ Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST

        """
        x = self.search_node(searchitem)
        if x is None:
            return None
        else:
            return self.search_node(searchitem)._element

    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None. 

        Args:
            searchitem: an object of any class stored in the BST
        """
        if searchitem == self._element:
            return self
        elif searchitem < self._element:
            if self._leftchild is None:
                return None
            elif self._leftchild._element == searchitem:
                return self._leftchild
            else:
                return self._leftchild.search_node(searchitem)
        elif searchitem > self._element:
            if self._rightchild is None:
                return None
            elif self._rightchild._element == searchitem:
                return self._rightchild
            else:
                return self._rightchild.search_node(searchitem)

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        if self._element is None:
            self._element = obj
        elif obj < self._element:
            if self._leftchild is None:
                self._leftchild = BSTNode(obj)
                self._leftchild._parent = self
                return obj
            else:
                self._leftchild.add(obj)
        else:
            if obj > self._element:
                if self._rightchild is None:
                    self._rightchild = BSTNode(obj)
                    self._rightchild._parent = self
                    return obj
                else:
                    self._rightchild.add(obj)

    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        if self._rightchild is None:
            return self
        else:
            return self._rightchild.findmaxnode()
    
    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        i = 0
        x = self
        while x._parent is not None:
            i += 1
            x = x._parent
        return i

    def subsize(self):
        size = 0
        if self._leftchild is not None:
            size += 1
            size += self._leftchild.subsize()
        if self._rightchild is not None:
            size += 1
            size += self._rightchild.subsize()
        return size

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree, 
        including this node.
        """
        x = self.subsize()
        return x + 1

    def leaf(self):
        """ Return True if this node has no children. """
        if self._rightchild is None and self._leftchild is None:
            return True
        else:
            return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if (self._rightchild is None and self._leftchild is not None) or (self._rightchild is
                                                                          not None and self._leftchild is  None):
            return True
        else:
            return False

    def full(self):
        """ Return true if this node has two children. """
        if self._rightchild is not None and self._leftchild is not None:
            return True
        else:
            return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if self._rightchild is not None or self._leftchild is not None:
            return True
        else:
            return False

    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        x = self.search_node(searchitem)
        if x is None:
            return None
        x.remove_node()
            
    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.

        Maintains the BST properties.
        """
        # if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element

        if self.full():
            x = self.findmaxnode()
            if self._parent is not None:
                if self._parent._element > self._element:
                    self._parent._leftchild = x
                else:
                    self._parent._rightchild = x
                if x._leftchild is not None:
                    x._parent._rightchild = x._leftchild
                self._leftchild._parent = x
                self._rightchild._parent = x
                self._leftchild = None
                self._rightchild = None
                self._parent = None
                return self._element
            else:
                x._parent._rightchild = None
                y = self._element
                self._element = x._element
                x._leftchild = None
                x._rightchild = None
                x._parent = None
                return y
        elif self.leaf():
            if self._parent is not None:
                if self._parent._element > self._element:
                    self._parent._leftchild = None
                else:
                    self._parent._rightchild = None
            self._leftchild = None
            self._rightchild = None
            self._parent = None
            y = self._element
            self._element = None
            return y
        elif self.semileaf():
            if self._leftchild is not None:
                if self._parent is not None:
                    if self._parent._element > self._element:
                        self._parent._leftchild = self._leftchild
                        self._leftchild._parent = self._parent
                    else:
                        self._parent._rightchild = self._leftchild
                        self._leftchild._parent = self._parent
                    self._leftchild = None
                    self._rightchild = None
                    self._parent = None
                    return self._element
                else:
                    x = self._leftchild
                    y = self._element
                    self._element = x._element
                    self._leftchild = x._leftchild
                    self._rightchild = x._rightchild
                    x._parent = None
                    x._leftchild = None
                    x._rightchild =None
                    return y
            elif self._rightchild is not None:
                if self._parent is not None:
                    if self._parent._element > self._element:
                        self._parent._leftchild = self._rightchild
                        self._rightchild._parent = self._parent
                    else:
                        self._parent._rightchild = self._rightchild
                        self._rightchild._parent = self._parent
                    self._leftchild = None
                    self._rightchild = None
                    self._parent = None
                    return self._element
                else:
                    x = self._rightchild
                    y = self._element
                    self._element = x._element
                    self._leftchild = x._leftchild
                    self._rightchild = x._rightchild
                    x._parent = None
                    x._leftchild = None
                    x._rightchild =None
                    return y



