pki ocsp response cache number
==============================

pki ocsp response cache number

Function
--------



The **pki ocsp response cache number** command sets the maximum number of OCSP responses that can be cached on a PKI entity.

The **undo pki ocsp response cache number** command restores the maximum number of OCSP responses that can be cached on a PKI entity to the default value.



By default, the maximum number of OCSP responses that can be cached on a PKI entity is 1000.


Format
------

**pki ocsp response cache number** *number*

**undo pki ocsp response cache number**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of OCSP responses that can be cached on a PKI entity. | The value is an integer that ranges from 1 to 5000. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

A PKI entity caches valid OCSP responses for subsequent query. If the number of cached OCSP responses reaches the value specified by number, the PKI entity stops caching OCSP responses.


Example
-------

# Set the maximum number of OCSP responses that can be cached on a PKI entity to 800.
```
<HUAWEI> system-view
[~HUAWEI] pki ocsp response cache number 800

```