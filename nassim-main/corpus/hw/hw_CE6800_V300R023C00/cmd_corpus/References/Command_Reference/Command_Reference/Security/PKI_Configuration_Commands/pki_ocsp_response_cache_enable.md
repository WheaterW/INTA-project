pki ocsp response cache enable
==============================

pki ocsp response cache enable

Function
--------



The **pki ocsp response cache enable** command enables a device to cache OCSP responses.

The **undo pki ocsp response cache enable** command disables a device from caching OCSP responses.



By default, the PKI OCSP response cache function is disabled.


Format
------

**pki ocsp response cache enable**

**undo pki ocsp response cache enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After you enable a PKI entity to cache OCSP responses, the PKI entity first searches its cache for the certificate revocation status. If the search fails, the PKI entity sends a request to the OCSP server. In addition, the device caches valid OCSP responses for subsequent query. The OCSP responses have a validity period. With OCSP response cache enabled, a PKI entity refreshes the cached OCSP responses every minute to clear expired OCSP responses.


Example
-------

# Enable the PKI OCSP response cache function
```
<HUAWEI> system-view
[~HUAWEI] pki ocsp response cache enable

```