import argparse
import secrets
import string


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not characters:
        raise ValueError("You must choose at least one character type.")

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator")

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Password length"
    )

    parser.add_argument(
        "--no-letters",
        action="store_true",
        help="Do not use letters"
    )

    parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Do not use numbers"
    )

    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Do not use symbols"
    )

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_letters=not args.no_letters,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols
        )

        print("Generated password:", password)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
