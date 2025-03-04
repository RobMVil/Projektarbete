import pytest
import time
from network_config_manager import NetworkConfigManager

@pytest.fixture()
def setup_teardown():
    manager = NetworkConfigManager()
    manager.connect()
    print("*******Setup*******")
    manager.update_hostname("1")
    manager.update_interface_state("down")
    manager.update_response_prefix("Standard Response")
    yield manager
    manager.disconnect()
    print("*******Disconnected*******")
    time.sleep(1)

@pytest.fixture()
def setup_teardown_test():
    manager = NetworkConfigManager()
    manager.connect()
    print("*******Setup TEST*******")
    manager.update_hostname("2")
    manager.update_interface_state("up")
    manager.update_response_prefix("Non-Standard Response")
    yield manager
    manager.disconnect()
    print("*******Disconnected TEST*******")
    time.sleep(1)

class Test_network_config:
    def test_show_hostname2(self, setup_teardown):
        assert setup_teardown.show_hostname() == "hostname: 1"

    def test_show_interface_state(self, setup_teardown):
        assert setup_teardown.show_interface_state() == "interface_state: down"

    def test_show_respnse_prefix(self, setup_teardown):
        assert setup_teardown.show_response_prefix() == "response_prefix: Standard Response"

    def test_updated_hostname(self, setup_teardown):
        setup_teardown.update_hostname("2")
        assert setup_teardown.show_hostname() == "hostname: 2"

    def test_updated_interface_state(self, setup_teardown):
        setup_teardown.update_interface_state("up")
        assert setup_teardown.show_interface_state() == "interface_state: up"
        
    def test_updated_response_prefix(self, setup_teardown):
        setup_teardown.update_response_prefix("Non-Standard Response")
        assert setup_teardown.show_response_prefix() == "response_prefix: Non-Standard Response"

class Test_network_different_values:
    def test_show_hostname(self, setup_teardown_test):
        assert setup_teardown_test.show_hostname() == "hostname: 2"