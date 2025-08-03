display isis system-id conflict
===============================

display isis system-id conflict

Function
--------



The **display isis system-id conflict** command displays information about system ID conflicts (if any).




Format
------

**display isis system-id conflict** [ **level-1** | **level-2** ] [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**display isis** [ *process-id* ] **system-id** **conflict** [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Displays information about Level-1 system ID conflicts. | - |
| **level-2** | Displays information about Level-2 system ID conflicts. | - |
| *process-id* | Displays information about system ID conflicts in a specified IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays information about system ID conflicts in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about system ID conflicts (if any), run the display isis system-id conflict command. The command output helps with troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about IS-IS system ID conflicts (if any).
```
<HUAWEI> system-view
[~HUAWEI] display isis system-id conflict
SystemID conflict for ISIS(1)
                           ------------------------------
                            Level-1 SystemID conflict 
                            -------------------------
                        Peer SystemID conflict detection 
                        -------------------------------- 
Conflict SystemID   : 2222.2222.2222 
Conflict Interface  : 100GE1/0/1
Begin Time          : 2014-10-31 10:42:31 
End Time            : Conflict may still persist 
Detect Result       : A system ID conflict may occur between the local and another devices. 

                            Level-2 SystemID conflict 
                            -------------------------
                       Remote SystemID conflict detection 
                        ---------------------------------- 
Hostname          RouterID          InterfaceAddr     NBR ID 
--                --                1.1.1.1           2222.2222.2222    
--                --                2.2.2.2           --                
Conflict SystemID   : 1111.1111.1111 
Begin Time          : 2014-10-30 19:56:29 
End Time            : Conflict may still persist 
Detect Result       : A system ID conflict may occur between two remote devices.

                        Peer SystemID conflict detection 
                        -------------------------------- 
Conflict SystemID   : 2222.2222.2222 
Conflict Interface  : 100GE1/0/1
Begin Time          : 2014-10-31 10:42:31 
End Time            : Conflict may still persist 
Detect Result       : A system ID conflict may occur between the local and another devices.

```

**Table 1** Description of the **display isis system-id conflict** command output
| Item | Description |
| --- | --- |
| Conflict SystemID | Conflicting system ID. |
| Conflict Interface | Interface on which a system ID conflict occurs. |
| Begin Time | Time when the conflict occurred. |
| End Time | Time when the conflict was cleared. If Conflict may still persist is displayed, the conflict has not yet cleared when you run the command. |
| Detect Result | System ID conflict detection result:   * A system ID conflict may occur between the local and another devices. * A system ID conflict may occur between two remote devices. * A system ID conflict may halt between the local and another devices. * A system ID conflict may halt between two remote devices. |
| Hostname | Dynamic hostname of the device on which a system ID conflict occurs. |
| RouterID | Router ID of the device on which a system ID conflict occurs. |
| InterfaceAddr | Interface IP address of the device on which a system ID conflict occurs. |
| NBR ID | Neighbor system ID of the device on which a system ID conflict occurs. |