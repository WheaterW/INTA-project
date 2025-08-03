option121
=========

option121

Function
--------

The **option121** command configures the classless static route for the DHCP client.

The **undo option121** command deletes a configured classless static route.

By default, no classless static route is configured.



Format
------

**option121 ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8>

**undo option121** [ **ip-address** *ip-address* *mask-length* *gateway-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies a destination IP address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies a mask length. | The value is an integer ranging from 0 to 32. |
| *gateway-address* | Specifies a gateway address. | The value is in dotted decimal notation. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **option121** command applies to only the DHCP server. The **option121** command configures Option 121 that defines a classless static route allocated to a client.

mask-length and gateway-address specify a classless static route. The
**option121** command configures a maximum of eight classless static routes.

**Precautions**

* To configure multiple classless static routes, run the **option121** command repeatedly.
* The **undo option121** command will delete all classless static routes. To delete one classless static route, run the **undo option121 ip-address ip-address mask-length gateway-address** command.


Example
-------

# In the IP address pool view, configure classless static routes delivered by the DHCP server.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] option121 ip-address 10.10.10.10 24 10.11.11.11

```