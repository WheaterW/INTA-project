pki file-format
===============

pki file-format

Function
--------



The **pki file-format** command sets the format for the saved certificate request, certificate, and CRL.



By default, the device stores certificate request, certificate, and CRL in PEM format.


Format
------

**pki file-format** { **der** | **pem** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **der** | Indicates that the format of a certificate request file is DER. | - |
| **pem** | Indicates that the format of a certificate request file is PEM. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To change the format for the saved certificate request, certificate, and CRL, for example, to use the certificate and CRL obtained through CMPv2 or LDAP, run the pki file-format command.The created self-signed certificate or local certificate can only be saved in PEM format.


Example
-------

# Set the format of saved certificate request, certificate, and CRL to DER.
```
<HUAWEI> system-view
[~HUAWEI] pki file-format der

```