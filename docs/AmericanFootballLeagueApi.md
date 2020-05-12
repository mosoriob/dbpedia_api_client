# dbpedia.AmericanFootballLeagueApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**americanfootballleagues_get**](AmericanFootballLeagueApi.md#americanfootballleagues_get) | **GET** /americanfootballleagues | List all instances of AmericanFootballLeague
[**americanfootballleagues_id_get**](AmericanFootballLeagueApi.md#americanfootballleagues_id_get) | **GET** /americanfootballleagues/{id} | Get a single AmericanFootballLeague by its id


# **americanfootballleagues_get**
> list[AmericanFootballLeague] americanfootballleagues_get(label=label, page=page, per_page=per_page)

List all instances of AmericanFootballLeague

Gets a list of all instances of AmericanFootballLeague (more information in http://dbpedia.org/ontology/AmericanFootballLeague)

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
    api_instance = dbpedia.AmericanFootballLeagueApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of AmericanFootballLeague
        api_response = api_instance.americanfootballleagues_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmericanFootballLeagueApi->americanfootballleagues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[AmericanFootballLeague]**](AmericanFootballLeague.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of AmericanFootballLeague. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **americanfootballleagues_id_get**
> AmericanFootballLeague americanfootballleagues_id_get(id)

Get a single AmericanFootballLeague by its id

Gets the details of a given AmericanFootballLeague (more information in http://dbpedia.org/ontology/AmericanFootballLeague)

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
    api_instance = dbpedia.AmericanFootballLeagueApi(api_client)
    id = 'id_example' # str | The ID of the AmericanFootballLeague to be retrieved

    try:
        # Get a single AmericanFootballLeague by its id
        api_response = api_instance.americanfootballleagues_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AmericanFootballLeagueApi->americanfootballleagues_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the AmericanFootballLeague to be retrieved | 

### Return type

[**AmericanFootballLeague**](AmericanFootballLeague.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given AmericanFootballLeague |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

