from math import floor
from random import randint
from TerminalApp_Base import ConsoleApplication

application: ConsoleApplication
in_game: bool = False
expected: int = 0
difficulty: int = 0
points: int = 0

def setup():
    global application, points

    application = ConsoleApplication(
        'Welcome to Math Game',
        {
        'Main': [
            ['1', 'Play Game - Easy'],
            ['2', 'Play Game - Standard'],
            ['3', 'Play Game - Hard']
        ],
        'Game': [
            ['', f'Points: {points}'],
            ['', 'Answer the question below'],
            ['', '(C to close, Q to Quit)']
        ]
    })

    application.show_intro()

def run_loop():
    global in_game, expected
    while True:
        state = 'Main' if not in_game else 'Game'

        if state == 'Main':
            update_point_output(points)
            application.show_inputs(state, not in_game)
            select_difficulty(application.read_input())

        else:
            question, expected = generate_question(difficulty)
            application.show_inputs(state, not in_game, question)
            if process_game_input(application.read_input()) == 'Stop':
                print("See you again!")
                break


def update_point_output(value: int):
    application.update_input_entry(
        'Game',
        0,
        f'Points: {value}',
        show_key = False)

def process_game_input(value: str):
    if value == 'Q':
        return 'Stop'
    elif value == 'C':
        close_game()
    else:
        if validate_question(expected, int(value)):
            add_points()
            update_point_output(points)
            print("Correct answer!")
        else:
            print("Wrong answer, try again.")

    return ''


def select_difficulty(key: str):
    global difficulty, points, in_game
    difficulty = int(key)
    in_game = True
    points = 0

def generate_question(dif: int):
    ops = (
        ('+', lambda a, b: a + b),
        ('-', lambda a, b: a - b),
        ('*', lambda a, b: a * b),
        ('/', lambda a, b: floor(a / b)))
    lhs:int = randint(1, 10)
    rhs:int = lhs
    while rhs == lhs:
        rhs = randint(1, 10)
        pass

    lhs = lhs**dif
    rhs = rhs**dif
    op = ops[randint(0, 3)]

    return f'{lhs}{op[0]}{rhs}', op[1](lhs, rhs)


def validate_question(exp: int, answer: int):
    return answer == exp


def add_points(amount: int = 1):
    global points
    points += amount

def close_game():
    global  in_game, points, difficulty
    modes = 'Easy', 'Normal', 'Hard'
    print(f'Scored {points} in {modes[difficulty - 1]}')
    in_game = False
    difficulty = 0
    points = 0

setup()
run_loop()