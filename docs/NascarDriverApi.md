# dbpedia.NascarDriverApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nascardrivers_get**](NascarDriverApi.md#nascardrivers_get) | **GET** /nascardrivers | List all instances of NascarDriver
[**nascardrivers_id_get**](NascarDriverApi.md#nascardrivers_id_get) | **GET** /nascardrivers/{id} | Get a single NascarDriver by its id


# **nascardrivers_get**
> list[NascarDriver] nascardrivers_get(label=label, page=page, per_page=per_page)

List all instances of NascarDriver

Gets a list of all instances of NascarDriver (more information in http://dbpedia.org/ontology/NascarDriver)

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
    api_instance = dbpedia.NascarDriverApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of NascarDriver
        api_response = api_instance.nascardrivers_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NascarDriverApi->nascardrivers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[NascarDriver]**](NascarDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of NascarDriver. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nascardrivers_id_get**
> NascarDriver nascardrivers_id_get(id)

Get a single NascarDriver by its id

Gets the details of a given NascarDriver (more information in http://dbpedia.org/ontology/NascarDriver)

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
    api_instance = dbpedia.NascarDriverApi(api_client)
    id = 'id_example' # str | The ID of the NascarDriver to be retrieved

    try:
        # Get a single NascarDriver by its id
        api_response = api_instance.nascardrivers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NascarDriverApi->nascardrivers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the NascarDriver to be retrieved | 

### Return type

[**NascarDriver**](NascarDriver.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given NascarDriver |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

