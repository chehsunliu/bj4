import argparse

import PyPtt


def main(username: str, password_from: str):
    with open(password_from, "r") as f:
        password = f.read()

    ptt_bot = PyPtt.API()
    ptt_bot.login(username, password)
    ptt_bot.logout()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password-from", required=True)

    args = parser.parse_args()
    main(**vars(args))
