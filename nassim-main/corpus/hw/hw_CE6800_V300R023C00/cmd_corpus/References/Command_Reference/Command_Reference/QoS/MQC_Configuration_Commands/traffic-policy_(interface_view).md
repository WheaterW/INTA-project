traffic-policy (interface view)
===============================

traffic-policy (interface view)

Function
--------



The **traffic-policy** command applies a traffic policy to an interface.

The **undo traffic-policy** command deletes a traffic policy from an interface.



By default, no traffic policy is applied to an interface.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**traffic-policy** *policy-name* **outbound**

**undo traffic-policy** *policy-name* **outbound**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**traffic-policy** *policy-name* **inbound**

**undo traffic-policy** *policy-name* **inbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a user-defined traffic policy. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **inbound** | Applies a traffic policy to the inbound direction. | - |
| **outbound** | Applies a traffic policy to the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **undo** | Cancels the current setting. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk Layer 2 sub-interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Layer 2 sub-interface view,Sub-interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Packets are classified based on Layer 2 information, Layer 3 information, or ACLs. To provide differentiated services for service flows, bind a traffic classifier and a traffic behavior to a traffic policy and apply the traffic policy. You can use the **traffic-policy** command to apply a created traffic policy to an interface.



**Prerequisites**



Run the **traffic policy** command to create a traffic policy and bind the traffic classifier and traffic behavior to the traffic policy.



**Precautions**

* After a traffic policy is applied, it cannot be deleted directly. To delete a traffic policy that has been applied, run the **undo traffic-policy** command in the corresponding view to unbind the traffic policy from the interface, and then run the **undo traffic policy** command in the system view to delete the traffic policy.
* After a traffic policy is applied, you can directly modify the matching rules of the traffic classifier, ACL rules, actions in the traffic behavior, and binding relationship between the traffic classifier and traffic behavior in the traffic policy. However, the modification may cause a failure to deliver the traffic policy. In this case, a message is displayed, indicating that the traffic policy fails to be delivered. If the traffic policy fails to be delivered, run the **display traffic-policy applied-record** command to check the cause of the failure.
* If a traffic policy is applied to an Eth-Trunk interface and a member interface is updated, the traffic policy is re-delivered. As a result, the applied traffic policy becomes invalid temporarily.
* A traffic policy can be applied only to the inbound direction in the Eth-Trunk Layer 2 sub-interface view or Layer 2 sub-interface view.
* For CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K and CE6820S:
* If an outbound ACL is configured on an Eth-Trunk sub-interface, you are advised to configure only a level-1 ACL. If a level-2 outbound ACL is configured, the forwarding performance deteriorates.


Example
-------

# Create a traffic policy p1, bind the created traffic classifier c1 and traffic behavior b1 to the traffic policy, and apply the traffic policy to the inbound direction on interface.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] traffic-policy p1 inbound

```