from board import Board 

def main():
    my_board = Board()
    name = input("What is your name ")
    print(f"Hello {name}")
    print(my_board.board)


if __name__ == "__main__":
    main()