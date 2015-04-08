from bicycle import bicycle 
from bicycle import bikeshop
from bicycle import customer

def main():
  #Creating bicyle shpop with 6 cycle models
  # create cycle models
  cycle1 = bicycle("rager", 10, 50)
  cycle2 = bicycle("sizzly", 8, 300)
  cycle3 = bicycle("champ", 8, 800)  
  cycle4 = bicycle("winner", 8, 400)
  cycle5 = bicycle("runner", 8, 600)
  cycle6 = bicycle("sundance", 8, 75)
  
  #Add to inventory
  bikemart = bikeshop("BikeMart")
  bikemart.add_inventory(cycle1,20,10 )
  bikemart.add_inventory(cycle2,20,5 )
  bikemart.add_inventory(cycle3,20,3 )
  bikemart.add_inventory(cycle4,20,2 )
  bikemart.add_inventory(cycle5,20,4 )
  bikemart.add_inventory(cycle6,20,1 )
  #Print inventory
  bikemart.display()
  
  #create customers
  customerlist = [customer("John", 200), customer("Paul", 500), customer("Eden", 1000)]
  
  for c in customerlist:
    print "Customer arrives at store "
    c.display()
    
    choice_list = bikemart.show_inventory(c.budget)
    print "With you budget your choices are "
    for i in range(len(choice_list)):
      print "{} . Name: {}, Cost: {}".format(i, choice_list[i].name, choice_list[i].cost)
      
    choice = int(raw_input("Which one would you like ?"))
    print "{} is a GREAT choice ".format(choice)
    bikemart.sold_bike(choice_list[choice])
    c.buycycle(choice_list[choice])
    print "Customer Status is now "
    c.display();
    print "\n The inventory now has \n"
    bikemart.display()
    print "-------------------------------------------------------"
    
  
  
if __name__ == '__main__':
  main()
