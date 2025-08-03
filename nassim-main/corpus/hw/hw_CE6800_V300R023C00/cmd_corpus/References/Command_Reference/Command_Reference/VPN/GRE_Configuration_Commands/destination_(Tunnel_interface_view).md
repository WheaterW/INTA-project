destination (Tunnel interface view)
===================================

destination (Tunnel interface view)

Function
--------



The **destination** command configures a destination address for a tunnel.

The **undo destination** command deletes the destination address of a tunnel.



By default, no destination address is configured for a tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**destination** [ **vpn-instance** *vpn-instance-name* ] *ip-address*

**undo destination** [ [ **vpn-instance** *vpn-instance-name* ] *ip-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the destination address of a tunnel belongs. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ip-address* | Specifies the destination address of a tunnel. | The value is in dotted decimal notation. |



Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring GRE tunnels, you need to create tunnel interfaces and use the **destination** command to configure the destination addresses of tunnels.

**Prerequisites**

The tunnel mode has been configured using the **tunnel-protocol** command.

**Configuration Impact**

The same source or destination IP address cannot be configured for two or more tunnel interfaces that use the same encapsulation protocol.


Example
-------

# Configure the destination IP address for a GRE tunnel named Tunnel10 as 2.2.2.2.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] tunnel-protocol gre
[*HUAWEI-Tunnel10] destination 2.2.2.2

```