display dfs-group lacp system-id
================================

display dfs-group lacp system-id

Function
--------



The **display dfs-group lacp system-id** command displays the LACP M-LAG system ID and priority information.




Format
------

**display dfs-group** *dfs-group-id* **lacp** **system-id** **m-lag** *m-lag-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **m-lag** *m-lag-id* | Specifies the ID of an M-LAG. | The value is an integer ranging from 1 to 2048. |
| **dfs-group** *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display dfs-group lacp system-id command to check information about LACP M-LAG system ID and priority of both ends. You can also check the information about IFM.Only the backup device in an M-LAG synchronizes the system ID and priority of the master device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the LACP M-LAG system ID and priority information.
```
<HUAWEI> display dfs-group 1 lacp system-id m-lag 1
---------------------------------------------------------------------------                    
Information of m-lag lacp system id and priority                                               
---------------------------------------------------------------------------                    
Local effective system id     : 00e0-fc12-3456                                                 
Local effective priority      : 20                                                             
Remote global system id       : 00e0-fc12-3456                                                 
Remote global priority        : 20                                                             
Send system id to remote      : 1                                                              
Receive system id from remote : 1                                                              
Send system id to IFM         : 1
---------------------------------------------------------------------------

```

**Table 1** Description of the **display dfs-group lacp system-id** command output
| Item | Description |
| --- | --- |
| Local effective system id | LACP M-LAG system ID that takes effect on the local device. Note that if DFS pairing fails and the system ID is configured only in the system view on the backup device, the configuration in the system view takes effect. If the system ID has been configured in the system view on the backup device and a system ID is configured on the M-LAG Eth-Trunk interface, the system ID configured on the M-LAG Eth-Trunk interface takes effect. After DFS pairing succeeds, the LACP M-LAG system ID that takes effect on the backup device is the system ID of the master device. When the DFS pairing status changes from successful to failure, check whether the LACP M-LAG system ID switchback is allowed. If the switchback is allowed, the system ID configured in the local system view is used. If the switchback is not allowed, the system ID synchronized from the master device is used. After the pairing is successful, you can change the priority of the DFS group to switch the master and backup devices in the DFS group. The LACP system ID that takes effect on the local end is not changed. |
| Local effective priority | Priority that takes effect on the local device. If DFS pairing fails and the priority is configured only in the system view on the backup device, the priority configured in the system view takes effect. If the priority has been configured in the system view on the backup device and a priority is configured on the M-LAG Eth-Trunk interface, the priority configured on the M-LAG Eth-Trunk interface takes effect. It should be noted that after the devices are paired successfully, the priority of the configuration that takes effect on the backup device is synchronized from the master device. When the DFS pairing status changes from successful to failure, check whether the switchback is allowed. If the switchback is allowed, the priority configured in the local system view is used. If the switchback is not allowed, the priority synchronized from the master device is used. After the pairing succeeds, you can change the priority of the DFS group to switch the master and backup devices in the DFS group. The LACP priority that takes effect on the local end is not changed. |
| Remote global system id | Global LACP M-LAG system ID of the peer end. When the local system ID takes effect, 0000-0000-0000 is displayed. |
| Remote global priority | Global priority of the peer end. When the local priority takes effect, 0 is displayed. |
| Send system id to remote | Number of protocol packets sent from the system ID of the local LACP M-LAG to the peer end. |
| Send system id to IFM | Number of messages sent to the IFM module. |
| Receive system id from remote | Number of system ID packets received by the local end from the peer end. |