reset pki global-ca
===================

reset pki global-ca

Function
--------



The **reset pki global-ca** command clears the content of the CA certificate, local certificate, CRL, and OCSP responder certificate imported to the memory.




Format
------

**reset pki global-ca**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Run this command to clear all certificates and CRLs in the memory and the ca\_config.ini on the flash. The corresponding certificate files on the flash of a device will not be deleted.Before you format the flash of a device, run the reset pki global-ca command.

**Precautions**

This command can clear the content of all CA certificates, local certificates, CRLs, and OCSP responder certificates. Exercise caution when using this command.


Example
-------

# Clear the content of the CA certificate, local certificate, CRL, and OCSP responder certificate imported to the memory.
```
<HUAWEI> reset pki global-ca

```