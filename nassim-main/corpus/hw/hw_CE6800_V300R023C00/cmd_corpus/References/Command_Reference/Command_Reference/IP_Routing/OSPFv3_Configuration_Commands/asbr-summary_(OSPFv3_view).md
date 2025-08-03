asbr-summary (OSPFv3 view)
==========================

asbr-summary (OSPFv3 view)

Function
--------



The **asbr-summary** command configures an ASBR to summarize routes imported by OSPFv3.

The **undo asbr-summary** command cancels the configuration of enabling an ASBR to summarize routes imported by OSPFv3.



By default, an ASBR does not summarize routes imported by OSPFv3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**asbr-summary** *ipv6-address* *prefix-length* [ **not-advertise** | [ **tag** *tag-value* ] | [ **cost** *cost-value* ] | [ **distribute-delay** *interval* ] ] \*

**undo asbr-summary** *ipv6-address* *prefix-length*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a summary route. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of a summary route. | The value is an integer ranging from 1 to 128. |
| **not-advertise** | Prevents the summary route with the specified IPv6 prefix length from being advertised. | By default, the summary route with the specified IPv6 prefix length is advertised. |
| **tag** *tag-value* | Specifies the tag used to control summary route advertisement. | The value is an integer ranging from 0 to 4294967295. |
| **cost** *cost-value* | Specifies the cost of a summary route. | The value is an integer that ranges from 1 to 16777214.  By default:   * For Type 1 external routes, the largest cost of the specific routes is used as the cost of the summary route. * For Type 2 external routes, the cost of the summary route is the maximum cost of the specific routes plus 1. |
| **distribute-delay** *interval* | Specifies the delay for advertising a summary route. | The value is an integer ranging from 1 to 65535, in seconds. This parameter has no default value. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Routes with the same IPv6 prefix can be summarized into a single route. On a large-scale OSPFv3 network, route lookup may slow down because of the large size of the routing table. To reduce the routing table size and simplify management, configure route summarization. Route summarization also prevents route flapping and improves network stability. If a link associated with a summary IPv6 address prefix frequently alternates between up and down, this function prevents the changes from being advertised to devices whose IPv6 addresses do not belong to the prefix of the summary route. If route summarization is configured on an ASBR using the **asbr-summary** command, the ASBR summarizes routes of all imported Type 5 LSAs within the summary address range. If a large number of routes with the same IPv6 prefix are imported, you can run the **asbr-summary** command to summarize them into one route.When a large number of summary routes exist, specify the distribute-delay parameter to set a delay in advertising the summary routes. This ensures that the advertised summary routes contain more valid routes and avoids network flapping and incorrect routing information.When OSPFv3 imports external routes and specific routes have been advertised, if the distribute-delay parameter is specified in the **asbr-summary** command, the specific routes are not withdrawn immediately. After the delay expires, the specific routes are withdrawn and the summary route is advertised.If the distribute-delay parameter is specified in the **asbr-summary** command for OSPFv3 route summarization and then external routes are imported, specific routes and the summary route are not advertised before the delay expires. The summary route is advertised only after the delay expires.

**Precautions**

This command applies only to ASBRs and is used to summarize routes imported by OSPFv3. The **abr-summary** command configures route summarization on an area border router (ABR).When the summarized route changes, the cost of the summary LSA may change, triggering route update. In specific scenarios, routing microloops may be triggered, causing temporary service interruptions. To prevent this problem, specify a fixed cost value when configuring summarization.After the imported routes are summarized, the following situations occur:

* If the local device is an ASBR in a common area, the local device summarizes all imported Type 5 LSAs within the summary address range.
* If the local device is an ASBR in an NSSA, the local device summarizes all imported Type 7 LSAs within the summary address range.
* If the local device functions as both an ASBR and an ABR in an NSSA, the local device summarizes routes of all imported Type 5 and Type 7 LSAs within the summary address range, but does not summarize routes of Type 5 LSAs translated from Type 7 LSAs.

The metric type and cost of the LSA generated after route summarization are as follows:

* If the routes to be summarized have both metric type 1 and metric type 2 or have only metric type 2, the metric type of the LSA generated after summarization is 2. If the cost value is not specified, the cost value is the maximum cost value of the summarized LSAs with metric type 2 plus 1.
* If the LSAs to be summarized have only metric type 1, the metric type of the LSA generated after summarization is 1. If the cost value is not specified, the maximum cost value of the LSAs with metric type 1 is used as the cost value.
* If the summarized LSAs contain both Type 5 LSAs and Type 5 LSAs converted from Type 7 LSAs, the metric type and cost of the summarized LSAs are obtained from the summarized Type 5 LSAs.
* Only when only Type 5 LSAs converted from Type 7 LSAs exist, the metric type and cost of the LSA generated after summarization are obtained from Type 5 LSAs converted from Type 7 LSAs.

Example
-------

# Configure an ASBR to summarize two imported OSPFv3 routes into a route with cost 20 and tag 100.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] asbr-summary 2001:db8:1::1 16 cost 20 tag 100

```