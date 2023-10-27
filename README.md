## Python SDK

[![Testing](https://github.com/mainflux/sdk-py/actions/workflows/python-testing.yml/badge.svg?branch=main)](https://github.com/mainflux/sdk-py/actions/workflows/python-testing.yml)
[![Check SDK documentation](https://github.com/mainflux/sdk-py/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/mainflux/sdk-py/actions/workflows/docs.yml)

This is the Mainflux Python SDK, a python driver for [Mainflux HTTP API](https://docs.mainflux.io/api/) API reference in the Swagger UI can be found [here](https://api.mainflux.io/).

Does both system administration (provisioning) and messaging.

## Installation

To install mainflux SDK to your system you will need to have pip installed.

1. To install in a virtual environment

```sh
virtualenv mainfluxVenv --python=python3.8
source mainfluxVenv/bin/activate
pip install mainflux
```

2. To install system wide

```sh
pip install mainflux
```

## Usage

You can interact with the mainflux API by calling the various Python SDK functions.

First you need to start mainflux in your system by following the guide [here](https://github.com/mainflux/mainflux#usage)

```python
from mainflux import SDK

default_url = "http://localhost"

sdk = SDK()

# Example to create an account
mf_resp = sdk.users.create({"email": "<user_email>", "password": "<user_password>"})
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)
```

## Documentation

Official documentation for the SDK is hosted at [here](https://github.com/mainflux/sdk-py/tree/main/docs/README.md). Documentation is auto-generated, the instructions to generate one are:

```sh
pip install lazydocs requests
python3 setup.py install
lazydocs --src-base-url="https://github.com/mainflux/sdk-py/blob/main/" --overview-file="README.md" mainflux
```

Please note that lazydocs requires Python version 3.5 or higher.

If you spot an error or a need for corrections, please let us know - or even better: send us a PR.

## Professional Support

There are many companies offering professional support for the Mainflux system.

If you need this kind of support, best is to reach out to [@drasko](https://github.com/drasko) directly, and he will point you out to the best-matching support team.

## Contributing

Thank you for your interest in Mainflux and the desire to contribute!

1. Take a look at our [open issues](https://github.com/mainflux/sdk-py/issues). The [good-first-issue](https://github.com/mainflux/sdk-py/labels/good-first-issue) label is specifically for issues that are great for getting started.
2. Checkout the [contribution guide](CONTRIBUTING.md) to learn more about our style and conventions.
3. Make your changes compatible to our workflow.

## Community

- [Google group](https://groups.google.com/forum/#!forum/mainflux)
- [Gitter](https://gitter.im/mainflux/mainflux?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
- [Twitter](https://twitter.com/mainflux)

## License

[Apache-2.0](LICENSE)
