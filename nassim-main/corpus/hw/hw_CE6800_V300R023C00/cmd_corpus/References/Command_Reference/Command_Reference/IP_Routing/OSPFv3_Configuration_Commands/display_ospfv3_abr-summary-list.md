display ospfv3 abr-summary-list
===============================

display ospfv3 abr-summary-list

Function
--------



The **display ospfv3 abr-summary-list** command displays information about OSPFv3 summary routes on an area border router (ABR).

The **display ospfv3 asbr-summary** command displays information about OSPFv3 summary routes on an AS boundary router (ASBR).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **abr-summary-list** [ *prefix* *prefix-length* ]

**display ospfv3** [ *process-id* ] **asbr-summary** [ *prefix* *prefix-length* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about summary routes in the specified OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |
| *prefix* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format X:X::X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | It is an integer ranging from 0 to 128. |
| **verbose** | Displays detailed information about OSPFv3 summary routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Route summarization reduces the amount of routing information transmitted between areas in an AS and the routing table size and improves device performance.After route summarization is configured using the **abr-summary** or **asbr-summary** command, you can run the **display ospfv3 abr-summary-list** or **display ospfv3 asbr-summary** command to check information about route summarization and detailed information about summary routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPFv3 summarized routes on an ASBR.
```
<HUAWEI> display ospfv3 asbr-summary

OSPFv3 Process (1)
 Prefix                                 Prefix-Len   Matched          Status        
 2001:DB8::                                 32           3 [Active]       Advertised

```

# Display information about OSPFv3 summary routes on an ABR.
```
<HUAWEI> display ospfv3 abr-summary-list

OSPFv3 Process (1)
Area ID  :  0.0.0.1
 Prefix                                 Prefix-Len   Matched          Status        
 2001:DB8::                             32           1 [Active]       Advertised

```

# Display detailed information about OSPFv3 summary routes on an ASBR.
```
<HUAWEI> display ospfv3 asbr-summary verbose

 OSPFv3 Process (1)
 Total summary address count: 1

                 Summary Address

 Prefix         : 2001:DB8::
 Prefix length  : 32
 Tag            : 1 (Not Configured)
 Status         : Advertised
 Cost           : 2 (Not Configured)
 Delay          : 0 (Not Configured)
 Type           : 2 (Larger than any link state path)

 The Count of Route is: 3

 Destination                             Mask       Protocol   Proc       Type       Metric    
 2001:DB8:2::1                           128        Static     0          2          1         
 2001:DB8:3::1                           128        Static     0          2          1         
 2001:DB8:4::1                           128        Static     0          2          1

```

**Table 1** Description of the **display ospfv3 abr-summary-list** command output
| Item | Description |
| --- | --- |
| OSPFv3 Process (1) | OSPFv3 process ID. |
| Prefix | Prefix of a summary route. |
| Prefix length | Length of prefix. |
| Prefix-Len | Length of prefix. |
| Matched | Status of a summary route. |
| Status | Whether a summary route is advertised:   * Advertised: yes. * NotAdvertise: no. |
| Area ID | Area ID. |
| Total summary address count | Number of routes summarized using the asbr-summary command. |
| Summary Address | Detailed information about a summary route. |
| Tag | Tag of a summary route.   * Configured: A tag is configured for the summary route. * Not Configured: No tag is configured for the summary route. |
| Cost | Cost of the summary route. |
| Delay | Delay for advertising a summary route. |
| Type | Type of AS external routes:   * 1: Type-1. * 2: Type-2. |
| The Count of Route is | Number of summarized routes. |
| Destination | Destination IP address of the summary route. |
| Mask | Mask of the summary route. |
| Protocol | Protocol of a summary route. |
| Proc | ID of the protocol to which a summary route belongs. |
| Metric | Cost of summary route. |