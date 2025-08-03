display ipv6 pathmtu
====================

display ipv6 pathmtu

Function
--------



The **display ipv6 pathmtu** command displays all IPv6 PMTU entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 pathmtu** [ **vpn-instance** *vpn-instance-name* ] { *ipv6-address* | **all** | **dynamic** | **static** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays PMTU entries with a specified IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv6-address* | Displays PMTU entries with a specified IPv6 address. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **all** | Displays all PMTU entries. | - |
| **dynamic** | Displays all dynamic PMTU entries. | - |
| **static** | Displays all static PMTU entries. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

When the MTU of the outbound interface on an intermediate device is smaller than the MTU of the source host, the PMTU discovery mechanism is used to determine the maximum size of packets that can be transmitted on the path, that is, a PMTU.To check dynamic and static PMTU entries, run the **display ipv6 pathmtu** command. The Router fragments packets into a size smaller than a set PMTU and forwards the fragments.

**Precautions**



If no PMTU is set using the **ipv6 pathmtu** command, no static PMTU entries are displayed in the **display ipv6 pathmtu** command output.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display PMTU entries of vpn1.
```
<HUAWEI> display ipv6 pathmtu vpn-instance vpn1 all
Total: 2        Dynamic: 1      Static: 1
- ----------------------------------------------------------------------------
IPv6 Destination Address                 ZoneID  PathMTU  LifeTime(M)  Type     Fragment Flag
2001:DB8::4                                   1     1500           10  Dynamic  NO
2001:DB8::3                                   1     1600  -            Static   NO

```

# Display all PMTU entries.
```
<HUAWEI> display ipv6 pathmtu all
Total: 2        Dynamic: 1      Static: 1
- ----------------------------------------------------------------------------
IPv6 Destination Address                 ZoneID  PathMTU  LifeTime(M)  Type     Fragment Flag
2001:DB8::2                                   0     1300           9   Dynamic  NO
2001:DB8::1                                   0     1500  -            Static   NO

```

**Table 1** Description of the **display ipv6 pathmtu** command output
| Item | Description |
| --- | --- |
| IPv6 Destination Address | IPv6 destination address. |
| ZoneID | Zone of an IPv6 address. |
| PathMTU | PMTU of an IPv6 address. |
| LifeTime(M) | Remaining lifetime of a dynamic PMTU entry, in minutes.  This field displays a hyphen (-) for a static PMTU entry. |
| Type | Type of a PMTU:   * Dynamic. * Static. |
| Fragment Flag | Fragmentation flag:   * YES: Packets are fragmented, and a fragment header is added to a packet. * NO: Packets are not fragmented. |
| Dynamic | Number of dynamic PMTU entries. |
| Static | Number of static PMTU entries. |
| Total | Total number of PMTU entries. |