class bicycle(object):
  def __init__(self, mname="", wt=0, c=0):
    self.name = mname
    self.weight = wt
    self.cost = c
  def display(self):
    print "Name: {}, Cost: {}, Weight: {}".format(self.name, self.cost, self.weight)
    
class bikeshopitem(object):
  def __init__(self, bike, marg, amt):
    self.bicycle = bike
    self.margin = marg
    self.number = amt
    self.sold = 0
    

class bikeshop(object):
  
  def __init__(self, bname):
    self.name = bname
    self.itemlist = []
    self.profit = 0
  def add_inventory(self,bike, marg, amt):
    bitem = bikeshopitem(bike, marg, amt)
    self.itemlist.append(bitem)
  def get_profit(self):
    return self.profit 
  def display(self):
    print "Shop: {}".format(self.name)
    for i in self.itemlist:
      print "Cycle Name: {}, Amount left: {}".format(i.bicycle.name, i.number)
    print "Profit made so far is {}".format(self.get_profit())  
  def sold_bike(self, bike):
    for i in self.itemlist:
#      print "{} and {}".format(bike, i.bicycle)
      if bike.name == i.bicycle.name:
        i.number = i.number - 1
        i.sold = i.sold + 1
        self.profit = self.profit + bike.cost * i.margin / 100.0
  def show_inventory(self, budget):
    cycle_list = []
    for i in self.itemlist:
      if i.bicycle.cost <= budget and i.number > 0:
        cycle_list.append(i.bicycle)
    return cycle_list    
  
class customer(object):
  def __init__(self, cname, budget):
    self.name = cname
    self.budget = budget
    self.bicycle = bicycle()
  def buycycle(self, bike):
    self.bicycle = bike
    self.budget = self.budget - bike.cost
  def has_money(self):
    return self.budget
  def display(self):
    print "Customer name : {}".format(self.name)
    print "Customer budget : {}".format(self.budget)
    self.bicycle.display()
  def get_budget(self):
    return self.budget
  
