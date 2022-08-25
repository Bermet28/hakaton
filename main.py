from views import *

def main():
    print('Hi, the following features are available to you: \n\tLIST -1\n\tRetrieve -2\n\tCREATE  -3\n\tUPDATE -4\n\tDELETE -5')
    choice = input('Enter action: ')
    if choice == '1':
        list_of_products()
    elif choice == '2':
        detail_retrieve()
    elif choice == '3':
        create_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    else:
        print('Invalid choice')
        main()
    
    ask = input('Do you want to continue (yes\no)')
    if ask.lower() == 'yes':
        main()
    else:
        print(' Goodbye!!')

main()
