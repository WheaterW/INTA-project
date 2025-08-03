Example for Configuring Dual-Homing of a Device to a Layer 3 Network Through an M-LAG in V-STP Mode (IPv6)
==========================================================================================================

Example for Configuring Dual-Homing of a Device to a Layer 3 Network Through an M-LAG in V-STP Mode (IPv6)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000002050368517__fig1327610128711), a device is dual-homed to a Layer 3 network through an M-LAG, with the following requirements:

* High reliability: If one access link fails, traffic needs to be quickly switched to the other link.
* High bandwidth utilization: Both access links are in active state and can load balance traffic.

**Figure 1** Network diagram for dual-homing a device to a Layer 3 network through an M-LAG![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, interface 5, and interface 6 on DeviceA represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, 100GE 1/0/5, and MEth0/0/0, respectively.

In this example, interface 1, interface 2, interface 3, interface 4, interface 5, and interface 6 on DeviceB represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, 100GE 1/0/5, and MEth0/0/0, respectively.

In this example, interface 1 and interface 2 on DeviceC represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000002124246692.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On DeviceD, bind uplink interfaces to an Eth-Trunk interface.
2. On DeviceA and DeviceB, configure V-STP, create a DFS group, bind IPv6 addresses of management interfaces to the DFS group, and configure peer-link interfaces and M-LAG member interfaces.
3. On DeviceA and DeviceB, configure IPv6 and MAC addresses for VLANIF interfaces so that DeviceA and DeviceB function as dual-active gateways for access devices.
4. On DeviceA, DeviceB, and DeviceC, configure OSPFv3 to ensure Layer 3 connectivity.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent an interface from being blocked by a spanning tree protocol in a V-STP scenario, you can configure main interfaces to implement Layer 3 connectivity or disable the spanning tree protocol on the device on the IP network side.
5. On DeviceA and DeviceB, add uplink and downlink interfaces to a Monitor Link group to prevent user-side traffic forwarding failures and traffic loss due to possible uplink faults.

#### Procedure

1. On DeviceD, bind uplink interfaces to an Eth-Trunk interface.
   
   
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] vlan batch 11
   [*DeviceD] interface eth-trunk 20
   [*DeviceD-Eth-Trunk20] mode lacp-static
   [*DeviceD-Eth-Trunk20] port link-type trunk
   [*DeviceD-Eth-Trunk20] port trunk allow-pass vlan 11
   [*DeviceD-Eth-Trunk20] trunkport 100ge 1/0/1 to 1/0/4
   [*DeviceD-Eth-Trunk20] quit
   [*DeviceD] commit
   ```
2. On DeviceA and DeviceB, configure V-STP, create a DFS group, bind IPv6 addresses of management interfaces to the DFS group, and configure peer-link interfaces and M-LAG member interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] stp mode rstp
   [*DeviceA] stp v-stp enable
   [*DeviceA] commit
   [~DeviceA] interface meth 0/0/0
   [~DeviceA-MEth0/0/0] ipv6 enable
   [*DeviceA-MEth0/0/0] ipv6 address 2001:db8:200:1::1 64
   [*DeviceA-MEth0/0/0] quit
   [*DeviceA] dfs-group 1
   [*DeviceA-dfs-group-1] dual-active detection source ipv6 2001:db8:200:1::1 peer 2001:db8:200:1::2
   [*DeviceA-dfs-group-1] priority 150
   [*DeviceA-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
   [*DeviceA-dfs-group-1] quit
   [*DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/4
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/5
   [*DeviceA-Eth-Trunk1] mode lacp-static
   [*DeviceA-Eth-Trunk1] peer-link 1
   [*DeviceA-Eth-Trunk1] port vlan exclude 1
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] vlan batch 11
   [*DeviceA] interface eth-trunk 10
   [*DeviceA-Eth-Trunk10] mode lacp-static
   [*DeviceA-Eth-Trunk10] port link-type trunk
   [*DeviceA-Eth-Trunk10] port trunk allow-pass vlan 11
   [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2
   [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/3
   [*DeviceA-Eth-Trunk10] dfs-group 1 m-lag 1
   [*DeviceA-Eth-Trunk10] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] stp mode rstp
   [*DeviceB] stp v-stp enable
   [*DeviceB] commit
   [~DeviceB] interface meth 0/0/0
   [~DeviceB-MEth0/0/0] ipv6 enable
   [*DeviceB-MEth0/0/0] ipv6 address 2001:db8:200:1::2 64
   [*DeviceB-MEth0/0/0] quit
   [*DeviceB] dfs-group 1
   [*DeviceB-dfs-group-1] dual-active detection source ipv6 2001:db8:200:1::2 peer 2001:db8:200:1::1
   [*DeviceB-dfs-group-1] priority 120
   [*DeviceB-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
   [*DeviceB-dfs-group-1] quit
   [*DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/4
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/5
   [*DeviceB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] peer-link 1
   [*DeviceB-Eth-Trunk1] port vlan exclude 1
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] vlan batch 11
   [*DeviceB] interface eth-trunk 10
   [*DeviceB-Eth-Trunk10] mode lacp-static
   [*DeviceB-Eth-Trunk10] port link-type trunk
   [*DeviceB-Eth-Trunk10] port trunk allow-pass vlan 11
   [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/2
   [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/3
   [*DeviceB-Eth-Trunk10] dfs-group 1 m-lag 1
   [*DeviceB-Eth-Trunk10] quit
   [*DeviceB] commit
   ```
