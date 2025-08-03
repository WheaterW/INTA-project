reset msdp all-instance sa-cache
================================

reset msdp all-instance sa-cache

Function
--------



The **reset msdp all-instance sa-cache** command clears (S, G) entries in the source active (SA) cache in all-instances.




Format
------

**reset msdp all-instance sa-cache** [ *group-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-address* | Specifies the group address carried in (S, G) information. | The value ranges from 224.0.0.0 to 239.255.255.255, in dotted decimal notation. If this parameter is not specified, all (S, G) information in the SA cache is cleared. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you want to clear (S, G) information from an SA cache, run the **reset msdp all-instance sa-cache** command.

**Configuration Impact**

(S, G) information in the SA cache cannot be restored after you clear it. So, confirm the action before you use this command.


Example
-------

# Clear the (S, G) entries with the group address being 225.5.4.3 in the SA cache of the all instance.
```
<HUAWEI> reset msdp all-instance sa-cache 225.5.4.3

```