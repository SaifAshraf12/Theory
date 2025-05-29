# activity 1
def difficult_assignment():
    assign = str(input("write your opinion about assignment:difficult or easy "))
    if assign == 'easy':
        print('easy assignment')
    else:
        print('difficult aasignment')
difficult_assignment()

# activity 2
review = difficult_assignment
review()

# activity 3
def my_name(name,department):
    print('nmae is ', name)
    print(name,"s department is", department)
my_name('saif','BBA')
my_name('BBA',"saif")
my_name(name='saif',department='BBA')

abc=my_name
abc('ahmad','BSE')
