Example for Configuring Dual-Homing of a Device to a Layer 2 Network Through an M-LAG in Root Bridge Mode
=========================================================================================================

Example for Configuring Dual-Homing of a Device to a Layer 2 Network Through an M-LAG in Root Bridge Mode

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564128877__en-us_task_0241512096_fig_dc_cfg_eth-trunk_008701), a server is dual-homed to a Layer 2 network through an M-LAG. As link aggregation between hosts and access devices only achieves link-level reliability, a fault on an access device may cause service interruption. As such, this cannot fulfill service reliability requirements. To address this problem, an M-LAG can be configured. When both M-LAG master and backup devices work properly, traffic is load balanced to them. In addition, services will not be affected if any of the two devices fails. As such, high service reliability is ensured. On an Ethernet network, a blocked interface cannot transmit DAD packets between M-LAG master and backup devices; therefore, a DFS group is configured and bound to the IP address of the Ethernet management interface on each of the two devices to ensure normal forwarding of DAD packets.

**Figure 1** Configuring dual-homing of a device to a Layer 2 network using an M-LAG![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, interface 5, interface 6, and interface 7 on DeviceA represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, 100GE 1/0/5, 100GE 1/0/6, and MEth0/0/0, respectively.

In this example, interface 1, interface 2, interface 3, interface 4, interface 5, interface 6, and interface 7 on DeviceB represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, 100GE 1/0/5, 100GE 1/0/6, and MEth0/0/0, respectively.

In this example, interface 1 and interface 2 on DeviceC represent 100GE 1/0/1 and 100GE 1/0/2, respectively.

In this example, interface 1 and interface 2 on DeviceD represent 100GE 1/0/1 and 100GE 1/0/2, respectively.

![](figure/en-us_image_0000001512689762.png)



#### Configuration Roadmap

1. Configure DeviceA and DeviceB as root bridges with the same bridge MAC address to ensure that both devices function as the root bridge on the Layer 2 network.
2. Configure IP addresses for the Ethernet management interface on DeviceA and DeviceB to ensure their Layer 3 connectivity so that DAD packets can be forwarded between them.
3. Configure M-LAG on DeviceA and DeviceB so that the server can be dual-homed to the M-LAG set up by DeviceA and DeviceB.

#### Procedure

1. Configure DeviceA and DeviceB as root bridges with the same bridge MAC address.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the downstream device dual-homed to the M-LAG member devices is a switching device, root protection must be configured.
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp root primary
   [*DeviceA] stp bridge-address 00e0-fc12-3458  //Configure the bridge MAC address of the root bridge (MAC address of the M-LAG master device).
   [*DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/2
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/5
   [*DeviceA-Eth-Trunk1] stp edged-port enable
   [*DeviceA-Eth-Trunk1] commit
   [~DeviceA-Eth-Trunk1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp root primary
   [*DeviceB] stp bridge-address 00e0-fc12-3458   //Configure the bridge MAC address of the root bridge.
   [*DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/2
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/5
   [*DeviceB-Eth-Trunk1] stp edged-port enable
   [*DeviceB-Eth-Trunk1] commit
   [~DeviceB-Eth-Trunk1] quit
   ```
2. Configure an IP address for the Ethernet management interface on DeviceA and DeviceB, respectively.
   
   
   
   Ensure that DeviceA and DeviceB can communicate at Layer 3 through their Ethernet management interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface meth 0/0/0
   [~DeviceA-MEth0/0/0] ip address 10.1.1.1 24
   [*DeviceA-MEth0/0/0] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface meth 0/0/0
   [~DeviceB-MEth0/0/0] ip address 10.1.1.2 24
   [*DeviceB-MEth0/0/0] quit
   [*DeviceB] commit
   ```
3. Create a DFS group on DeviceA and DeviceB and bind the IP address of the Ethernet management interface on each of the two devices to the DFS group.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] dfs-group 1
   [*DeviceA-dfs-group-1] dual-active detection source ip 10.1.1.1 peer 10.1.1.2
   [*DeviceA-dfs-group-1] priority 150
   [*DeviceA-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
   [*DeviceA-dfs-group-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] dfs-group 1
   [*DeviceB-dfs-group-1] dual-active detection source ip 10.1.1.2 peer 10.1.1.1
   [*DeviceB-dfs-group-1] priority 120
   [*DeviceB-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
   [*DeviceB-dfs-group-1] quit
   [*DeviceB] commit
   ```
4. Configure a peer-link between DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface eth-trunk 0
   [*DeviceA-Eth-Trunk0] mode lacp-static
   [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/3
   [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/4
   [*DeviceA-Eth-Trunk0] undo stp enable
   [*DeviceA-Eth-Trunk0] peer-link 1
   [*DeviceA-Eth-Trunk0] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 0
   [*DeviceB-Eth-Trunk0] mode lacp-static
   [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/3
   [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/4
   [*DeviceB-Eth-Trunk0] undo stp enable
   [*DeviceB-Eth-Trunk0] peer-link 1
   [*DeviceB-Eth-Trunk0] quit
   [*DeviceB] commit
   ```
5. Add the Eth-Trunk interfaces connecting DeviceA to the server and DeviceB to the server to VLAN 11 and bind the interfaces to the DFS group.
   
   
   
   The uplink interfaces that connect the server to DeviceA and DeviceB must be added to an Eth-Trunk interface, and the working mode of the Eth-Trunk interface must be the same as that of the Eth-Trunk interfaces on both devices. In this example, the Eth-Trunk interfaces on both devices are configured to work in static LACP mode.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] vlan batch 11
   [*DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] mode lacp-static
   [*DeviceA-Eth-Trunk1] port link-type access
   [*DeviceA-Eth-Trunk1] port default vlan 11
   [*DeviceA-Eth-Trunk1] dfs-group 1 m-lag 1
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] vlan batch 11
   [*DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] port link-type access
   [*DeviceB-Eth-Trunk1] port default vlan 11
   [*DeviceB-Eth-Trunk1] dfs-group 1 m-lag 1
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
6. Configure the link between DeviceA and DeviceC and the link between DeviceB and DeviceD, and configure the interface type and allowed VLAN.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface eth-trunk 2
   [*DeviceA-Eth-Trunk2] mode lacp-static
   [*DeviceA-Eth-Trunk2] port link-type trunk
   [*DeviceA-Eth-Trunk2] port trunk allow-pass vlan 11
   [*DeviceA-Eth-Trunk2] trunkport 100ge 1/0/1
   [*DeviceA-Eth-Trunk2] trunkport 100ge 1/0/6
   [*DeviceA-Eth-Trunk2] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 2
   [*DeviceB-Eth-Trunk2] mode lacp-static
   [*DeviceB-Eth-Trunk2] port link-type trunk
   [*DeviceB-Eth-Trunk2] port trunk allow-pass vlan 11
   [*DeviceB-Eth-Trunk2] trunkport 100ge 1/0/1
   [*DeviceB-Eth-Trunk2] trunkport 100ge 1/0/6
   [*DeviceB-Eth-Trunk2] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 11
   [~DeviceC] interface eth-trunk 2
   [*DeviceC-Eth-Trunk2] mode lacp-static
   [*DeviceC-Eth-Trunk2] port link-type trunk
   [*DeviceC-Eth-Trunk2] port trunk allow-pass vlan 11
   [*DeviceC-Eth-Trunk2] trunkport 100ge 1/0/1
   [*DeviceC-Eth-Trunk2] trunkport 100ge 1/0/2
   [*DeviceC-Eth-Trunk2] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] vlan batch 11
   [~DeviceD] interface eth-trunk 2
   [*DeviceD-Eth-Trunk2] mode lacp-static
   [*DeviceD-Eth-Trunk2] port link-type trunk
   [*DeviceD-Eth-Trunk2] port trunk allow-pass vlan 11
   [*DeviceD-Eth-Trunk2] trunkport 100ge 1/0/1
   [*DeviceD-Eth-Trunk2] trunkport 100ge 1/0/2
   [*DeviceD-Eth-Trunk2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Display information about the M-LAG with DFS group ID 1.
```
[~DeviceA] display dfs-group 1 m-lag
*                     : Local node
Heart beat state      : OK
Node 1 *
  Dfs-Group ID        : 1
  Priority            : 150
  Dual-active Address : 10.1.1.1
  VPN-Instance        : public net
  State               : Master
  Causation           : -
  System ID           : 00e0-fc12-3456
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
  System ID           : 00e0-fc12-3457
  SysName             : DeviceB
  Version             : V300R023C00
  Device Type         : CE6860-SAN
```

In the preceding command output, the **Heart beat state** field displays **OK**, indicating that the heartbeat status is normal. DeviceA is node 1 with a priority of 150 and serves as the M-LAG master device (the **State** field displays **Master**), whereas DeviceB is node 2 with a priority of 120 and serves as the M-LAG backup device (the **State** field displays **Backup**). In addition, the **Causation** field displays **-**, indicating that the M-LAG is set up successfully.

# Display M-LAG information on DeviceA.

```
[~DeviceA] display dfs-group 1 node 1 m-lag brief
* - Local node

M-Lag ID     Interface      Port State    Status                Consistency-check
       1     Eth-Trunk 1    Up            active(*)-active      --


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
```

# Display M-LAG information on DeviceB.

```
[~DeviceB] display dfs-group 1 node 2 m-lag brief
* - Local node

M-Lag ID     Interface      Port State    Status                Consistency-check
       1     Eth-Trunk 1    Up            active-active(*)      --


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
```

In the preceding command outputs, the **Port State** fields of node 1 and node 2 display **Up**, and the M-LAG status of node 1 and node 2 is **active**, indicating that the M-LAG configuration is correct.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  dfs-group 1
   priority 150
   dual-active detection source ip 10.1.1.1 peer 10.1.1.2
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%#
  #
  vlan batch 11
  #
  stp bridge-address 00e0-fc12-3458
  stp instance 0 root primary
  #
  interface MEth0/0/0
   ip address 10.1.1.1 255.255.255.0
  #
  interface Eth-Trunk0
   mode lacp-static
   stp disable
   peer-link 1
  #
  interface Eth-Trunk1
   port default vlan 11
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk2
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static 
  #
  interface 100GE1/0/1
   eth-trunk 2
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  interface 100GE1/0/3
   eth-trunk 0
  #
  interface 100GE1/0/4
   eth-trunk 0
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface 100GE1/0/6
   eth-trunk 2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  dfs-group 1
   priority 120
   dual-active detection source ip 10.1.1.2 peer 10.1.1.1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!=I9f8>C{!P_bhB31@7r-=jrS8c|_"(Bn~#=!!!!!!!!!!!!!!!9!!!!kx-6@.tGA(wAt/IQXl6>[g{6YlOi9$!!!!!!!!!!%+%#
  #
  vlan batch 11
  #
  stp bridge-address 00e0-fc12-3458
  stp root primary
  #
  interface MEth0/0/0
   ip address 10.1.1.2 255.255.255.0
  #
  interface Eth-Trunk0
   mode lacp-static
   stp disable
   peer-link 1
  #
  interface Eth-Trunk1
   port default vlan 11
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk2
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 2
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  interface 100GE1/0/3
   eth-trunk 0
  #
  interface 100GE1/0/4
   eth-trunk 0
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface 100GE1/0/6
   eth-trunk 2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 11
  #
  interface Eth-Trunk2
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 2
  #
  interface 100GE1/0/2
   eth-trunk 2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 11
  #
  interface Eth-Trunk2
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 2
  #
  interface 100GE1/0/2
   eth-trunk 2
  #
  return
  ```