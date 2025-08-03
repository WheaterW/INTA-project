ipv6 route recursive-lookup nd vlink-direct-route protocol static
=================================================================

ipv6 route recursive-lookup nd vlink-direct-route protocol static

Function
--------



The **ipv6 route recursive-lookup nd vlink-direct-route protocol static** command allows IPv6 static routes to be recursed to ND Vlink direct routes.

The **undo ipv6 route recursive-lookup nd vlink-direct-route protocol static** command disables IPv6 static routes from being recursed to ND Vlink direct routes.



By default, IPv6 static routes are not recursed to ND Vlink direct routes.


Format
------

**ipv6 route recursive-lookup nd vlink-direct-route protocol static**

**undo ipv6 route recursive-lookup nd vlink-direct-route protocol static**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **ipv6 route recursive-lookup nd vlink-direct-route protocol static** command is used in Layer 2 access to Layer 3 scenarios. It is used together with the recursive-lookup host-route parameter in the ipv6 route-static command to recurse IPv6 static routes only to ND Vlink direct routes.When a Layer 2 link fails, for example, the physical interface corresponding to a Layer 2 device fails, traffic can be quickly switched to the backup path to prevent black-hole routes.



**Precautions**



After the **ipv6 route recursive-lookup nd vlink-direct-route protocol static** command is run globally, all IPv6 static routes can be recursed to ND Vlink direct routes. After the **undo ipv6 route recursive-lookup nd vlink-direct-route protocol static** command is run, IPv6 static routes cannot be recursed to ND Vlink direct routes.




Example
-------

# Allow IPv6 static routes to be recursed to ND Vlink direct routes.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route recursive-lookup nd vlink-direct-route protocol static

```

**Table 1** Description of the **ipv6 route recursive-lookup nd vlink-direct-route protocol static** command output
| Item | Description |
| --- | --- |
| vlink-direct-route | Vlink direct route. |