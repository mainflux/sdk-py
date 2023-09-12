from mainflux import sdk

import json
import requests_mock

s= sdk.SDK()

certs= {
  "cert_serial": "22:16:df:60:c2:99:bc:c4:9b:1d:fd:71:5e:e9:07:d9:1b:3c:85:1d",
  "client_cert": "-----BEGIN CERTIFICATE-----\nMIIEATCCAumgAwIBAgIUIhbfYMKZvMSbHf1xXukH2Rs8hR0wDQYJKoZIhvcNAQEL\nBQAwLjEsMCoGA1UEAxMjbWFpbmZsdXguY29tIEludGVybWVkaWF0ZSBBdXRob3Jp\ndHkwHhcNMjMwODIxMTAwMjE5WhcNMjMwOTIwMTAwMjQ4WjAvMS0wKwYDVQQDEyRj\nODkyMzViNy0xZDU0LTQyY2YtODdlYi0yNDgzMWY3NDE0ZTEwggEiMA0GCSqGSIb3\nDQEBAQUAA4IBDwAwggEKAoIBAQDL2AXzhrmzqOVfqGQA9evsqM0n5BjL3F3FCo2q\n1vMVq8HrCmJ1qXk1h6coz5KILiloLET5PFALFqwHByBzNAg0IZUbTTTh8YuUtiq+\nbnRa2MOZZzQtXB1T6tPkAtcxdJ+H3j0eEIAbYh4DJiq8l1NmU0siCaFLHJ+pwJr5\ndGwGgWOW3sotrUvN9vVsXM41SgxJOeps765/lKQjSxTdhEERLsu6pQ+68K1WNYKg\npCO9kB2Dmu3jtoV34kMyhg1ptaegztEFrSgA8bSIsR4X19itIR5ku4jZb6pnmPcM\nBwHJlJXTl9zdzSC4MXOdb8aOXEROTsVuFGn5fnZ9OWDWXeEhAgMBAAGjggEUMIIB\nEDAOBgNVHQ8BAf8EBAMCA6gwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMC\nMB0GA1UdDgQWBBSmppsLhLCf6N44sY6Np7/k+z//tzAfBgNVHSMEGDAWgBRXKFnr\nLL2mS5RUzzlVZHJup20WfTA7BggrBgEFBQcBAQQvMC0wKwYIKwYBBQUHMAKGH2h0\ndHA6Ly92YXVsdDo4MjAwL3YxL3BraV9pbnQvY2EwLwYDVR0RBCgwJoIkYzg5MjM1\nYjctMWQ1NC00MmNmLTg3ZWItMjQ4MzFmNzQxNGUxMDEGA1UdHwQqMCgwJqAkoCKG\nIGh0dHA6Ly92YXVsdDo4MjAwL3YxL3BraV9pbnQvY3JsMA0GCSqGSIb3DQEBCwUA\nA4IBAQCZla9Opcq6RQqnCoih9VCg3JbU0PmpfeM+2LtWziH51PyeIOxB5b244SPe\nUtLzSv4lAB6tsq4aYx67n7suiv1E50E9xOXtVq1s/yO/bhvR2NIQL3bFc61ZGW3C\nVetPdSfESwXqi5jdWcacs+F66ZFEza3fFYLgl7D8Bdd3i9hKlgK7pWDrhcDpgwMA\nabIRbQ4nuCyf8OVeklCUfbilRrvESrWIy9r0PjViZbJDFIFEs9uEvBUFcDokzJqY\nzVH1+pduYw7x5JzJy/cK8TGX3JdKK7Y058jnSrO3ZkW4uKQ3bCWD5kB0wNanrp+a\nfD1NTEQ0etWwdlylVx4JjtwA4T1k\n-----END CERTIFICATE-----",
  "client_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEoQIBAAKCAQEAy9gF84a5s6jlX6hkAPXr7KjNJ+QYy9xdxQqNqtbzFavB6wpi\ndal5NYenKM+SiC4paCxE+TxQCxasBwcgczQINCGVG0004fGLlLYqvm50WtjDmWc0\nLVwdU+rT5ALXMXSfh949HhCAG2IeAyYqvJdTZlNLIgmhSxyfqcCa+XRsBoFjlt7K\nLa1Lzfb1bFzONUoMSTnqbO+uf5SkI0sU3YRBES7LuqUPuvCtVjWCoKQjvZAdg5rt\n47aFd+JDMoYNabWnoM7RBa0oAPG0iLEeF9fYrSEeZLuI2W+qZ5j3DAcByZSV05fc\n3c0guDFznW/GjlxETk7FbhRp+X52fTlg1l3hIQIDAQABAoIBACOiqz+sgNBgqWC0\nrm7gjxL7W4oqvQ7+gkING0EPfMWAFlGBqj7Jls/93AItb39xGnoEqzYrDg8yMna0\nDz80jG6YpFl2gNUzBeTEh+psotiy5lbuDNgVL2dZORu2R2p06eK1vleAKPUgjQCd\n7oCzr7fGve7AYjsgUOU7L5yGdtAYBLL4nu6XfMC9kWxHKwVMhWSRSZO4gr83Yhld\nsHrlLlSMYciuXWSZSMGvFTQc3jj8tyq9TqMTysqgbM++6E4KyzATwW2DsoiiMAPl\n/2wyG1GxsNHreeSxxAFQw4NhxY5ud34jYi6NNpR2u2kaa17eFD/YVyMTn+9gyugc\nuFt0tjECgYEA5CYve2BhowU6kSUx0055Kf1mD24MpGo29tKzR98m9Rc045iUMwdc\n51skrTjdVcskDYDVZ1cklO1dCerQBLJ3zc6iqyVdoABj0pMlfWvRyYj+8oRa1AgJ\n1K0FMkcT9UJ3jTxidoF3/8/sRZEvpuxIb6wSfNEoJVIxqFsz71khWrUCgYEA5LpH\nuKSHqzE2E2UHd9dXbTWf1ZxHbCMJrWMwMXDo1SenlR9E/W/WD7IXrGvdL6PWky9L\nHUxdbuOxMBIGEhRIFFgKBElZVuG5pBAt/1GPx1Skm0tg6V5DvndqQavfYyFVhZ3T\nR0I5tYFBaA7BwVsI1aQTryofZFZ8gRGyIgGUtD0CgYBufn/ohNlElreyrAzhhdPw\nniTbvDSrPDW6fHkPiefYM5EN2UuNGzfHZMDyk+O+NVAUqhywm+e/qOWyc+KjI7wa\nFMV7lfEuGII/7bvublWAAbVXxvomTm5UbidiHkJwOeyknmYhdrqjThPj7VjiwvSi\nAPhDMxj6WkBqhSE1/jjFMQJ/JmsjoOAB6b9aVeeiWX7SMIXRUw/s7zzzYyxF7AgL\nE8KVY3bdH7SpP/mqAEwd2uKqKA7JjyJEj1uvZ2OfoWnGsaQYCqBHYVCI3gXZtAj/\nHXwaKft/S7OJrXRhZKZ53yy6MLdRxaZaCyKq2c+gu9mOolPs+n8YxsHAJ+3Q/eVG\nFQKBgQChCjj0dZAMQd4q/UBfk8cMIZCbDnd1qm/9rwcW4hObvpB0WG8AZ7uE8W1K\nDS+SHu+4n3aA9gY4CSwOdLRz/mMng9cs3wjWiLUsHPAkneANYMNsuikJMM+IVdiv\nZVih7y8Q6BNZOQfpIqR8BNjft8MinJTN//ephL6REOaPzlHfhw==\n-----END RSA PRIVATE KEY-----",
  "expiration": "2023-09-20T10:02:48Z",
  "thing_id": "3d49a42f-63fd-491b-9784-adf4b64ef347"
}
token =  "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI2NzM1NTksImlhdCI6MTY5MjYxOTU1OSwiaWRlbnRpdHkiOiJpbnNwaXJpbmdfZ29sZGJlcmdAZW1haWwuY29tIiwiaXNzIjoiY2xpZW50cy5hdXRoIiwic3ViIjoiYzk2ZWQwNmQtNTM5Zi00YjAxLTk2MWUtNTA0MjJmZjQ0OTBkIiwidHlwZSI6ImFjY2VzcyJ9.6J34t9Ts0VmjfsdxeUd66DQihFuB-mwlJ884KwoCjT1FmNr70yPjtIXpOvRjA58ggs-5kTh_ZZh25KtkTipWEg"
thing_id=  "2544670a-a992-4865-8222-24e5deed7bae"
cert_id= "22:16:df:60:c2:99:bc:c4:9b:1d:fd:71:5e:e9:07:d9:1b:3c:85:1d"

