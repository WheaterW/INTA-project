ip urpf disable
===============

ip urpf disable

Function
--------



The **ip urpf disable** command configures URPF check disabling for the specified traffic.

The **undo ip urpf disable** command cancels URPF check disabling for the specified traffic.



By default, reverse address check is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ip urpf disable**

**undo ip urpf disable**


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

After URPF check is enabled on an interface, the device performs the URPF check on all the packets passing through the interface. To prevent the packets of a certain type from being discarded, you can disable URPF check for these packets. For example, if the device is configured to trust all the packets from a certain server, the device does not check these packets. If you need to disable URPF check, you can run commands in the traffic behavior view and associate the traffic behavior and a traffic classifier with a traffic policy. When the traffic policy is applied globally or applied to an interface, or a VLAN, the device does not perform URPF check on the traffic that matches the traffic classifier rules.

**Follow-up Procedure**

Run the **traffic policy** command to create a traffic policy and run the **classifier behavior** command in the traffic policy view to bind the traffic classifier to the traffic behavior containing the action of disabling URPF check.

**Precautions**

* The **undo ip urpf disable** command only cancels URPF check disabling in a traffic behavior. To enable URPF for all flows on an interface, run the ip urpf (interface view) command.
* A traffic policy containing a traffic behavior that defines the **ip urpf disable** command can be applied only to the inbound direction.

Example
-------

# Disable the URPF check function of traffic behavior b1.
```
<HUAWEI> system-view
[~HUAWEI] traffic behavior b1
[*HUAWEI-behavior-b1] ip urpf disable

```