# dbpedia.AgglomerationApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agglomerations_get**](AgglomerationApi.md#agglomerations_get) | **GET** /agglomerations | List all instances of Agglomeration
[**agglomerations_id_get**](AgglomerationApi.md#agglomerations_id_get) | **GET** /agglomerations/{id} | Get a single Agglomeration by its id


# **agglomerations_get**
> list[Agglomeration] agglomerations_get(label=label, page=page, per_page=per_page)

List all instances of Agglomeration

Gets a list of all instances of Agglomeration (more information in http://dbpedia.org/ontology/Agglomeration)

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
    api_instance = dbpedia.AgglomerationApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of Agglomeration
        api_response = api_instance.agglomerations_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgglomerationApi->agglomerations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[Agglomeration]**](Agglomeration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of Agglomeration. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agglomerations_id_get**
> Agglomeration agglomerations_id_get(id)

Get a single Agglomeration by its id

Gets the details of a given Agglomeration (more information in http://dbpedia.org/ontology/Agglomeration)

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
    api_instance = dbpedia.AgglomerationApi(api_client)
    id = 'id_example' # str | The ID of the Agglomeration to be retrieved

    try:
        # Get a single Agglomeration by its id
        api_response = api_instance.agglomerations_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgglomerationApi->agglomerations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Agglomeration to be retrieved | 

### Return type

[**Agglomeration**](Agglomeration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given Agglomeration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

