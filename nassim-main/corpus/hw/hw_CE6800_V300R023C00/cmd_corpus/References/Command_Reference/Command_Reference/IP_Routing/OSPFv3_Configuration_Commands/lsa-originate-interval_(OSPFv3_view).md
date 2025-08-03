lsa-originate-interval (OSPFv3 view)
====================================

lsa-originate-interval (OSPFv3 view)

Function
--------



The **lsa-originate-interval** command sets the interval at which OSPFv3 LSAs are updated.

The **undo lsa-originate-interval** command restores the default setting.



By default, the intelligent timer is enabled; the maximum interval at which LSAs are updated is 5000 ms, the initial interval is 500 ms, and the holding interval is 1000 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**lsa-originate-interval** { **0** | **intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **other-type** *interval* ] | **other-type** *interval* [ **intelligent-timer** *max-interval* *start-interval* *hold-interval* ] }

**undo lsa-originate-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **0** | Set the interval at which OSPFv3 LSAs are updated to 0 ms. | - |
| **intelligent-timer** | Sets the interval for updating OSPFv3 Type 1 LSAs (Router-LSAs), Type 2 LSAs (Network-LSAs), Type 5 LSAs (AS-external-LSAs), Type 7 LSAs (NSSA-LSAs), Type 8 LSAs (Link-LSAs), and Type 33 LSAs (E-Router-LSAs) through an intelligent timer. | - |
| *max-interval* | Specifies the maximum interval at which OSPFv3 LSAs are updated. | The value is an integer ranging from 1 to 120000, in milliseconds. |
| *start-interval* | Specifies the initial interval at which OSPFv3 LSAs are updated. | The value is an integer ranging from 0 to 60000, in milliseconds. |
| *hold-interval* | Specifies the holding interval at which OSPFv3 LSAs are updated. | The value is an integer ranging from 1 to 60000 in milliseconds. |
| **other-type** *interval* | Specifies the interval for OSPFv3 Type 3 LSAs (Inter-Area-Prefix-LSAs), Type 4 LSAs (Inter-Area-Router-LSAs), Type 9 LSAs (Intra-Area-Prefix-LSAs), Type 10 LSAs (Intra-Area-TE-LSAs), and Type 42 LSAs (SRv6 Locator LSAs). | The value is an integer ranging from 0 to 10, in seconds. The default value is 5. |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent excessive consumption of network bandwidth and device resources due to network connections or frequent route flapping on a stable network that requires fast route convergence, you can run the intelligent-timer command to set the interval for updating LSAs, in milliseconds. In this manner, topology or route changes can be immediately advertised to the network through LSAs, speeding up route convergence on the network.Due to the timer restriction, when the configured interval is less than 100 ms, the interval is updated based on 100 ms.

**Implementation Procedure**

* When lsa-originate-interval 0 is configured, the interval is not adjusted.
* The maximum age of LSAs (except inter-area-prefix LSAs, external LSAs, and E-external LSAs) is not adjusted.
* If both this command and the lsa-originate-interval suppress-flapping command are configured and the interval needs to be adjusted using both commands, the device uses the larger value as the flapping suppression time.
* The rules for processing the LSA interval of the intelligent timer are as follows:LSA interval. If the interval is greater than max-interval, the interval is not adjusted. The number of LSA updates is cleared.Interval for generating LSAs. If the interval is shorter than the specified interval, the system attempts to generate LSAs after the specified interval and increases the number of LSA updates by 1.The interval for sending LSAs is set as follows:a. The initial interval for updating LSAs is specified by start-interval.b. For the nth (nâ¥2) time, when hold-interval x 2^(n-2) is smaller than max-interval, the interval for updating LSAs is equal to hold-interval x 2^(n-2).c. For the nth (nâ¥2) time, when hold-interval x 2^(n-2) is greater than or equal to max-interval and the interval for updating LSAs is max-interval, OSPF updates LSAs at max-interval for three consecutive times. Then, go back to Step a, LSAs are updated at the initial interval specified by start-interval.
* Intelligent timer. When processing router LSAs at a specified interval, the intelligent timer adjusts configuration parameters based on the number and status of neighbors.If the number of neighbors in Exchange or Loading state is greater than 5 and the number of neighbors in Full state is greater than 10, the rules for adjusting max-interval, hold-interval, and max-interval are as follows:If the number of full neighbors ranges from 11 to 100, set hold-interval to 10s and max-interval to 20s.If the number of full neighbors ranges from 101 to 500, set hold-interval to 20s and max-interval to 40s.If the number of full neighbors is greater than 500, set hold-interval to 30s and max-interval to 60s.
* Rules for processing the interval of other-type LSAs:If other-type interval is set to 0, the interval is not adjusted.If the interval for generating LSAs is shorter than the value of other-type interval, no LSA is generated. Instead, LSA generation is delayed based on the calculated remaining interval.

Example
-------

# Set the maximum interval at which OSPFv3 LSAs are updated to 10000 ms, the initial interval to 700 ms, and the hold interval to 4000 ms.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] lsa-originate-interval intelligent-timer 10000 700 4000

```