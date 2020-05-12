# dbpedia.BoxingStyleApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boxingstyles_get**](BoxingStyleApi.md#boxingstyles_get) | **GET** /boxingstyles | List all instances of BoxingStyle
[**boxingstyles_id_get**](BoxingStyleApi.md#boxingstyles_id_get) | **GET** /boxingstyles/{id} | Get a single BoxingStyle by its id


# **boxingstyles_get**
> list[BoxingStyle] boxingstyles_get(label=label, page=page, per_page=per_page)

List all instances of BoxingStyle

Gets a list of all instances of BoxingStyle (more information in http://dbpedia.org/ontology/BoxingStyle)

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
    api_instance = dbpedia.BoxingStyleApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of BoxingStyle
        api_response = api_instance.boxingstyles_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoxingStyleApi->boxingstyles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[BoxingStyle]**](BoxingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of BoxingStyle. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boxingstyles_id_get**
> BoxingStyle boxingstyles_id_get(id)

Get a single BoxingStyle by its id

Gets the details of a given BoxingStyle (more information in http://dbpedia.org/ontology/BoxingStyle)

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
    api_instance = dbpedia.BoxingStyleApi(api_client)
    id = 'id_example' # str | The ID of the BoxingStyle to be retrieved

    try:
        # Get a single BoxingStyle by its id
        api_response = api_instance.boxingstyles_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BoxingStyleApi->boxingstyles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the BoxingStyle to be retrieved | 

### Return type

[**BoxingStyle**](BoxingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given BoxingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

