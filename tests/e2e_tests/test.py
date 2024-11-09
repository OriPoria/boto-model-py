import os

from boto_model_py import run_transformation, RunTransformationStatus


def test():
    if not os.path.exists("response"):
        os.mkdir("response")
    for file in os.listdir("inputs"):
        transformation_status = run_transformation(f"inputs/{file}", "response")
        if transformation_status.status != "OK":
            raise Exception(f"Fail to run transformation on file {file}")
        print(f"Transformed {file} successfully")


def test_single():
    run_transformation(f"inputs/list_buckets", "response")
