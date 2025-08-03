traffic-policy global
=====================

traffic-policy global

Function
--------



The **traffic-policy global** command applies a traffic policy to the system.

The **undo traffic-policy global** command deletes a traffic policy that is applied to the system.



By default, no traffic policy is applied to the system.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**traffic-policy** *policy-name* **global** [ **slot** *slot-id* ] **outbound**

**undo traffic-policy** *policy-name* **global** [ **slot** *slot-id* ] **outbound**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**traffic-policy** *policy-name* **global** [ **slot** *slot-id* ] **inbound**

**undo traffic-policy** *policy-name* **global** [ **slot** *slot-id* ] **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a user-defined traffic policy. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **slot** *slot-id* | Specifies the device where the traffic policy is applied. | - |
| **outbound** | Applies a traffic policy to the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **inbound** | Applies a traffic policy to the inbound direction. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Packets are classified based on Layer 2 information, Layer 3 information, or ACLs. To provide differentiated services for service flows, bind a traffic classifier and a traffic behavior to a traffic policy and apply the traffic policy.You can use the **traffic-policy global** command to apply a traffic policy to the system.

**Prerequisites**

A traffic policy has been created by using the **traffic policy** command.

**Precautions**

* A traffic policy cannot be applied to the same direction in the system and in the slot simultaneously.
* The applied traffic policy cannot be deleted. To delete this traffic policy, run the **undo traffic-policy** command in the corresponding view to unbind the traffic policy and then run the **undo traffic policy** command in the system view to delete the traffic policy.
* You can change the traffic classification rules, ACL rules, actions defined by the traffic behavior, and relationship between the traffic classifier and traffic behaviors of an applied traffic policy. However, the changes may lead to a failure in delivering the traffic policy. If the traffic policy fails to be delivered, a message indicating the failure cause will be displayed. To view the traffic policy delivery failure cause, run the **display traffic-policy applied-record** command.

Example
-------

# Create a traffic policy p1, bind the created traffic classifier c1 and traffic behavior b1 to the traffic policy, and apply the traffic policy to the inbound direction.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] traffic-policy p1 global inbound

```