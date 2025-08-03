qos group
=========

qos group

Function
--------



The **qos group** command creates a QoS group and displays its view, or directly displays the view of an existing QoS group.

The **undo qos group** command deletes a QoS group.



By default, no QoS group is configured.


Format
------

**qos group** *group-name*

**undo qos group** *group-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a QoS group. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the same traffic policy needs to be applied to multiple VLANs or interfaces or multiple traffic classifiers based on source IP addresses need to be bound to the same traffic policy, many ACL resources are consumed. You can add the VLANs, source IP addresses, or interfaces to the same QoS group. In this case, only one ACL resource is consumed, so ACL resources of the device are saved.



**Follow-up Procedure**



Run the **group-member** command in the QoS group view to add interfaces, source IP addresses, or VLANs to the QoS group.



**Precautions**

A QoS group can contain only members of the same type. For example, an interface and a VLAN cannot be added to the same QoS group.A traffic policy cannot be applied to an interface or a VLAN that is added to a QoS group. An interface or a VLAN to which a traffic policy is applied cannot be added to a QoS group.


Example
-------

# Create a QoS group named qosgroup1 and enter the view of the QoS group qosgroup1.
```
<HUAWEI> system-view
[~HUAWEI] qos group qosgroup1
[*HUAWEI-qos-group-qosgroup1]

```