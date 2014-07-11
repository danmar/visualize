visualize
=========

visualize code. the goal is to rely heavily on comments in the code.

the intention will be to give an overview of code. The details will be seen by looking at the code.

this is highly experimental right now.

Relying on comments will hopefully reveal when the code is not commented well.

State machines
--------------

The statemachine.py script detect state machines in the code and generate corresponding dot files.

For this to work, the state machine must use a enum variable for the state. And the state machine must be implemented with a switch.


Value flow
----------

Will show value flow in functions. labview-like. A block of code in a function that has a proper comment will be shown as a block with inputs and outputs.

