display ospf graceful-restart
=============================

display ospf graceful-restart

Function
--------



The **display ospf graceful-restart** command displays the status of OSPF GR.




Format
------

**display ospf** [ *process-id* ] **graceful-restart** [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id Specifies the ID of an OSPF process. | The value is an integer that ranges from 1 to 4294967295. |
| **verbose** | Displays detailed information about OSPF GR. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view details of the GR and the statistics, run the **display ospf graceful-restart** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about OSPF GR.
```
<HUAWEI> display ospf graceful-restart verbose
OSPF Process 1 with Router ID 10.1.1.1               

 Helper-policy support                : planned, strict lsa check
 Current GR state                     : normal

 Number of restarting neighbors : 0

 Last exit reason:
  On Helper     : none
  All area count      : 1
              Area ID    : 0.0.0.1
 Authtype       :  None     Area flag : Normal
 Normal interface count: 1
 Interface: 10.6.6.2 (Vlanif100)
 GR state : Normal                  State: BDR          Type: Broadcast
 Neighbor count of this interface : 1
 Neighbor          IP address         GR state     Helper period   Grace Period Left   Last Helper Exit reason
 10.1.1.1           10.6.6.1            Normal       0               0                   none

```

# Display the status of OSPF GR in non-IETF mode.
```
<HUAWEI> display ospf graceful-restart
OSPF Process 1 with Router ID 10.1.1.1               

 Helper-mode                          : non-ietf
 Helper-policy support                : --
 Current GR state                     : normal

 Number of restarting neighbors : 0

 Last exit reason:
  On Helper     : none

```

# Display the status of OSPF GR in IETF mode.
```
<HUAWEI> display ospf graceful-restart
OSPF Process 1 with Router ID 10.1.1.1               

 Helper-policy support                : planned and un-planned, strict lsa check
 Current GR state                     : normal

 Number of restarting neighbors : 0

 Last exit reason:
  On Helper     : none

```

**Table 1** Description of the **display ospf graceful-restart** command output
| Item | Description |
| --- | --- |
| Helper-policy support | Policy that supports the Helper:   * planned: indicates that the Helper supports only planned GR. * un-planned: indicates the Helper supports unplanned GR. * strict lsa check: indicates that the Helper supports strict external LSA check. * ignore external lsa check: indicates that the Helper does not check external LSAs. * never: indicates that the device does not support the Helper mode. |
| Current GR state | Current GR status:   * Normal: indicates that GR is in the Normal state. * Helper: indicates that the device enters the Helper mode. |
| GR state | GR status of an interface:   * Normal. * Helper. |
| Number of restarting neighbors | Number of restarted routers displayed on the Helper. |
| Last exit reason | Reason why the device exits from GR.   * none: indicates that GR is not implemented. * successful exit: indicates that the OSPF process exits after GR is implemented successfully. * grace period expire recv flush grace lsa: indicates that the GR restarter deletes the flushed grace LSA. * recv change lsa: indicates that the local interface receives the changed LSA. * recv two grace lsa: indicates that the local interface receives two grace LSAs. * recv one way hello: indicates that the local interface receives a 1-way Hello packet from the peer interface. That is, the neighbor goes Down. * policy check fail: indicates that the Helper policy check fails. * nbr reset: indicates that NBR restarts. * if change: indicates that the status of an interface changes. For example, the interface changes from Up to Down or the configuration of the interface changes. * proc change: indicates that the configuration of the Helper in this OSPF instance changes. |
| Last Helper Exit reason | Cause for exiting the helper mode of the neighbor for the last time:   * none: indicates that GR does not occur. * successful exit: indicates that GR is correctly performed and ended. * grace period expired: indicates that the GR period expires. * received flushed grace LSA: indicates that flushed grace LSAs are received. * flooding changed LSA: indicates that changed LSAs are received. * received multiple grace LSA: indicates that multiple grace LSAs are received. * received 1-way hello packet: indicates that 1-way Hello packets are received. * policy check failed for received grace LSA: indicates that the Helper policy is not matched. * neighbor reset: indicates that topology changes after the reset command is run on the neighbor of the helper. * interface state changed: indicates that the interface status is changed. * graceful restart unconfigured at process level: indicates that GR is not configured for the neighbor. |
| On Helper | Reason why the Helper exits from GR. |
| Helper period | Period of the GR helper. |
| All area count | Number of areas in the process. |
| Area ID | Area ID. |
| Area flag | Area flag:   * Normal. * NSSA. * Stub. |
| Authtype | Authentication type. |
| Normal interface count | Number of interfaces in the area. |
| Neighbor count of this interface | Number of neighbors on the interface. |
| Neighbor | Neighbor ID. |
| IP address | IP address of a neighboring interface. |
| Grace Period Left | Remaining time of the GR Helper. |
| Helper-mode | Helper mode. |
| Interface | IP address of the interface. |
| State | Interface status:   * Point to Point. * DR. * BDR. * DROther. * Waiting. * Down. |
| Type | Interface type:   * P2P. * P2MP. * NBMA. * Broadcast. |