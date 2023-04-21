Names = []
While True:
    Try:
        Name = input()
    Except EOFError:
        Break
    Names.append(name)

Num_names = len(names)
If num_names == 1:
    Print(“Adieu, adieu, to”, names[0])
Elif num_names == 2:
    Print(“Adieu, adieu, to”, names[0], “and”, names[1])
Elif num_names > 2:
    For I in range(num_names – 1):
        Print(names[i] + “,”, end=” “)
    Print(“and”, names[-1])
    For name in names:
        Print(“Adieu, adieu, to”, name)


