# dbpedia.SambaSchoolApi

All URIs are relative to *https://dbpedia.mosorio.me/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sambaschools_get**](SambaSchoolApi.md#sambaschools_get) | **GET** /sambaschools | List all instances of SambaSchool
[**sambaschools_id_get**](SambaSchoolApi.md#sambaschools_id_get) | **GET** /sambaschools/{id} | Get a single SambaSchool by its id


# **sambaschools_get**
> list[SambaSchool] sambaschools_get(label=label, page=page, per_page=per_page)

List all instances of SambaSchool

Gets a list of all instances of SambaSchool (more information in http://dbpedia.org/ontology/SambaSchool)

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
    api_instance = dbpedia.SambaSchoolApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of SambaSchool
        api_response = api_instance.sambaschools_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SambaSchoolApi->sambaschools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[SambaSchool]**](SambaSchool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of SambaSchool. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sambaschools_id_get**
> SambaSchool sambaschools_id_get(id)

Get a single SambaSchool by its id

Gets the details of a given SambaSchool (more information in http://dbpedia.org/ontology/SambaSchool)

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
    api_instance = dbpedia.SambaSchoolApi(api_client)
    id = 'id_example' # str | The ID of the SambaSchool to be retrieved

    try:
        # Get a single SambaSchool by its id
        api_response = api_instance.sambaschools_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SambaSchoolApi->sambaschools_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the SambaSchool to be retrieved | 

### Return type

[**SambaSchool**](SambaSchool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given SambaSchool |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

