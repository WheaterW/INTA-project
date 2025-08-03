asbr-summary
============

asbr-summary

Function
--------



The **asbr-summary** command configures an AS boundary router (ASBR) to summarize routes imported by OSPF.

The **undo asbr-summary** command disables ASBRs from summarizing routes imported by OSPF.



By default, ASBRs do not summarize routes imported by OSPF.


Format
------

**asbr-summary** *ip-address* *mask* [ [ **not-advertise** | **generate-null0-route** ] | **tag** *tag-value* | **cost** *cost-value* | **distribute-delay** *interval* ] \*

**undo asbr-summary** *ip-address* *mask*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a summary route. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of the IP address of the summary route. | The value is in dotted decimal notation. |
| **not-advertise** | Prevents the summary route from being advertised.  If this parameter is not specified, the summary route is advertised. | - |
| **generate-null0-route** | Generates a black-hole route in the RM module to prevent routing loops. | - |
| **tag** *tag-value* | Specifies the tag of the summary route. | The value is an integer ranging from 0 to 4294967295. |
| **cost** *cost-value* | Specifies the cost of the summary route. | The value is an integer ranging from 0 to 16777214.  By default:   * For Type 1 external routes, the largest cost of the routes for summarization is used as the cost of the summary route. * For Type 2 external routes, the largest cost of the routes for summarization plus 1 is used as the cost of the summary route. |
| **distribute-delay** *interval* | Specifies the delay for advertising the summary route. | The value is an integer ranging from 1 to 65535. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a large-scale OSPF network is deployed, the route search speed may be slowed down because the size of the OSPF routing table is too large. To solve this problem, you can configure route summarization to reduce the size of the routing table and simplify management.Route summarization allows multiple routes with the same IP prefix to be summarized into one route. If a link within the summary IP address range frequently alternates between Up and Down, the change is not advertised to the devices beyond the summary IP address range. This prevents route flapping on the network and improves network stability.If the imported routes have the same prefix, you can run the **asbr-summary** command to summarize these routes and advertise them as one summary route. Route summarization reduces the size of a routing table and improves device performance.

**Precautions**

* When there are a large number of summary routes, you can configure the distribute-delay parameter to set the delay for advertising the summary routes. This ensures that the summary routes advertised each time contain more valid routes, preventing inaccurate routing information caused by network flapping.
* Route summarization takes effect only when the imported routes are within the summary network segment configured on the device. If generate-null0-route is specified when route summarization takes effect, a blackhole route is generated, and the blackhole route has a higher priority than the Type 5 and Type 7 LSAs received from other devices.
* After the imported routes are summarized, the following situations occur:
* If the local device is an ASBR in a common area, the local device summarizes all imported Type 5 LSAs within the summarized address range.
* If the local device is an ASBR in an NSSA, the local device summarizes all imported Type 7 LSAs within the summarized address range.
* If the local device functions as both an ASBR and an ABR in an NSSA, the local device summarizes all imported Type 5 and Type 7 LSAs within the summarized address range and also summarizes Type 5 LSAs translated from Type 7 LSAs.
* When a summarized route changes, the cost of the summary LSA may change, triggering route update. In specific scenarios, routing microloops may be triggered, causing temporary service interruptions. To prevent this problem, specify a fixed cost value when configuring summarization.
* The metric type and cost of the LSA generated after route summarization are as follows:
* If the summarized routes have both metric type 1 and metric type 2 or have only metric type 2, the metric type of the LSA generated after summarization is 2. When the cost value is not specified in the command, the cost value is the maximum cost value of the summarized routes with metric type 2 plus 1.
* If the summarized routes have only metric type 1, the metric type of the LSA generated after summarization is 1. If the cost value is not specified in the command, the maximum cost value of the LSA with metric type 1 is used as the cost value.
* If the summarized routes contain both Type 5 routes and the Type 5 routes converted from Type 7 routes, the metric type and cost of the LSA generated after summarization are obtained from the summarized Type 5 LSA.
* If only Type 5 routes converted from Type 7 LSAs exist, the metric type and cost of the summarized LSA are obtained from the Type 5 LSAs converted from the summarized Type 7 LSAs.

Example
-------

# Configure route summarization for imported routes.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] asbr-summary 10.2.0.0 255.255.0.0 not-advertise tag 2 cost 100

```