display stp vlan history
========================

display stp vlan history

Function
--------



The **display stp vlan history** command displays historical port role changes and priorities of triggering port rule changes.




Format
------

**display stp vlan** [ *vlan-id* ] **history**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Displays historical information about the spanning tree protocol in a specified VLAN.  If vlan-id is not specified, the historical information about all VLANs is displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

In the VBST topology, when a VLAN is configured on an interface, you can run this command to check historical information about the spanning tree protocol of an interface that joins the VLAN. At this time, you do not need to pay attention to the mapping between VLANs and instances.

**Prerequisites**

The following configuration must be performed before you run this command:

* In the system view, the **stp enable** command has been run to enable VBST globally.
* In the interface view, the **stp enable** command has been run to enable VBST on a port.

**Precautions**

Nothing is displayed if VBST is not enabled globally or on ports.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display historical information of VLAN 2 when running VBST.
```
<HUAWEI> display stp vlan 2 history
 VLAN 2 history trace:
 ----------------------------------------------------------
 Interface: 100GE1/0/1
     Role Transition       : Disable -> Designated
     Is Aged               : Yes
     Time                  : 2016-10-08 14:42:48
     Root Priority         : 32770
     Root MAC              : 00e0-fc12-3456
     Root Path Cost        : 0
     Designated Priority   : 32770
     Designated Bridge MAC : 00e0-fc12-3456
     Port Priority         : 128
     Port Id               : 2

```

**Table 1** Description of the **display stp vlan history** command output
| Item | Description |
| --- | --- |
| Role Transition | Role change. |
| Designated Priority | Priority of the specified bridge. |
| Designated Bridge MAC | MAC address of the specified bridge. |
| Is Aged | Whether a timer is aged. |
| Time | Displayed time. |
| Root Priority | Priority of the root bridge. |
| Root MAC | MAC address of the root bridge. |
| Root Path Cost | Root path cost. |
| Port Priority | Port priority. |
| Port Id | Port index. |
| Interface | Port name. |