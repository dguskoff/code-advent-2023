import re
from collections import Counter
from enum import Enum


class Pulses(Enum):
    High = (1,)
    Low = 2


class Module:
    def input_action(self, i=0, pulse=Pulses.Low):
        pass

    def add_input(self):
        return 0


class Broadcaster(Module):
    def __init__(self, name: str, outputs: str):
        self._output = [o.strip() for o in outputs.split(",")]
        self._name = name

    def input_action(self, i=0, pulse=Pulses.Low):
        return (self, pulse)

    pass


class FlipFlop(Module):
    def __init__(self, name: str, outputs: str):
        self._name = name
        self._output = [o.strip() for o in outputs.split(",")]
        self._state = Pulses.Low

    def input_action(self, i=0, pulse=Pulses.Low):
        if pulse == Pulses.Low and self._s == Pulses.Low:
            self._state = Pulses.High
        elif pulse == Pulses.Low and self._s == Pulses.High:
            self._state = Pulses.Low
        else:
            return None
        return (self, self._state)


class Conjunction(Module):
    def __init__(self, name: str, outputs: str):
        self._name = name
        self._inputs = []
        self._output = [o.strip() for o in outputs.split(",")]
        self._state = Pulses.High

    def add_inputs(self) -> int:
        self._input_s.append(False)
        return len(self._input_s) - 1

    def input_action(self, i: int, pulse: Pulses):
        self._inputs[i] = pulse
        if all(self._inputs == Pulses.Low):
            self._state = Pulses.High
        elif all(self._inputs == Pulses.High):
            self._state = Pulses.Low
        return (self, self._state)


class Output(Module):
    def __init__(self, name):
        self._get_low = False
        self._name = name

    def input_action(self, i, v):
        if not v:
            self._get_low = True

    def received_low(self) -> bool:
        return self._get_low

    pass


class StateMachine:
    def __init__(self):
        self._bc = None
        self._source_modules = []
        self.reset()

    def reset(self):
        self._num_button_press = 0
        self._num_low = 0
        self._num_high = 0

    def add_bc(self, name: str, str_of_outputs: str):
        self._bc = Broadcaster(name, str_of_outputs)

    def add_ff(self, name: str, str_of_outputs: str):
        self._source_modules.append(FlipFlop(name, str_of_outputs))

    def add_con(self, name: str, str_of_outputs: str):
        self._source_modules.append(Conjunction(name, str_of_outputs))

    def init(self):
        s = ""


sm = StateMachine()
with open("Data/_20_t1.txt", "r") as f:
    for line in f:
        if "broadcaster" in line:
            sm.add_bc("bc", line.split("->")[1])
        elif "%" in line:
            sm.add_ff(
                line.split("->")[0].strip().removeprefix("%"), line.split("->")[1]
            )
        elif "&" in line:
            sm.add_ff(
                line.split("->")[0].strip().removeprefix("&"), line.split("->")[1]
            )
    s = ""
