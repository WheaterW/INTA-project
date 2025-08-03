deny | permit
=============

deny | permit

Function
--------



The **deny** command denies service flows that match a specified rule.

The **permit** command configures the device to forward the packets matching the rule according to the original policy without performing any action.

The **undo** command restores the default configuration.



By default, the permit command is used to forward packets matching traffic classification rules according to the original policy.


Format
------

**deny**

**permit**

**undo** { **deny** | **permit** }


Parameters
----------

None

Views
-----

Traffic behavior view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device implements access control using a traffic policy. That is, you can use a traffic policy containing deny | permit on the device so that the device provides the firewall function to filter out specified types of packets. The deny | permit command only filters data packets, but does not process control packets sent to the CPU.

**Precautions**

When you specify a packet filtering action for packets matching an ACL, if the ACL rule defines permit, the device processes packets according to the action (deny or permit) in the traffic behavior. If the ACL rule defines deny, the device discards packets regardless of whether deny or permit is configured in the traffic behavior.In the same traffic behavior, the deny action cannot be used with other traffic actions except for traffic statistics and flow mirroring. Before adding other traffic actions such as re-marking to a traffic behavior, ensure that the traffic behavior does not contain the deny action. If the traffic behavior contains the deny action, configure the permit action before configuring other traffic actions.


Example
-------

# Configure a traffic policy p1 to prevent the packets from VLAN 2 to pass through 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match vlan 2
[*HUAWEI-classifier-c1] quit
[*HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] deny
[*HUAWEI-behavior-b1] quit
[*HUAWEI] traffic policy p1
[*HUAWEI-trafficpolicy-p1] classifier c1 behavior b1
[*HUAWEI-trafficpolicy-p1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] traffic-policy p1 inbound

```