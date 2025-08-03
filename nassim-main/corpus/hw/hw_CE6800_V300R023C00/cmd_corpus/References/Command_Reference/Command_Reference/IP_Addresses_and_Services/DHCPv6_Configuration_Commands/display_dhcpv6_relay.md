display dhcpv6 relay
====================

display dhcpv6 relay

Function
--------



The **display dhcpv6 relay** command displays the configuration of the interface enabled with the DHCPv6 relay function.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 relay** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays the configuration of the specified interface. | - |
| *interface-name* | Displays the configuration of the specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If no interface is specified, the configuration of all the interfaces enabled with the DHCPv6 relay function is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configurations of all interfaces enabled with the DHCPv6 relay function.
```
<HUAWEI> display dhcpv6 relay
Interface               Mode          Destination
-------------------------------------------------------------------------
100GE1/0/1            Relay            FC00:4::3
Vlanif10              Relay            FC00:1::1:1
--------------------------------------------------------------------------------
 Print count : 2                    Total count : 2

```

**Table 1** Description of the **display dhcpv6 relay** command output
| Item | Description |
| --- | --- |
| Interface | Interface enabled with DHCPv6 relay functions. |
| Mode | DHCPv6 function mode. |
| Destination | Destination address of DHCPv6 relay messages.  Address pointing to the DHCPv6 server, address of the next-hop DHCPv6 relay, or DHCPv6 server group.  To configure the address, run the dhcpv6 relay destination or dhcpv6 relay server-select command. |
| Print count | The number of interfaces enabled with DHCPv6 relay functions that are displayed. |
| Total count | The total number of interfaces enabled with DHCPv6 relay functions. |