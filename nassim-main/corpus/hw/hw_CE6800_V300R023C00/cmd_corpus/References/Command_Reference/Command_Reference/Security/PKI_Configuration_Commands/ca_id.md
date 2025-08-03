ca id
=====

ca id

Function
--------



The **ca id** command specifies a certificate authority (CA) trusted by a PKI realm.

The **undo ca id** command deletes the CA trusted by a PKI realm.



By default, no trusted CA is configured in a PKI realm.


Format
------

**ca id** *ca-name*

**undo ca id**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ca-name* | Specifies the name of a CA trusted by a PKI realm. | The value is a string of 1 to 64 case-sensitive  characters, and can contain spaces. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the ca id command is executed to specify the CA trusted by the device, the CA then requests, obtains, revokes, or queries the device's certificate.


Example
-------

# Specify the CA root\_ca trusted by the PKI realm abc.
```
<HUAWEI> system-view
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] ca id root_ca

```