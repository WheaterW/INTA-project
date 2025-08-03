description (PKI access configuration view)
===========================================

description (PKI access configuration view)

Function
--------



The **description** command configures description for a certificate access policy.

The **undo description** command deletes the description of a certificate access policy.



By default, a certificate access policy does not have a description.


Format
------

**description** *description*

**undo description**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *description* | The description is configured for the certificate access policy. | The value is a string of 1 to 128 case-sensitive characters without question marks (?). |



Views
-----

PKI access configuration view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Proper description helps administrators understand the purpose of a certificate access policy, improving certificate searching and maintenance efficiency.


Example
-------

# Configure description for the certificate access policy.
```
<HUAWEI> system-view
[~HUAWEI] pki certificate access-control-policy name policy1
[*HUAWEI-pki-access-policy1] description trust to untrust

```