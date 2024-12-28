#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:10:41 2024

@author: davidsimbandumwe
"""

from dotenv import load_dotenv
import os
from datetime import datetime


class Env_Vars:

    FRED_API_KEY = None
    GPT_KEY = None

    def __init__(self):
        """
        Initializes the FREDDataReader with a FRED API key.
        """
        # Load .env file
        load_dotenv()

        # Access environment variables
        Env_Vars.FRED_API_KEY = os.getenv("fred_api_key")
        Env_Vars.GPT_KEY = os.getenv("gpt_key")

        os.environ["OPENAI_API_KEY"] = Env_Vars.GPT_KEY

    def __str__(self):
        for attribute in dir(self):
            ret_value = ''
            if not attribute.startswith('__'):
                value = getattr(self, attribute)
                ret_value = ret_value + ' ' + value
                print(f"{attribute}: {value}")

        return ret_value


if __name__ == "__main__":
    e_var = Env_Vars()
    print(f"{e_var}: {e_var}")
