display bgp ipv6 routing-table statistics
=========================================

display bgp ipv6 routing-table statistics

Function
--------



The **display bgp ipv6 routing-table statistics** community command displays statistics about the routing information of the specified BGP4+ routes in the public routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp ipv6 routing-table statistics active**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **active** | Specifies the number of active routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can specify different parameters to view the specific routing information.

**Precautions**

During route flapping, the route statistics may differ from the actual number of routes on the network because some routes are still on the way.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about active BGP4+ routes.
```
<HUAWEI> display bgp ipv6 routing-table statistics active
Total Number of Prefix Advertised to RM : 2
Total Number of Active Route : 2

```

**Table 1** Description of the **display bgp ipv6 routing-table statistics** command output
| Item | Description |
| --- | --- |
| Total Number of Prefix Advertised to RM | Total number of routes delivered to the RM module. |
| Total Number of Active Route | Number of active routes. |