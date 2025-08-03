display fwm vlan statistics
===========================

display fwm vlan statistics

Function
--------



The **display fwm vlan statistics** command displays VLAN resource statistics.




Format
------

**display fwm vlan statistics** [ **slot** *slot-id* | **ipc** | **resource-apply** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies a Slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **ipc** | Displays statistics about IPC connections,disconnections and messages. | - |
| **resource-apply** | Displays statistics about multicast resources. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

VLAN services may fail to be configured when VLAN resources on a device are insufficient. When locating VLAN service faults, run the **display fwm vlan statistics** command to view VLAN resource statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display VLAN resource statistics.
```
<HUAWEI> display fwm vlan statistics
----------------------------------------------------------------------                                                              
                     Vlan Basic Info Statistic                                                                                      
----------------------------------------------------------------------                                                              
Slot                         :                 01                                                                                   
McIdApplySuccess             :                  1                                                                                   
McIdApplyFail                :                  0                                                                                   
IpcHup                       :                  0                                                                                   
IpcConnect                   :                  0                                                                                   
----------------------------------------------------------------------

```

# Display statistics about IPC connections,disconnections and messages in VLANs.
```
<HUAWEI> display fwm vlan statistics ipc
----------------------------------------------------------------------
Slot IpcHup/LastTime            IpcConnect/LastTime
----------------------------------------------------------------------
  01      0/1970-01-01 00:00:00          0/1970-01-01 00:00:00
----------------------------------------------------------------------
----------------------------------------------------------------------                                                              
                     Vlan IPC Couter Statistic                                                                                      
----------------------------------------------------------------------                                                              
Vlan IPC FwdRes Smooth Num   :                  2                                                                                   
Vlan IPC Cfg    Smooth Num   :                  2                                                                                   
Vlan IPC PVMap  Smooth Num   :                  4                                                                                   
Vlan IPC PVCfg  Smooth Num   :                  2                                                                                   
Vlan IPC FwdRes Verify Num   :                402                                                                                   
Vlan IPC Cfg    Verify Num   :                402                                                                                   
Vlan IPC PVMap  Verify Num   :               3819                                                                                   
Vlan IPC PVCfg  Verify Num   :               3819                                                                                   
----------------------------------------------------------------------

```

# Display statistics about multicast resources in VLANs.
```
<HUAWEI> display fwm vlan statistics resource-apply
----------------------------------------------------------------------
Slot McIdSuccess/LastTime            McIdFail/LastTime
----------------------------------------------------------------------
  01        4094/2020-10-20 16:36:55        0/1970-01-01 00:00:00
----------------------------------------------------------------------

```

**Table 1** Description of the **display fwm vlan statistics** command output
| Item | Description |
| --- | --- |
| Vlan IPC FwdRes Smooth Num | Number of forward resource smooth IPC message. |
| Vlan IPC Cfg Smooth Num | Number of vlan configuration smooth IPC message. |
| Vlan IPC PVMap Smooth Num | Number of port and vlan map smooth IPC message. |
| Vlan IPC PVCfg Smooth Num | Number of port and vlan configuration smooth IPC message. |
| Vlan IPC FwdRes Verify Num | Number of forward resource verify IPC message. |
| Vlan IPC Cfg Verify Num | Number of vlan configuration verify IPC message. |
| Vlan IPC PVMap Verify Num | Number of port and vlan map verify IPC message. |
| Vlan IPC PVCfg Verify Num | Number of port and vlan configuration verify IPC message. |
| Slot | Slot. |
| McIdApplySuccess | Number of successful multicast resource applications. |
| McIdApplyFail | Number of failed multicast resource applications. |
| IpcHup | Number of IPC disconnections. |
| IpcConnect | Number of IPC connection setup times. |
| LastTime | Last time when an IPC connection is set up or torn down, or when multicast resources are successfully applied or fail to be applied. |
| McIdSuccess | Number of successful multicast resource applications. |
| McIdFail | Number of failed multicast resource applications. |