#Rony Vargas
#Kargo Software Engineer Intern
#Assesment Submission
#March 2020

"""
Solution for Kargo Software Engineer Assesment.

Question:
Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.


Utilized depth-first-search under assumption one-to-one map is not dependent on character index. (unlike isomorphic strings)
Working as expect, O(N!) where N length of string (Uniqueness of string, based on number of unique characters.)
(Runs well with up to 15/16 unique chars)

Assumptions: 
Lowercase letters are different than uppercase (a != A)

example:
    aa -> aA == False


Mapping is not related to character index in string 

example:
    aab -> abb == True
    F(a) = b, F(b) = a
"""

import sys
from collections import Counter


def charFreq(string):
    """Function takes a string and returns list with each character frequency.

    Arguments:
        string (String): string that will be processed

    Returns:
        List (ints): Frequency of each unique character. Ordered by decreasing order (most common first) 

    """

    characters = Counter()
    result = []
    
    for c in string:
        characters.update(c)

    for i in characters.values():
        result.append(i)

    result.sort(reverse=True)
        
    return result


def mapDFS(paths, current, nextGoal, goals):
    """Recursive function that explorers mapping possibilities and returns True if path that crosses ALL goals is possible.

    Arguments:
         paths (list of ints): currently available paths to choose from
         current (int): Current subtotal before selecting next potential path
         nextGoal (int): current target goal index from goals array
         goals (list of ints) list of all goals that NEED to be visited


    Returns:
        Boolean: Returns True if Target has been found
                 Returns False once search path has been exhausted 

    """

    for path in paths:        
        potential = current + path
        
        if potential > goals[nextGoal]:
            continue;

        if potential == goals[len(goals)-1]:
            return True
        
        pathsLeft = list(paths)
        pathsLeft.remove(path)

        if potential == goals[nextGoal]:
            if mapDFS(pathsLeft, potential, nextGoal + 1, goals):
                return True
        
        elif mapDFS(pathsLeft, potential, nextGoal, goals):
            return True

    return False



def findMapping(s1, s2):
    """Driver function for dfs function.

    Creates the queue list and goals, then calls a recursive depth-first-search function with intial parameters

    Parameters:
        s1 (string): First string that needs to be mapped to the other
        s2 (string): Second string which will be mapped onto and where goals are derived from
    
    Returns:
        Boolean: Returns result from dfs search
            True: if mapping is successfully found
            False: If all feasible paths have been exhausted

    """

    queue = charFreq(s1)
    goals = charFreq(s2)

    if queue[0] > goals[0]:
        return False

    if len(goals)>1:
        for i in range(1, len(goals)):
            goals[i] += goals[i-1]

    return mapDFS (queue, 0, 0, goals)    
    

def main():
    """Main function takes two strings and determines if one-to-one mapping exists.
    
    True or False result will print to output
    No output if number of arguments incorrect

    Parameters:
        argv[1] (String): String1, String source to be mapped
        argv[2] (String): String2, String to be mapped too

    Returns:
        int:
            0: successful execution
           -1: parameters missing or invalid
    """

    if len(sys.argv) < 3 or len(sys.argv) > 3:
        #print ("invalid arguments")
        return -1

    if len(sys.argv[1]) != len(sys.argv[2]):
        #print (len(sys.argv[1]) , len(sys.argv[2]) )
        print ("false")
        return 0

    result = findMapping(sys.argv[1], sys.argv[2])

    #Correct output to match doc requirements  
    if result:
        result = "true"
    else:
        result = "false"
                         
    print (result)
    return 0


if __name__ == "__main__":
    main()
