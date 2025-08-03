dhcpv6 relay vss-control insert enable
======================================

dhcpv6 relay vss-control insert enable

Function
--------



The **dhcpv6 relay vss-control insert enable** command enables the function of inserting the VSS-Control option into Relay-Forward messages on a DHCPv6 relay interface in the inter-VPN scenario.

The **undo dhcpv6 relay vss-control insert enable** command disables the function of inserting the VSS-Control option into Relay-Forward messages on a DHCPv6 relay interface in the inter-VPN scenario.



By default, the function of inserting the VSS-Control option into Relay-Forward messages on a DHCPv6 relay interface in the inter-VPN scenario is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay vss-control insert enable**

**undo dhcpv6 relay vss-control insert enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a DHCPv6 client and server are located in different VPNs, you must run this command on the DHCPv6 relay agent. The DHCPv6 relay agent inserts the VSS-Control option into a Relay-forward message and sends the option to the remote DHCPv6 server. The option carries information about the VPN to which the client belongs. The DHCPv6 server then searches for the corresponding address pool based on the option and allocates an address to the client.

**Prerequisites**



A Layer 2 interface has been switched to a Layer 3 interface using the **undo portswitch** command.




Example
-------

# Enable a DHCPv6 relay agent to insert VSS-Control options into DHCPv6 messages received on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcpv6 relay vss-control insert enable

```