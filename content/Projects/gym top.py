import random

class gym_member():
    def __init__(self,unique_membership_number,first_name,surname,telephone):
        self.unique_membership_number=unique_membership_number
        self.first_name=first_name
        self.surname=surname
        self.telephone=telephone

    def edit_info(self):
        while True:
            user_input=input('what do you want to edit \n(unique membership number= UNM)\n(first name)\n(last name)\n(surname)\n(telephone)\n(exit)')
            if user_input=='UNM':
                user_input==input('change to:')
                self.unique_membership_number=user_input
            elif user_input=='first name':
                user_input=input('change to:')
                self.first_name=user_input
            elif user_input=='surname':
                user_input=input('change to:')
                self.surname=user_input
            elif user_input=='telephone':
                user_input=input('change to:')
                self.telephone=user_input
            elif user_input=='exit':return
            
    def show_info(self):
        print('(unique membership number)({})'.format(self.unique_membership_number))
        print('(first name)({})'.format(self.first_name))
        print('(surname)({})'.format(self.surname))
        print('(telephone)({})'.format(self.telephone))

    def del_account(self):
        del self

    def menu(self):
        while True:
            user_input=input('(edit)\n(info)\n(del account)\n(exit)')
            if user_input=='edit':self.edit_info()
            elif user_input=='info':self.show_info()
            elif user_input=='del account':self.del_account()
            elif user_input=='exit':return
            print('--------------------------------------------------------')

def main():
    gym_person=gym_member(random.randint(1000000000000,9999999999999),'Jib','maclovin',999)
    gym_person.menu()

if __name__=='__main__':
    main()
