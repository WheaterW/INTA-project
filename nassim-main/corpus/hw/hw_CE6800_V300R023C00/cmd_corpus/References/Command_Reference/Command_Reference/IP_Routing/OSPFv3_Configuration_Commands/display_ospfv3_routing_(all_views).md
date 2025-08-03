display ospfv3 routing (all views)
==================================

display ospfv3 routing (all views)

Function
--------



The **display ospfv3 routing** command displays the OSPFv3 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **routing** [ [ *ipv6-address* *prefix-length* ] | **ase-routes** | **inter-routes** | **intra-routes** | **nssa-routes** ] [ **verbose** ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]

**display ospfv3** [ *process-id* ] **routing** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length. | It is an integer ranging from 0 to 128. |
| **ase-routes** | Displays the statistics of OSPFv3 AS external routes. | - |
| **inter-routes** | Displays the statistics of OSPFv3 inter-area routes. | - |
| **intra-routes** | Displays the statistics of OSPFv3 intra-area routes. | - |
| **nssa-routes** | Displays the statistics of OSPFv3 NSSA routes. | - |
| **verbose** | Displays detailed information about OSPFv3 routes. | - |
| **age** | Displays the LSAs that age in the scope. | - |
| **min-value** *min-age-value* | Displays OSPFv3 routing table information with the aging time greater than or equal to min-age-value. | The value is an integer ranging from 0 to 4294967295. |
| **max-value** *max-age-value* | Displays OSPFv3 routing table information with the aging time less than or equal to max-age-value. | The value is an integer ranging from 0 to 4294967295. |
| **statistics** | Displays all routes in the OSPFv3 routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view information about the OSPFv3 routing table, run the display ospfv3 routing command. The command output helps you troubleshoot OSPFv3 faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the OSPFv3 routing table.
```
<HUAWEI> display ospfv3 routing
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
         N - NSSA
 Flags: A - Added to URT6, LT - Locator Routing

 OSPFv3 Process (1)
   Destination                                                    Metric
     Nexthop
   2001:DB8:1::/64                                                      3124
     via FE80::1441:0:E213:1, 100GE1/0/1, Flags :A
     Priority      :Low

```

# Display routing information about the OSPFv3 NSSA.
```
<HUAWEI> display ospfv3 routing nssa-routes
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6

OSPFv3 Process (1)
     Destination                                                         Metric
       Next-hop
E2   2001:DB8:6::1/128                                                        1
N      via FE80::3A6D:7CFF:FE61:1200, Vlanif13, Flags : A

```

**Table 1** Description of the **display ospfv3 routing (all views)** command output
| Item | Description |
| --- | --- |
| Codes | The following is the explanation of the abbreviations:   * E2: Type 2 external route. * E1: Type 1 external route. * IA: inter-area route. * N: NSSA route. |
| OSPFv3 Process | OSPFv3 process ID. |
| Destination | Destination addresses. |
| Metric | Cost to the destination. |
| Nexthop | Next hop to the destination. |
| via | Link-local address of the next hop. |
| Flags | Routing information flag.  A: Indicates that the route is added to the IPv6 unicast routing table.  LT: locator route. |
| Priority | OSPFv3 convergence priority:   * Critical. * High. * Medium. * Low. |
| Next-hop | Next hop to the destination. |