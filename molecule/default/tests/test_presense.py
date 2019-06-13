import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nodejs_pkg_exists(host):
    assert host.file('/var/www/www_example_com/node_modules/fo/fo.js').exists
