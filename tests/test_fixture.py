import pytest
from network_config_manager import NetworkConfigManager
import time

class Test_network_config:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.manager = NetworkConfigManager()
        self.manager.connect()
        print("*****Setup*****")
        self.manager.update_hostname("1")
        self.manager.update_interface_state("down")
        self.manager.update_response_prefix("Standard Response")
        yield
        self.manager.disconnect()
        print("*****Disconnect*****")
        time.sleep(1)

    def test_show_hostname(self):
        assert self.manager.show_hostname() == "hostname: 1"

    def test_show_interface_state(self):
        assert self.manager.show_interface_state() == "interface_state: down"

    def test_show_respnse_prefix(self):
        assert self.manager.show_response_prefix() == "response_prefix: Standard Response"

    def test_updated_hostname(self):
        self.manager.update_hostname("2")
        assert self.manager.show_hostname() == "hostname: 2"

    def test_updated_interface_state(self):
        self.manager.update_interface_state("up")
        assert self.manager.show_interface_state() == "interface_state: up"

    def test_updated_response_prefix(self):
        self.manager.update_response_prefix("Non-Standard Response")
        assert self.manager.show_response_prefix() == "response_prefix: Non-Standard Response"