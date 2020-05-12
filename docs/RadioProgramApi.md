# dbpedia.RadioProgramApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**radioprograms_get**](RadioProgramApi.md#radioprograms_get) | **GET** /radioprograms | List all instances of RadioProgram
[**radioprograms_id_get**](RadioProgramApi.md#radioprograms_id_get) | **GET** /radioprograms/{id} | Get a single RadioProgram by its id


# **radioprograms_get**
> list[RadioProgram] radioprograms_get(label=label, page=page, per_page=per_page)

List all instances of RadioProgram

Gets a list of all instances of RadioProgram (more information in http://dbpedia.org/ontology/RadioProgram)

### Example

```python
from __future__ import print_function
import time
import dbpedia
from dbpedia.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://dbpedia.mosorio.dev/v0.0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = dbpedia.Configuration(
    host = "https://dbpedia.mosorio.dev/v0.0.1"
)


# Enter a context with an instance of the API client
with dbpedia.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dbpedia.RadioProgramApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of RadioProgram
        api_response = api_instance.radioprograms_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadioProgramApi->radioprograms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[RadioProgram]**](RadioProgram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of RadioProgram. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radioprograms_id_get**
> RadioProgram radioprograms_id_get(id)

Get a single RadioProgram by its id

Gets the details of a given RadioProgram (more information in http://dbpedia.org/ontology/RadioProgram)

### Example

```python
from __future__ import print_function
import time
import dbpedia
from dbpedia.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://dbpedia.mosorio.dev/v0.0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = dbpedia.Configuration(
    host = "https://dbpedia.mosorio.dev/v0.0.1"
)


# Enter a context with an instance of the API client
with dbpedia.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dbpedia.RadioProgramApi(api_client)
    id = 'id_example' # str | The ID of the RadioProgram to be retrieved

    try:
        # Get a single RadioProgram by its id
        api_response = api_instance.radioprograms_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RadioProgramApi->radioprograms_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the RadioProgram to be retrieved | 

### Return type

[**RadioProgram**](RadioProgram.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given RadioProgram |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

