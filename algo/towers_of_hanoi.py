def towers_of_hanoi(disk, source, destination, auxillary):
    if disk == 1:
        print("Move disk ", disk, " from ", source, " to ", destination)
    else:
        towers_of_hanoi(disk - 1, source, auxillary, destination)
        print("Move disk ", disk, " from ", source, " to ", destination)
        towers_of_hanoi(disk - 1, auxillary, destination, source)


towers_of_hanoi(3, "A", "C", "B")
