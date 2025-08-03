pki match-sm2-key
=================

pki match-sm2-key

Function
--------



The **pki match-sm2-key** command configures a device to search for the SM2 key pair associated with a specific certificate.




Format
------

**pki match-sm2-key certificate-filename** *file-name*


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

Run this command to check the SM2 key pair corresponding to a certificate. After configuration, the system searches for all the local SM2 key pairs, compares them with the specified certificate and outputs the matched SM2 key pair name once it is searched out.


Example
-------

# Configure a device to search for the SM2 key pair that matches the certificate file sm2.cer.
```
<HUAWEI> system-view
[~HUAWEI] pki match-sm2-key certificate-filename sm2.cer
 Info: The file sm2.cer contains certificates 1.
 Info: Certificate 1 from file sm2.cer matches SM2 key sm2.key.

```