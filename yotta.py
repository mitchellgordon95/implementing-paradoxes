import numpy as np
import matplotlib.pyplot as plt

PRIZES_NO_SPLITS = [.1, .15, .70, 8, 0, 0, 0, 0, 0, 0, .3, 10, 0, 0]
ODDS = [44, 72, 344, 3934, 108396, 8536197, 3277899625, 1.8, 3, 14, 164, 4517, 355675, 136579151]


def draw_tickets(n=1):
    """Draw yotta ball tickets"""
    probs = 1 / np.array(ODDS)
    probs = probs / np.sum(probs)
    return np.random.choice(PRIZES_NO_SPLITS, size=n, replace=True, p=probs)


def invest(dollars, weeks, compounding):

    if compounding:
        winnings = 0
        for week in range(weeks):
            tickets_per_week = int(dollars / 25)
            tickets = draw_tickets(tickets_per_week)
            winnings += np.sum(tickets)
            dollars += np.sum(tickets)
        return winnings
    else:
        tickets_per_week = int(dollars / 25)
        tickets = draw_tickets(tickets_per_week * weeks)
        winnings = np.sum(tickets)
        return winnings


def experiment(dollars, weeks, trials=10000, compounding=False):
    fig, axes = plt.subplots()

    axes.set_xlabel("Money Won")
    axes.set_ylabel("# People")

    winnings = []
    for i in range(trials):
        winnings.append(invest(dollars, weeks, compounding=compounding))

    axes.hist(winnings, 100)

    axes.set_title(f"Invest ${int(dollars / 1000)}k For One Year")
    fig.savefig(f'yotta_{dollars}_{weeks}_{trials}_{compounding}.png')

experiment(1000, 52, compounding=False)
plt.show()
