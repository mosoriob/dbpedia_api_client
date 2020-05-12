# dbpedia.FootballMatchApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**footballmatchs_get**](FootballMatchApi.md#footballmatchs_get) | **GET** /footballmatchs | List all instances of FootballMatch
[**footballmatchs_id_get**](FootballMatchApi.md#footballmatchs_id_get) | **GET** /footballmatchs/{id} | Get a single FootballMatch by its id


# **footballmatchs_get**
> list[FootballMatch] footballmatchs_get(label=label, page=page, per_page=per_page)

List all instances of FootballMatch

Gets a list of all instances of FootballMatch (more information in http://dbpedia.org/ontology/FootballMatch)

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
    api_instance = dbpedia.FootballMatchApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of FootballMatch
        api_response = api_instance.footballmatchs_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FootballMatchApi->footballmatchs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[FootballMatch]**](FootballMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of FootballMatch. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **footballmatchs_id_get**
> FootballMatch footballmatchs_id_get(id)

Get a single FootballMatch by its id

Gets the details of a given FootballMatch (more information in http://dbpedia.org/ontology/FootballMatch)

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
    api_instance = dbpedia.FootballMatchApi(api_client)
    id = 'id_example' # str | The ID of the FootballMatch to be retrieved

    try:
        # Get a single FootballMatch by its id
        api_response = api_instance.footballmatchs_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FootballMatchApi->footballmatchs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FootballMatch to be retrieved | 

### Return type

[**FootballMatch**](FootballMatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given FootballMatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

