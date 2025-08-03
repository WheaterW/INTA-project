ocsp nonce enable
=================

ocsp nonce enable

Function
--------



The **ocsp nonce enable** command adds a nonce extension to the OCSP request sent by a PKI entity.

The **undo ocsp nonce enable** command cancels the configuration.



By default, the OCSP request sent by a PKI entity contains a nonce extension.


Format
------

**ocsp nonce enable**

**undo ocsp nonce enable**


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

To improve security and reliability of communication between PKI entity and OCSP server, this command adds a nonce extension (a random value) to the OCSP request sent by the PKI entity. If the nonce extension values on the PKI entity and OCSP server are different, communication fails.


Example
-------

# Add a nonce extension to the OCSP request sent by a PKI entity
```
<HUAWEI> system-view
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] ocsp nonce enable

```