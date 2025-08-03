dhcpv6 relay option79 insert enable
===================================

dhcpv6 relay option79 insert enable

Function
--------



The **dhcpv6 relay option79 insert enable** command inserts the Option79 field into DHCPv6 messages.

The **undo dhcpv6 relay option79 insert enable** command restores the default setting.



By default, the Option79 option is not inserted into DHCPv6 messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dhcpv6 relay option79 insert enable**

**undo dhcpv6 relay option79 insert enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MAC address is used to identify the DHCPv4 client on the IPv4 network and the DUID is used to identify the DHCPv6 client on the IPv6 network. In an IPv4 and IPv6 dual-stack service deployment scenario, the administrator wants to establish connections between clients' MAC addresses and IPv4 or IPv6 addresses obtained by the clients and perform unified management over dual-stack clients based on the MAC address. However, the MAC address of the DHCPv6 client cannot be identified using the DUID currently.As defined in RFC, a DHCPv6 relay agent can fill the link address and link type of a client into the Option79 field. When a device functions as a DHCPv6 relay agent, you can run the **dhcpv6 relay option79 insert enable** command to insert the Option79 field into DHCPv6 messages for enabling the DHCPv6 server to obtain the clients' MAC addresses. When this command is run and the DHCPv6 relay agent receives a Request message from a client, it inserts the Option79 field into the Request message and forwards the message to the DHCPv6 server. The DHCPv6 server then obtains the MAC address of the client by parsing the Option79 field.

**Prerequisites**

The DHCPv6 relay function has been enabled in the interface view.

**Precautions**

Only the first-hop DHCPv6 relay agent supports this function.This function takes effect for all interfaces if it is configured in the system view, and takes effect for a specified interface if it is configured in the view of the interface. If this command is configured in both the interface view and system view, the configuration in the interface view takes effect.


Example
-------

# Insert the Option79 option into DHCPv6 messages in the system view.
```
<HUAWEI> system-view
[~HUAWEI] dhcpv6 relay option79 insert enable

```

# Insert the Option79 field into DHCPv6 messages in the interface view.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] dhcpv6 relay destination fc00:1::1
[*HUAWEI-Vlanif100] dhcpv6 relay option79 insert enable

```