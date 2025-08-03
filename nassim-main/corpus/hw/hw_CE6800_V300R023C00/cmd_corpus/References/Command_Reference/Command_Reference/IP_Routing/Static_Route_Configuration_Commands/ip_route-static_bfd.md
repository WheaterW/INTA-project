ip route-static bfd
===================

ip route-static bfd

Function
--------



The **ip route-static bfd** command sets the BFD parameters for a static route.

The **undo ip route-static bfd** command cancels BFD parameters of a static route.



By default, BFD parameters of a static route are not set.


Format
------

**ip route-static bfd** { *interface-name* | *interface-type* *interface-number* } { *nexthop-address* } [ **local-address** *address* ] [ **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* ] \*

**ip route-static bfd** [ **vpn-instance** *vpn-instance-name* ] *nexthop-address* **local-address** *address* [ **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* ] \*

**undo ip route-static bfd** { *interface-name* | *interface-type* *interface-number* } { *nexthop-address* }

**undo ip route-static bfd** [ **vpn-instance** *vpn-instance-name* ] *nexthop-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |
| *nexthop-address* | Specifies the next-hop address. | The value is in dotted decimal notation. |
| **local-address** *address* | Specifies the local address. | The value is in dotted decimal notation. |
| **min-rx-interval** *min-rx-interval* | Specifies the minimum interval at which BFD control packets are received. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-tx-interval** *min-tx-interval* | Specifies the minimum interval at which BFD control packets are sent. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier* | Specifies the detection time multiplier. | The value is an integer ranging from 3 to 50. The default value is 3. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance that the next hop belongs to. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To configure BFD parameters for a static route, run the ip route-static bfd command.

**Implementation Procedure**

When setting BFD parameters for a static route, you need to specify the outbound interface or next hop.

**Configuration Impact**

To modify BFD parameters, you need to update BFD parameters of all the corresponding static routes.If BFD parameters are configured, but the local-address ip-address parameter is not, BFD sessions may fail to be negotiated.If the **undo ip route-static bfd** command is run, the static route is unbound from all BFD sessions. Therefore, exercise caution when running the command.

**Precautions**

* When configuring BFD for a single route, you need to check whether BFD parameters are set for the static route.
* Search for BFD parameters according to the static route's outbound interface, next hop, and the VPN instance to which the next hop belongs.
* If none of min-rx-interval, min-tx-interval, and detect-multiplier is specified when BFD parameters are configured, the global default BFD parameters are used.
* When configuring dynamic BFD for VPN static route, set BFD parameters as follows:If vpn-instance is specified, the VPN instance must be the same as the VPN instance to which the next hop of the static route belongs.When an outbound interface is configured, the VPN instance to which the next hop of the static route belongs must be the VPN instance bound to the outbound interface.

Example
-------

# Set the next hop address to 1.1.1.1, local address to 10.11.11.1, and minimum interval at which BFD packets are received to 100 ms for a static route.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static bfd 1.1.1.1 local-address 10.11.11.1 min-rx-interval 100

```