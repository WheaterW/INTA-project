crl load
========

crl load

Function
--------



The **crl load** command loads a certificate revocation list (CRL) to an SSL policy.

The **undo crl load** command unloads a CRL from an SSL policy.



By default, no CRLs are loaded to SSL policies.


Format
------

**crl load** *crlType* *crlFile*

**undo crl load** *crlType* *crlFile*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *crlType* | Loads a CRL to an SSL policy. | Enumerated type, there are three levels:   * pem-crl: Loads a PEM CRL to an SSL policy. * asn1-crl: Loads an ASN1 CRL to an SSL policy. |
| *crlFile* | Specifies the name of a CRL.  This file must be saved in the security sub-directory of the system directory. | The value is a string of 1 to 64 case-sensitive characters without a blank space.  The specified file name must be consistent with the name of the uploaded file.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The lifetime of a digital certificate is limited. A Certificate Authority (CA) can revoke a digital certificate to shorten the lifetime of the digital certificate. A CRL is a list of certificates that have been revoked, and therefore should not be relied upon. The CRL is issued by a CA. If a CA revokes a certificate, the key pair defined in the certificate can no longer be used even if the certificate does not expire. After a certificate in a CRL expires, the certificate is deleted from the CRL to shorten the CRL.If the key carried in a certificate is disclosed or a certificate needs to be revoked, use a third-party tool to revoke the certificate. The certificate will be marked revoked and added to a CRL.

**Prerequisites**

The **ssl policy** command has been used in the system view to create an SSL policy.

**Configuration Impact**

After a CRL is loaded to a client, the client checks whether the server's certificate is in the CRL when the client attempts to access the server. If the server's certificate is in the CRL, the connection fails.

**Precautions**

A maximum of two CRL files can be loaded to an SSL policy.


Example
-------

# Load a PEM CRL to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy policy1
[~HUAWEI-ssl-policy-policy1] crl load pem-crl server.pem

```