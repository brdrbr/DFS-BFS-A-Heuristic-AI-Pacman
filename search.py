# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    startstate = problem.getStartState()
    
    stack = util.Stack()
    
    explorednodes = []
    
    stack.push([startstate, []])
    
    while not stack.isEmpty():
        
        node, procedure = stack.pop()
        
        if node not in explorednodes:
            
            if problem.isGoalState(node):
                
                return procedure
            
            explorednodes.append(node)
            
            for nextnode, miniprocedure, cost in problem.getSuccessors(node):
                
                nextprocedure = procedure + [miniprocedure]
                
                stack.push([nextnode, nextprocedure])

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startstate = problem.getStartState()
    
    queue = util.Queue()
    
    explorednodes = []
    
    queue.push([startstate, []])
    
    while not queue.isEmpty():
        
        node, procedure = queue.pop()
        
        if node not in explorednodes:
            
            if problem.isGoalState(node):
                
                return procedure
            
            explorednodes.append(node)
            
            for nextnode, miniprocedure, cost in problem.getSuccessors(node):
                
                nextprocedure = procedure + [miniprocedure]
                
                queue.push([nextnode, nextprocedure])

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    startstate = problem.getStartState()
    
    priqueue = util.PriorityQueue()
    
    explorednodes = []
    
    priqueue.push([startstate, [], 0], 0)
    
    while not priqueue.isEmpty():
        
        node, procedure, cost = priqueue.pop()
        
        if node not in explorednodes:
            
            if problem.isGoalState(node):
                
                return procedure
            
            explorednodes.append(node)
            
            for nextnode, miniprocedure, minicost in problem.getSuccessors(node):
                
                nextprocedure = procedure + [miniprocedure]
                
                nextcost = cost + minicost
                
                priqueue.push([nextnode, nextprocedure, nextcost], nextcost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    priqueue = util.PriorityQueue()

    explorednodes = [] 

    startstate = problem.getStartState()

    priqueue.push([startstate, [], 0] , 0)

    while not priqueue.isEmpty():

        node, procedure, cost = priqueue.pop()
        
        explorednodes.append([node, cost])

        if problem.isGoalState(node):
            return procedure

        for nextnode, miniprocedure, minicost in problem.getSuccessors(node):
            
            nextprocedure = procedure + [miniprocedure]
            
            nextcost = problem.getCostOfActions(nextprocedure)
            
            newNode = (nextnode, nextprocedure, nextcost)

            isexplored = False
            
            for i in explorednodes:
                state, cost2 = i

                if nextnode == state:
                    if nextcost >= cost2:
                        isexplored = True

            if not isexplored:
                
                priqueue.push(newNode, nextcost + heuristic(nextnode, problem))
                
                explorednodes.append([nextnode, nextcost])

    return procedure

    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
