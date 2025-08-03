key-usage
=========

key-usage

Function
--------



The **key-usage** command configures the purpose description for a certificate public key.

The **undo key-usage** command deletes the purpose description of a certificate public key.



By default, a certificate public key does not have a purpose description.


Format
------

**key-usage** { **signature** | **encipherment** }

**undo key-usage**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **signature** | Specifies a certificate public key for signature. | - |
| **encipherment** | Specifies a certificate public key for encryption. | - |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After a purpose description is configured for a certificate public key, the CA server can obtain the purpose of the public key during certificate enrollment.


Example
-------

# Set the purpose description for the certificate public key to signature.
```
<HUAWEI> system-view
[~HUAWEI] pki realm e
[*HUAWEI-pki-realm-e] key-usage signature

```