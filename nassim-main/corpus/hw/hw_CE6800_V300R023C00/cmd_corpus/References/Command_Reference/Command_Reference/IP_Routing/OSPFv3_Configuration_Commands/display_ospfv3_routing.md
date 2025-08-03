display ospfv3 routing
======================

display ospfv3 routing

Function
--------



The **display ospfv3 routing** command displays the OSPFv3 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **routing** { **abr-routes** | **asbr-routes** } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPFv3 process ID. | The value is an integer ranging from 1 to 4294967295. |
| **abr-routes** | Displays the routing table of an ABR. | - |
| **asbr-routes** | Displays routing table of an ASBR. | - |
| **verbose** | Displays detailed information about OSPFv3 routes. | - |



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
   2001:DB8:1::/64                                                3124
     via FE80::1441:0:E213:1, 100GE1/0/1, Flags :A
     Priority      :Low

```

# Display detailed information about the OSPFv3 routing table.
```
<HUAWEI> display ospfv3 routing verbose

Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6, LT - Locator Routing

OSPFv3 Process (1)
Destination   :2001:DB8::                     Prefix Length    :96
Metric        :1                              Type             :INTRA-AREA
Nexthop       :directly connected             Nexthop Interface:100GE1/0/1
Flags         :A
Priority      :Low                            Age              :20h05m58s

```

# Display routing information about the OSPFv3 NSSA.
```
<HUAWEI> display ospfv3 routing abr-routes
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6

OSPFv3 Process (1)
     Destination                                                         Metric
       Next-hop
E2   2001:DB8:6::1/128                                                   1
N      via FE80::3A6D:7CFF:FE61:1200, Vlanif13, Flags : A

```

**Table 1** Description of the **display ospfv3 routing** command output
| Item | Description |
| --- | --- |
| Codes | The following is the explanation of the abbreviations:   * E2: Type 2 external route. * E1: Type 1 external route. * IA: inter-area route. * N: NSSA route. |
| OSPFv3 Process | OSPFv3 process. |
| Destination | Destination address. |
| Metric | Cost to the destination. |
| Nexthop | Next hop to the destination. |
| Nexthop Interface | Next-hop outbound interface to the destination. |
| via | Link-local address of the next hop. |
| Flags | Route information flag.  A: The route is added to the IPv6 unicast routing table. |
| Priority | OSPFv3 convergence priority:   * Critical. * High. * Medium. * Low. |
| Prefix Length | Prefix length of an IPv6 address. |
| Age | The time difference between the last update and the current time. |