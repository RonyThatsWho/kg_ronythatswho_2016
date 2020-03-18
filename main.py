#Rony Vargas
#Kargo Software Engineer Intern
#Assesment Submission
#March 2020

"""


"""

def main():
    """
    Main function takes two strings and determines if one-to-one mapping exists
    True or False result will print to output
    No output if arguements incorrect

    Parameters:
        argv[1] (String): String1, String source to be mapped
        argv[2] (String): String2, String to be mapped too

    Returns:
        int:
            0: successful execution
           -1: parameters missing or invalid
    """

    if len(sys.argv) < 3 ^ len(sys.argv) > 3 :
        print (sys.argv)
        print ("invalid arguements")
        return -1

    if len(sys.argv[1]) != len(sys.argv[2]):
        print ("false")
        return 0
    
    return 0


main()


