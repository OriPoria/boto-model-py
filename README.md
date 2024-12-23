# Boto Model Python
A code generation library that converts AWS boto3 responses into a Python module with fully hierarchical data classes 
representing the response structure.

The package provides a single gateway function. This function takes the path to a boto3 response JSON syntax and a 
desired output path, generating Python data classes and enums based on the response structure.

This utility is designed for Python-boto3 developers who want quick access to boto3 response attributes and the full 
benefits of Pydantic BaseModel and Python enums, without dealing with the complexity of deep dictionary hierarchies.
## How to use
### Clarification
`boto3` package is expected to be installed in the target environment where generated code is created. There is no 
installation of boto3 package during installation of `boto-model-py` package.
### Pre-steps
1. To install this package, you can use `pip`, the Python package installer. Run the following command in your terminal:
```shell
pip install boto-model-py
```
### Usage
The main transformation script relies on responses syntax from boto3 documentation website.
- Link: [boto3 API services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
1. Choose from boto3 website the API you want to use and copy its `response syntax` dictionary syntax into local path
2. Run cli command to transform local copy of the `response syntax` from boto3 into base model classes using `bmpy` command
The command has 2 main parameters:
   1. file_path: path to local `response syntax` file
   2. output_path: path to folder where output module is created - the response module location
   3. with_metadata: flag to indicate whether to include the response metadata in the base class or not 
```shell
bmpy <file_path> <output_path>
```
#### Example
1. Writing the following code section to get list of all buckets in my account:

```python
import boto3
service = "s3"
client = boto3.client(service, region_name="us-east-2")
buckets = client.list_buckets()
```
2. Go to the boto3 `list_buckets` API request docs: [bot3 API list_buckets](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/list_buckets.html)
3. Copy response syntax into a local file called `input`
```shell
touch list_buckets_input
```
intput file:
```text
{
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    }
}
```
4. Running `bmpy` command and generate response module in the desired location (suppose I have `response` folder in my project)
```shell
bmpy list_buckets_input response
```
5. The response module is under generated under the `output_path` folder, with the with a class called `ListBucketsResponse`. 
You can import it in the project, and load the response into the base class. Then using all pydantic base class feature is easy.

[Expected output from GitHubRepo](tests/unit_tests/files/expected_list_buckets_response.py) 
```python
import boto3

from response.list_buckets_response import ListBucketsResponse

service = "s3"
client = boto3.client(service, region_name="us-east-2")
buckets = client.list_buckets()

buckets_object = ListBucketsResponse(**buckets)
for bucket in buckets_object.Buckets:
    print(bucket.Name)
    print(bucket.CreationDate)

print(buckets_object.model_dump_json(indent=3))
```
### Flags
- --with_metadata - By default, loading the response dictionary into the boto-model-py object does not include the 
`response_metadata` attribute. With using this flag on running the transformation script, this attribute is included
on loading the response into the boto-model-py object.
## Response folder
Under `response` folder you can see a batch of responses output from several example from boto3 responses tests. You can
take your desired module class into your repo or generate the response class by using the boto-model-py package.
## Developer setups
In order to contribute to the repository
### Prerequisites
- python3.9 or above
### Git clone
```shell
git clone https://github.com/OriPoria/boto-model-py.git
```
### Installation of venv
```shell
cd boto-model-py
python3.9 -m venv venv
source ./venv/bin/activate
```
### Install requirements.txt
```shell
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.