display multicast ipv6 statistics
=================================

display multicast ipv6 statistics

Function
--------



The **display multicast ipv6 statistics** command displays IPv6 PIM entry restriction and statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display multicast ipv6 global** { **pim** **sm** | **all** } **statistics**

**display multicast ipv6** { **all-instance** | **vpn-instance** *vpn-instance-name* } **pim** **sm** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **pim** | Specifies pim protocol. | - |
| **sm** | Specifies sm protocol. | - |
| **all** | Specifies all protocol. | - |
| **global** | Specify global configuration. | - |
| **all-instance** | Indicates all VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check limits and statistics on PIM-SM entries in the IPv6 address family of a specified VPN instance or all VPN instances, run the **display multicast ipv6 pim sm statistics** command.To check PIM entry restriction and statistics in IPv6 PIM-SM mode, run the display multicast ipv6 global pim sm statistics command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display PIM entry restriction and statistics in IPv6 PIM-SM mode.
```
<HUAWEI> display multicast ipv6 global pim sm statistics
------------------------------------------------------------------
PIM-SM        Number        Limit         Threshold(Upper%/Lower%)
------------------------------------------------------------------
(*, G)        0             --            --                      
(S, G)        0             1000          80/70                   
------------------------------------------------------------------

```

# Display limits and statistics on PIM-SM entries in the IPv6 address family of a VPN instance named vpn1.
```
<HUAWEI> display multicast ipv6 vpn-instance vpn1 pim sm statistics
VPN-Instance: vpn1
------------------------------------------------------------------
PIM-SM        Number        Limit         Threshold(Upper%/Lower%)
------------------------------------------------------------------
(*, G)        3             2000          80/71                   
(S, G)        5             1000          80/71   
-----------------------------------------------------------------

```

**Table 1** Description of the **display multicast ipv6 statistics** command output
| Item | Description |
| --- | --- |
| PIM-SM | Type of PIM-SM entry for which a limit takes effect. The value can be (\*, G) or (S, G). |
| Number | Number of created PIM entries. |
| Limit | Limit on the number of PIM entries. If no limit is set, -- is displayed. |
| Threshold(Upper%/Lower%) | Upper and lower thresholds for PIM entry alarms. If they are not set, -- is displayed. |
| VPN-Instance | Name of a VPN instance. |