3. On DeviceA and DeviceB, configure IPv6 and MAC addresses for VLANIF interfaces so that DeviceA and DeviceB function as dual-active gateways for access devices.
   
   
   
   DeviceA and DeviceB must be configured with the same virtual IPv6 address and virtual MAC address.
   
   # Configure DeviceA.
   ```
   [~DeviceA] interface vlanif 11
   [*DeviceA-Vlanif11] ipv6 enable
   [*DeviceA-Vlanif11] ipv6 address 2001:db8:2:1::1 64
   [*DeviceA-Vlanif11] mac-address 0000-5e00-0101
   [*DeviceA-Vlanif11] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] interface vlanif 11
   [*DeviceB-Vlanif11] ipv6 enable
   [*DeviceB-Vlanif11] ipv6 address 2001:db8:2:1::1 64
   [*DeviceB-Vlanif11] mac-address 0000-5e00-0101
   [*DeviceB-Vlanif11] quit
   [*DeviceB] commit
   ```
4. On DeviceA, DeviceB, and DeviceC, configure OSPFv3 to ensure Layer 3 connectivity. The ID of the OSPFv3 area to which DeviceA, DeviceB, and DeviceC belong must be different from the ID of the OSPFv3 area to which DeviceA, DeviceB, and DeviceD belong.
   
   # Configure DeviceA.
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:3:1::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] area 0
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   [*DeviceA-ospfv3-1] area 1
   [*DeviceA-ospfv3-1-area-0.0.0.1] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] ospfv3 1 area 0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 11
   [*DeviceA-Vlanif11] ospfv3 1 area 1
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:4:1::1 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] area 0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] area 1
   [*DeviceB-ospfv3-1-area-0.0.0.1] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] ospfv3 1 area 0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface vlanif 11
   [*DeviceB-Vlanif11] ospfv3 1 area 1
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] undo portswitch
   [*DeviceC-100GE1/0/1] ipv6 enable
   [*DeviceC-100GE1/0/1] ipv6 address 2001:db8:3:1::2 64
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ipv6 enable
   [*DeviceC-100GE1/0/2] ipv6 address 2001:db8:4:1::2 64
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] area 0
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   [~DeviceC] interface 100ge 1/0/1
   [~DeviceC-100GE1/0/1] ospfv3 1 area 0
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] ospfv3 1 area 0
   [*DeviceC] commit
   ```
5. On DeviceA and DeviceB, add uplink and downlink interfaces to a Monitor Link group.
   
   # Configure DeviceA.
   ```
   [~DeviceA] monitor-link group 1
   [*DeviceA-mtlk-group1] port 100ge 1/0/1 uplink
   [*DeviceA-mtlk-group1] port eth-trunk 10 downlink 1
   [*DeviceA-mtlk-group1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   ```
   [~DeviceB] monitor-link group 1
   [*DeviceB-mtlk-group1] port 100ge 1/0/1 uplink
   [*DeviceB-mtlk-group1] port eth-trunk 10 downlink 1
   [*DeviceB-mtlk-group1] quit
   [*DeviceB] commit
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
  Dual-active Address : 2001:db8:200:1::1
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
  Dual-active Address : 2001:db8:200:1::2
  VPN-Instance        : public net
  State               : Backup
  Causation           : -
  System ID           : 00e0-fc12-3458
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
       1     Eth-Trunk 10   Up            active(*)-active      --              


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
       1     Eth-Trunk 10   Up            active-active(*)      -- 


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
   dual-active detection source ipv6 2001:db8:200:1::1 peer 2001:db8:200:1::2
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%#
  #
  vlan batch 11
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif11
   ipv6 enable
   ipv6 address 2001:db8:2:1::1/64
   mac-address 0000-5e00-0101
   ospfv3 1 area 1
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ipv6 enable
   ipv6 address 2001:db8:200:1::1/64
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3:1::1/64
   ospfv3 1 area 0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port Eth-Trunk10 downlink 1
  #
  ospfv3 1
   area 0.0.0.0
   area 0.0.0.1
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
   dual-active detection source ipv6 2001:db8:200:1::2 peer 2001:db8:200:1::1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!=I9f8>C{!P_bhB31@7r-=jrS8c|_"(Bn~#=!!!!!!!!!!!!!!!9!!!!kx-6@.tGA(wAt/IQXl6>[g{6YlOi9$!!!!!!!!!!%+%#
  #
  vlan batch 11
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif11
   ipv6 enable
   ipv6 address 2001:db8:2:1::1/64
   ospfv3 1 area 1
   mac-address 0000-5e00-0101  
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ipv6 enable
   ipv6 address 2001:db8:200:1::2/64
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4:1::1/64
   ospfv3 1 area 0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port Eth-Trunk10 downlink 1
  #
  ospfv3 1
   area 0.0.0.0
   area 0.0.0.1
  #
  return
  
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3:1::2/64
   ospfv3 1 area 0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4:1::2/64
   ospfv3 1 area 0
  #
  ospfv3 1
   area 0.0.0.0
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
  interface Eth-Trunk20
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 20
  #
  interface 100GE1/0/2
   eth-trunk 20
  #
  interface 100GE1/0/3
   eth-trunk 20
  #
  interface 100GE1/0/4
   eth-trunk 20
  #
  return
  
  ```