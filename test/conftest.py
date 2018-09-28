import quest
import pytest
import tempfile
import warnings
import os
import shutil
from time import time
from data import CACHED_SERVICES


def get_or_generate_test_cache(update=False, skip=False):
    test_cache_dir = os.environ.get('QUEST_CACHE_DIR') or os.path.join(quest.util.get_quest_dir(),
                                                                       '.cache', 'test_cache')
    if skip:
        # TODO with features refactor there are some tests that access cache that are not skipped.
        return test_cache_dir
    quest.api.update_settings({'CACHE_DIR': test_cache_dir})
    start = None
    if not os.path.exists(test_cache_dir) or update:
        print('Generating the providers metadata cache for tests. This may take several minutes.')
        start = time()

    # prevent warnings
    warnings.simplefilter('ignore')

    provider_plugins = quest.plugins.load_providers()

    for name in CACHED_SERVICES:
        provider, service, _ = quest.util.parse_service_uri(name)
        if provider.startswith('user'):
            continue
        provider_plugin = provider_plugins[provider]

        cache_file = os.path.join(quest.util.get_cache_dir(provider_plugin.name), service + '_catalog.p')
        if update or not os.path.exists(cache_file):
            try:
                print('Updating test cache for service: {0}'.format(name))
                quest.api.get_tags(name, update_cache=update)
            except Exception as e:
                print('The following error prevented the cache for the {0} service from updating: {1}: {2}'
                      .format(name, type(e).__name__, str(e)))

    # re-enable warnings
    warnings.simplefilter('default')

    if start is not None:
        print('Generated test cash in {0} seconds'.format(time() - start))

    return test_cache_dir


@pytest.fixture(scope='session')
def get_base_dir(request):
    base_dir_obj = tempfile.TemporaryDirectory()
    base_dir = base_dir_obj.name
    test_cache_dir = get_or_generate_test_cache()
    os.mkdir(os.path.join(base_dir, '.cache'))
    os.symlink(test_cache_dir, os.path.join(base_dir, '.cache', 'test_cache'))

    def cleanup():
        base_dir_obj.cleanup()

    request.addfinalizer(cleanup)
    return base_dir


@pytest.fixture
def reset_settings(api, get_base_dir):
    test_settings = {'BASE_DIR': get_base_dir,
                     'CACHE_DIR': os.path.join('.cache', 'test_cache'),
                     'PROJECTS_DIR': 'projects',
                     'USER_SERVICES': []
                     }

    api.update_settings(test_settings)
    return test_settings


@pytest.fixture
def reset_projects_dir(reset_settings, request):
    base_dir = reset_settings['BASE_DIR']
    projects_dir = os.path.join(base_dir, 'projects')

    def cleanup():
        shutil.rmtree(projects_dir, ignore_errors=True)

    cleanup()
    request.addfinalizer(cleanup)

    metadata = {'NUMBER_OF_PROJECTS': 4,
                'BASE_DIR': reset_settings['BASE_DIR'],
                }
    quest.api.get_projects()
    return metadata


@pytest.fixture(scope='session')
def api():
    return quest.api

