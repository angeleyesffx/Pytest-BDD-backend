import os
import yaml
import pytest
from tests.features.commons.utils import random_data_generator
import random


class Config(object):

    def __init__(self, environment):
        self.environment = environment

    def get_environment_basic_config(environment, key):
        config_env = environment.get(key)
        return config_env

    def get_config_from_country(environment, country, key):
        config_country = environment.get("countries").get(country).get(key)
        return config_country


    def get_config_from_entity(environment, country, service, key):
        config_entity = environment.get("countries").get(country).get("services").get(service).get(key)
        return config_entity


    def get_config_from_method(environment, country, service, method, key):
        config_method = environment.get("countries").get(country).get("services").get(service).get(method).get(key)
        return config_method


    def get_config_from_version(environment, country, service, method, version, key):
        config_version = environment.get("countries").get(country).get("services").get(service).get(method).get(
            "versions").get(
            version).get(key)
        return config_version

    def get_timezone(environment, country):
        timezone = environment.get("countries").get(country).get("timezone")
        if timezone:
            return timezone
        return "America/Louisville"

def pytest_addoption(parser):
    parser.addoption("--config_yaml", action="store", default="config",
                     help="The configuration file to be used for the tests")
    parser.addoption("--environment", action="store", default="sit",
                     help="The configuration of the environment to be used for the tests")


@pytest.fixture
def set_up_environment(request):
    config_yaml_name = request.config.getoption("--config_yaml")
    env = request.config.getoption("--env")
    config_data = select_the_config_file(config_yaml_name)
    config_env = select_the_environment(env, config_data)
    return config_env


def read_yml_file(yml_file_name):
    file_path = os.path.dirname(__file__) + "/features/" + yml_file_name + ".yml"
    if os.path.exists(file_path):
        with open(file_path) as file:
            data = yaml.full_load(file)
            file.close()
            return data
    else:
        raise FileNotFoundError("File does not exist in the path {0}".format(file_path))


def select_the_config_file(config_yaml):
    if config_yaml is None:
        config_file = read_yml_file("config")
        return config_file
    else:
        config_file = read_yml_file(config_yaml)
        return config_file


def select_the_environment(env, config_yaml):
    for item in config_yaml.keys():
        if item == env:
            return config_yaml.get(env)







