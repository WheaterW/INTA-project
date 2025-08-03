display dfs-group
=================

display dfs-group

Function
--------



The **display dfs-group** command displays M-LAG information.




Format
------

**display dfs-group** *dfs-group-id* **m-lag**

**display dfs-group** *dfs-group-id* **node** *node-id* **m-lag**

**display dfs-group** *dfs-group-id* **peer-link**

**display dfs-group** [ *dfs-group-id* ] [ **node** *node-id* ] **m-lag** **brief**

**display dfs-group** [ *dfs-group-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dfs-group-id* | Specifies the ID of a DFS group. | The value is 1. |
| **m-lag** | Specifies multi-chassis link aggregation. | - |
| **node** *node-id* | Specifies the ID of a node. | The value is 1 or 2. |
| **peer-link** | Specifies peer link information. | - |
| **brief** | Brief information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display dfs-group** command displays information about all M-LAG nodes, including information about a user-side interface on a node and pairing information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display peer-link information.
```
<HUAWEI> display dfs-group 1 peer-link
Peer-link information
-----------------------------------------------------------------
Total Interface(s): 1
Peer-link Id      : 1
Port Name         : Eth-Trunk0
Port State        : Down
Link Type         : Physical link

```

# Display information about the M-LAG with DFS group 1 and node 1.
```
<HUAWEI> display dfs-group 1 node 1 m-lag brief
* - Local node  
                                                                                                                  
M-Lag ID     Interface      Port State    Status                Consistency-check            
       1     Eth-Trunk 40   Up            active(*)-active      success                      
       5     Eth-Trunk 41   Up            active(*)-inactive    failed(5)                    
                                                                                             
Failed reason:                                                                               
    1 -- Relationship between vlan and port is inconsistent                                  
    2 -- STP configuration under the port is inconsistent                                    
    3 -- STP port priority configuration is inconsistent                                     
    4 -- LACP mode of M-LAG is inconsistent                                                  
    5 -- M-LAG configuration is inconsistent                                                 
    6 -- The number of M-LAG members is inconsistent
    7 -- LACP system-id of M-LAG is inconsistent
    8 -- LACP priority of M-LAG is inconsistent
    9 -- STP port edged configuration is inconsistent
    10 -- M-LAG mode configuration is inconsistent
<HUAWEI> display dfs-group 1 node 1 m-lag
* - Local node                                                                           
                                                                                         
M-Lag ID          : 1                                                                    
Interface         : Eth-Trunk 101                                                        
Port State        : Up                                                                 
Status            : active(*)-active                                                 
Member Port Role  : Master(*)-Backup

```

# Display information about the M-LAG with DFS group 1.
```
<HUAWEI> display dfs-group 1 m-lag
*                     : Local node
Heart beat state      : OK
Node 1 *
  Dfs-Group ID        : 1
  Priority            : 150
  Dual-active Address : 10.1.1.1
  VPN-Instance        : public net 
  State               : Master
  Causation           : -
  System ID           : 00e0-fc12-3457
  SysName             : DeviceA
  Version             : V300R023C00
  Device Type         : CE6860-SAN
Node 2
  Dfs-Group ID        : 1
  Priority            : 120
  Dual-active Address : 10.1.1.2
  VPN-Instance        : public net 
  State               : Backup
  Causation           : -
  System ID           : 00e0-fc12-3458
  SysName             : DeviceB
  Version             : V300R023C00
  Device Type         : CE6860-SAN

```

# Display information about DFS group 1.
```
<HUAWEI> display dfs-group
  Dfs-Group ID        : 1
  Priority            : 100
  Dual-active Address : 192.168.1.1
  VPN-Instance        : public net
  System ID           : 00e0-fc12-3456
  SysName             : DeviceA
  Up-delay/Interval   : 240/0
  Switch-delay        : 0

  Configuration consistency check: failed
  Type 1 configuration: Global STP configuration is inconsistent
                        V-STP configuration is inconsistent
                        LACP system-id of M-LAG is inconsistent
                        LACP priority of M-LAG is inconsistent
                        PEER-LINK STP configuration is inconsistent
                        PEER-LINK LACP configuration is inconsistent
                        STP port edged configuration is inconsistent
  Type 2 configuration: BD configuration is inconsistent
                        BDIF configuration is inconsistent
                        VLAN configuration is inconsistent
                        M-LAG configuration is inconsistent
                        VLANIF configuration is inconsistent
                        M-LAG IP configuration is consistent
                        VLANIF reserved for vxlan bypass configuration is consistent
                        PEER-LINK VLAN configuration is inconsistent
                        Election mode configuration is inconsistent

```

# Display information about DFS group 1 (for the CE6820H, CE6820H-K, CE6820S, and CE6885-LL in low latency mode).
```
<HUAWEI> display dfs-group
  Dfs-Group ID        : 1
  Priority            : 100
  Dual-active Address : 192.168.1.1
  VPN-Instance        : public net
  System ID           : 00e0-fc12-3456
  SysName             : HUAWEI
  Up-delay/Interval   : 240/0
  Switch-delay        : 0

  Configuration consistency check: failed
  Type 1 configuration: Global STP configuration is inconsistent
                        V-STP configuration is inconsistent
                        LACP system-id of M-LAG is inconsistent
                        LACP priority of M-LAG is inconsistent
                        PEER-LINK STP configuration is inconsistent
                        PEER-LINK LACP configuration is inconsistent
                        STP port edged configuration is inconsistent
  Type 2 configuration: VLAN configuration is inconsistent
                        M-LAG configuration is inconsistent
                        VLANIF configuration is inconsistent
                        M-LAG IP configuration is consistent
                        VLANIF reserved for vxlan bypass configuration is consistent
                        PEER-LINK VLAN configuration is inconsistent
                        Election mode configuration is inconsistent

```

**Table 1** Description of the **display dfs-group** command output
| Item | Description |
| --- | --- |
| Peer-link information | Peer-link information. |
| Peer-link Id | ID of the peer-link. |
| Total Interface(s) | Number of interfaces on the peer-link. |
| Port State | Port status:   * Down. * Up. |
| Port Name | Name of a port. |
| State | Device status:  Master.  Backup. |
| Link Type | Peer-link connection type:   * Physical link. * Virtual link. |
| Type 1 configuration | Type 1 configuration type. |
| Type 2 configuration | The configuration type is type 2. |
| \* | Local node. |
| \* - Local node | Local node. |
| M-Lag ID | ID of the M-LAG. |
| Interface | Corresponding user-side Eth-Trunk. |
| Status | Whether the traffic is reachable:   * active: Traffic is reachable. * inactive: Traffic is unreachable. |
| Consistency-check | Whether the configuration consistency check is successful:   * 1 success: The check is successful. * 2 failed(n): The check fails. n indicates the code of the failure cause. * 3 -: The consistency check is disabled. |
| Failed reason | Cause of the configuration consistency check failure. |
| Member Port Role | Status of a member interface:  1 Master: The M-LAG member interface is in the master state.  2 Backup: The M-LAG member interface is in the backup state.  3 Invalid: The state is invalid. |
| Heart beat state | Heartbeat status:   * OK: The heartbeat status is online. * Lost: The heartbeat status is offline. |
| Dfs-Group ID | DFS group ID. |
| Priority | Priority of the DFS group. |
| Dual-active Address | Dual-active IP address. |
| Address | IP address bound to the DFS group. |
| VPN-Instance | Vpn instance. |
| Causation | Failure cause:  1 -: The negotiation is successful.  2 NOPEERLINK: No peer-link is configured.  3 NOADDRESS: No IP address is bound.  4 SAMEMAC: The source MAC addresses of protocol packets are the same.  5 TYPEMISMATCH: The bound address type is not matched.  6 TIMEOUT: Protocol packet receiving times out, that is, no protocol packet is received.  7 PEERLINKDOWN: The peer-link is down.  8 DETECT: The local device can receive Hello packets from the remote device but cannot receive information packets from it.  9 AUTHENTICATION FAILED: The device authentication for DFS group pairing fails.  10 VERSIONMISMATCH: The versions do not match.  11 NOAUTHENTICATION: No authentication password is configured.  12 DEVICETYPEMISMATCH: The device types do not match.  13 PEERLINKTYPEMISMATCH: The peer-link types do not match. |
| System ID | System MAC address. |
| SysName | Device name. |
| Version | Device version. |
| Device Type | Device series. |
| Up-delay/Interval | Up-delay: Delay for the M-LAG member interface to report the Up event.  Interval: Automatic recovery interval between M-LAG member interfaces based on the delay in reporting the Up event. |
| Switch-delay | LACP M-LAG system ID switching delay. |
| Configuration consistency check | M-LAG configuration consistency check result:  success: The check is successful.  failed: The check fails.  --: The consistency check is disabled. |