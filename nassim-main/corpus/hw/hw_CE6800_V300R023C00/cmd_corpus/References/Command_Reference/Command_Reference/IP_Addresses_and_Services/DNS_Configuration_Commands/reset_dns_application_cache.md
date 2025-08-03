reset dns application cache
===========================

reset dns application cache

Function
--------



The **reset dns application cache** command clears the cache of the application domain name resolution.




Format
------

**reset dns application cache** [ *domain-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Clear the cache of the application domain name resolution of the specific domain name. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Run this command if you need to clear the cache of the application domain name resolution.

**Precautions**

Clearing the cache of the application domain name resolution may impact the services. Perform the operation with caution.


Example
-------

# Clear the cache of the application domain name resolution.
```
<HUAWEI> reset dns application cache

```