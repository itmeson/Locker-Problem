class Locker:
  def __init__(self, id):
    """set each locker with a unique id"""
    self.id = id          # Locker ID number to figure out who should be closing/opening this locker
    self.isOpen = False   # True if open, false if closed
    self.flipCount = 0    # number of times this locker has been flipped
    self.students = []    # list of all students who flipped this locker

  def flip(self, s):
    """Flip one locker"""
    self.isOpen = not self.isOpen
    self.flipCount += 1
    self.students.append(s)

  def __repr__(self):
    """Returns a string listing the status of a locker"""
    from termcolor import colored
    if(self.isOpen):
      state = colored("{:8}".format("open"), "green")
    else:
      state = "closed"
    output = "{:4}{:8}{:4}{}".format(str(self.id), state, str(self.flipCount), str(self.students))
    return output

  def reset(self):
    """Reset a single locker to closed and erase its history"""
    self.isOpen = False
    self.flipCount = 0
    self.students = []

    
class Hallway:
    def __init__(self, N):
        self.lockers = [Locker(i+1) for i in range(N)]
    
    def __repr__(self):
        output = '\n'.join(x.__repr__() for x in self.lockers)
        return output
            
    def reset(self):
        """Reset all the lockers to closed and erase their history"""
        for locker in self.lockers:
            locker.reset()
        