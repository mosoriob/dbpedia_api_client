# dbpedia.FormerMunicipalityApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formermunicipalitys_get**](FormerMunicipalityApi.md#formermunicipalitys_get) | **GET** /formermunicipalitys | List all instances of FormerMunicipality
[**formermunicipalitys_id_get**](FormerMunicipalityApi.md#formermunicipalitys_id_get) | **GET** /formermunicipalitys/{id} | Get a single FormerMunicipality by its id


# **formermunicipalitys_get**
> list[FormerMunicipality] formermunicipalitys_get(label=label, page=page, per_page=per_page)

List all instances of FormerMunicipality

Gets a list of all instances of FormerMunicipality (more information in http://dbpedia.org/ontology/FormerMunicipality)

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
    api_instance = dbpedia.FormerMunicipalityApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of FormerMunicipality
        api_response = api_instance.formermunicipalitys_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormerMunicipalityApi->formermunicipalitys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[FormerMunicipality]**](FormerMunicipality.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of FormerMunicipality. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **formermunicipalitys_id_get**
> FormerMunicipality formermunicipalitys_id_get(id)

Get a single FormerMunicipality by its id

Gets the details of a given FormerMunicipality (more information in http://dbpedia.org/ontology/FormerMunicipality)

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
    api_instance = dbpedia.FormerMunicipalityApi(api_client)
    id = 'id_example' # str | The ID of the FormerMunicipality to be retrieved

    try:
        # Get a single FormerMunicipality by its id
        api_response = api_instance.formermunicipalitys_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormerMunicipalityApi->formermunicipalitys_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormerMunicipality to be retrieved | 

### Return type

[**FormerMunicipality**](FormerMunicipality.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given FormerMunicipality |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

