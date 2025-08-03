abr-summary (OSPFv3 area view)
==============================

abr-summary (OSPFv3 area view)

Function
--------



The **abr-summary** command configures route summarization on an area border router (ABR).

The **undo abr-summary** command disables route summarization from an ABR.



By default, route summarization is not configured on ABRs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**abr-summary** *ipv6-address* *prefix-length* [ **not-advertise** | **cost** *cost-value* ] \*

**undo abr-summary** *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a summary route. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of a summary route. | The value is an integer ranging from 1 to 128. |
| **not-advertise** | Prevents the summary route with the specified IPv6 prefix length from being advertised. | By default, the summary route with the specified IPv6 prefix length is advertised. |
| **cost** *cost-value* | Specifies the cost of a summary route. | The value is an integer ranging from 0 to 16777214.  By default, the largest cost of the specific routes for summarization is used as the cost of the summary route. |



Views
-----

OSPFv3 area view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Routes with the same IPv6 prefix can be summarized into one route. On a large-scale OSPFv3 network, route lookup may slow down because of the large size of the routing table. To reduce the routing table size and simplify management, configure route summarization. With route summarization, if a link connected to a device within an IPv6 address range that has been summarized alternates between Up and Down, the link status change is not advertised to the devices beyond the IPv6 address range. This prevents route flapping and improves network stability.To configure route summarization on an ABR, run the **abr-summary** command. When an ABR transmits routing information to other areas, it generates Type 3 LSAs for each network segment. If contiguous segments exist in this area, run the **abr-summary** command to summarize these segments into one segment so that the ABR sends only one summarized LSA. The summarization reduces the routing table size and improves device performance.

**Precautions**

This command applies only to ABRs and is used to summarize routes in an area. The **asbr-summary** command configures an AS boundary router (ASBR) to summarize routes imported by OSPFv3.

When the summarized route changes, the cost of the summary LSA may change, triggering route update. In specific scenarios, routing microloops may be triggered, causing temporary service interruptions. To prevent this problem, specify a fixed cost value when configuring summarization.

After routes are summarized:

* If the local device is a non-PE, the local device summarizes all intra-area routes within the summary address range configured using the command. The cost of the LSA generated after summarization is the largest cost of the summarized routes.
* If the local device is a PE and the command is configured in the backbone area:
* If BGP route import is configured and the cost value is set to inherit the minimum value (inherit-minimum), all Type 3 LSAs within the summary address range generated when BGP routes are imported are summarized, and the cost value of the LSA generated for the backbone area is the smallest cost value of the summarized routes.
* If BGP route import is configured and inherit-minimum is not specified, all Type 3 LSAs within the summary address range generated when BGP routes are imported are summarized, and the maximum cost of the summarized routes is used as the cost of the LSA generated for the backbone area.
* If intra-area routes within the summary address range exist in the backbone area, the maximum cost of all summarized routes is used as the cost of LSAs generated for areas outside the backbone area.
* If a cost value is specified, the cost value of the LSA generated after summarization is the configured value.

Example
-------

# In OSPFv3 area 1, summarize routes 2001:db8:1:1::/64 and 2001:db8:1:2::/64 into route 2001:db8:1::/48 with cost 400, and advertise the summarized route to other areas.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] area 1
[*HUAWEI-ospfv3-1-area-0.0.0.1] abr-summary 2001:db8:1:: 48 cost 400

```