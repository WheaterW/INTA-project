software crl load (User view)
=============================

software crl load (User view)

Function
--------



The **software crl load** command loads a digital signature Certificate Revocation List (CRL) file to the system.



By default, a specified digital signature certificate CRL is loaded.


Format
------

**software crl load** *crlName*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *crlName* | Specifies the name of a revocation list. | The value is a string of 5 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The lifetime of a digital certificate is limited. A Certificate Authority (CA) can revoke a digital certificate to shorten the lifetime of the digital certificate. A CRL specifies a list of invalid certificates issued by CAs. If a CA revokes a certificate, the declaration about authorized key pairs is revoked before the certificate expires. Once the CRL expires, data listed in the CRL is deleted to shorten the CRL.If an issued digital signature certificate needs to be revoked due to key disclosure or other reasons, a third-party tool can be used to mark the certificate invalid and add the certificate to a digital certificate CRL. To load the latest digital signature CRL file to a device, run the **software crl load** command. After the file is loaded, the device does not verify the digital signature certificate upon next startup.


Example
-------

# Load a CRL file to the system.
```
<HUAWEI> software crl load crldata-new.crl

```