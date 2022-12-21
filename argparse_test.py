import argparse

parser = argparse.ArgumentParser(description="Our example parser.")


parser.add_argument("name", help='filename')
parser.add_argument("-age", type=int)
parser.add_argument("-cars", nargs='+')
parser.add_argument("-balance", type=int)
parser.add_argument("-address", nargs=2)
#name| -age|
args = parser.parse_args()

# print(args)
#
# print(f"{args.name=}")
# print(f"{args.age=}")
if args.age>17:
    print(f"This is {args.name} , he is adult, his age is {args.age}")
else:
    print(f"This is {args.name} , he isn't adult, his age is {args.age}")


if args.cars != None:
    cars = list(args.cars)

    i = 1
    print(f"This is {args.name} cars:")
    for car in cars:
        print(f"{i} -> {car}")
        i+=1



if args.balance != None:
    print(f"{args.balance=}👌")

if args.address !=None:
    print(f"{args.name} is living on {args.address[0]} number {args.address[1]}")


# parser.add_argument("--filename", "-f", required=True)
# parser.add_argument("--medals", actions="store_true", required=False)
#
# args = parser.parse_args()
#
# print(f"{args.filename=}")
#
# print(args)
