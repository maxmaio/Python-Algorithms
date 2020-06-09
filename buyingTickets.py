def waitingTime(tickets, p):
    total_steps = tickets[p]
    first_half = tickets[:p]
    second_half = tickets[p+1:]

    for num in first_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p]

    for num in second_half:
        if num < tickets[p]:
            total_steps += num
        else:
            total_steps += tickets[p] - 1

    return total_steps