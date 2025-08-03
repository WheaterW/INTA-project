display dhcpv6 relay configuration
==================================

display dhcpv6 relay configuration

Function
--------



The **display dhcpv6 relay configuration** command displays configuration information about a DHCPv6 relay agent.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 relay configuration** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays configuration information about the DHCPv6 relay agent with the specified interface type and number. | - |
| *interface-name* | Displays configuration information about the DHCPv6 relay agent with the specified interface name. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command on a DHCPv6 relay agent to check configuration information about a DHCPv6 relay agent including the source interface information and whether the Option79 field is inserted into DHCP messages.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configuration information about a DHCPv6 relay agent.
```
<HUAWEI> display dhcpv6 relay configuration
DHCPv6 relay running information: global
Source interface:       -
Option79 insert:        enable
DHCPv6 relay running information: Vlanif10
Source interface:       -
Option79 insert:        enable
Vss-control insert:     disable

```

**Table 1** Description of the **display dhcpv6 relay configuration** command output
| Item | Description |
| --- | --- |
| DHCPv6 relay running information | Configuration information about a DHCPv6 relay agent, including configuration information in the global view and interface view. |
| Source interface | Specifies the interface IPv6 address as the source IPv6 address for sending messages.  To configure this item, run the dhcpv6 relay source-interface command. |
| Option79 insert | Whether to insert the Option79 field into DHCPv6 messages. The value can be:   * enable: The Option79 field is inserted into DHCPv6 messages. * disable: The Option79 field is not inserted into DHCPv6 messages.   To configure this item, run the dhcpv6 relay option79 insert enable command. |
| Vss-control insert | Whether to insert the Vss-control field into DHCPv6 messages. The value can be:   * enable: The Vss-control field is inserted into DHCPv6 messages. * disable: The Vss-control field is not inserted into DHCPv6 messages.   To configure this item, run the dhcpv6 relay vss-control insert enable command. |