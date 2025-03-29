from typing import Dict, List, Tuple, Callable

class ConsoleApplication:

    def __init__(self, intro_text: str, inputs: Dict):
        self.intro_text = intro_text
        self.inputs = dict[str, List[Tuple]]()
        self.set_inputs(inputs)

    def set_inputs(self, input_dict: Dict[str, List[Tuple[str, str, Callable]]]):
        self.inputs = input_dict

    def update_input_entry(
            self,
            key: str,
            index: int,
            desc: str,
            input_key: str = '',
            show_key: bool = True):

        desc = f'{input_key} - {desc}' if show_key else desc
        self.inputs[key][index] = input_key, desc

    def show_intro(
            self,
            padding: int = 20,
            padding_char: str = '=',
            break_line: bool = True):

        print(padding_char * padding)
        print(self.intro_text)
        print(padding_char * padding)
        if break_line:
            print('')

    def show_inputs(self, key: str, include_digit: bool = True, suffix: str = ''):
        for tup in self.inputs[key]:
            print(f'{tup[0]} - {tup[1]}' if include_digit else tup[1])

        if suffix != '':
            print(suffix)

    def read_input_for(self, key: str, run_associated_callback: bool = False):
        input_value = input()

        if run_associated_callback:
            for tup in self.inputs[key]:
                if input_value == tup[0]:
                    tup[2]()

        return input_value