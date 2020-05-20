import pytest
import pathlib
import nipkg_assembler.create_default_package as nipm


def test_create_default_package():
    nipm.main('tests/temp_package', 'nipkg_assembler/default_package', False)
    assert pathlib.Path('tests/temp_package').exists()
