# dbpedia.ClericalAdministrativeRegionApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clericaladministrativeregions_get**](ClericalAdministrativeRegionApi.md#clericaladministrativeregions_get) | **GET** /clericaladministrativeregions | List all instances of ClericalAdministrativeRegion
[**clericaladministrativeregions_id_get**](ClericalAdministrativeRegionApi.md#clericaladministrativeregions_id_get) | **GET** /clericaladministrativeregions/{id} | Get a single ClericalAdministrativeRegion by its id


# **clericaladministrativeregions_get**
> list[ClericalAdministrativeRegion] clericaladministrativeregions_get(label=label, page=page, per_page=per_page)

List all instances of ClericalAdministrativeRegion

Gets a list of all instances of ClericalAdministrativeRegion (more information in http://dbpedia.org/ontology/ClericalAdministrativeRegion)

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
    api_instance = dbpedia.ClericalAdministrativeRegionApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of ClericalAdministrativeRegion
        api_response = api_instance.clericaladministrativeregions_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClericalAdministrativeRegionApi->clericaladministrativeregions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[ClericalAdministrativeRegion]**](ClericalAdministrativeRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of ClericalAdministrativeRegion. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clericaladministrativeregions_id_get**
> ClericalAdministrativeRegion clericaladministrativeregions_id_get(id)

Get a single ClericalAdministrativeRegion by its id

Gets the details of a given ClericalAdministrativeRegion (more information in http://dbpedia.org/ontology/ClericalAdministrativeRegion)

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
    api_instance = dbpedia.ClericalAdministrativeRegionApi(api_client)
    id = 'id_example' # str | The ID of the ClericalAdministrativeRegion to be retrieved

    try:
        # Get a single ClericalAdministrativeRegion by its id
        api_response = api_instance.clericaladministrativeregions_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClericalAdministrativeRegionApi->clericaladministrativeregions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the ClericalAdministrativeRegion to be retrieved | 

### Return type

[**ClericalAdministrativeRegion**](ClericalAdministrativeRegion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given ClericalAdministrativeRegion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

