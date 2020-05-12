# dbpedia.MotorcycleRiderApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**motorcycleriders_get**](MotorcycleRiderApi.md#motorcycleriders_get) | **GET** /motorcycleriders | List all instances of MotorcycleRider
[**motorcycleriders_id_get**](MotorcycleRiderApi.md#motorcycleriders_id_get) | **GET** /motorcycleriders/{id} | Get a single MotorcycleRider by its id


# **motorcycleriders_get**
> list[MotorcycleRider] motorcycleriders_get(label=label, page=page, per_page=per_page)

List all instances of MotorcycleRider

Gets a list of all instances of MotorcycleRider (more information in http://dbpedia.org/ontology/MotorcycleRider)

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
    api_instance = dbpedia.MotorcycleRiderApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of MotorcycleRider
        api_response = api_instance.motorcycleriders_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MotorcycleRiderApi->motorcycleriders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[MotorcycleRider]**](MotorcycleRider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of MotorcycleRider. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **motorcycleriders_id_get**
> MotorcycleRider motorcycleriders_id_get(id)

Get a single MotorcycleRider by its id

Gets the details of a given MotorcycleRider (more information in http://dbpedia.org/ontology/MotorcycleRider)

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
    api_instance = dbpedia.MotorcycleRiderApi(api_client)
    id = 'id_example' # str | The ID of the MotorcycleRider to be retrieved

    try:
        # Get a single MotorcycleRider by its id
        api_response = api_instance.motorcycleriders_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MotorcycleRiderApi->motorcycleriders_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the MotorcycleRider to be retrieved | 

### Return type

[**MotorcycleRider**](MotorcycleRider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given MotorcycleRider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

