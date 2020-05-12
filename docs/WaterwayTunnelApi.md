# dbpedia.WaterwayTunnelApi

All URIs are relative to *https://dbpedia.mosorio.dev/v0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waterwaytunnels_get**](WaterwayTunnelApi.md#waterwaytunnels_get) | **GET** /waterwaytunnels | List all instances of WaterwayTunnel
[**waterwaytunnels_id_get**](WaterwayTunnelApi.md#waterwaytunnels_id_get) | **GET** /waterwaytunnels/{id} | Get a single WaterwayTunnel by its id


# **waterwaytunnels_get**
> list[WaterwayTunnel] waterwaytunnels_get(label=label, page=page, per_page=per_page)

List all instances of WaterwayTunnel

Gets a list of all instances of WaterwayTunnel (more information in http://dbpedia.org/ontology/WaterwayTunnel)

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
    api_instance = dbpedia.WaterwayTunnelApi(api_client)
    label = 'label_example' # str | Filter by label (optional)
page = 1 # int | Page number (optional) (default to 1)
per_page = 100 # int | Items per page (optional) (default to 100)

    try:
        # List all instances of WaterwayTunnel
        api_response = api_instance.waterwaytunnels_get(label=label, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaterwayTunnelApi->waterwaytunnels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label** | **str**| Filter by label | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **per_page** | **int**| Items per page | [optional] [default to 100]

### Return type

[**list[WaterwayTunnel]**](WaterwayTunnel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array with the instances of WaterwayTunnel. |  * link - Information about pagination <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **waterwaytunnels_id_get**
> WaterwayTunnel waterwaytunnels_id_get(id)

Get a single WaterwayTunnel by its id

Gets the details of a given WaterwayTunnel (more information in http://dbpedia.org/ontology/WaterwayTunnel)

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
    api_instance = dbpedia.WaterwayTunnelApi(api_client)
    id = 'id_example' # str | The ID of the WaterwayTunnel to be retrieved

    try:
        # Get a single WaterwayTunnel by its id
        api_response = api_instance.waterwaytunnels_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WaterwayTunnelApi->waterwaytunnels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the WaterwayTunnel to be retrieved | 

### Return type

[**WaterwayTunnel**](WaterwayTunnel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the details of a given WaterwayTunnel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

