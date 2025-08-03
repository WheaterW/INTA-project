cmp-request verification-cert
=============================

cmp-request verification-cert

Function
--------



The **cmp-request verification-cert** command configures the certificate file for verifying the CA response signature.

The **undo cmp-request verification-cert** command deletes the certificate file for verifying the CA response signature.



By default, no certificate file for verifying the CA response signature is configured.


Format
------

**cmp-request verification-cert** *cert-file-name*

**undo cmp-request verification-cert**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *cert-file-name* | Specifies the certificate file name. | The value is a string of 1 to 64 case-sensitive characters, excluding backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), question marks (?), and slashes (/). |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After this command is executed, the device uses the configured certificate to verify the CA response signature. This command configures the CA certificate.If this command is not executed and the CA response mode is signature, the device constructs a certificate chain based on the certificates in the response messages sent by the device itself and CA to verify the CA response signature. If the MAC mode is set, the device uses the MAC to verify the CA response signature. That is, this command does not take effect.

**Prerequisites**

The certificate file for verifying the CA response signature exists.


Example
-------

# Configure the certificate file for verifying the CA response signature.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request verification-cert aa.der

```