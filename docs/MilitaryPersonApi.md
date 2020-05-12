# dbpedia.MilitaryPersonApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**militarypersons_get**](MilitaryPersonApi.md#militarypersons_get) | **GET** /militarypersons | List all instances of MilitaryPerson
[**militarypersons_id_get**](MilitaryPersonApi.md#militarypersons_id_get) | **GET** /militarypersons/{id} | Get a single MilitaryPerson by its id


# **militarypersons_get**
> list[MilitaryPerson] militarypersons_get(label=label, page=page, per_page=per_page)

List all instances of MilitaryPerson

Gets a list of all instances of MilitaryPerson (more information in http://dbpedia.org/ontology/MilitaryPerson)

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
    api_instance = dbpedia.MilitaryPersonApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of MilitaryPerson
        api_response = api_instance.militarypersons_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MilitaryPersonApi->militarypersons_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[MilitaryPerson]**](MilitaryPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of MilitaryPerson. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **militarypersons_id_get**
> MilitaryPerson militarypersons_id_get(id)

Get a single MilitaryPerson by its id

Gets the details of a given MilitaryPerson (more information in http://dbpedia.org/ontology/MilitaryPerson)

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
    api_instance = dbpedia.MilitaryPersonApi(api_client)
    id = 'id_example' # str | The ID of the MilitaryPerson to be retrieved

    try:
        # Get a single MilitaryPerson by its id
        api_response = api_instance.militarypersons_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MilitaryPersonApi->militarypersons_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the MilitaryPerson to be retrieved | 

### Return type

[**MilitaryPerson**](MilitaryPerson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given MilitaryPerson |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

