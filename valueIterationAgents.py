# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """

  def __init__(self, mdp, discount=0.9, iterations=100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
          mdp.isTerminal(state)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter()  # A Counter is a dict with default 0
    self.run()
    # Write value iteration code here
    "*** YOUR CODE HERE ***"

  def run(self):
    states = self.mdp.getStates()
    for i in range(self.iterations):
      # print 'value is, ', self.values
      current_vals = self.values.copy()
      # print 'current value is ', current_vals
      for state in states:
        # print 'the state is', state
        if not self.mdp.isTerminal(state):
          action = self.getAction(state)
          current_vals[state] = self.computeQValueFromValues(state,action)
      self.values = current_vals



  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]

  def computeQValueFromValues(self, state, action):
    """
      Compute the Q-value of action in state from the
      value function stored in self.values.
    """
    "*** YOUR CODE HERE ***"
    q = 0
    newStates = self.mdp.getTransitionStatesAndProbs(state, action)
    # print 'new states are ', newStates
    for x in newStates:
      q += x[1] * (self.mdp.getReward(state, action, x[0]) + self.discount * self.values[x[0]])
      # print 'q is ', q
    return q


  def computeActionFromValues(self, state):
    """
      The policy is the best action in the given state
      according to the values currently stored in self.values.

      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    newDict = util.Counter()
    # calculate all the Values of actions from a state
    # and chose the value with the highest score
    for action in self.mdp.getPossibleActions(state):
      newDict[action] = self.computeQValueFromValues(state, action)
    # print 'the action that we chose is ', newDict.argMax()
    return newDict.argMax()




  def getPolicy(self, state):
    return self.computeActionFromValues(state)

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.computeActionFromValues(state)

  def getQValue(self, state, action):
    return self.computeQValueFromValues(state, action)