# dbpedia.BullfighterApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bullfighters_get**](BullfighterApi.md#bullfighters_get) | **GET** /bullfighters | List all instances of Bullfighter
[**bullfighters_id_get**](BullfighterApi.md#bullfighters_id_get) | **GET** /bullfighters/{id} | Get a single Bullfighter by its id


# **bullfighters_get**
> list[Bullfighter] bullfighters_get(label=label, page=page, per_page=per_page)

List all instances of Bullfighter

Gets a list of all instances of Bullfighter (more information in http://dbpedia.org/ontology/Bullfighter)

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
    api_instance = dbpedia.BullfighterApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of Bullfighter
        api_response = api_instance.bullfighters_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BullfighterApi->bullfighters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Bullfighter]**](Bullfighter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Bullfighter. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bullfighters_id_get**
> Bullfighter bullfighters_id_get(id)

Get a single Bullfighter by its id

Gets the details of a given Bullfighter (more information in http://dbpedia.org/ontology/Bullfighter)

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
    api_instance = dbpedia.BullfighterApi(api_client)
    id = 'id_example' # str | The ID of the Bullfighter to be retrieved

    try:
        # Get a single Bullfighter by its id
        api_response = api_instance.bullfighters_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BullfighterApi->bullfighters_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Bullfighter to be retrieved | 

### Return type

[**Bullfighter**](Bullfighter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Bullfighter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

