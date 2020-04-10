import logging


# Create simple formatter
simple_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a more detailed formatter
detailed_formatter = logging.Formatter('[%(asctime)s - %(name)s %(funcName)20s() %(process)d %(thread)d] %(levelname)s: %(message)s')

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler("app.log", mode='w')
file_handler.setLevel(logging.INFO)

# We set simple formatter for console and detailed formatter to file handler
console_handler.setFormatter(simple_formatter)
file_handler.setFormatter(detailed_formatter)

# Setup a new logger
logger = logging.getLogger("example-logger")
logger.setLevel(logging.DEBUG)

# Map existing handlers to this logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Start using logger
def do_something():
    logger.info('Hello, this is my first informational log. This will go to '
                'console and file but with different formatting')


def do_something_else():
    logger.debug("Test debug severity level")
    logger.warning("Hello, this is my second log. This time it's a warning log")
    try:
        10/0
    except ZeroDivisionError:
        logger.error('Tried to divide by 0', exc_info=True)


if __name__ == '__main__':
    do_something()
    do_something_else()
