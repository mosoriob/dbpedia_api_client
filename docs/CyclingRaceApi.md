# dbpedia.CyclingRaceApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cyclingraces_get**](CyclingRaceApi.md#cyclingraces_get) | **GET** /cyclingraces | List all instances of CyclingRace
[**cyclingraces_id_get**](CyclingRaceApi.md#cyclingraces_id_get) | **GET** /cyclingraces/{id} | Get a single CyclingRace by its id


# **cyclingraces_get**
> list[CyclingRace] cyclingraces_get(label=label, page=page, per_page=per_page)

List all instances of CyclingRace

Gets a list of all instances of CyclingRace (more information in http://dbpedia.org/ontology/CyclingRace)

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
    api_instance = dbpedia.CyclingRaceApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of CyclingRace
        api_response = api_instance.cyclingraces_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CyclingRaceApi->cyclingraces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[CyclingRace]**](CyclingRace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of CyclingRace. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cyclingraces_id_get**
> CyclingRace cyclingraces_id_get(id)

Get a single CyclingRace by its id

Gets the details of a given CyclingRace (more information in http://dbpedia.org/ontology/CyclingRace)

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
    api_instance = dbpedia.CyclingRaceApi(api_client)
    id = 'id_example' # str | The ID of the CyclingRace to be retrieved

    try:
        # Get a single CyclingRace by its id
        api_response = api_instance.cyclingraces_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CyclingRaceApi->cyclingraces_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the CyclingRace to be retrieved | 

### Return type

[**CyclingRace**](CyclingRace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given CyclingRace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

