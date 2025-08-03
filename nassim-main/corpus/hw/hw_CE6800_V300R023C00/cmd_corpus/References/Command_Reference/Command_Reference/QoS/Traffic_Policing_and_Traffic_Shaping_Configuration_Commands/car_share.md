car share
=========

car share

Function
--------



The **car share** command configures aggregated CAR in a traffic behavior.

The **undo car share** command cancels aggregated CAR in a traffic behavior.



By default, aggregated CAR is not configured in a traffic behavior.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**car** *car-name* **share**

**undo car share**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *car-name* | Specifies the name of a QoS CAR profile. | The value is a string of 1 to 31 case-sensitive characters without spaces or question marks (?). It cannot be i, if, ifg, s, st, sta, stat, stati, statis, statist, statisti, statistic, or statistics. |



Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When multiple traffic classifiers are defined in a traffic policy and traffic behaviors associated with the traffic classifiers define CAR (using the car cir command) and aggregated CAR, the system limits the rates of flows using the configured CAR, aggregates the flows, and limits the rate of the aggregated traffic using the aggregated CAR in sequence. This process is called hierarchical traffic policing.

Hierarchical traffic policing multiplexes traffic statistics and controls services in a fine-granular manner. For example, hierarchical traffic policing limits the service traffic of level-1 and level-2 users or traffic of level-1 and level-2 user groups.

**Prerequisites**

A QoS CAR profile has been configured using the **qos car** command in the system view. Only the committed information rate (CIR) is configured in the profile.A QoS CAR profile has been configured using the **car** command in the traffic behavior view. The CIR of this CAR profile must be smaller than the CIR of the QoS CAR profile configured by the **qos car** command.

**Precautions**

The traffic policy defining the aggregated CAR action can only be used in the inbound direction.After aggregated CAR is configured, all the rules in the traffic classifiers bound to the same traffic behavior share the CAR index. The system aggregates all the flows matching these traffic classifiers and uses CAR to limit the rate of the flows. If the traffic classifiers define both Layer 2 and Layer 3 information, the aggregated CAR configuration is invalid.A traffic policy limits the traffic rate using the aggregated CAR only in the current applied object. For example, when the traffic policy p1 defining the aggregated CAR is applied to interface1 and interface2, the aggregated CAR applies to traffic on interface1 and interface2 respectively, without affecting each other.


Example
-------

# Configure aggregated CAR in the traffic behavior tb1.
```
<HUAWEI> system-view
[~HUAWEI] qos car qoscar1 cir 2000 kbps
[*HUAWEI] traffic behavior tb1
[*HUAWEI-behavior-tb1] car cir 1000 kbps pir 123456 kbps
[*HUAWEI-behavior-tb1] car qoscar1 share

```