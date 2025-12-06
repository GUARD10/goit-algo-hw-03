from koch_draw import draw_snowflake


def main():
    while True:
        level = int(input("Enter recurse level (0–8): "))

        if level > 8 or level < 0:
            print("Level must be between 0 and 8")
            continue

        draw_snowflake(level)

        command = input("Enter 'q' to quit or any other key to continue: ")
        if command.lower() == 'q':
            break


if __name__ == "__main__":
    main()