import pytest


@pytest.fixture
def set_up():
    print('system enter success')
    yield
    print('exit from system')


@pytest.fixture(scope='module')
def some():
    print('Start')
    yield
    print('The end')

# @pytest.fixture(scope='function')
# def some():
#     print('Start')
#     yield
#     print('The end')
#
# @pytest.fixture(scope='class')
# def some():
#     print('Start')
#     yield
#     print('The end')