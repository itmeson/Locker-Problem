class Locker:
  locker_counter = 1
  #this creates a default locker
  def __init__(self):
    #set each locker with a unique id
    self.id = Locker.locker_counter
    Locker.locker_counter += 1
    self.isOpen = False
    self.flipCount = 0
    self.students = [] #list of all studnets who flipped this locker


  def flip(self, s):
    self.isOpen = not self.isOpen
    self.flipCount += 1
    self.students.append(s)

  def status(self):
    #returns a string listing the status of a locker
    s = str(self.id) + ":"
    if(self.isOpen):
      s += " open: "
    else:
      s += " closed: "
    s = s + str(self.flipCount) +" "+  str (self.students)
    return s

  def reset(self):
    Locker.locker_counter=1
