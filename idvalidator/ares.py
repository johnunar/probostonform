import requests
import xmltodict
from requests import RequestException

from idvalidator.exceptions import AresConnectionError, AresResponseError, AresSystemError


def validate_business_id_checksum(business_id):
    """
    Validate czech business ID

    :param business_id: business id to be checked (8-digit identificator)
    :type business_id: string
    :returns True if ID valid, False if ID invalid
    """

    # Check if the given ID has the right length
    if len(business_id) != 8:
        return False

    checksum = 0

    business_id_reversed = business_id[::-1][1:8]
    for i, char in enumerate(business_id_reversed, start=2):
        try:
            checksum += int(char) * i
        except ValueError:
            return False

    remainder = checksum % 11

    if (remainder == 0 and business_id[-1] == '1') or (remainder == 1 and business_id[-1] == '0') or (
            business_id[-1] == '%s' % (11 - remainder)):
        return True
    else:
        return False


def validate_business_id_ares(business_id):
    """
    Validate given business_id with ARES
    https://wwwinfo.mfcr.cz/ares/ares_xml_standard.html.cz

    :param business_id: business id to be checked (8-digit identificator)
    :type business_id: string
    :returns True if ID valid, False if ID invalid
    """

    ARES_URL = "https://wwwinfo.mfcr.cz/cgi-bin/ares/darv_std.cgi/"
    params = {'ico': business_id}

    try:
        response = requests.get(ARES_URL, params=params)
    except RequestException as e:
        raise AresConnectionError('The server was unable to establish connection to ARES: ' + str(e))

    if response.status_code != 200:
        raise AresResponseError(response.status_code)

    response.encoding = 'utf-8'
    ares_data = xmltodict.parse(response.text)

    response_root = ares_data['are:Ares_odpovedi']

    # Check for ARES errors
    ares_error = response_root['are:Odpoved'].get('are:Error')
    if ares_error is not None:
        raise AresSystemError(ares_error['dtt:Error_kod'], ares_error['dtt:Error_text'])

    # Get the number of results for the given business ID
    results_count = response_root['are:Odpoved']['are:Pocet_zaznamu']
    print(results_count)

    if int(results_count) == 0:
        return False
    else:
        return True
