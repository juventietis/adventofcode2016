class State(object):
    def __init__(self, key):
        self.key = key
        self.up_state = None
        self.right_state = None
        self.down_state = None
        self.left_state = None

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


def initialise_states_part1():
    state1 = State(1)
    state2 = State(2)
    state3 = State(3)
    state4 = State(4)
    state5 = State(5)
    state6 = State(6)
    state7 = State(7)
    state8 = State(8)
    state9 = State(9)
    state1.update_state(state1, state2, state4, state1)
    state2.update_state(state2, state3, state5, state1)
    state3.update_state(state3, state3, state6, state2)
    state4.update_state(state1, state5, state7, state4)
    state5.update_state(state2, state6, state8, state4)
    state6.update_state(state3, state6, state9, state5)
    state7.update_state(state4, state8, state7, state7)
    state8.update_state(state5, state9, state8, state7)
    state9.update_state(state6, state9, state9, state8)
    return state5

def initialise_states_part2():
    state1 = State(1)
    state2 = State(2)
    state3 = State(3)
    state4 = State(4)
    state5 = State(5)
    state6 = State(6)
    state7 = State(7)
    state8 = State(8)
    state9 = State(9)
    statea = State("A")
    stateb = State("B")
    statec = State("C")
    stated = State("D")
    state1.update_state(state1, state1, state3, state1)
    state2.update_state(state2, state3, state6, state2)
    state3.update_state(state1, state4, state7, state2)
    state4.update_state(state4, state4, state8, state3)
    state5.update_state(state5, state6, state5, state5)
    state6.update_state(state2, state7, statea, state5)
    state7.update_state(state3, state8, stateb, state6)
    state8.update_state(state4, state9, statec, state7)
    state9.update_state(state9, state9, state9, state8)
    statea.update_state(state6, stateb, statea, statea)
    stateb.update_state(state7, statec, stated, statea)
    statec.update_state(state8, statec, statec, stateb)
    stated.update_state(stateb, stated, stated, stated)
    return state5


def solve(input_data, initial_state):
    state = initial_state
    keys = []
    for instructions_keys in input_data:
        for i in instructions_keys.strip():
            state = state.move(i)
            print("Data {0} new state {1}".format(i, state))
        keys.append(state.key)

    print(keys)


initial_state_p1 = initialise_states_part1()
initial_state_p2 = initialise_states_part2()

input_data = None
with open("input.dat") as data:
    input_data = data.readlines()

solve(input_data, initial_state_p1)
solve(input_data, initial_state_p2)
