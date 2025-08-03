traffic-policy (VPN instance view)
==================================

traffic-policy (VPN instance view)

Function
--------



The **traffic-policy** command applies a traffic policy to a VPN instance.

The **undo traffic-policy** command unbinds a traffic policy from a VPN instance.



By default, no traffic policy is applied to a VPN instance.


Format
------

**traffic-policy** *policy-name* **inbound**

**undo traffic-policy** *policy-name* **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **inbound** | Applies a traffic policy to a VPN instance in the inbound direction. | - |



Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Packets are classified based on Layer 2 information, Layer 3 information, or ACL rules. To implement differentiated services for service flows of the packets, bind a traffic classifier and a traffic behavior to the created traffic policy and apply the traffic policy. The **traffic-policy** command applies a traffic policy to a VPN instance.

**Prerequisites**

A traffic policy has been created by using the **traffic policy** command.

**Precautions**

* After a traffic policy is applied to a VPN instance, the traffic policy takes effect for packets received and sent in the VPN instance.
* After a traffic policy is applied to a VPN instance, you cannot directly delete the traffic policy or the traffic classifier and traffic behavior in the traffic policy. To delete the traffic policy that has been applied, run the **undo traffic-policy** command in the corresponding view to unbind the traffic policy and then run the **undo traffic policy** command in the system view to delete the traffic policy.
* You can change the traffic classification rules, ACL rules, actions defined by the traffic behavior, and relationship between the traffic classifier and traffic behaviors of an applied traffic policy. However, the changes may lead to a failure in delivering the traffic policy. If the traffic policy fails to be delivered, a message indicating the failure cause will be displayed. To view the traffic policy delivery failure cause, run the **display traffic-policy applied-record** command.
* A traffic policy can be applied to a VPN instance only in the inbound direction.
* When a traffic policy is applied to a VPN instance, traffic classifiers bound to the traffic policy cannot match IPv6 packets.

Example
-------

# Create a traffic policy p1, bind the created traffic classifier c1 and traffic behavior b1 to the traffic policy, and apply the traffic policy to the VPN instance test in the inbound direction.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] ip vpn-instance test
[*HUAWEI-vpn-instance-test] traffic-policy p1 inbound

```