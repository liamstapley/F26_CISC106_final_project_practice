from bakery import assert_equal
from drafter import *
from dataclasses import dataclass


hide_debug_information()
set_website_title("Final Project Practice: Assignment Counter")
set_website_framed(False)


@dataclass
class State:
    count: int


@route
def index(state: State) -> Page:
    print("index run")
    return Page(state, [
        "Assignments left to do today: " + str(state.count) + "\n",
        Button("-10", "minus_ten"),
        Button("-5", "decrement_by_5"),
        Button("-1", "decrement"),
        Button("+1", "increment"),
        Button("+5", "increment_by_5"),
        Button("+10", "add_ten"),
        Button("Double it", "double_count"),
        Button("Reset", "reset_count")
    ])


@route
def increment(state: State) -> Page:
    state.count = state.count + 1
    return index(state)

@route
def increment_by_5(state: State) -> Page:
    state.count = state.count + 5
    return index(state)

@route
def add_ten(state: State) -> Page:
    state.count = state.count + 10
    return index(state)

@route
def double_count(state: State) -> Page:
    print("Before doubling:", state.count)
    state.count = state.count * 2
    print("After doubling:", state.count)
    return index(state)

@route
def decrement(state: State) -> Page:
    if state.count >= 1:
        state.count = state.count - 1
    else:
        pass
    return index(state)

@route
def decrement_by_5(state: State) -> Page:
    if state.count >= 5:
        state.count = state.count - 5
    else:
        pass
    return index(state)

@route
def minus_ten(state: State) -> Page:
    if state.count >= 10:
        state.count = state.count - 10
    else:
        pass
    return index(state)

@route
def reset_count(state: State) -> Page:
    state.count = 5
    return index(state)


assert_state(increment(State(0)), State(1))
assert_state(reset_count(State(7)), State(5))
assert_has(index(State(3)), "Assignments left to do today: 3")


start_server(State(5))
