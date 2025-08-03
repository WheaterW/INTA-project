lsa-arrival-interval (OSPF view)
================================

lsa-arrival-interval (OSPF view)

Function
--------



The **lsa-arrival-interval** command sets the interval at which LSAs are received.

The **undo lsa-arrival-interval** command restores the default configuration.



By default, the intelligent timer is enabled. The maximum interval at which LSAs are updated is 1000 milliseconds (ms), the initial interval is 500 ms, and the Holdtime interval is 500 ms.


Format
------

**lsa-arrival-interval** *interval*

**lsa-arrival-interval intelligent-timer** *max-interval* *start-interval* *hold-interval*

**undo lsa-arrival-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which LSAs are received. | The value is an integer ranging from 0 to 10000, in ms. |
| **intelligent-timer** | Enables an intelligent timer to receive LSAs. | - |
| *max-interval* | Specifies the maximum interval at which LSAs are received. | The value ranges from 1 to 300000, in milliseconds. |
| *start-interval* | Specifies the initial interval at which LSAs are received. | The value ranges from 0 to 60000, in milliseconds. |
| *hold-interval* | Specifies the Holdtime interval at which LSAs are received. | The value is an integer ranging from 1 to 60000, in milliseconds. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

OSPF defines that the interval at which LSAs are received is 1s, which prevents network connections or frequent route flapping from consuming excessive network bandwidth or device resources.On a stable network that requires fast route convergence, you can change the interval at which LSAs are received to 0s. In this manner, the device can fast respond to topology or route changes, which speeds up route convergence.On an unstable network, routes are calculated frequently, which consumes a great number of CPU resources. In addition, LSPs that describe the unstable topology are generated and transmitted on the unstable network. Frequently processing such LSAs affects the rapid and stable operation of the entire network. You can configure an intelligent timer so that the device can dynamically adjust the interval according to the user configuration and the frequency of triggering events (such as route calculation) to speed up network convergence.If there is no special network requirement, default values are recommended.

**Implementation Procedure**

* For LSAs with the maximum age, LSAs can be received.
* If a router ID conflict may occur in a self-originated router LSA, the router can receive the LSA.
* If both this command and the lsa-arrival-interval suppress-flapping command are configured, LSAs are received only when both commands are configured.
* The rules for the intelligent timer to receive and process LSAs are as follows:

1. Interval at which LSAs are received. If the interval is greater than or equal to max-interval, LSAs are received. All RX counters are cleared.
2. LSA interval. When the value is smaller than max-interval,(1) When LSAs are updated for the first time, the LSA receiving counter is set to 1, and the specified interval for calculating and updating LSAs is calculated. If the interval for calculating LSAs is shorter than the specified interval, LSAs are not received.(2) If LSAs are updated not for the first time and the LSA interval is shorter than the specified interval, the specified interval and LSA update counter remain unchanged, and LSAs are not received.(3) If the LSA is not updated for the first time and the LSA interval is greater than or equal to the specified interval, the LSA receiving counter increases by 1, and the specified interval is recalculated and updated. The LSA is received.

The interval for sending LSAs is set as follows:a. The value of the counter for receiving LSAs is 1, and the interval for receiving LSAs is specified by start-interval.b. The value of the counter for receiving LSAs is n (nâ¥2). When hold-interval x 2^(n-2) is smaller than max-interval, the interval for receiving LSAs is set to hold-interval x 2^(n-2).c. The value of the LSA receiving counter is n (nâ¥2). When hold-interval x 2^(n-2) is greater than or equal to max-interval, the value of the max counter increases by 1.If the value of max is less than or equal to 3, the interval for receiving LSAs is set to max-interval.If the value of the max counter exceeds 3, the max counter is cleared. Then, go back to Step a, the value of the LSA receiving counter is updated to 1, and the interval for receiving LSAs is set to the initial interval specified by start-interval.

* Rules for configuring a non-intelligent timer:If lsa-arrival-interval 0 is configured, LSA updates can be received.If lsa-arrival-interval is set to a non-zero value, no LSA update is received because the interval for receiving LSAs is shorter than the configured value.

**Precautions**

Setting the interval in the lsa-arrival-interval command to be a value less than or equal to the Holdtime interval specified in the lsa-originate-interval command is recommended.


Example
-------

# Set the interval at which LSAs are received to 0 milliseconds.
```
<HUAWEI> system-view
[~HUAWEI] ospf 1
[*HUAWEI-ospf-1] lsa-arrival-interval 0

```