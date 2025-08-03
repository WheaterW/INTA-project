display isis route
==================

display isis route

Function
--------



The **display isis route** command displays IS-IS routes.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display isis route** [ *process-id* | **vpn-instance** *vpn-instance-name* ] [ **ipv4** ] [ **verbose** | [ **level-1** | **level-2** ] | *ip-address* [ *mask* | *mask-length* ] ] \*

**display isis** *process-id* **route** [ **ipv4** ] [ *ip-address* [ *mask* | *mask-length* ] | { **level-1** | **level-2** } | **verbose** ] \*

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display isis route** [ *process-id* | **vpn-instance** *vpn-instance-name* ] **ipv6** [ **verbose** | [ **level-1** | **level-2** ] | *ipv6-address* [ *prefix-length* ] ] \*

**display isis** *process-id* **route** **ipv6** [ *ipv6-address* [ *prefix-length* ] | { **level-1** | **level-2** } | **verbose** ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays IS-IS routes of a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **ipv4** | Displays IPv4 routes. | - |
| **verbose** | Displays detailed information about IS-IS routes. | - |
| **level-1** | Displays IS-IS Level-1 routes. | - |
| **level-2** | Displays IS-IS Level-2 routes. | - |
| *ip-address* | Specifies the IP address in dotted decimal notation. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of the IPv4 address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of the IPv4 address. | The value is an integer ranging from 0 to 32. |
| **ipv6** | Displays IPv6 routes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *ipv6-address* | Specifies the IPv6 destination address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the mask length of the IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | It is an integer ranging from 0 to 128. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view IS-IS Multicast IGP (MIGP) routing information, run the display isis migp-routing command. You can run the display isis migp-routing command to view the physical interface of the route with a TE tunnel interface as the outbound interface.A device maintains information about all locally reachable routes, such as outbound interfaces, next hops, and link costs. You can run the **display isis route** command to view the information. Based on the information, you can check the traffic forwarding paths and change the forwarding paths by adjusting link costs.

**Precautions**

If no level is specified, both Level-1 and Level-2 routes are displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IS-IS IPv4 routes.
```
<HUAWEI> display isis route ipv4
                         Route information for ISIS(1)
                         -----------------------------
                        ISIS(1) Level-1 Forwarding Table
                        --------------------------------

 IPV4 Destination     Int.Cost   Ext.Cost ExitInterface   NextHop         Flags
--------------------------------------------------------------------------------
 1.1.1.0/24           10         NULL     LoopBack1       Direct          D/-/L/-
 2.2.2.0/24           10         NULL     LoopBack2       Direct          D/-/L/-

     Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                               U-Up/Down Bit Set, LP-Local Prefix-Sid
     Protect Type: L-Link Protect, N-Node Protect


                        ISIS(1) Level-2 Forwarding Table
                        --------------------------------

 IPV4 Destination     Int.Cost   Ext.Cost ExitInterface   NextHop         Flags
--------------------------------------------------------------------------------
 1.1.1.0/24           10         NULL     LoopBack1       Direct          D/-/L/-
 2.2.2.0/24           10         NULL     LoopBack2       Direct          D/-/L/-

     Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                               U-Up/Down Bit Set, LP-Local Prefix-Sid
     Protect Type: L-Link Protect, N-Node Protect


                         Route information for ISIS(2)
                         -----------------------------
                        ISIS(2) Level-1 Redistribute Table
                        --------------------------------

 Type IPV4 Destination     IntCost    ExtCost     Tag         SID     AvoidLoopState
----------------------------------------------------------------------------------------
 I    1.1.1.1/32           0          NULL        NULL        NULL        N
 I    2.2.2.2/32           0          NULL        NULL        NULL        N

    Type: D-Direct, I-ISIS, S-Static, O-OSPF, B-BGP, R-RIP, U-UNR, OP-OPR

```

**Table 1** Description of the **display isis route** command output
| Item | Description |
| --- | --- |
| Level-1 | IS-IS Level-1 route. |
| IPV4 Destination | IPv4 destination address or mask. |
| IPV4 Dest | IPv4 destination address or mask. |
| ExitInterface | Outbound interface name. |
| NextHop | Next hop of the route. |
| Flags | Routing information flag.   * D-Direct: direct route. * A-Added to URT: The route has been added to the unicast routing table. * L-Advertised in LSPs: indicates that the route is advertised through an LSP. * S-IGP Shortcut: indicates that an IGP Shortcut-enabled interface is available on the path to the destination. * U-Up/Down Bit Set: Up/Down bit. * LP-Local Prefix-Sid: local prefix label. |
| Protect Type | ProtectType:L-Link Protect,N-Node Protect. |
| Level-2 | IS-IS Level-2 routes. |
| Type | Type of an imported route.   * D-Direct: direct route. * I-ISIS: IS-IS routes. * S-Static: static route. * O-OSPF: OSPF route. * B-BGP: BGP route. * R-RIP: RIP route. * U-UNR: UNR route. * OP-OPR: OPR route.   This field is displayed when external routes are imported using the import-route command. |
| IntCost | Internal cost, that is, the cost of an IS-IS route. |
| ExtCost | IPv4 external cost, the cost of other protocol route imported by IS-IS.  This field displays the cost of the route imported using the import-route cost-type external command. |
| Tag | Tag of imported routes. The field is displayed only after external routes are imported using the.  import-route command. |
| SID | Label value of imported routes. The field is displayed only after external routes are imported using the.  import-route command. |
| AvoidLoopState | Anti-loop alarm status of imported routes.   * Y: The imported route is in the loop prevention alarm state. * N: The imported route is not in the loop prevention alarm state. |
| Cost | IPv6 destination cost. |
| Interface | Outbound interface name. |