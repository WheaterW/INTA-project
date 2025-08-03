mac-vlan enable
===============

mac-vlan enable

Function
--------



The **mac-vlan enable** command enables VLAN classification based on MAC addresses.

The **undo mac-vlan enable** command disables VLAN classification based on MAC addresses.



By default, VLAN classification based on MAC addresses is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mac-vlan enable**

**undo mac-vlan enable**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When users frequently change their physical locations, you need to re-classify VLANs for the users. If the users want to remain in the original VLANs, you can run the **mac-vlan enable** command to enable VLAN classification based on MAC addresses. In this manner, you do not need to re-classify VLANs when users change their physical locations. This improves user security and increases user access flexibility.VLAN classification based on MAC addresses is applicable to only a simple networking environment where network interface cards are seldom changed. In addition, all users on the network must be pre-defined.

**Prerequisites**



The **mac-vlan enable** command can be run only on Layer 2 interfaces. If the interface is a Layer 3 interface, run the **portswitch** command to change the interface from Layer 3 mode to Layer 2 mode.




Example
-------

# Enable VLAN classification based on MAC addresses.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] undo shutdown
[*HUAWEI-100GE1/0/1] mac-vlan enable

```