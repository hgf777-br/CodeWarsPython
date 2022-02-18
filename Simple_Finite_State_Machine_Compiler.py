import re

class FSM(object):
    
    def __init__(self, instructions):
        items = [re.findall("[A-z]+[0-9]*|[0-9]+", item) for item in instructions.splitlines()]
        print(items)
        #self.fsm_states = {e: (n0, n1, o) for e, n0, n1, o in items}
        
    
    def run_fsm(self, start, sequence):
        state = start
        states = [start]
        for s in sequence:
            state = self.fsm_states[state][s]
            states.append(state)
        return (state, self.fsm_states[state][2], states)
        # return tuple: (final_state, final_state_output, path)

instructions = \
'''S1; S1, S2; 9
S2; S1, S3; 10
S3; S4, S3; 8
S4; S4, S1; 0'''

#instructions = \
"""Locked; Locked, Unlocked; 0
Unlocked; Locked, Unlocked; 1"""

f = FSM(instructions)

#print(f.run_fsm('S1', [0, 1, 1, 0, 1]))