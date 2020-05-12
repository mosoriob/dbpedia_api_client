# dbpedia.RallyDriverApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rallydrivers_get**](RallyDriverApi.md#rallydrivers_get) | **GET** /rallydrivers | List all instances of RallyDriver
[**rallydrivers_id_get**](RallyDriverApi.md#rallydrivers_id_get) | **GET** /rallydrivers/{id} | Get a single RallyDriver by its id


# **rallydrivers_get**
> list[RallyDriver] rallydrivers_get(label=label, page=page, per_page=per_page)

List all instances of RallyDriver

Gets a list of all instances of RallyDriver (more information in http://dbpedia.org/ontology/RallyDriver)

### Example

```python
from __future__ import print_function
import time
import dbpedia
from dbpedia.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://dbpedia.mosorio.me/v0.0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = dbpedia.Configuration(
    host = "https://dbpedia.mosorio.me/v0.0.1"
)


# Enter a context with an instance of the API client
with dbpedia.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dbpedia.RallyDriverApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of RallyDriver
        api_response = api_instance.rallydrivers_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RallyDriverApi->rallydrivers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[RallyDriver]**](RallyDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of RallyDriver. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rallydrivers_id_get**
> RallyDriver rallydrivers_id_get(id)

Get a single RallyDriver by its id

Gets the details of a given RallyDriver (more information in http://dbpedia.org/ontology/RallyDriver)

### Example

```python
from __future__ import print_function
import time
import dbpedia
from dbpedia.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://dbpedia.mosorio.me/v0.0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = dbpedia.Configuration(
    host = "https://dbpedia.mosorio.me/v0.0.1"
)


# Enter a context with an instance of the API client
with dbpedia.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = dbpedia.RallyDriverApi(api_client)
    id = 'id_example' # str | The ID of the RallyDriver to be retrieved

    try:
        # Get a single RallyDriver by its id
        api_response = api_instance.rallydrivers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RallyDriverApi->rallydrivers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the RallyDriver to be retrieved | 

### Return type

[**RallyDriver**](RallyDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given RallyDriver |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

