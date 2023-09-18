import pytest

def pytest_addoption(parser):
    parser.addoption(
        '--id', action='store', default='2074661', help='ID'
    )
    parser.addoption(
        '--pw', action='store', default='bdpdnjs05*', help='password'
    )
    parser.addoption(
        '--resv-date', action='store', default='1', help='Reservation Date'
    )
    parser.addoption(
        '--resv-state', action='store', default='충북', help='Reservation State'
    )
    parser.addoption(
        '--resv-si', action='store', default='제천시', help='Reservation Si' 
    )
    parser.addoption(
        '--resv-room-type', action='store', default='2', help='Reservation Room type index shown in website' 
    )

@pytest.fixture
def auto_resv_params(resvInfo):
    
    auto_resv_params = {}
    auto_resv_params['id'] = resvInfo.config.getoption('--id')
    auto_resv_params['pw'] = resvInfo.config.getoption('--pw')
    auto_resv_params['resv_date'] = resvInfo.config.getoption('--resv-date')
    auto_resv_params['resv_state'] = resvInfo.config.getoption('--resv-state')
    auto_resv_params['resv_si'] = resvInfo.config.getoption('--resv-si')
    auto_resv_params['resv_room_type'] = resvInfo.config.getoption('--resv-room-type')
    
    if auto_resv_params['id'] is None or auto_resv_params['password'] is None:
        pytest.skip()
    
    return auto_resv_params