qos car inbound
===============

qos car inbound

Function
--------



The **qos car inbound** command applies a QoS CAR profile to an interface in the inbound direction to police traffic entering the interface.

The **undo qos car inbound** command unbinds a QoS CAR profile from an interface in the inbound direction.



By default, no QoS CAR profile is applied to an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos car inbound** *car-name*

**undo qos car inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *car-name* | Specifies the name of a QoS CAR profile. | The value must be the name of an existing QoS CAR profile on the device. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,50GE interface view,Eth-Trunk interface view,Layer 2 sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a QoS CAR profile is created, you must apply the QoS CAR profile to an interface to police user service traffic (such as voice and video service traffic). This command applies a created QoS CAR profile to a specified interface in the inbound direction.

**Prerequisites**

A QoS CAR profile has been created using the **qos car** command.

**Implementation Procedure**

After a QoS CAR profile is applied to an interface, the system collects statistics on forwarded and discarded packets. You can use the **display qos car statistics** command to view packet statistics on the interface.

**Precautions**

* If the same QoS CAR needs to be configured on multiple interfaces, you can perform the configuration in a port group to reduce the workload.
* Configuring the **qos car inbound** command occupies system resources. If system resources are insufficient, the configuration may fail.
* If both a QoS CAR profile and a traffic policy containing a traffic policing action are applied to an interface, QoS CAR parameters do not take effect because the traffic policy has a higher priority than the QoS CAR profile.
* If traffic policing is performed for incoming packets on an interface, protocol packets sent to the local device may be discarded because the rate of protocol packets exceeds the policing rate. You can use a traffic policy containing the traffic policing action to implement refined traffic policing.
* If **percent** *percent-value*is specified when you run the **qos car** command to create a QoS CAR profile, the QoS CAR profile can be applied only to physical interfaces.


Example
-------

# Apply the QoS CAR profile qoscar1 to 100GE1/0/1 in the inbound direction.
```
<HUAWEI> system-view
[~HUAWEI] qos car qoscar1 cir 10000 kbps cbs 10240 bytes
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] qos car inbound qoscar1
[*HUAWEI-100GE1/0/1] quit

```