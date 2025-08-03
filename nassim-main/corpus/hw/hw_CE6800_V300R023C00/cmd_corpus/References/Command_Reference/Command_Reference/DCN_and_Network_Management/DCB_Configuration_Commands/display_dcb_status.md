display dcb status
==================

display dcb status

Function
--------



The **display dcb status** command displays DCB configurations on the local and remote devices.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb status** [ **interface** { *interface-name* | *interface-type* *interface-num* } ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Displays the DCBX configuration on a specified interface.   * interface-type specifies the type of an interface. * interface-number specifies the number of an interface.   If this parameter is not specified, DCBX parameters configured on all interfaces of the local and remote devices are displayed. | - |
| **interface** *interface-name* | Displays the DCBX configuration on a specified interface.   * interface-name specifies the name of an interface.   If this parameter is not specified, DCBX parameters configured on all interfaces of the local and remote devices are displayed. | - |
| **verbose** | Displays detailed DCB configurations. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run the display dcb status command to view DCB configurations on the local and remote devices to locate DCB faults. If configurations on the local and remote devices are different, DCB negotiation may fail.

**Precautions**

When the Intel DCBX standard is used, the UDP or TCP type cannot be identified separately. When the UDP or TCP type is set on the remote end, the remote end configuration queried on the local end does not distinguish the TCP or UDP type.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DCBX configurations on 100GE1/0/1.
```
<HUAWEI> display dcb status interface 100ge 1/0/1 verbose
DCB Runinfo Verbose:
BW PCT: Bandwidth percent
-------------------------------------------------------------------------------
Interface : 100GE1/0/1
-------------------------------------------------------------------------------
Service           Configuration   Local                 Remote
-------------------------------------------------------------------------------
PFC               Priority        3                     -
-------------------------------------------------------------------------------
ETS        PG-ID  Configuration   Local                 Remote
               0  Queue           0 1 2 4 5             -
                  BW PCT          50                    -
               1  Queue           3                     -
                  BW PCT          50                    -
              15  Queue           6 7                   -
                  BW PCT          -                     -
-------------------------------------------------------------------------------
APP-TLV           Application     Local                 Remote
                  FCoE                7                      -
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb status** command output
| Item | Description |
| --- | --- |
| Interface | Interface where DCB is enabled. |
| Service | DCB function configured on the interface:  -PFC: Priority-based Flow Control.  -ETS: Enhanced Transmission Selection.  -APP-TLV: Service priority in the APP TLV. |
| Configuration | Configuration item:  -Priority: priority of queues with PFC enabled.  -Queue: queues that join the priority group.  -BW PCT: bandwidth of the priority group. |
| Local | Local configuration. |
| Remote | Configure the remote end. |
| PG-ID | ID of a priority group. |
| Application | Service priority:  -FCoE: FCoE service priority.  -FIP: FIP service priority.  -ISCSI: ISCSI service priority. |