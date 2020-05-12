# dbpedia.BaseballTeamApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**baseballteams_get**](BaseballTeamApi.md#baseballteams_get) | **GET** /baseballteams | List all instances of BaseballTeam
[**baseballteams_id_get**](BaseballTeamApi.md#baseballteams_id_get) | **GET** /baseballteams/{id} | Get a single BaseballTeam by its id


# **baseballteams_get**
> list[BaseballTeam] baseballteams_get(label=label, page=page, per_page=per_page)

List all instances of BaseballTeam

Gets a list of all instances of BaseballTeam (more information in http://dbpedia.org/ontology/BaseballTeam)

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
    api_instance = dbpedia.BaseballTeamApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of BaseballTeam
        api_response = api_instance.baseballteams_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BaseballTeamApi->baseballteams_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[BaseballTeam]**](BaseballTeam.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of BaseballTeam. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **baseballteams_id_get**
> BaseballTeam baseballteams_id_get(id)

Get a single BaseballTeam by its id

Gets the details of a given BaseballTeam (more information in http://dbpedia.org/ontology/BaseballTeam)

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
    api_instance = dbpedia.BaseballTeamApi(api_client)
    id = 'id_example' # str | The ID of the BaseballTeam to be retrieved

    try:
        # Get a single BaseballTeam by its id
        api_response = api_instance.baseballteams_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BaseballTeamApi->baseballteams_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the BaseballTeam to be retrieved | 

### Return type

[**BaseballTeam**](BaseballTeam.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given BaseballTeam |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

