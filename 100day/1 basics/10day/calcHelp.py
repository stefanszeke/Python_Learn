def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid input, try again')
            continue
        
def get_operator(prompt: str, operations: dict) -> str:
    while True:
        op = input(prompt)
        if op in operations.keys():
            return op
        else:
            print('Invalid operator, please enter one of: ' + ', '.join(operations.keys()))