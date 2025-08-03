display vrrp6 state-change interface vrid
=========================================

display vrrp6 state-change interface vrid

Function
--------



The **display vrrp6 state-change interface vrid** command displays the changes in the status of a specified Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display vrrp6 state-change interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If the status of a VRRP6 backup group is abnormal, run the display vrrp6 state-change interface vrid command to view the latest 10 changes in the status of the VRRP6 backup group. The changes include:

* Time when the status of the VRRP6 backup group changed
* Statuses before and after the status of the VRRP6 backup group changed
* Reason of the change in the status of the VRRP6 backup group

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the changes in the status of VRRP6 backup group 1 on 100GE 1/0/1.
```
<HUAWEI> display vrrp6 state-change interface 100GE 1/0/1 vrid 1
Time                      SourceState   DestinationState     Reason
  ---------------------------------------------------------------
  2011-01-27 15:29:45       Backup        Master               Protocol timer expired
  2011-01-27 15:29:42       Initialize    Backup               Interface up

```

**Table 1** Description of the **display vrrp6 state-change interface vrid** command output
| Item | Description |
| --- | --- |
| Time | Time when the status of the VRRP6 backup group changed. |
| SourceState | Status before the status of the VRRP6 backup group changed:   * Master. * Backup. * Initialize. |
| DestinationState | Status after the status of the VRRP6 backup group changed:   * Master. * Backup. * Initialize. |
| Reason | Reason of the change in the status of the VRRP6 backup group:   * Admin-vrrp drove. * BFD configure deleted. * Interface up. * Interface down. * Link BFD session down. * Link BFD session up. * Link BFD session deleted. * Peer BFD session down. * Priority calculation. * Protocol timer expired. * Track interface. * Track BFD session. * No available active board. * Active board restore. * Protocol skew timer expired. |