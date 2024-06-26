# IvyCheck Python  SDK


## SDK Installation

```bash
pip install ivycheck
```

## SDK Example Usage

### Example

```python
import ivycheck

ivy = ivycheck.IvyCheck(
    api_key="<YOUR_TOKEN_HERE>",
)

ivy.checks.hallucination(text="It is sunny outside", context="It is rainig cats and dogs")

# {'passed': False,
#  'score': 0.0003337860107421875,
#  'message': 'Hallucination detected',
#  'findings': None,
#  'sanitized_output': None}



```

## Available Resources and Operations

### Checks

- [hallucination](https://docs.ivycheck.com/checks/hallucination) - Hallucination
- [pii](https://docs.ivycheck.com/checks/pii) - Pii
- [prompt_injection](https://docs.ivycheck.com/checks/prompt_injection) - Prompt Injection


## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:

```python
import ivycheck
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = ivycheck.IvyCheck(client: http_client)
```

<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      |
| --------- | ---- | ----------- |
| `api_key` | http | HTTP Bearer |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:

```python
import ivycheck

ivy = ivycheck.IvyCheck(
    api_key="<YOUR_BEARER_TOKEN_HERE>",
)


res = ivy.checks.hallucination(response='<value>', context='<value>', project_id='<value>')

if res.check_result is not None:
    # handle response
    pass

```
