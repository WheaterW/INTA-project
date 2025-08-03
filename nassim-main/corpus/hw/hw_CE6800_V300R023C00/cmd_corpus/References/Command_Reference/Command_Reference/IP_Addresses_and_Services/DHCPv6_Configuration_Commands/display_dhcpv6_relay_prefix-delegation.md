display dhcpv6 relay prefix-delegation
======================================

display dhcpv6 relay prefix-delegation

Function
--------



The **display dhcpv6 relay prefix-delegation** command displays the DHCPv6 PD routing information forwarded by the DHCPv6 Relay.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 relay prefix-delegation** { **client** [ **interface** { *interface-type* *interface-num* | *interface-name* } ] | **route** [ **interface** { *interface-type* *interface-num* | *interface-name* } ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **client** | Displays information about DHCPv6 PD clients. | - |
| **interface** *interface-type* *interface-num* | Specifies the interface type and interface number. | - |
| *interface-name* | Specifies an interface name. | - |
| **route** | Displays routing information learned from DHCPv6 PD clients. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display dhcpv6 relay prefix-delegation command is used on DHCPv6 relay agents. This command displays routing information that DHCPv6 relay agents learn from DHCPv6 PD terminals, including the destination IPv6 address, next hop address, outbound interface, and protocol type of each route. You can also use this command to view DHCPv6 PD routing information forwarded by the DHCPv6 Relay.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about DHCPv6 PD terminals.
```
<HUAWEI> display dhcpv6 relay prefix-delegation client
--------------------------------------------------------------------------------
 DUID_EN       : 000612E978E600E04C774E5A 
 Interface     : Vlanif62        
 IPv6 address  : FC00:1::4E5A 
     IA PD     : IA ID 1, T1 600, T2 900,     
         IA Prefix: FC00:3::/96
            preferred lifetime 900 , valid lifetime 1200
            expired at 2010.02.21 15:01:54
         IA Prefix: FC00:4::/96
            preferred lifetime 900 , valid lifetime 1200
            expired at 2010.02.21 15:01:54
--------------------------------------------------------------------------------
 Total count : 1  Print count : 1

```

# Display DHCPv6 PD routing information forwarded by the DHCPv6 Relay.
```
<HUAWEI> display dhcpv6 relay prefix-delegation route
--------------------------------------------------------------------------------
 Destination   : FC00:1::/96
 Next-hop      : FC00:2::1
 Interface     : Vlanif62
 Protocol type : OPR
 Destination   : FC00:2::/96
 Next-hop      : FC00:2::2
 Interface     : Vlanif62
 Protocol type : OPR
--------------------------------------------------------------------------------
 Total count : 2  Print count : 2

```

**Table 1** Description of the **display dhcpv6 relay prefix-delegation** command output
| Item | Description |
| --- | --- |
| DUID\_EN | DHCPv6 unique identifier (DUID) of a client, which is defined by the vendor. |
| Interface | Outbound interface of a route. |
| Interface | Client access interface. |
| IPv6 address | IPv6 address of a client. |
| IA PD | IPv6 prefix contained in the packet sent from a client. |
| Total count | Number of routes displayed. |
| Print count | Number of routes printed. A maximum of 512 routes can be printed. |
| Destination | Destination network segment of a route. |
| Next-hop | Next hop address of a route. |
| Protocol type | Protocol type used by a route. |