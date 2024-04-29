from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

l = []

button_states = [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9,buttonplus, buttonminus,buttonligmed]

def button_pressed(button_index):
    if button_states[button_index]:
        l.append(button_index)

def nul_trykket():
    button_pressed(0)

def et_trykket():
    button_pressed(1)

def to_trykket():
    button_pressed(2)

def tre_trykket():
    button_pressed(3)

def fire_trykket():
    button_pressed(4)

def fem_trykket():
    button_pressed(5)

def seks_trykket():
    button_pressed(6)

def syv_trykket():
    button_pressed(7)

def otte_trykket():
    button_pressed(8)

def ni_trykket():
    button_pressed(9)

def createOperend():
    j = len(l)
    n=0
    for i in range(j):
        n += l[i]*10**(j-1)
    return n 

def buttonPlus():
    button_pressed(buttonPlus)
    plusOperater=Plus_operate()
    plusOperater.set_a=createOperend()

def buttonMinus():
    button_pressed(buttonMinus)
    minusOperater=Minus_operate()
    minusOperater.set_a=createOperend()

def buttonLigmed():
    global operatorState
    if operatorState == "plus":
        buttonPlus()
    elif operatorState == "minus":
        buttonMinus()

class Lommeregner():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, operator: Operator) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._operator = operator

    @property
    def operator(self) -> Operator:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._operator

    @operator.setter
    def operator(self, operator: Operator) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._operator = operator

    def lommeregner(self, a: float, b: float) -> float:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        # ...

        #print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._operator.do_operate(a,b)
        print("Resultat:",result)

        # ...


class Operator(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_operate(self, a: float,b: float) -> float:
        pass
operatorState = ""
class Plus_operate(Operator):
    global operatorState
    def __init__(self):
        operatorState = "plus"
    def do_operate(self) -> float:
        return self.a + self.b
    def set_a(self,a):
        self.a=a 


class Minus_operate(Operator):
    global operatorState
    def __init__(self):
        operatorState = "minus"
    def do_operate(self, a) -> float:
        return self.a - self.b   
    def set_a(self,a):
        self.a=a

'''class Gange_operate(Operator):
    def do_operate(self, a: float,b: float) -> float:
        return a * b  
    
class Devider_operate(Operator):
    def do_operate(self, a: float,b: float) -> float:
        return a / b  

'''

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Lommeregner(Plus_operate())
    #print("Client: Strategy is set to normal sorting.")
    context.lommeregner(5,3)
    print()

    #print("Client: Strategy is set to reverse sorting.")
    context.operator = Minus_operate()
    context.lommeregner(5,3)
    '''
    context.operator = Gange_operate()
    context.lommeregner(5,3)

    context.operator = Devider_operate()
    context.lommeregner(5,3)
    '''