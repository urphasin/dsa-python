class LinkedList:
  class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

  def __init__(self):
    self.head = None

  
  def __repr__(self):
    pass

  def __contains__(self, item):
    pass

  def __len__(self):
    pass

  def append(self, value):
    if self.head is None:
      self.head = self.Node(value)

  def prepend(self, value):
    pass

  def pop(self):
    pass

  def insert(self, value, index):
    pass

  def delete(self, value):
    pass

  def get(self, index):
    pass

  def print(self):
    pass


if __name__ == "__main__":
  pass