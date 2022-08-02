"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(get_score(score))
    random_score = random.randint(0, 100)
    print(random_score, get_score(random_score))


def get_score(score):
    if score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score < 50:
        return "Bad"
    elif score < 0:
        return "Invalid score"

main()