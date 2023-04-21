Import random


Def main():
    Level = get_level()
    Score = 0
    For I in range(10):
        Problem = generate_problem(level)
        Answer = prompt_answer(problem)
        If answer == problem[2]:
            Score += 1
        Else:
            Print(“EEE”)
            For j in range(2):
                Answer = prompt_answer(problem)
                If answer == problem[2]:
                    Score += 1
                    Break
                Else:
                    Print(“EEE”)
            Else:
                Print(f”The correct answer is {problem[2]}”)
    Print(f”Your score is {score}/10”)


Def get_level():
    While True:
        Level = input(“Enter level (1, 2, or 3): “)
        If level.isdigit() and int(level) in (1, 2, 3):
            Return int(level)
        Print(“Invalid level. Please enter 1, 2, or 3.”)


Def generate_problem(level):
    X = random.randint(0, 10**level – 1)
    Y = random.randint(0, 10**level – 1)
    Result = x + y
    Return f”{x} + {y} = {result}”


Def prompt_answer(problem):
    While True:
        Answer = input(problem + “ “)
        If answer.isdigit():
            Return int(answer)
        Print(“Invalid answer. Please enter a non-negative integer.”)


If __name__ == “__main__”:
    Main()
