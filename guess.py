import random
import os
import sys

BEST_SCORE_FILE = "best_score.txt"
MIN_VAL = 1
MAX_VAL = 100


def load_best_score():
    try:
        if not os.path.exists(BEST_SCORE_FILE):
            return None
        with open(BEST_SCORE_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except Exception:
        return None


def save_best_score(score):
    try:
        with open(BEST_SCORE_FILE, "w", encoding="utf-8") as f:
            f.write(str(score))
    except Exception:
        pass


def choose_difficulty():
    print("Choose difficulty:")
    print("  1) Easy  (unlimited tries)")
    print("  2) Medium (10 tries)")
    print("  3) Hard  (7 tries)")
    while True:
        choice = input("Select 1/2/3 (default 1): ").strip()
        if choice == "":
            return None
        if choice in ("1", "easy"):
            return None
        if choice in ("2", "medium"):
            return 10
        if choice in ("3", "hard"):
            return 7
        print("Please enter 1, 2, or 3.")


def play_round(max_attempts=None):
    secret = random.randint(MIN_VAL, MAX_VAL)
    attempts = 0
    best = load_best_score()

    if max_attempts:
        print(f"You have {max_attempts} attempts to guess the number.")

    while True:
        try:
            guess = input(f"Enter your guess ({MIN_VAL}-{MAX_VAL}) or 'q' to quit: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)

        if guess.lower().strip() == "q":
            print("Goodbye!")
            sys.exit(0)

        if not guess.strip().isdigit():
            print("Please enter a valid integer.")
            continue

        guess = int(guess)
        if guess < MIN_VAL or guess > MAX_VAL:
            print(f"Please pick a number between {MIN_VAL} and {MAX_VAL}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            if best is None or attempts < best:
                print("🏆 New best score!")
                save_best_score(attempts)
            else:
                print(f"Best score remains {best} tries.")
            return True

        if max_attempts and attempts >= max_attempts:
            print(f"Out of attempts — the number was {secret}.")
            return False


def main():
    print("🎯 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {MIN_VAL} and {MAX_VAL}...")

    while True:
        max_attempts = choose_difficulty()
        play_round(max_attempts=max_attempts)

        again = input("Play again? (y/N): ").strip().lower()
        if not again.startswith("y"):
            print("Thanks for playing — goodbye!")
            break


if __name__ == "__main__":
    main()
