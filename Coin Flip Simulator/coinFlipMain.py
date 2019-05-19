from random import randint

playing = True

heads = 0
tails = 0

while playing:
    print("Welcome to coin flip simulator. Here you can keep playing and at the end"
          "get the number of heads and tails that have appeared")
    status = int(input("Enter 1 to play and 0 to stop\n"))
    if status == 1:
        playing = True
        flip_result = randint(0, 1)
        if flip_result == 1:
            heads = heads + 1
            print("It's a head")
        else:
            tails = tails + 1
            print("It's a tail")
    else:
        playing = False
        print("Thank you for playing the coin flipper.")
        print("Number of heads is "+str(heads))
        print("Number of tails is "+str(tails))
        exit(0)
