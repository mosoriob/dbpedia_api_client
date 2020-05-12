# dbpedia.AnatomicalStructureApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anatomicalstructures_get**](AnatomicalStructureApi.md#anatomicalstructures_get) | **GET** /anatomicalstructures | List all instances of AnatomicalStructure
[**anatomicalstructures_id_get**](AnatomicalStructureApi.md#anatomicalstructures_id_get) | **GET** /anatomicalstructures/{id} | Get a single AnatomicalStructure by its id


# **anatomicalstructures_get**
> list[AnatomicalStructure] anatomicalstructures_get(label=label, page=page, per_page=per_page)

List all instances of AnatomicalStructure

Gets a list of all instances of AnatomicalStructure (more information in http://dbpedia.org/ontology/AnatomicalStructure)

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
    api_instance = dbpedia.AnatomicalStructureApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of AnatomicalStructure
        api_response = api_instance.anatomicalstructures_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnatomicalStructureApi->anatomicalstructures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[AnatomicalStructure]**](AnatomicalStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of AnatomicalStructure. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anatomicalstructures_id_get**
> AnatomicalStructure anatomicalstructures_id_get(id)

Get a single AnatomicalStructure by its id

Gets the details of a given AnatomicalStructure (more information in http://dbpedia.org/ontology/AnatomicalStructure)

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
    api_instance = dbpedia.AnatomicalStructureApi(api_client)
    id = 'id_example' # str | The ID of the AnatomicalStructure to be retrieved

    try:
        # Get a single AnatomicalStructure by its id
        api_response = api_instance.anatomicalstructures_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnatomicalStructureApi->anatomicalstructures_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the AnatomicalStructure to be retrieved | 

### Return type

[**AnatomicalStructure**](AnatomicalStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given AnatomicalStructure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

