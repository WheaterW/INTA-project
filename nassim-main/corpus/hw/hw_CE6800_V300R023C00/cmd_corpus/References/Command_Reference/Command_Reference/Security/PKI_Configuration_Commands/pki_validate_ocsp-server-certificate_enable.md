pki validate ocsp-server-certificate enable
===========================================

pki validate ocsp-server-certificate enable

Function
--------



The **pki validate ocsp-server-certificate enable** command enables the function that uses the OCSP server certificate to verify OCSP server packets.

The **undo pki validate ocsp-server-certificate enable** command disables the function that uses the OCSP server certificate to verify OCSP server packets.



By default, the function that uses the OCSP server certificate to verify OCSP server packets is enabled.


Format
------

**pki validate ocsp-server-certificate enable**

**undo pki validate ocsp-server-certificate enable**


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

**Usage Scenario**

For security purposes, you are advised to enable the function that uses the OCSP server certificate to verify OCSP server packets. If OCSP server packets fail the verification, the device discards these packets.

**Precautions**

If the imported OCSP server certificate is not the correct one, OCSP server packets fail the verification, causing the local certificate to become unavailable. To prevent this problem, import the correct OCSP server certificate. If no OCSP server certificate can be obtained, run the **undo pki validate ocsp-server-certificate enable** command to disable the function that uses the OCSP server certificate to verify OCSP server packets.


Example
-------

# Enable the function that uses the OCSP server certificate to verify OCSP server packets.
```
<HUAWEI> system-view
[~HUAWEI] pki validate ocsp-server-certificate enable

```