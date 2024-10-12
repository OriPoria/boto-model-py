import argparse

from boto_model_py.run import run_transformation


def main():
    parser = argparse.ArgumentParser(
        description="Generate pydantic base model from boto3 response format"
    )

    parser.add_argument("file_path", type=str, help="The path of the file definition")
    parser.add_argument(
        "output_path", type=str, help="The path location of the generated module"
    )
    parser.add_argument(
        "--with_metadata", action="store_true", help="Add response metadata to object"
    )

    args = parser.parse_args()

    file_path = args.file_path
    output_path = args.output_path
    with_metadata = args.with_metadata
    run_transformation(
        file_path=file_path, output_path=output_path, with_metadata=with_metadata
    )


if __name__ == "__main__":
    main()
