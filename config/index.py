'''
    Load environment variables from .env file
'''

from dotenv import dotenv_values
config = dotenv_values(".env")
