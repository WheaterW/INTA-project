mld snooping send-router-alert disable
======================================

mld snooping send-router-alert disable

Function
--------



The **mld snooping send-router-alert disable** command configures the device to add the Router-Alert option in the IP header of an MLD message sent to a specified VLAN.

The **undo mld snooping send-router-alert disable** command configures the device not to add the Router-Alert option in the IP header of an MLD message sent to a specified VLAN.



By default, the device adds the Router-Alert option in the IP header of an MLD message sent to a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping send-router-alert disable**

**undo mld snooping send-router-alert disable**


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

Router-Alert is a mechanism used to identify protocol messages. Messages carrying the Router-Alert option are delivered to the routing protocol layer for processing.By default, devices do not check whether messages carry the Router-Alert option for the sake of compatibility, and send all MLD messages to the upper layer for processing. To improve device performance, reduce costs, and ensure protocol security, run the undo mld snooping send-router-alert disable command to configure the device not to add the Router-Alert option in the IP header of an MLD message sent to a specified VLAN.


Example
-------

# Configure the device not to add the Router-Alert option in the IP header of an MLD message sent to VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] undo mld snooping send-router-alert disable

```