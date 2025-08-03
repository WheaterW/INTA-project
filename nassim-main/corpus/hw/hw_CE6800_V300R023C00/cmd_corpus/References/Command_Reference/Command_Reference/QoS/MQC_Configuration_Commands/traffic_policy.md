traffic policy
==============

traffic policy

Function
--------



The **traffic policy** command creates a traffic policy and displays the traffic policy view, or displays the view of an existing traffic policy.

The **undo traffic policy** command deletes a traffic policy.



By default, no traffic policy is created in the system.


Format
------

**traffic policy** *policy-name*

**undo traffic policy** *policy-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a user-defined traffic policy. | The value is a string of 1 to 31 case-sensitive characters. It must start with a letter or digit, and cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Packets are obtained based on Layer 2 information, Layer 3 information, or ACLs. To implement differentiated services for service flows of packets, bind a traffic classifier and a traffic behavior to the created traffic policy and apply the traffic policy. You can use the **traffic policy** command to create a traffic policy.

**Prerequisites**

A traffic classifier and a traffic behavior have been created.

**Implementation Procedure**

Run the **classifier behavior** command in the traffic policy view to associate the traffic policy with a traffic classifier and a traffic behavior.

**Follow-up Procedure**



Run the traffic-policy global, traffic-policy (interface view), or traffic-policy (VLAN view) command to apply the traffic policy to the system, an interface, or a VLAN to make the created traffic policy take effect.



**Precautions**

* If the traffic policy that you want to delete has been applied to the system, an interface, or a VLAN, run the **undo traffic-policy** command to unbind the traffic policy in the corresponding view. Then run the **undo traffic policy** command in the system view to delete the traffic policy.
* On the device, a maximum of 2048 traffic policies can be created and multiple pairs of traffic classifiers and traffic behaviors can be configured in a traffic policy.


Example
-------

# Create a traffic policy p1.
```
<HUAWEI> system-view
[~HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1]

```