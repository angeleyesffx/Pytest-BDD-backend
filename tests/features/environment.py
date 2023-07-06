from random import random

from tests.conftest import Config
from tests.features.commons.utils import random_data_generator


def get_execute_flag():
    return True


def get_base_url(environment, country, service, method, version):
    url = str(Config.get_environment_basic_config(environment, "base_url")) + str(
        get_url(environment, country, service, method, version))
    return url


def get_zip_payload(environment, country, service, method, version):
    zip_payload = Config.get_config_from_version(environment, country, service, method, version, 'zip_payload')
    return zip_payload


def is_request_through_middleware_api(environment, country, service, method):
    request_through_middleware_api = Config.get_config_from_method(environment, country, service, method,
                                                                  "request_through_middleware_api")
    return request_through_middleware_api


def get_auth_payload(environment, country, service, method):
    payload = "grant_type=" + str(
        get_auth_grant_type(environment, country, service, method)) + "&client_id=" + str(
        get_auth_client_id(environment, country, service, method)) + "&scope=" + str(
        get_auth_scope(environment, country, service, method)) + "&client_secret=" + str(
        get_auth_client_secret(environment, country, service, method)) + ""
    return payload


def get_auth_token(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        return str(Config.get_config_from_country(environment, country, "middleware_api_auth_token"))
    else:
        return str(Config.get_config_from_method(environment, country, service, method, "auth_token"))


def get_timezone(environment, country):
    timezone = str(Config.get_config_from_country(environment, country, "timezone"))
    if timezone:
        return timezone
    return "America/Louisville"


def get_vendor_id(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        vendor_id = str(Config.get_config_from_country(environment, country, "middleware_api_vendor_id"))
        return vendor_id
    else:
        vendor_id = str(Config.get_config_from_method(environment, country, service, method, "auth_vendor_id"))
        return vendor_id


def get_auth_type(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_type = str(Config.get_config_from_country(environment, country, "middleware_api_auth_type"))
        return auth_type
    else:
        auth_type = str(Config.get_config_from_method(environment, country, service, method, "auth_type"))
        return auth_type


def get_auth_method(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_method = str(Config.get_config_from_country(environment, country, "middleware_api_auth_method"))
        return auth_method
    else:
        auth_method = str(Config.get_config_from_method(environment, country, service, method, "auth_method"))
        return auth_method


def get_auth_url(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_url = str(Config.get_config_from_country(environment, country, "middleware_api_auth_url"))
        return auth_url
    else:
        auth_url = str(Config.get_config_from_method(environment, country, service, method, "auth_url"))
        return auth_url


def get_auth_scope(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_scope = str(Config.get_config_from_country(environment, country, "middleware_api_auth_scope"))
        return auth_scope
    else:
        auth_scope = str(Config.get_config_from_method(environment, country, service, method, "auth_scope"))
        return auth_scope


def get_auth_grant_type(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_grant_type = str(Config.get_config_from_country(environment, country, "middleware_api_auth_grant_type"))
        return auth_grant_type
    else:
        auth_grant_type = str(Config.get_config_from_method(environment, country, service, method, "auth_grant_type"))
        return auth_grant_type


def get_auth_client_id(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_client_id = str(Config.get_config_from_country(environment, country, "middleware_api_auth_client_id"))
        return auth_client_id
    else:
        auth_client_id = str(Config.get_config_from_method(environment, country, service, method, "auth_client_id"))
        return auth_client_id


def get_auth_client_secret(environment, country, service, method):
    if is_request_through_middleware_api(environment, country, service, method):
        auth_client_secret = str(
            Config.get_config_from_country(environment, country, "middleware_api_auth_client_secret"))
        return auth_client_secret
    else:
        auth_client_secret = str(
            Config.get_config_from_method(environment, country, service, method, "auth_client_secret"))
        return auth_client_secret


def get_url(environment, country, service, method, version):
    if is_request_through_middleware_api(environment, country, service, method):
        url = Config.get_config_from_version(environment, country, service, method, version, "url")
        return url
    else:
        url = Config.get_config_from_version(environment, country, service, method, version, "value_stream_url")
        return url


def get_supported_languages(environment, country):
    supported_languages = Config.get_config_from_country(environment, country, "supported_languages")
    languages = supported_languages.replace(' ', '').split(",")
    language = random.choice(languages)
    return language


def get_id_prefix(environment, country, service, method, version):
    id_prefix = Config.get_config_from_version(environment, country, service, method, version, "id_prefix")
    return id_prefix


def define_country_fake_data(country):
    if country in ['ar', 'co', 'de', 'do', 'ec', 'hn', 'pa', 'pe', 'py', 'sv', 'uy']:
        selected_fake_data = 'es'
    elif country == 'br':
        selected_fake_data = 'pt_BR'
    elif country == 'de':
        selected_fake_data = 'en_DE'
    elif country == 'ca':
        selected_fake_data = 'en_CA'
    elif country == 'gb':
        selected_fake_data = 'en_GB'
    elif country == 'mx':
        selected_fake_data = 'es_MX'
    elif country == 'pt':
        selected_fake_data = 'pt_PT'
    elif country == 'kr':
        selected_fake_data = 'ko-KR'
    elif country == 'us':
        selected_fake_data = 'en_US'
    else:
        selected_fake_data = 'en'
    return selected_fake_data


def get_param_keys(environment, country, service, method, version):
    param_keys = Config.get_config_from_version(environment, country, service, method, version, "param_keys")
    if param_keys is not None:
        params = param_keys.replace(" ", "")
        return params


def create_param_dict(params):
    # using strip() and split()  methods
    if params != 'None' and params != 'none' and params != '' and params is not None:
        result = dict((key.strip(), value.strip())
                      for key, value in (element.split(':')
                                         for element in params.split(',')))
        return result


def get_data_param_keys(environment, country, params, static_params=None, prefix=None):
    language = define_country_fake_data(country)
    static_params = create_static_params_dict(static_params)
    param_dict = create_param_dict(params)
    data = None
    if static_params is not None:
        for key, value in static_params.items():
            param_dict[key] = value
    if param_dict is not None:
        data = random_data_generator(param_dict, language, prefix)
    return data


def get_static_params(environment, country, service, method, version):
    static_params = Config.get_config_from_version(environment, country, service, method, version, "static_params")
    if static_params is not None:
        params = static_params.replace(" ", "")
        return params


def create_static_params_dict(static_params):
    # using strip() and split()  methods
    if static_params != 'None' and static_params != 'none' and static_params != '' and static_params is not None:
        result = dict((key.strip(), value.strip())
                      for key, value in (element.split('=')
                                         for element in static_params.split(',')))
        return result


def get_encoding_type(environment, country, service, method, version):
    encoding_type = Config.get_config_from_version(environment, country, service, method, version, "encoding_type")
    return encoding_type


def get_template_name(environment, country, service, method, version):
    template_name = Config.get_config_from_version(environment, country, service, method, version, "template_name")
    return template_name


def get_data_source(environment, country, service, method, version):
    data_name = Config.get_config_from_version(environment, country, service, method, version, "csv_data_source")
    return data_name


def get_csv_strategy(environment, country, service, method, version):
    csv_strategy = Config.get_config_from_version(environment, country, service, method, version, "csv_strategy")
    return csv_strategy


def get_csv_scenario(environment, country, service, method, version):
    csv_scenario = Config.get_config_from_version(environment, country, service, method, version, "csv_scenario")
    if not csv_scenario:
        return None
    scenarios_list = csv_scenario.replace(' ', '').split(",")
    return scenarios_list


def get_amount_data_mass(environment, country, service, method, version):
    amount_data_mass = Config.get_config_from_version(environment, country, service, method, version, "amount_data_mass")
    return amount_data_mass
