# dbpedia.HollywoodCartoonApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hollywoodcartoons_get**](HollywoodCartoonApi.md#hollywoodcartoons_get) | **GET** /hollywoodcartoons | List all instances of HollywoodCartoon
[**hollywoodcartoons_id_get**](HollywoodCartoonApi.md#hollywoodcartoons_id_get) | **GET** /hollywoodcartoons/{id} | Get a single HollywoodCartoon by its id


# **hollywoodcartoons_get**
> list[HollywoodCartoon] hollywoodcartoons_get(label=label, page=page, per_page=per_page)

List all instances of HollywoodCartoon

Gets a list of all instances of HollywoodCartoon (more information in http://dbpedia.org/ontology/HollywoodCartoon)

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
    api_instance = dbpedia.HollywoodCartoonApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of HollywoodCartoon
        api_response = api_instance.hollywoodcartoons_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HollywoodCartoonApi->hollywoodcartoons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[HollywoodCartoon]**](HollywoodCartoon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of HollywoodCartoon. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hollywoodcartoons_id_get**
> HollywoodCartoon hollywoodcartoons_id_get(id)

Get a single HollywoodCartoon by its id

Gets the details of a given HollywoodCartoon (more information in http://dbpedia.org/ontology/HollywoodCartoon)

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
    api_instance = dbpedia.HollywoodCartoonApi(api_client)
    id = 'id_example' # str | The ID of the HollywoodCartoon to be retrieved

    try:
        # Get a single HollywoodCartoon by its id
        api_response = api_instance.hollywoodcartoons_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HollywoodCartoonApi->hollywoodcartoons_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the HollywoodCartoon to be retrieved | 

### Return type

[**HollywoodCartoon**](HollywoodCartoon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given HollywoodCartoon |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

