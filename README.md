# IvyCheck-SDK

<!-- Start SDK Installation [installation] -->

## SDK Installation

```bash
pip install ivycheck
```

<!-- End SDK Installation [installation] -->

## SDK Example Usage

### Example

```python
import ivycheck

ivy = ivycheck.IvyCheck(
    api_key="<YOUR_TOKEN_HERE>",
)

res = ivy.checks.hallucination(text="It is sunny outside", context="It is rainig cats and dogs")
# CheckResult(passed=False, score=0.9992709300131537, message='Hallucination detected')

```

## Available Resources and Operations

### [checks](docs/sdks/checks/README.md)

- [hallucination](https://docs.ivycheck.com/checks/hallucination) - Hallucination
- [pii](https://docs.ivycheck.com/checks/pii) - Pii
- [prompt_injection](https://docs.ivycheck.com/checks/prompt_injection) - Prompt Injection
<!-- End Available Resources and Operations [operations] -->

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

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.