url= "http://localhost"

def test_issue(requests_mock):
    requests_mock.register_uri( "POST", url + "/certs", headers={"location": "/certs/" + thing_id}, json=certs, status_code=201)
    r = s.certs.issue(thing_id=thing_id, valid= "10h", token=token)
    assert r.error.status == 0
    assert certs == r.value
    
def test_issue_bad_token(requests_mock):
    requests_mock.register_uri( "POST", url + "/certs", headers={"location": "/certs/" + thing_id}, json=certs, status_code=401)
    r = s.certs.issue(thing_id=thing_id, valid= "10h", token=token)
    assert r.error.status == 1
    assert r.error.message == "Missing or invalid access token provided."

def test_view_by_thing(requests_mock):
    requests_mock.register_uri( "GET", url + "/serials" + "/" + thing_id, json=certs, status_code=200)
    r = s.certs.view_by_thing(thing_id=thing_id, token=token)
    assert r.error.status == 0
    assert certs == r.value
    
def test_view_by_thing_bad_token(requests_mock):
    requests_mock.register_uri( "GET", url + "/serials" + "/" + thing_id, json=certs, status_code=404)
    r = s.certs.view_by_thing(thing_id=thing_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed to retrieve corresponding certificate."
    
def test_view_by_serial(requests_mock):
    requests_mock.register_uri( "GET", url + "/certs" + "/" + cert_id, json=certs, status_code=200)
    r = s.certs.view_by_serial(cert_id=cert_id, token=token)
    assert r.error.status == 0
    assert certs == r.value
    
def test_view_by_serial_bad_token(requests_mock):
    requests_mock.register_uri( "GET", url + "/certs" + "/" + cert_id, json=certs, status_code=404)
    r = s.certs.view_by_serial(cert_id=cert_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed to retrieve corresponding certificate." 

def test_revoke(requests_mock):
    requests_mock.register_uri( "DELETE", url + "/certs" + "/" + thing_id, status_code=200)
    r = s.certs.revoke(thing_id=thing_id, token=token)
    assert r.error.status == 0
    
def test_revoke_bad_response(requests_mock):
    requests_mock.register_uri( "DELETE", url + "/certs" + "/" + thing_id, status_code=404)
    r = s.certs.revoke(thing_id=thing_id, token=token)
    assert r.error.status == 1
    assert r.error.message == "Failed to revoke corresponding certificate."
