lsa-originate-interval
======================

lsa-originate-interval

Function
--------



The **lsa-originate-interval** command sets the interval at which LSAs are updated.

The **undo lsa-originate-interval** command restores the default configuration.



By default, the intelligent timer is enabled; the maximum interval at which LSAs are updated is 5000 ms, the initial interval is 500 ms, and the Holdtime interval is 1000 ms.For Type-3,Type-4 and Type-10 LSAs, the default interval is 5s.


Format
------

**lsa-originate-interval** { **0** | **intelligent-timer** *max-interval* *start-interval* *hold-interval* [ **other-type** *interval* ] | **other-type** *interval* [ **intelligent-timer** *max-interval* *start-interval* *hold-interval* ] }

**undo lsa-originate-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **0** | Sets the interval at which LSAs are updated to 0 ms, that is, deletes the initial interval (5s) for updating LSAs. | - |
| **intelligent-timer** | Uses an intelligent timer to set the interval for updating OSPF Type 1 LSAs (Router-LSAs), Type 2 LSAs (Network-LSAs), Type 5 LSAs (AS-External-LSAs), Type 7 LSAs (NSSA-LSAs), and some Type 10 LSAs (only Extended Link Opaque LSAs). | - |
| *max-interval* | Specifies the maximum interval at which LSAs are updated. | The value ranges from 1 to 300000, in milliseconds. |
| *start-interval* | Specifies the initial interval at which LSAs are updated. | The value ranges from 0 to 60000, in milliseconds. |
| *hold-interval* | Specifies the Holdtime interval at which LSAs are updated. | The value is an integer ranging from 1 to 60000 in milliseconds. |
| **other-type** *interval* | Sets the interval for updating OSPF Type 3 LSAs (Network-Summary-LSAs), Type 4 LSAs (ASBR-Summary-LSAs), and some Type 10 LSAs (except Extended Link Opaque LSAs). | The value is an integer ranging from 0 to 10, in seconds. The default value is 5. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF sets a 5-second update interval for LSAs. This prevents network connections or frequent route flapping from consuming excessive network bandwidth or device resources. On a stable network that requires fast route convergence, you can alter the interval to 0 seconds. In this manner, LSAs indicating topology or route changes can be advertised immediately, which speeds up route convergence. When the network is unstable, route calculation may be performed frequently, which consumes a large number of CPU resources. In addition, LSAs that describe the unstable topology are generated and transmitted on the unstable network. Frequently processing such LSAs affects the rapid and stable operation of the entire network. You can configure an intelligent timer so that the device can dynamically adjust the interval based on the user configuration and the frequency of triggering events (such as route calculation) to quickly stabilize the network.If there is no special requirement for the network, using the default value is recommended.Due to the timer restriction, when the configured interval is less than 100 ms, the interval is updated based on 100 ms.

**Implementation Procedure**

* When lsa-originate-interval 0 is configured, the interval is not adjusted.
* For the LSAs of the maximum age (except Opaque-area LSAs and Opaque-as LSAs), the interval is not adjusted.
* If both this command and the lsa-originate-interval suppress-flapping command are configured and the interval needs to be adjusted using both commands, the device uses the larger value as the flapping suppression time.
* The rules for processing the LSA interval of the intelligent timer are as follows:LSA interval. If the interval is greater than max-interval, the interval is not adjusted. The number of LSA updates is cleared.Interval for generating LSAs. If the interval is shorter than the specified interval, the system attempts to generate LSAs after the specified interval and increases the number of LSA updates by 1.The interval for sending LSAs is set as follows:a. The initial interval for updating LSAs is specified by start-interval.b. For the nth (nâ¥2) time, when hold-interval x 2^(n-2) is smaller than max-interval, the interval for updating LSAs is equal to hold-interval x 2^(n-2).c. For the nth (nâ¥2) time, when hold-interval x 2^(n-2) is greater than or equal to max-interval and the interval for updating LSAs is max-interval, OSPF updates LSAs at max-interval for three consecutive times. Then, go back to Step a, LSAs are updated at the initial interval specified by start-interval.
* Intelligent timer. When processing router LSAs at a specified interval, the intelligent timer adjusts configuration parameters based on the number and status of neighbors.If the number of neighbors in Exchange or Loading state is greater than 5 and the number of neighbors in Full state is greater than 10, the rules for adjusting max-interval, hold-interval, and max-interval are as follows:If the number of full neighbors ranges from 11 to 100, set hold-interval to 10s and max-interval to 20s.If the number of full neighbors ranges from 101 to 500, set hold-interval to 20s and max-interval to 40s.If the number of full neighbors is greater than 500, set hold-interval to 30s and max-interval to 60s.
* Rules for processing the interval of other-type LSAs:If other-type interval is set to 0, the interval is not adjusted.If the interval for generating LSAs is shorter than the value of other-type interval, no LSA is generated. Instead, LSA generation is delayed based on the calculated remaining interval.

**Precautions**

Setting the interval in the lsa-originate-interval command to be a value greater than or equal to the Holdtime interval specified in the lsa-arrival-interval command is recommended.


Example
-------

# Set the interval at which LSAs are updated to 0 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] lsa-originate-interval 0

```