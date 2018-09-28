import pytest
from data import SERVICES_CATALOG_COUNT, SERVICE_DOWNLOAD_OPTIONS, DOWNLOAD_OPTIONS_FROM_ALL_SERVICES

pytestmark = pytest.mark.usefixtures('reset_projects_dir')


def test_get_noaa_ncep(api):
    providers = api.get_providers()
    assert 'noaa-ncep' in providers


def test_get_services(api):
    services = ['svc://noaa-ncep:ncep_gfs', 'svc://noaa-ncep:ncep_nam']
    all_services = api.get_services()
    for item in services:
        assert item in all_services


@pytest.mark.parametrize('catalog_entry, options', SERVICE_DOWNLOAD_OPTIONS)
def test_download(api, catalog_entry, options):
    api.new_collection('test')
    # d = api.add_datasets('test', catalog_entry)
    # print(d)
    # api.stage_for_download(d[0], options=options)[0]
    # result = api.download_datasets(d, raise_on_error=True)
    # assert result[d[0]] == 'downloaded'


@pytest.mark.parametrize('service, options', [(k, v) for k, v in DOWNLOAD_OPTIONS_FROM_ALL_SERVICES.items()])
def test_download_options_for_services(api, service, options):
    actual = api.get_download_options(service)[service]
    expected = options
    assert actual == expected


@pytest.mark.parametrize("service, expected, tolerance", SERVICES_CATALOG_COUNT)
def test_search_catalog_from_service(api, service, expected, tolerance):
    catalog_entries = api.search_catalog(service)
    # assert number of catalog entries is within tolerance of expected
    assert abs(len(catalog_entries) - expected) < tolerance