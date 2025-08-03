traffic-policy (bridge domain view)
===================================

traffic-policy (bridge domain view)

Function
--------



The **traffic-policy** command applies a traffic policy to a BD.

The **undo traffic-policy** command deletes a traffic policy from a BD.



By default, no traffic policy is applied to a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**traffic-policy** *policy-name* { **inbound** | **outbound** }

**undo traffic-policy** *policy-name* { **inbound** | **outbound** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a traffic policy. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **inbound** | Applies a traffic policy to the inbound direction of a BD. | - |
| **outbound** | Applies a traffic policy to the outbound direction of a BD. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Packets are classified based on Layer 2 information, Layer 3 information, or ACLs. To provide differentiated services for service flows, bind a traffic classifier and a traffic behavior to a traffic policy and apply the traffic policy. You can use the **traffic-policy** command to apply a traffic policy to a BD.

**Prerequisites**

A traffic policy has been created by using the **traffic policy** command.

**Precautions**

* After a traffic policy is applied to a BD, the traffic policy takes effect for packets received and sent in the BD.
* After a traffic policy is applied to a BD, you cannot directly delete the traffic policy. To delete the traffic policy that has been applied, run the **undo traffic-policy** command in the corresponding view to unbind the traffic policy and then run the **undo traffic policy** command in the system view to delete the traffic policy.
* You can change the traffic classification rules, ACL rules, actions defined by the traffic behavior, and relationship between the traffic classifier and traffic behaviors of an applied traffic policy. However, the changes may lead to a failure in delivering the traffic policy. If the traffic policy fails to be delivered, a message indicating the failure cause will be displayed. To view the traffic policy delivery failure cause, run the **display traffic-policy applied-record** command.

Example
-------

# Create a traffic policy p1, bind the created traffic classifier c1 and traffic behavior b1 to the traffic policy, and apply the traffic policy to the inbound direction in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] traffic-policy p1 inbound

```