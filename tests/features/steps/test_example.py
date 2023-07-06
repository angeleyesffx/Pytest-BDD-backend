import uuid

from pytest_bdd import scenarios, given, when, then, parsers

from tests.features.commons.payloadBuilder import data_and_header_creation, create_payload
from tests.features.commons.requestBuilder import send_request, create_header
from tests.features.environment import get_template_name, get_data_source, get_auth_url, get_auth_method, get_auth_type, \
    get_auth_token, get_auth_payload, get_base_url, is_request_through_middleware_api, get_zip_payload, get_id_prefix, \
    get_csv_strategy, get_param_keys, get_static_params, get_amount_data_mass, get_timezone

scenarios('../example.feature')


@given(parsers.parse('an user from the country {country} with the valid credential'), target_fixture="get_the_country")
def get_the_country(country):
    return country


@when(parsers.parse('the user choose the entity {entity} and the API method {method} - {version}'),
      target_fixture="get_entity_method_and_version")
def get_entity_method_and_version(entity, method, version):
    return entity, method, version


@when(parsers.parse('the user prepare the request using {scenario} information'), target_fixture="arrange_data_scenario")
def arrange_data_scenario(set_up_environment, scenario, get_the_country, get_entity_method_and_version ):
        country = get_the_country
        entity, method, version = get_entity_method_and_version
        data_source = get_data_source(set_up_environment, country, entity, method, version)
        param_keys = get_param_keys(set_up_environment, country, entity, method, version)
        static_params = get_static_params(set_up_environment,country, entity, method, version)
        amount_data_mass = get_amount_data_mass(set_up_environment, country, entity, method, version)
        data, data_header = data_and_header_creation("scenario_line", data_source, country, "", scenario,
                                                     None, param_keys, static_params, amount_data_mass)
        return data, data_header


@when(parsers.parse('the user get a valid token'), target_fixture="get_header_to_access")
def get_header_to_access(set_up_environment, get_the_country, get_entity_method_and_version, arrange_data_scenario):
    country = get_the_country
    entity, method, version = get_entity_method_and_version
    request_trace_id = "Pytest-API-" + country.upper() + "-" + method.upper() + "-" + \
                       version.upper() + "-" + str(uuid.uuid4().hex)
    timezone = get_timezone(set_up_environment, country)
    auth_url = get_auth_url(set_up_environment,country, entity, method)
    auth_method = get_auth_method(set_up_environment, country, entity, method)
    auth_type = get_auth_type(set_up_environment,country, entity, method)
    auth_token = get_auth_token(set_up_environment,country, entity, method)
    auth_payload = get_auth_payload(set_up_environment,country, entity, method)
    auth_header = {"requestTraceId": request_trace_id, "country": country.upper(), "timezone": timezone}
    zip_payload_needed = get_zip_payload(set_up_environment, country, entity, method, version)
    data, data_header = arrange_data_scenario
    header = create_header(data_header, auth_url, auth_method, auth_type, auth_payload, auth_token, request_trace_id,
                           auth_header, zip_payload_needed)
    return header, data



@when(parsers.parse('the user send the request'), target_fixture="send_the_request")
def send_the_request(set_up_environment, get_the_country, get_entity_method_and_version, get_header_to_access):
    country = get_the_country
    entity, method, version = get_entity_method_and_version
    header, data = get_header_to_access
    url = get_base_url(set_up_environment, country, entity, method, version)
    request_name = country + "-" + entity + "-" + method + "-" + version
    template_name = get_template_name(set_up_environment, country, entity, method, version)
    request_through_middleware_api = is_request_through_middleware_api(set_up_environment, country, entity, method)
    zip_payload_needed = get_zip_payload(set_up_environment, country, entity, method, version)
    payload = create_payload(template_name, data, entity, method, version, False,
                             request_through_middleware_api)
    request = send_request(request_name, method, url, header, payload, data, False, request_through_middleware_api,
                          zip_payload_needed)
    return request



@then(parsers.parse('the status response to the valid request should be status: {status}'),
      target_fixture="check_valid_response_status")
def check_valid_response_status(send_the_request):
    request = send_the_request
    assert request.status_code in range(200, 220)


@then(parsers.parse('the status response to the invalid request should be status: {status}'),
      target_fixture="check_invalid_response_status")
def check_invalid_response_status(send_the_request):
    request = send_the_request
    assert request.status_code == 400
