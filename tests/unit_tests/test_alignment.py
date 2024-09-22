from boto_model_py.preprocessing import alignment


def test_alignment():
    with open("inputs/describe_key") as f:
        s_ = f.read()
    print(alignment(s_))