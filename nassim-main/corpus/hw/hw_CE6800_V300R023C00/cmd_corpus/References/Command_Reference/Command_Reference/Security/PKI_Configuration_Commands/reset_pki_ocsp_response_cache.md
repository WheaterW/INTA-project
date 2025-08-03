reset pki ocsp response cache
=============================

reset pki ocsp response cache

Function
--------



The **reset pki ocsp response cache** command resets an OCSP response cache.




Format
------

**reset pki ocsp response cache**


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

The PKI entity caches valid OCSP responses for future searches. If the number of cached OCSP responses reaches the maximum value, no more OCSP responses can be cached. To ensure that the latest OCSP responses can be cached, you can run this command to clear the OCSP response cache first.


Example
-------

# Reset an OCSP response cache.
```
<HUAWEI> reset pki ocsp response cache

```