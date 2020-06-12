import argparse
import sys

def calc(args):
    if(args.operation =="add"):
        return args.x + args.y 
    else:
        return args.x - args.y 


def main():
    parser= argparse.ArgumentParser("Description")

    parser.add_argument("--x",type=float,default=1.0,help="What is the first number?")
    parser.add_argument("--y",type=float,default=1.0,help="What is the second number?")
    parser.add_argument("--operation",type=str,default="add",help="What is the operation?")

    args = parser.parse_args()

    print(calc(args))


if __name__ == "__main__":
    main()
