import pytest
from network_config_manager import NetworkConfigManager

class Test_network_config:
    def setup_method(self):
        self.manager = NetworkConfigManager()
        self.manager.connect()
        self.manager.update_hostname("1")
        self.manager.update_interface_state("down")
        self.manager.update_response_prefix("Standard Response")
    def teardown_method(self):
        self.manager.disconnect()
    def test_show_host_name(self):
        assert self.manager.show_hostname() == "hostname: 1"