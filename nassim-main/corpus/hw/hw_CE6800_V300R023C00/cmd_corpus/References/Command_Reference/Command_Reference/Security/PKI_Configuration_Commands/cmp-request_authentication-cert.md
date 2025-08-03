cmp-request authentication-cert
===============================

cmp-request authentication-cert

Function
--------



The **cmp-request authentication-cert** command configures the certificate for identity authentication in the request through CMPv2.

The **undo cmp-request authentication-cert** command deletes the certificate for identity authentication in the request through CMPv2.



By default, no certificate for identity authentication in the request through CMPv2 is configured.


Format
------

**cmp-request authentication-cert** *cert-name*

**undo cmp-request authentication-cert**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cert-name* | Specifies the name of a certificate file. | The certificate file name must exist and cannot contain backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), question marks (?), or slashes (/). |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Run this command to configure the certificate for identity authentication if you need to apply for a certificate through CMPv2. For different requests through CMPv2, the required certificates are as follows:

* For Initialization Requests (IR), the required certificate is an external identity certificate.
* For certification requests (CR), the required certificate is the one that the CA has already issued to the device.
* For the key update requests (KUR), the required certificate is the one that the CA has already issued to the device and is also the one to be updated.

**Prerequisites**

An identity authentication in the request through CMPv2 exists.


Example
-------

# Configure the certificate for identity authentication in the request through CMPv2.
```
<HUAWEI> system-view
[~HUAWEI] pki import-certificate local filename cert_local.cer
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request authentication-cert cert_local.cer

```