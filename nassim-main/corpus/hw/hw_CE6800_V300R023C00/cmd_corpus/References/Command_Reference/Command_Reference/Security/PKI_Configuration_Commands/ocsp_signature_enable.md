ocsp signature enable
=====================

ocsp signature enable

Function
--------



The **ocsp signature enable** command enables the function of signing OCSP request packets.

The **undo ocsp signature enable** command disables the function of signing OCSP request packets.



By default, the function of signing OCSP request packets is disabled.


Format
------

**ocsp signature enable**

**undo ocsp signature enable**


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

hen the certificate check mode is set to OCSP, the device sends OCSP request packets to the OCSP server. To improve access security, run this command to enable signing on OCSP request packets.


Example
-------

# enables the function of signing OCSP.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] ocsp signature enable

```