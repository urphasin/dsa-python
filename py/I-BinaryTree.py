class BinaryTree:
    """Linked Representation of a binary tree structure."""
    class Node:
      __slots__ = '_element', '_parent', '_left', '_right'
      def __init__(self, element, parent=None, left=None, right=None):
          self._element = element
          self._parent = parent
          self._left = None
          self._right = None
    
    class Position:
      """An abstraction representing the location of a single element"""
      def __init__(self, container, node):
        self

T = ["A", "B", "C", "D", "E", "F", "G"]

