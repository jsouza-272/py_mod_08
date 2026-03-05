import os
import dotenv

dotenv.load_dotenv(verbose=True)
print(os.environ)
# os.environ['MATRIX'] = '10'
print(os.getenv('MATRIX'))
# os.putenv('MATRIX', '5')
# os.reload_environ()
# print('\n\n\n\n', os.environ)
# dotenv.load_dotenv()
# print(os.getenv('MATRIX'))
# print(os)
