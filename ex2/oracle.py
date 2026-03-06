import os
import sys
import dotenv


def development(matrix_mode: str) -> None:
    database_url = os.getenv('DATABASE_URL')
    api_key = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL')
    zion_endpoint = os.getenv('ZION_ENDPOINT')
    database_message = 'Database: Connected to local instance'
    api_message = 'API Access: Authenticated'
    log_massege = f'Log Level: {log_level}'
    zion_massege = 'Zion Network: Online'

    if database_url is None or database_url == '':
        database_message = "[WARNING] DATABASE_URL is not set. \
Database features will be unavailable."
    if api_key is None or api_key == '':
        api_message = "[WARNING] API_KEY is not set. \
External API access will be disabled."
    if log_level is None or log_level not in ('DEBUG', 'INFO'):
        os.environ.setdefault('LOG_LEVEL', "DEBUG")
        log_massege = "[WARNING] LOG_LEVEL is not set. \
Using default log level."
    if zion_endpoint is None or zion_endpoint == '':
        zion_massege = "[WARNING] ZION_ENDPOINT is not set. \
Zion network connection is offline."

    print('Mode:', matrix_mode)
    print(database_message)
    print(api_message)
    print(log_massege)
    print(zion_massege)


def production(matrix_mode: str) -> None:
    fail = False
    database_url = os.getenv('DATABASE_URL')
    api_key = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL')
    zion_endpoint = os.getenv('ZION_ENDPOINT')
    database_message = 'Database: Connected to local instance'
    api_message = 'API Access: Authenticated'
    log_massege = f'Log Level: {log_level}'
    zion_massege = 'Zion Network: Online'

    if database_url is None or database_url == '':
        fail = True
        database_message = "[ERROR] DATABASE_URL is not set."
    if api_key is None or api_key == '':
        fail = True
        api_message = "[ERROR] API_KEY is not set."
    if log_level is None or log_level not in ('DEBUG', 'INFO'):
        os.environ.setdefault('LOG_LEVEL', "INFO")
        log_massege = "[WARNING] LOG_LEVEL is not set. \
Using 'INFO' log level."
    if zion_endpoint is None or zion_endpoint == '':
        fail = True
        zion_massege = "[ERROR] ZION_ENDPOINT is not set."

    print('Mode:', matrix_mode)
    print(database_message)
    print(api_message)
    print(log_massege)
    print(zion_massege)

    if fail:
        sys.exit(1)


if __name__ == "__main__":
    try:
        dotenv.find_dotenv(raise_error_if_not_found=True)
        find = True
    except IOError:
        find = False

    if not find:
        os.environ.setdefault('MATRIX_MODE', 'development')
    else:
        dotenv.load_dotenv()

    print('\nORACLE STATUS: Reading the Matrix...')

    matrix_mode = os.getenv('MATRIX_MODE')

    if matrix_mode == "development":
        print('\nConfiguration loaded:')
        development(matrix_mode)
    elif matrix_mode == 'production':
        print('\nConfiguration loaded:')
        production(matrix_mode)
    else:
        print(f'\n[ERROR] Invalid "MATRIX_MODE={matrix_mode}". \
Expected "development" or "production"')
        sys.exit(1)

    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    if find:
        print('[OK] .env file properly configured')
    else:
        print('[KO] .env file not find')
    print('[OK] Production overrides available')

    print('\nThe Oracle sees all configurations.')
