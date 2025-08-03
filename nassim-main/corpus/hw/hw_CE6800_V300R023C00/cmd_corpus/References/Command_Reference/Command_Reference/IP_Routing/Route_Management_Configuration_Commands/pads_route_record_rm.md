pads route record rm
====================

pads route record rm

Function
--------



The **pads route record rm** command configures the percentage of the maximum number of BGP prefix records that can be recorded for PADS.



By default, the percentage of the maximum number of prefixes recorded by BGP is 100%.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**pads route record rm** { **ipv4** | **ipv6** } **protocol** **bgp** **percent** *percent-number*

**undo pads route record rm** { **ipv4** | **ipv6** } **protocol** **bgp** **percent** [ *percent-number* ]

For CE6885-LL (low latency mode):

**pads route record rm ipv4 protocol bgp percent** *percent-number*

**undo pads route record rm ipv4 protocol bgp percent** [ *percent-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv4** | Configures an IPv4 address family. | - |
| **ipv6** | Configures an IPv6 address family.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **protocol** | Configures a specific routing protocol. | - |
| **bgp** | Configures BGP. | - |
| **percent** *percent-number* | Specifies the percentage of the maximum number of prefix records recorded by BGP. | The value is an integer ranging from 1 to 99, in percentage. The default value is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **pads diagnose route record rm** command displays the route change track recorded by PADS, which helps locate routing loops, check the source of abnormal routes, and determine the correct service path. You can run the **pads route record rm** command to set the percentage of the maximum number of BGP prefix records recorded by PADS.

**Precautions**

If the configured percentage is smaller than the current one, all data in the current PADS record is deleted.


Example
-------

# Set the percentage of the maximum number of prefixes recorded in the BGP IPv4 address family to 80 for PADS.
```
<HUAWEI> system-view
[~HUAWEI] pads route record rm ipv4 protocol bgp percent 80

```