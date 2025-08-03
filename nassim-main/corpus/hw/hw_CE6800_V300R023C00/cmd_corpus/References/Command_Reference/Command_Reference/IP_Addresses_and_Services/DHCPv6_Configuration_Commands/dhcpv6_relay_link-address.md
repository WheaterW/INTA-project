dhcpv6 relay link-address
=========================

dhcpv6 relay link-address

Function
--------



The **dhcpv6 relay link-address** command configures a DHCPv6 relay gateway address.

The **undo dhcpv6 relay link-address** command restores the default DHCPv6 relay gateway address.



By default, a DHCPv6 relay agent selects the first configured IPv6 global unicast address from an interface with DHCPv6 relay enabled as its gateway address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay link-address** *ipv6-address*

**undo dhcpv6 relay link-address** [ *ipv6-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 address as the gateway address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The IPv6 address of the first DHCPv6 relay agent is used as the DHCPv6 relay gateway address for clients and is carried in the link-address field in DHCPv6 relay messages. The DHCPv6 server uses the link-address field to determine the network segment on which a client resides so that the server can assign an IPv6 address on this network segment to the client.If the **dhcpv6 relay link-address** command is not run, the DHCPv6 relay agent selects the first configured IPv6 global unicast address on the interface enabled with the DHCPv6 relay function as the gateway address of the relay agent. This makes address planning and allocation difficult. To allow clients connecting to a DHCPv6 relay interface to obtain IPv6 addresses on the same network segment, run the **dhcpv6 relay link-address** command to configure a gateway address. Then the DHCPv6 relay interface uses this configured gateway address for all DHCPv6 request messages it receives.

**Precautions**

The configured DHCPv6 relay gateway address must be a global unicast address of the DHCPv6 relay interface.An interface can have only one IPv6 address configured as the DHCPv6 relay gateway address. If a gateway address has been configured for an interface and the **dhcpv6 relay link-address** command is run, the newly configured gateway address replaces the original one.


Example
-------

# Set the gateway address to 2001:db8::1 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcpv6 relay link-address 2001:db8::1

```