from mainflux import sdk

import json, requests_mock

s = sdk.SDK()


def test_version(requests_mock):
    requests_mock.get("http://localhost/version", json='{"version":"0.15.0"}')
    v = s.version()
    assert "0.15.0" == json.loads(v)["version"]
