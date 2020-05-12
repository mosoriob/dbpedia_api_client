# dbpedia.VicePrimeMinisterApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viceprimeministers_get**](VicePrimeMinisterApi.md#viceprimeministers_get) | **GET** /viceprimeministers | List all instances of VicePrimeMinister
[**viceprimeministers_id_get**](VicePrimeMinisterApi.md#viceprimeministers_id_get) | **GET** /viceprimeministers/{id} | Get a single VicePrimeMinister by its id


# **viceprimeministers_get**
> list[VicePrimeMinister] viceprimeministers_get(label=label, page=page, per_page=per_page)

List all instances of VicePrimeMinister

Gets a list of all instances of VicePrimeMinister (more information in http://dbpedia.org/ontology/VicePrimeMinister)

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
    api_instance = dbpedia.VicePrimeMinisterApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of VicePrimeMinister
        api_response = api_instance.viceprimeministers_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VicePrimeMinisterApi->viceprimeministers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[VicePrimeMinister]**](VicePrimeMinister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of VicePrimeMinister. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **viceprimeministers_id_get**
> VicePrimeMinister viceprimeministers_id_get(id)

Get a single VicePrimeMinister by its id

Gets the details of a given VicePrimeMinister (more information in http://dbpedia.org/ontology/VicePrimeMinister)

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
    api_instance = dbpedia.VicePrimeMinisterApi(api_client)
    id = 'id_example' # str | The ID of the VicePrimeMinister to be retrieved

    try:
        # Get a single VicePrimeMinister by its id
        api_response = api_instance.viceprimeministers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VicePrimeMinisterApi->viceprimeministers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the VicePrimeMinister to be retrieved | 

### Return type

[**VicePrimeMinister**](VicePrimeMinister.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given VicePrimeMinister |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

