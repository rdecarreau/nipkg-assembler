import pytest
import pathlib
import yaml
from nipkg_assembler.update_control_file import *


def test_update_control_file():
    main('tests/temp_package', 'Version', '9.9.9')
    with open('tests/temp_package/control/control', 'r') as cf:
        control = yaml.safe_load(cf)
    assert control["Version"] == '9.9.9'
