for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            print("  B  ", end = "") #instead of printing chars, print a box with an attribute
        else:
            print("  W  ", end = "") #instead of printing chars, print a box with an attribute
    print("\n")
