from task_3.task_3 import hanoy


def parse_state(log_line: str):
    prefix = "Current state: "
    if not log_line.startswith(prefix):
        return None
    return eval(log_line[len(prefix):])


def test_hanoy_final_state():
    n = 5
    log = hanoy(n)

    final_state_line = log[-1]
    assert final_state_line.startswith("End state:")

    state = eval(final_state_line.split(":", 1)[1].strip())

    assert state == {
        'A': [],
        'B': [],
        'C': [5, 4, 3, 2, 1]
    }


def test_hanoy_step_count():
    n = 5
    log = hanoy(n)

    move_steps = [line for line in log if line.startswith("Move disc")]

    assert len(move_steps) == 2 ** n - 1


def test_states_match_moves():
    n = 4
    log = hanoy(n)

    state = {'A': [4, 3, 2, 1], 'B': [], 'C': []}

    for i, line in enumerate(log):
        if not line.startswith("Move disc"):
            continue

        parts = line.replace("Move disc from ", "").split(":")
        move, disc_str = parts[0], parts[1].strip()

        source, rest = move.split(" to ")
        target = rest.strip()

        disk = int(disc_str)

        assert state[source][-1] == disk

        state[source].pop()
        state[target].append(disk)

        next_line = log[i + 1]
        parsed = parse_state(next_line)

        assert parsed == state


def test_no_illegal_moves():
    n = 4
    log = hanoy(n)

    state = {'A': [4, 3, 2, 1], 'B': [], 'C': []}

    for line in log:
        if not line.startswith("Move disc"):
            continue

        parts = line.replace("Move disc from ", "").split(":")
        move, disc_str = parts[0], parts[1].strip()

        source, rest = move.split(" to ")
        target = rest.strip()

        disk = int(disc_str)

        assert state[source][-1] == disk
        state[source].pop()

        if state[target]:
            assert state[target][-1] > disk, f"Illegal move detected"

        state[target].append(disk)
