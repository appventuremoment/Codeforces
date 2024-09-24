for _ in range(int(input())):
    input()
    out = 'YES'
    tasks = [*input()]
    curr = tasks[0]
    done = [curr]
    for task in tasks:
        if curr != task:
            if task in done:
                out = 'NO'
                break
            else:
                done.append(task)
                curr = task
    print(out)