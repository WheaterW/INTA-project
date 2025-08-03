ipv6 route-static bfd
=====================

ipv6 route-static bfd

Function
--------



The **ipv6 route-static bfd** command sets BFD parameters for an IPv6 static route.

The **undo ipv6 route-static bfd** command deletes the BFD parameters set for an IPv6 static route.



By default, no BFD parameters are configured for an IPv6 static route.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static bfd** { *interface-name* | *interface-type* *interface-number* } *nexthop-address* [ **local-address** *ipv6-address* ] [ **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* ] \*

**ipv6 route-static bfd** [ **vpn-instance** *vpn-instance-name* ] *nexthop-address* **local-address** *ipv6-address* [ **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* ] \*

**undo ipv6 route-static bfd** { *interface-name* | *interface-type* *interface-number* } *nexthop-address*

**undo ipv6 route-static bfd** [ **vpn-instance** *vpn-instance-name* ] *nexthop-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| *nexthop-address* | Specifies a next hop IPv6 address. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **local-address** *ipv6-address* | Specifies a local IPv6 address.  If this parameter is not specified, the link-local address of the interface is used as the local IPv6 address. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| **min-rx-interval** *min-rx-interval* | Specifies the minimum interval at which BFD control packets are received. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **min-tx-interval** *min-tx-interval* | Specifies the minimum interval at which BFD control packets are sent. | The value is an integer ranging from 3 to 1000, in milliseconds. The default value is 1000. |
| **detect-multiplier** *multiplier* | Specifies the detection time multiplier. | The value is an integer in the range 3 to 50. The default value is 3. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the next hop address belongs. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain question marks (?). The VPN instance name cannot be <b>\_public\_</b>. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set BFD parameters for a single IPv6 static route, run the ipv6 route-static bfd command.

**Implementation Procedure**

When setting BFD parameters for an IPv6 static route in the system view, you need to specify the outbound interface or the next hop of the IPv6 static route.

**Configuration Impact**

After BFD parameters are modified, the BFD parameters of all IPv6 static routes are updated.If BFD parameters are configured, but the local-address ipv6-address parameter is not, BFD sessions may fail to be negotiated.If the undo ipv6 route-static bfd command is run, the static route is unbound from all BFD sessions. Therefore, exercise caution when running the command.

**Precautions**

* When configuring BFD for a single IPv6 static route, check whether BFD parameters are set for the IPv6 static route.
* Search for BFD parameters of a single IPv6 unicast route based on the outbound interface, next hop address, or the IPv6 address family-enabled VPN instance to which the next hop address of the route belongs.
* If none of min-rx-interval, min-tx-interval, or detect-multiplier is specified, the global default values of BFD parameters are used.
* When you configure BFD parameters for a static VPN route, specifying a VPN instance and specifying an outbound interface are mutually exclusive. If an outbound interface is specified in this configuration, the VPN instance created on the next hop is used as the VPN instance bound to the outbound interface.


Example
-------

# Set the next hop address to 2001:db8:1::1, local address to 2001:db8:2::1, and minimum interval at which BFD packets are received to 100 ms for a static route.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static bfd 2001:db8:1::1 local-address 2001:db8:2::1 min-rx-interval 100

```