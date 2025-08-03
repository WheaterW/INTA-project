display ospf router-id conflict
===============================

display ospf router-id conflict

Function
--------



The **display ospf router-id conflict** command displays information about router ID conflicts (if any).




Format
------

**display ospf** [ *process-id* ] **router-id** **conflict**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

If router ID conflicts exist on the network and are not resolved automatically, route flapping may occur. To check information about router ID conflicts (if any), run the display ospf router-id conflict command. The command output helps with the check on incorrect configurations.

**Precautions**

* The obtained router ID conflicts do not necessarily exist on the network.
* The command displays information about the router ID conflicts only between two devices.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about router ID conflicts (if any).
```
<HUAWEI> system-view
[~HUAWEI] display ospf router-id conflict
OSPF Process 2 with Router ID 2.2.2.2
                     Router ID conflict Information
                     ------------------------------

                            Area: 0.0.0.0

Conflict Router ID  : 10.10.10.10
Begin Time          : 2018-07-10 15:42:42+06:00 DST
End Time            : 2018-07-10 15:47:54+06:00 DST
Detect Result       : A router ID conflict may halt between two remote devices.
Lsa1                :
    IP Addr         : 3.3.3.3
    IP Addr         : 4.4.4.4
Lsa2                :
    IP Addr         : 192.168.1.1
    IP Addr         : --

```

**Table 1** Description of the **display ospf router-id conflict** command output
| Item | Description |
| --- | --- |
| Conflict Router ID | Conflicting router ID. |
| Begin Time | Begin time of the conflict detection. |
| End Time | End time of the conflict detection. |
| Detect Result | Detection result. |
| Lsa1 | Interface IP address in the LSA of one of the devices with the conflicting router ID. |
| IP Addr | Interface IP address of the device with the conflicting router ID. |
| Lsa2 | Interface IP address in the LSA of the other device with the conflicting router ID. |
| Area | Area ID. |