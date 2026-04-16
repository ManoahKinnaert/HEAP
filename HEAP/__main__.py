from experiments import *

if __name__ == "__main__":
    while True:
        exp_num = int(input("What experiment would you like to run (1-3)?\n"))
        if exp_num == 1:
            Heap1().run() 
        elif exp_num == 2:
            pass 
        elif exp_num == 3:
            pass 
        else:
            print("Error: invalid experiment number")

        cmd = input("Would you like to quit? (y/n) ")
        if cmd.lower() == "y": break
