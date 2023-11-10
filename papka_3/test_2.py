class Auto:
    def ride(self):
        print('Riding on a ground')
    
class Boat:
    def swim(self):
        print('Floating on water')
    
class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim() 




class ContactList(list):
    def __init__(self, args):
        self.args = args
    def  search_by_name(self, name):
        self.name = name
        list_ = []
        for i in self.args:
            if self.name in i:
                list_.append(i)
        return list_
            

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Olya')) 