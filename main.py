
import config
config.LOGS_PATH = config.LOGS_PATH.format(module="main")

from app import main_app


def main():
    main_app.run()


if __name__ == '__main__':
    main()
