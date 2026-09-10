import sys
class REG_ERROR(Exception):
    """  Base class for exception """
    pass

class Name_field_error(Error1):
    """  This is customized error """
    pass

num=10
while True:
    try:
        in_number = input("enter the number")
        in_number = int(in_number)
        print(num, in_number)
        if in_number > num:
            print(num, in_number)
            raise Name_field_error
        else:
            break
    except Name_field_error:
        print("Try again")        
    except:
        print(sys.exc_info()[1] )
        print("Something went wrong")

    finally:
        dict

    
