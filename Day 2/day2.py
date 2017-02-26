

class State(object):
    def __init__(self, key, up_state, right_state, down_state, left_state):
        self.key = key
        self.up_state = up_state
        self.right_state = right_state
        self.down_state = down_state
        self.left_state = left_state

    def __repr__(self):
        return str(self.key)

    def update_state(self, up_state, right_state, down_state, left_state):
        self.up_state = up_state
        self.right_state = right_state
        self.down_state = down_state
        self.left_state = left_state

    def move(self, dir):
        print("Moving {0}".format(dir))
        if(dir=='U'):
            return self.up_state
        elif(dir == 'R'):
            return self.right_state
        elif(dir == 'D'):
            return self.down_state
        elif(dir == 'L'):
            return self.left_state
        else:
            raise Exception("Unknown move action {0}".format(dir))

state1 = State(1, None, None, None, None)
state2 = State(2, None, None, None, None)
state3 = State(3, None, None, None, None)
state4 = State(4, None, None, None, None)
state5 = State(5, None, None, None, None)
state6 = State(6, None, None, None, None)
state7 = State(7, None, None, None, None)
state8 = State(8, None, None, None, None)
state9 = State(9, None, None, None, None)
state1.update_state(state1, state2, state4, state1)
state2.update_state(state2, state3, state5, state1)
state3.update_state(state3, state3, state6, state2)
state4.update_state(state1, state5, state7, state4)
state5.update_state(state2, state6, state8, state4)
state6.update_state(state3, state6, state9, state5)
state7.update_state(state4, state8, state7, state7)
state8.update_state(state5, state9, state8, state7)
state9.update_state(state6, state9, state9, state8)

initial_state = state5

input_data = None
with open("input.dat") as data:
    input_data = data.readlines()

state = initial_state
keys = []
for instructions_keys in input_data:
    for i in instructions_keys.strip():
        state = state.move(i)
        print("Data {0} new state {1}".format(i, state))
    keys.append(state.key)

print(keys)