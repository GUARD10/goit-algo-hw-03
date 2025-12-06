def move_disks(n, source, auxiliary, target, state, steps):
    if n == 0:
        return

    move_disks(n - 1, source, target, auxiliary, state, steps)

    disk = state[source].pop()
    state[target].append(disk)

    steps.append(f"Move disc from {source} to {target}: {disk}")
    steps.append(f"Current state: {state}")

    move_disks(n - 1, auxiliary, source, target, state, steps)


def hanoy(n):
    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    steps = [f"Sart stat: {state}"]
    move_disks(n, 'A', 'B', 'C', state, steps)
    steps.append(f"End state: {state}")

    return steps

def main():
    n = int(input("Enter count of discs: "))
    for step in hanoy(n):
        print(step)


if __name__ == "__main__":
    main()
