display software crl (All views)
================================

display software crl (All views)

Function
--------



The **display software crl** command displays information about a digital signature certificate revocation list (CRL) file.




Format
------

**display software crl**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If an issued digital signature certificate needs to be revoked due to key disclosure or other reasons, a third-party tool can be used to mark the certificate invalid and add the certificate to a digital certificate CRL. To check information about the digital signature CRL file, run the display software crl command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the digital signature CRL file that has been loaded to the system.
```
<HUAWEI> display software crl
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Slot ID          Publisher                                                                        Issue Date                     Status  Signature Algorithm
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
1                C=CN,O=Huawei,CN=Huawei Root CA                                                  2019-07-06 02:29:01            Valid   sha256RSA
1                C=CN,O=Huawei,CN=Huawei Code Signing Certificate Authority                       2019-06-17 12:28:22            Valid   sha256RSA
1                C=CN,O=Huawei,CN=Huawei Timestamp Certificate Authority                          2019-06-29 01:11:29            Valid   sha256RSA
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display software crl (All views)** command output
| Item | Description |
| --- | --- |
| Slot ID | Slot ID of the board where the CRL is configured. |
| Publisher | CRL publisher. |
| Issue Date | CRL release date. |
| Status | CRL status.   * Valid: The list is valid. * InValid: The list is invalid. |
| Signature Algorithm | Signature algorithm:   * sha256RSA: sha256RSA algorithm. * RSASSA-PSS: RSASSA-PSS algorithm. |