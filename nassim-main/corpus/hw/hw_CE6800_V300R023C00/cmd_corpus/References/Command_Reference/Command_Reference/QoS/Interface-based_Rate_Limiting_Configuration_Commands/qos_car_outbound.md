qos car outbound
================

qos car outbound

Function
--------



The **qos car outbound** command applies a QoS CAR profile to an interface in the outbound direction to police traffic on the interface.

The **undo qos car outbound** command unbinds a QoS CAR profile from an interface in the outbound direction.



By default, no QoS CAR profile is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos car outbound** *car-name*

**undo qos car outbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *car-name* | Specifies the name of a QoS CAR profile. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a QoS CAR profile is created, you can run the qos car outbound command to apply the QoS CAR profile to an interface in the outbound direction to police traffic leaving the interface.

**Prerequisites**

A QoS CAR profile has been created using the **qos car** command.

**Precautions**

* After a QoS CAR profile is applied to a Layer 2 sub-interface, the **display qos car statistics** command cannot be used to query packet statistics.
* Configuring the qos car outbound command occupies system resources. If system resources are insufficient, the configuration may fail.
* If a QoS CAR profile and a traffic policy containing the traffic policing action are applied to the same interface, QoS CAR parameters defined in the QoS CAR profile do not take effect because the traffic policy takes precedence over the QoS CAR profile.
* A QoS CAR profile can be applied only to the outbound direction of dot1q and QinQ Layer 2 sub-interfaces for VLAN tag termination.

Example
-------

# Apply a QoS CAR profile named car1 to police traffic in the outbound direction of 100GE1/0/1.1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1.1
[~HUAWEI-100GE1/0/1.1] qos car outbound car1

```