# dbpedia.MotorcycleApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**motorcycles_get**](MotorcycleApi.md#motorcycles_get) | **GET** /motorcycles | List all instances of Motorcycle
[**motorcycles_id_get**](MotorcycleApi.md#motorcycles_id_get) | **GET** /motorcycles/{id} | Get a single Motorcycle by its id


# **motorcycles_get**
> list[Motorcycle] motorcycles_get(label=label, page=page, per_page=per_page)

List all instances of Motorcycle

Gets a list of all instances of Motorcycle (more information in http://dbpedia.org/ontology/Motorcycle)

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
    api_instance = dbpedia.MotorcycleApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of Motorcycle
        api_response = api_instance.motorcycles_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MotorcycleApi->motorcycles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Motorcycle]**](Motorcycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Motorcycle. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motorcycles_id_get**
> Motorcycle motorcycles_id_get(id)

Get a single Motorcycle by its id

Gets the details of a given Motorcycle (more information in http://dbpedia.org/ontology/Motorcycle)

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
    api_instance = dbpedia.MotorcycleApi(api_client)
    id = 'id_example' # str | The ID of the Motorcycle to be retrieved

    try:
        # Get a single Motorcycle by its id
        api_response = api_instance.motorcycles_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MotorcycleApi->motorcycles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Motorcycle to be retrieved | 

### Return type

[**Motorcycle**](Motorcycle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Motorcycle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

