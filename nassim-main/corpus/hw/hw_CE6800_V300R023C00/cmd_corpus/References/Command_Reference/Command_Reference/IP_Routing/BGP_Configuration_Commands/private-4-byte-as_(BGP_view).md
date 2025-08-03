private-4-byte-as (BGP view)
============================

private-4-byte-as (BGP view)

Function
--------



The **private-4-byte-as** command enables or disables the 4-byte private AS number capability.



By default, the 4-byte private AS number capability is enabled.


Format
------

**private-4-byte-as enable**

**private-4-byte-as disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables the 4-byte private AS number capability. | - |
| **enable** | Enables the 4-byte private AS number capability. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the 4-byte private AS number capability is enabled, private AS numbers range from 64512 to 65534, and from 4200000000 to 4294967294. 65535 and 4294967295 are reserved for special use. If 4-byte private AS numbers are disabled, private AS numbers range from 64512 to 65534, and 65535 is reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.

**Precautions**

When the **private-4-byte-as** command configuration changes, the device re-advertises local routes to peers for which the peer public-as-only import [ force ] command is run.


Example
-------

# Enable the 4-byte private AS number function.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] private-4-byte-as enable

```