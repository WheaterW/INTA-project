mld snooping require-router-alert
=================================

mld snooping require-router-alert

Function
--------



The **mld snooping require-router-alert** command configures interfaces in a VLAN to discard MLD messages that do not carry the Router-Alert option in IP headers.

The **undo mld snooping require-router-alert** command restores the default configuration.



By default, the MLD messages accepted by a device from a VLAN do not need to carry the Router Alert option.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping require-router-alert**

**undo mld snooping require-router-alert**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Router-Alert is a mechanism used to identify protocol messages. Messages carrying the Router-Alert option are delivered to the routing protocol layer for processing.By default, devices do not check whether messages carry Router-Alert options for the sake of compatibility, and send all MLD messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, run the mld snooping require-router-alert command to configure a device to discard MLD messages that do not carry Router-Alert options. After the command is run, the device checks whether a received MLD message carries the Router-Alert option and discards the message if it does not carry the Router-Alert option.


Example
-------

# Configure interfaces in VLAN 2 to discard MLD messages that do not carry the Router-Alert option in IP headers.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping require-router-alert

```