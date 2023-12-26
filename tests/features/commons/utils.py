import os
from faker import Faker
import uuid
from datetime import datetime, timedelta
from tests.features.commons.stringManipulation import split_string_after, generate_random_number
import random

import os
from faker import Faker
import uuid
from datetime import datetime, timedelta
from tests.features.commons.stringManipulation import split_string_after, generate_random_number
import random


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(os.path.join(os.getcwd(), folder_path))


def delete_file(file_path):
    if file_exists(file_path):
        os.remove(file_path)


def file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

