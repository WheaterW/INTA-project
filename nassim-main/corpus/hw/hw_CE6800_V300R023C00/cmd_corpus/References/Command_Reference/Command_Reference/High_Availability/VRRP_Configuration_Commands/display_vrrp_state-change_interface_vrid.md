display vrrp state-change interface vrid
========================================

display vrrp state-change interface vrid

Function
--------



The **display vrrp state-change interface vrid** command enables the system to trace changes in the status of a specified VRRP group.




Format
------

**display vrrp state-change interface** { *interface-name* | *interface-type* *interface-number* } **vrid** *virtual-router-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface configured with a VRRP group. | - |
| *interface-type* | Specifies the type an interface configured with a VRRP group. | - |
| *interface-number* | Specifies the number of the interface configured with a VRRP group. | - |
| *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If a VRRP group does not work properly, the display vrrp state-change interface vrid command can be used to trace changes in the VRRP status. Information about the last 10 changes in the VRRP status can be displayed. The command output includes the time when the status changed, the statuses before and after the change, and change reasons.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display changes in the status of VRRP group 1 on 100GE 1/0/1.1.
```
<HUAWEI> display vrrp state-change interface 100GE 1/0/1.1 vrid 1
Time                      SourceState   DestinationState     Reason
  ---------------------------------------------------------------
  2011-01-27 15:29:45       Backup        Master               Protocol timer expired
  2011-01-27 15:29:42       Initialize    Backup               Interface up

```

**Table 1** Description of the **display vrrp state-change interface vrid** command output
| Item | Description |
| --- | --- |
| Time | Time when the VRRP status changed. |
| SourceState | Status before the change:   * Master. * Backup. * Initialize. |
| DestinationState | Status after the change:   * Master. * Backup. * Initialize. |
| Reason | Reason of the VRRP status change:   * Admin-vrrp drove. * BFD configure deleted. * Interface up. * Interface down. * Ignore interface down. * Link BFD session down. * Link BFD session up. * Link BFD session deleted. * Link BFD down-number changed. * Peer BFD session down. * Priority calculation. * Protocol timer expired. * Track interface. * Track BFD session. |