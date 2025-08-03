reset bgp evpn flap-info
========================

reset bgp evpn flap-info

Function
--------



The **reset bgp evpn flap-info** command clears statistics about BGP EVPN route flapping.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset bgp instance** *instance-name* **evpn** **flap-info**

**reset bgp instance** *instance-name* **evpn** **flap-info** { **mac-route** | **prefix-route** } *prefix*

**reset bgp evpn flap-info**

**reset bgp evpn flap-info** { **mac-route** | **prefix-route** } *prefix*

**reset bgp instance** *instance-name* **evpn** { *ip-address* | *ipv6-address* } **flap-info**

**reset bgp evpn** { *ip-address* | *ipv6-address* } **flap-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Clears route dampening information about a specified BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **mac-route** | Indicates MAC advertisement routes. | - |
| **prefix-route** | Indicates IP prefix routes. | - |
| *prefix* | Specifies the prefix of an EVPN route. | An EVPN route prefix has the following formats:  MAC advertisement route. The value is in the format of E:M:H-H-H:L:X.X.X.X or E:M:H-H-H:L: [X:X::X:X], where:   * E indicates the ID of the VLAN to which the MAC address belongs. * M is fixed at 48, indicating the length of the MAC address. * H-H-H indicates the MAC address. The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. * L is fixed at 0, indicating the mask length of the IP address corresponding to the MAC address. * X.X.X.X indicates the IP address corresponding to the MAC address. Currently, this part can only be displayed as 0.0.0.0. * X:X::X:X indicates the IPv6 address corresponding to the MAC address.   IP Prefix route. The value is in the format of L:X.X.X.X:M or L:[X:X::X:X]:M, where:   * L is fixed at 0. * X.X.X.X indicates the ip address of host routes. * M indicates the mask length of host routes. * X:X::X:X indicates the ipv6 address of host routes. |
| *ip-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies the IPv6 address of a peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The process of adding a route to and then deleting the route from a routing table is called route flapping.When route flapping occurs, the routing protocol sends Update packets to neighbors. The neighbors that receive the Update packets need to recalculate routes and modify their routing tables. Frequent route flapping consumes extensive bandwidth and CPU resources and can even affect network operations.To clear flapping statistics about BGP EVPN routes on the public network, run the **reset bgp evpn flap-info** command. The command output helps you monitor route changes and locate network problems.

**Prerequisites**

Run the **display bgp evpn all routing-table flap-info** command to view statistics about BGP-EVPN route flapping. The command output shows specific flapping routes.

**Configuration Impact**

After the **reset bgp evpn flap-info** command is run, route flapping statistics are cleared and cannot be displayed.

**Follow-up Procedure**

After clearing route flapping statistics, run the **display bgp evpn all routing-table flap-info** command again to check BGP-EVPN route flapping statistics for fault locating.


Example
-------

# Clear the flapping statistics about the BGP EVPN routes.
```
<HUAWEI> reset bgp evpn flap-info

```