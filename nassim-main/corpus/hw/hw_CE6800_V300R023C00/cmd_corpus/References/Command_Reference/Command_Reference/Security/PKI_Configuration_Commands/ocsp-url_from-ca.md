ocsp-url from-ca
================

ocsp-url from-ca

Function
--------



The **ocsp-url from-ca** command configures the PKI entity to obtain the OCSP server's URL from the Authority Info Access (AIA) option in the CA certificate.

The **undo ocsp-url from-ca** command disables the PKI entity from obtaining the OCSP server's URL from the Authority Info Access (AIA) option in the CA certificate.



By default, a PKI entity does not obtain OCSP server's URL from the CA certificate's AIA option.


Format
------

**ocsp-url from-ca**

**undo ocsp-url from-ca**


Parameters
----------

None

Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a PKI entity uses OCSP to check certificate validity and the certificate to be checked contains an AIA extension, you can run this command to configure the PKI entity to obtain the OCSP server URL from the AIA extension. If the certificate to be checked does not contain the AIA extension, you can run the **ocsp url** command to configure a URL for the OCSP server on the PKI entity.

**Precautions**

The certificate revocation status can be checked only after the PKI realm is associated with a specified CA using the **ca-name** command.


Example
-------

# Configure the PKI entity to obtain OCSP server's URL from the CA certificate's AIA option.
```
<HUAWEI> system-view
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] ocsp-url from-ca

```