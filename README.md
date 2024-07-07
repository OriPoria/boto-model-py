# Boto Model Python
Library with single command purposed to transform boto3 response format from boto3 website into a pydantic base model
complete class hierarchy.
## Setups
### Prerequisites
- python3.12 or above
### Installation of venv
```shell
cd boto-model-py
python3.12 -m venv venv
source ./venv/bin/activate
```
### Install requirements.txt
```shell
pip install -r requirements.txt
```
## How to use
The main transformation script relies on responses syntax from boto3 documentation website.
- Link: [boto3 API services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)
1. Choose from boto3 website the API you want to use and copy its `response syntax` dictionary syntax
2. Create under `inputs` folder new file named with the name of the API request
```shell
touch inputs/api_request_name
```
3. Run the transformation script with the path to the new input file as the single argument
```shell
python main.py inputs/api_request_name
```
4. New python module is created under `dist` folder with the following naming:
`<api request name>_response.py`
5. Copy the response python module into your project and load the dictionary response into the base class from the 
new response module. The base class of the new response module is the last class, following the naming:
`ApiRequestNameResponse`.
```python
import ApiRequestNameResponse

response = boto3_client.get_api_name()
response_object = ApiRequestNameResponse(**response)
```
With the above syntax you have the full intellisense and type hint of the response instead python dictionary syntax
### Flags
- --with_metadata - By default, loading the response dictionary into the boto-model-py object does not include the 
`response_metadata` attribute. With using this flag on running the transformation script, this attribute is included
on loading the response into the boto-model-py object.