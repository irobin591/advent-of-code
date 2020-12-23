# Advent of Code 2020
# Day 22
# Author: irobin591

import os
import doctest

with open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r') as input_file:
    input_data = input_file.read().strip().split('\n\n')


def calc_score(deck):
    score = 0
    for i, card in enumerate(deck[::-1]):
        score += (i+1)*card
    return score


def part1(input_data):
    """
    >>> part1(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n\\n'))
    306
    """
    # Combat card game

    deck1 = list(map(int, input_data[0].split('\n')[1:]))
    deck2 = list(map(int, input_data[1].split('\n')[1:]))

    # Play rounds until a deck is empty
    while len(deck1) != 0 and len(deck2) != 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        # Add cards to winning deck, highest card first
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)
        pass

    # Calc player score
    score1 = calc_score(deck1)
    score2 = calc_score(deck2)

    return max([score1, score2])


def part2(input_data):
    """
    >>> part2(open(os.path.join(os.path.dirname(__file__), "test_part1.txt"), 'r').read().strip().split('\\n\\n'))
    291
    """
    # Recursive Combat card game

    deck1 = list(map(int, input_data[0].split('\n')[1:]))
    deck2 = list(map(int, input_data[1].split('\n')[1:]))

    def play_recursive_combat(deck1, deck2):
        previous_decks1 = []
        previous_decks2 = []

        # Play rounds until a deck is empty
        while len(deck1) != 0 and len(deck2) != 0:
            # Check if deck is the same as before TODO
            if deck1 in previous_decks1 and deck2 in previous_decks2:
                return (1,0)
            previous_decks1.append(deck1.copy())
            previous_decks2.append(deck2.copy())

            # Draw top cards
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)

            if len(deck1) >= card1 and len(deck2) >= card2:
                # Play another recursive round of Recursive Combat
                score1, score2 = play_recursive_combat(deck1[:card1].copy(), deck2[:card2].copy())
                if score1 > 0:
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    deck2.append(card2)
                    deck2.append(card1)
            else:
                # Add cards to winning deck, highest card first
                if card1 > card2:
                    deck1.append(card1)
                    deck1.append(card2)
                else:
                    deck2.append(card2)
                    deck2.append(card1)

        return calc_score(deck1), calc_score(deck2)

    score1, score2 = play_recursive_combat(deck1, deck2)

    return max(score1, score2)


if __name__ == "__main__":
    doctest.testmod()
    print("Part One: {}".format(part1(input_data)))
    print("Part Two: {}".format(part2(input_data)))
    pass