# dbpedia.GolfPlayerApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**golfplayers_get**](GolfPlayerApi.md#golfplayers_get) | **GET** /golfplayers | List all instances of GolfPlayer
[**golfplayers_id_get**](GolfPlayerApi.md#golfplayers_id_get) | **GET** /golfplayers/{id} | Get a single GolfPlayer by its id


# **golfplayers_get**
> list[GolfPlayer] golfplayers_get(label=label, page=page, per_page=per_page)

List all instances of GolfPlayer

Gets a list of all instances of GolfPlayer (more information in http://dbpedia.org/ontology/GolfPlayer)

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
    api_instance = dbpedia.GolfPlayerApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of GolfPlayer
        api_response = api_instance.golfplayers_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GolfPlayerApi->golfplayers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[GolfPlayer]**](GolfPlayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of GolfPlayer. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **golfplayers_id_get**
> GolfPlayer golfplayers_id_get(id)

Get a single GolfPlayer by its id

Gets the details of a given GolfPlayer (more information in http://dbpedia.org/ontology/GolfPlayer)

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
    api_instance = dbpedia.GolfPlayerApi(api_client)
    id = 'id_example' # str | The ID of the GolfPlayer to be retrieved

    try:
        # Get a single GolfPlayer by its id
        api_response = api_instance.golfplayers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GolfPlayerApi->golfplayers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the GolfPlayer to be retrieved | 

### Return type

[**GolfPlayer**](GolfPlayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given GolfPlayer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

