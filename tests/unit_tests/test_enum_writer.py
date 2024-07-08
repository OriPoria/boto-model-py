from boto_model_py.enum_writer import generate_enum_var_name


def test_generate_enum_var_name_camel():
    res = generate_enum_var_name("testSet")
    assert res == "TEST_SET"


def test_generate_enum_var_name_all_upper():
    res = generate_enum_var_name("TEST")
    assert res == "TEST"
