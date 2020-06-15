import pytest
import pathlib
from nipkg_assembler.update_control_file import *


def test_create_default_package():
    main('tests/temp_package', 'nipkg_assembler/default_package', False)
    assert pathlib.Path('tests/temp_package').exists()
