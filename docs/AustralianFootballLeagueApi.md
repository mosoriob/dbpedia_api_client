# dbpedia.AustralianFootballLeagueApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**australianfootballleagues_get**](AustralianFootballLeagueApi.md#australianfootballleagues_get) | **GET** /australianfootballleagues | List all instances of AustralianFootballLeague
[**australianfootballleagues_id_get**](AustralianFootballLeagueApi.md#australianfootballleagues_id_get) | **GET** /australianfootballleagues/{id} | Get a single AustralianFootballLeague by its id


# **australianfootballleagues_get**
> list[AustralianFootballLeague] australianfootballleagues_get(label=label, page=page, per_page=per_page)

List all instances of AustralianFootballLeague

Gets a list of all instances of AustralianFootballLeague (more information in http://dbpedia.org/ontology/AustralianFootballLeague)

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
    api_instance = dbpedia.AustralianFootballLeagueApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of AustralianFootballLeague
        api_response = api_instance.australianfootballleagues_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AustralianFootballLeagueApi->australianfootballleagues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[AustralianFootballLeague]**](AustralianFootballLeague.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of AustralianFootballLeague. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **australianfootballleagues_id_get**
> AustralianFootballLeague australianfootballleagues_id_get(id)

Get a single AustralianFootballLeague by its id

Gets the details of a given AustralianFootballLeague (more information in http://dbpedia.org/ontology/AustralianFootballLeague)

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
    api_instance = dbpedia.AustralianFootballLeagueApi(api_client)
    id = 'id_example' # str | The ID of the AustralianFootballLeague to be retrieved

    try:
        # Get a single AustralianFootballLeague by its id
        api_response = api_instance.australianfootballleagues_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AustralianFootballLeagueApi->australianfootballleagues_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the AustralianFootballLeague to be retrieved | 

### Return type

[**AustralianFootballLeague**](AustralianFootballLeague.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given AustralianFootballLeague |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

