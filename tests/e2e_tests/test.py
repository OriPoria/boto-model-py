from boto_model_py.run import run_transformation


def test():
    run_transformation("inputs/list_buckets", "response")

