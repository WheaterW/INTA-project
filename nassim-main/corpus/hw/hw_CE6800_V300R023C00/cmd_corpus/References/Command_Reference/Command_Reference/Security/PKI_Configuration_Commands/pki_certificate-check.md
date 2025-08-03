pki certificate-check
=====================

pki certificate-check

Function
--------



The **pki certificate-check** command configures the mode of checking the global certificate revocation status.

The **undo pki certificate-check** command restores the default configuration.



By default, the CRL check for the global certificate revocation status is enabled. If the CRL mode is unavailable, the certificate is regarded as valid.


Format
------

**pki certificate-check crl** [ **none** ]

**pki certificate-check none**

**undo pki certificate-check**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **none** | Indicates that the system does not check whether a certificate is revoked. | - |
| **crl** | Sets the check method to Certificate Revocation List (CRL). | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When verifying the peer certificate, a PKI entity often needs to check whether the peer certificate is valid, for example, whether the peer certificate expires or is added to the CRL. In this case, you can run this command to check the peer certificate status.The global certificate revocation status can be checked in any of the following ways:

* CRL modeRun the **pki import-crl** command to import a CRL to the device memory.
* None modeIf no CRL server is available for the PKI entity or the PKI entity does not need to check the peer certificate status, the None mode can be used. In this mode, the PKI entity does not check whether a certificate has been revoked. In this mode, the system does not check whether the certificate chain is complete, but still verifies the certificate validity period and issuer.You can perform the following operations as required:
* Run the **pki certificate-check crl** command to use the CRL mode only.
* Run the **pki certificate-check crl none** command to use the CRL mode first, and then the none mode if the CRL mode is unavailable.
* Run the **pki certificate-check none** command to use the none mode, so that the device does not check the certificate revocation status.
* Run the **undo pki certificate-check** command to restore the default certificate check mode (pki certificate-check crl none).


Example
-------

# Set the certificate check method to crl in global.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate-check crl

```