pki match-rsa-key
=================

pki match-rsa-key

Function
--------



The **pki match-rsa-key** command configures a device to search for the RSA key pair associated with a specific certificate.




Format
------

**pki match-rsa-key certificate-filename** *file-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **certificate-filename** *file-name* | Specifies the name of a certificate file. | The value must be an existing certificate file name. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Run this command to check the RSA key pair corresponding to a certificate. After configuration, the system searches for all the local RSA key pairs, compares them with the specified certificate and outputs the matched RSA key pair name once it is searched out.


Example
-------

# Configure a device to search for the RSA key pair that matches certificate file local.cer.
```
<HUAWEI> system-view
[~HUAWEI] pki match-rsa-key certificate-filename local.cer
 Info: The file local.cer contains certificates 1. 
 Info: Certificate 1 from file local.cer matches RSA key rsa2

```