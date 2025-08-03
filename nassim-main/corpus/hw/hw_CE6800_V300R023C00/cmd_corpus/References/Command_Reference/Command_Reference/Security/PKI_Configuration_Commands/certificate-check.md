certificate-check
=================

certificate-check

Function
--------



The **certificate-check** command sets the method of checking whether a certificate in the PKI realm is revoked.

The **undo certificate-check** command cancels the method of checking whether a certificate in the PKI realm is revoked.



By default, the system does not check whether a certificate in the PKI realm is revoked.


Format
------

**certificate-check** { { **crl** | **ocsp** } \* [ **none** ] | **none** }

**undo certificate-check**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **crl** | Sets the check method to Certificate Revocation List (CRL). | - |
| **ocsp** | Sets the check method to Online Certificate Status Protocol (OCSP). | - |
| **none** | Indicates that the system does not check whether a certificate is revoked. | - |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a PKI entity verifies the peer certificate, it often needs to check whether the peer certificate is valid, for example, whether the peer certificate has expired or has been added to the CRL. In this case, you can run this command to check the peer certificate status.The following methods can be used to check the certificate revocation status in a PKI realm:

* CRL modeLDAP mode and LDAPv3 template mode: A PKI entity obtains a CRL from an LDAP server by sending a CRL query request packet carrying the attributes and identifier of the LDAP server.
* None modeIf no CRL server is available for the PKI entity or the PKI entity does not need to check the peer certificate status, the None mode can be used. In this mode, the PKI entity does not check whether a certificate has been revoked; the system does not check whether the certificate chain is complete, but still verifies the certificate validity period and issuer.You can perform the following operations as required:
* If the **certificate-check crl** command is configured, use only the CRL mode.
* If the **certificate-check crl none** command is configured, use the CRL mode first. If the CRL mode is unavailable, use the None mode.
* If the **certificate-check ocsp none** command is configured, use the OCSP mode first. If the OCSP mode is unavailable, use the None mode.
* If the **certificate-check crl ocsp** command is configured for a certificate, the CRL mode is used first. If the CRL mode is unavailable, use the OCSP mode. If neither of the modes is unavailable, the certificate is considered invalid.
* If the **certificate-check ocsp crl** command is configured for a certificate, use the OCSP mode first. If the OCSP mode is unavailable, use the CRL mode. If neither of the modes is unavailable, the certificate is considered invalid.
* If the **certificate-check crl ocsp none** command is configured, use the CRL mode first. If the CRL mode is unavailable, use the OCSP mode. If neither of the modes is available, use the None mode.
* If the **certificate-check ocsp crl none** command is configured, use the OCSP mode first. If the OCSP mode is unavailable, use the CRL mode. If neither of the modes is available, use the None mode.
* If the **certificate-check none** command is configured, use the None mode. That is, the device does not check the certificate revocation status.

**Precautions**

If this command is not executed in a PKI realm, the global certificate check method takes effect. The global certificate check method is configured by the **pki certificate-check** command in the system view.The device can use the method configured in the PKI realm to check certificate status only after the PKI realm is associated with a certain CA using the **ca-name** command.After the **certificate-check crl** command is configured, if the device does not have the CRL file, the device fails the certificate verification, and the certificate becomes invalid.


Example
-------

# Set the certificate check method to crl none in PKI realm test. If the CRL mode is unavailable, the certificate is regarded as valid.
```
<HUAWEI> system-view
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] certificate-check crl none

```