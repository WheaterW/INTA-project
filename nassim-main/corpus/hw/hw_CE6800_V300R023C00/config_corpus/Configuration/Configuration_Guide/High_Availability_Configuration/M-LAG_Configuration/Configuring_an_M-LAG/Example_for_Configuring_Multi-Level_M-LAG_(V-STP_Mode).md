Example for Configuring Multi-Level M-LAG (V-STP Mode)
======================================================

Example for Configuring Multi-Level M-LAG (V-STP Mode)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001715064873__fig7709173194617), multi-level M-LAG ensures reliability, improves link utilization, and expands the network scale in dual-homing mode, meeting customer requirements. In addition, aggregation devices function as dual-active gateways, and core and aggregation devices are cross-connected to ensure device-level reliability. A server is connected to access devices in load balancing or active/standby mode. If load balancing mode is used for server access, you are advised to configure the M-LAG to work in dual-active mode. If active/standby mode is used for server access, you are advised to configure the M-LAG to work in active/standby mode. In this example, the server is connected to access devices in load balancing mode. M-LAG devices at the access and aggregation layers use independent links as DAD links to improve reliability.

**Figure 1** Network diagram for configuring multi-level M-LAG![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, interface 5, interface 6, and interface 7 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, 100GE 1/0/5, 100GE 1/0/6, and 100GE 1/0/7, respectively.


  
![](figure/en-us_image_0000002001229902.png)

**Table 1** Data plan
| Device Name | Interface | IP Address | Virtual MAC Address |
| --- | --- | --- | --- |
| DeviceA | 100GE1/0/4 | 10.1.1.1/24 | - |
| DeviceB | 100GE1/0/4 | 10.1.1.2/24 | - |
| DeviceC | 100GE1/0/1 | 10.4.1.1/24 | - |
| 100GE1/0/2 | 10.5.1.1/24 | - |
| VLANIF 11 | 10.3.1.1/24 | 0000-5e00-0110 |
| VLANIF 100 | 10.10.10.1/30 | - |
| 100GE1/0/5 | 10.2.1.1/24 | - |
| DeviceD | 100GE1/0/1 | 10.6.1.1/24 | - |
| 100GE1/0/2 | 10.7.1.1/24 | - |
| VLANIF 11 | 10.3.1.1/24 | 0000-5e00-0110 |
| VLANIF 100 | 10.10.10.2/30 | - |
| 100GE1/0/5 | 10.2.1.2/24 | - |
| DeviceE | 100GE1/0/1 | 10.4.1.2/24 | - |
| 100GE1/0/2 | 10.7.1.2/24 | - |
| DeviceF | 100GE1/0/1 | 10.6.1.2/24 | - |
| 100GE1/0/2 | 10.5.1.2/24 | - |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. On DeviceA and DeviceB at the access layer, configure M-LAG, links between the access and aggregation layers, and server access.
2. On DeviceC and DeviceD at the aggregation layer, configure M-LAG, links between the aggregation and access layers, Layer 3 gateways, and the egress network.
3. On DeviceE and DeviceF at the core layer, configure interface IP addresses and enable OSPF to implement Layer 3 communication with the aggregation layer.

#### Procedure

1. Configure DeviceA and DeviceB at the access layer.
   1. Configure M-LAG.
      
      
      
      # Configure M-LAG in V-STP mode.
      
      Configure DeviceA.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceA
      [*HUAWEI] commit
      [~DeviceA] stp mode rstp
      [*DeviceA] stp v-stp enable
      [*DeviceA] commit
      ```
      
      Configure DeviceB.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceB
      [*HUAWEI] commit
      [~DeviceB] stp mode rstp
      [*DeviceB] stp v-stp enable
      [*DeviceB] commit
      ```
      
      # Configure a DFS group and bind IP addresses to the DFS group.
      
      Configure DeviceA.
      
      ```
      [~DeviceA] dfs-group 1
      [*DeviceA-dfs-group-1] priority 150
      [*DeviceA-dfs-group-1] dual-active detection source ip 10.1.1.1 peer 10.1.1.2
      [*DeviceA-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceA-dfs-group-1] quit
      [*DeviceA] commit
      ```
      
      Configure DeviceB.
      
      ```
      [~DeviceB] dfs-group 1
      [*DeviceB-dfs-group-1] priority 120
      [*DeviceB-dfs-group-1] dual-active detection source ip 10.1.1.2 peer 10.1.1.1
      [*DeviceB-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceB-dfs-group-1] quit
      [*DeviceB] commit
      ```
      
      # Deploy an independent direct physical link for M-LAG heartbeat detection.
      
      Configure DeviceA.
      
      ```
      [~DeviceA] interface 100ge 1/0/4
      [~DeviceA-100GE1/0/4] undo portswitch
      [*DeviceA-100GE1/0/4] ip address 10.1.1.1 24
      [*DeviceA-100GE1/0/4] m-lag unpaired-port reserved
      [*DeviceA-100GE1/0/4] quit
      [*DeviceA] commit
      ```
      
      Configure DeviceB.
      
      ```
      [~DeviceB] interface 100ge 1/0/4
      [~DeviceB-100GE1/0/4] undo portswitch
      [*DeviceB-100GE1/0/4] ip address 10.1.1.2 24
      [*DeviceB-100GE1/0/4] m-lag unpaired-port reserved
      [*DeviceB-100GE1/0/4] quit
      [*DeviceB] commit
      ```
      
      # Configure peer-link interfaces in the M-LAG.
      
      Configure DeviceA.
      
      ```
      [~DeviceA] interface Eth-Trunk0
      [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/5
      [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/6
      [*DeviceA-Eth-Trunk0] mode lacp-static
      [*DeviceA-Eth-Trunk0] peer-link 1
      [*DeviceA-Eth-Trunk0] port vlan exclude 1
      [*DeviceA-Eth-Trunk0] quit
      [*DeviceA] commit
      ```
      
      Configure DeviceB.
      
      ```
      [~DeviceB] interface Eth-Trunk0
      [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/5
      [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/6
      [*DeviceB-Eth-Trunk0] mode lacp-static
      [*DeviceB-Eth-Trunk0] peer-link 1
      [*DeviceB-Eth-Trunk0] port vlan exclude 1
      [*DeviceB-Eth-Trunk0] quit
      [*DeviceB] commit
      ```
   2. Configure links between the access and aggregation layers.
      
      
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] vlan batch 11
      [*DeviceA] interface Eth-Trunk10
      [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/1
      [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2
      [*DeviceA-Eth-Trunk10] mode lacp-static
      [*DeviceA-Eth-Trunk10] port link-type trunk
      [*DeviceA-Eth-Trunk10] undo port trunk allow-pass vlan 1
      [*DeviceA-Eth-Trunk10] port trunk allow-pass vlan 11
      [*DeviceA-Eth-Trunk10] dfs-group 1 m-lag 10
      [*DeviceA-Eth-Trunk10] quit
      [*DeviceA] commit
      ```
      
      # Configure DeviceB.
      
      ```
      [~DeviceB] vlan batch 11
      [*DeviceB] interface Eth-Trunk10
      [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/1
      [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/2
      [*DeviceB-Eth-Trunk10] mode lacp-static
      [*DeviceB-Eth-Trunk10] port link-type trunk
      [*DeviceB-Eth-Trunk10] undo port trunk allow-pass vlan 1
      [*DeviceB-Eth-Trunk10] port trunk allow-pass vlan 11
      [*DeviceB-Eth-Trunk10] dfs-group 1 m-lag 10
      [*DeviceB-Eth-Trunk10] quit
      [*DeviceB] commit
      ```
   3. Configure server access.
      
      
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] interface Eth-Trunk1
      [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/3
      [*DeviceA-Eth-Trunk1] mode lacp-static
      [*DeviceA-Eth-Trunk1] port link-type trunk
      [*DeviceA-Eth-Trunk1] undo port trunk allow-pass vlan 1
      [*DeviceA-Eth-Trunk1] port trunk allow-pass vlan 11
      [*DeviceA-Eth-Trunk1] dfs-group 1 m-lag 1
      [*DeviceA-Eth-Trunk1] quit
      [*DeviceA] commit
      ```
      
      # Configure DeviceB.
      
      ```
      [~DeviceB] interface Eth-Trunk1
      [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/3
      [*DeviceB-Eth-Trunk1] mode lacp-static
      [*DeviceB-Eth-Trunk1] port link-type trunk
      [*DeviceB-Eth-Trunk1] undo port trunk allow-pass vlan 1
      [*DeviceB-Eth-Trunk1] port trunk allow-pass vlan 11
      [*DeviceB-Eth-Trunk1] dfs-group 1 m-lag 1
      [*DeviceB-Eth-Trunk1] quit
      [*DeviceB] commit
      ```
2. Configure DeviceC and DeviceD at the aggregation layer.
   1. Configure M-LAG.
      
      
      
      # Configure M-LAG in V-STP mode.
      
      Configure DeviceC.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceC
      [*HUAWEI] commit
      [~DeviceC] stp mode rstp
      [*DeviceC] stp v-stp enable
      [*DeviceC] commit
      ```
      
      Configure DeviceD.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceD
      [*HUAWEI] commit
      [~DeviceD] stp mode rstp
      [*DeviceD] stp v-stp enable
      [*DeviceD] commit
      ```
      
      # Configure a DFS group and bind IP addresses to the DFS group.
      
      Configure DeviceC.
      
      ```
      [~DeviceC] dfs-group 1
      [*DeviceC-dfs-group-1] priority 150
      [*DeviceC-dfs-group-1] dual-active detection source ip 10.2.1.1 peer 10.2.1.2
      [*DeviceC-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceC-dfs-group-1] quit
      [*DeviceC] commit
      ```
      
      Configure DeviceD.
      
      ```
      [~DeviceD] dfs-group 1
      [*DeviceD-dfs-group-1] priority 120
      [*DeviceD-dfs-group-1] dual-active detection source ip 10.2.1.2 peer 10.2.1.1
      [*DeviceD-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceD-dfs-group-1] quit
      [*DeviceD] commit
      ```
      
      # Deploy an independent direct physical link for M-LAG heartbeat detection.
      
      Configure DeviceC.
      
      ```
      [~DeviceC] interface 100ge 1/0/5
      [~DeviceC-100GE1/0/5] undo portswitch
      [*DeviceC-100GE1/0/5] ip address 10.2.1.1 24
      [*DeviceC-100GE1/0/5] m-lag unpaired-port reserved
      [*DeviceC-100GE1/0/5] quit
      [*DeviceC] commit
      ```
      
      Configure DeviceD.
      
      ```
      [~DeviceD] interface 100ge 1/0/5
      [~DeviceD-100GE1/0/5] undo portswitch
      [*DeviceD-100GE1/0/5] ip address 10.2.1.2 24
      [*DeviceD-100GE1/0/5] m-lag unpaired-port reserved
      [*DeviceD-100GE1/0/5] quit
      [*DeviceD] commit
      ```
      
      # Configure peer-link interfaces in the M-LAG.
      
      Configure DeviceC.
      
      ```
      [~DeviceC] interface Eth-Trunk0
      [*DeviceC-Eth-Trunk0] trunkport 100ge 1/0/6
      [*DeviceC-Eth-Trunk0] trunkport 100ge 1/0/7
      [*DeviceC-Eth-Trunk0] mode lacp-static
      [*DeviceC-Eth-Trunk0] peer-link 1
      [*DeviceC-Eth-Trunk0] port vlan exclude 1
      [*DeviceC-Eth-Trunk0] quit
      [*DeviceC] commit
      ```
      
      Configure DeviceD.
      
      ```
      [~DeviceD] interface Eth-Trunk0
      [*DeviceD-Eth-Trunk0] trunkport 100ge 1/0/6
      [*DeviceD-Eth-Trunk0] trunkport 100ge 1/0/7
      [*DeviceD-Eth-Trunk0] mode lacp-static
      [*DeviceD-Eth-Trunk0] peer-link 1
      [*DeviceD-Eth-Trunk0] port vlan exclude 1
      [*DeviceD-Eth-Trunk0] quit
      [*DeviceD] commit
      ```
   2. Configure links between the aggregation and access layers.
      
      
      
      # Configure DeviceC.
      
      ```
      [~DeviceC] vlan batch 11
      [*DeviceC] interface Eth-Trunk10
      [*DeviceC-Eth-Trunk10] trunkport 100ge 1/0/3
      [*DeviceC-Eth-Trunk10] trunkport 100ge 1/0/4
      [*DeviceC-Eth-Trunk10] mode lacp-static
      [*DeviceC-Eth-Trunk10] port link-type trunk
      [*DeviceC-Eth-Trunk10] undo port trunk allow-pass vlan 1
      [*DeviceC-Eth-Trunk10] port trunk allow-pass vlan 11
      [*DeviceC-Eth-Trunk10] dfs-group 1 m-lag 10
      [*DeviceC-Eth-Trunk10] quit
      [*DeviceC] commit
      ```
      
      # Configure DeviceD.
      
      ```
      [~DeviceD] vlan batch 11
      [*DeviceD] interface Eth-Trunk10
      [*DeviceD-Eth-Trunk10] trunkport 100ge 1/0/3
      [*DeviceD-Eth-Trunk10] trunkport 100ge 1/0/4
      [*DeviceD-Eth-Trunk10] mode lacp-static
      [*DeviceD-Eth-Trunk10] port link-type trunk
      [*DeviceD-Eth-Trunk10] undo port trunk allow-pass vlan 1
      [*DeviceD-Eth-Trunk10] port trunk allow-pass vlan 11
      [*DeviceD-Eth-Trunk10] dfs-group 1 m-lag 10
      [*DeviceD-Eth-Trunk10] quit
      [*DeviceD] commit
      ```
   3. Configure Layer 3 gateways. On DeviceC and DeviceD, configure the same IP addresses and MAC addresses for VLANIF interfaces so that the devices function as dual-active gateways for the access layer.
      
      
      
      # Configure DeviceC.
      
      ```
      [~DeviceC] interface vlanif 11
      [*DeviceC-Vlanif11] ip address 10.3.1.1 24
      [*DeviceC-Vlanif11] mac-address 0000-5e00-0110
      [*DeviceC-Vlanif11] quit
      [*DeviceC] commit
      ```
      
      # Configure DeviceD.
      
      ```
      [~DeviceD] interface vlanif 11
      [*DeviceD-Vlanif11] ip address 10.3.1.1 24
      [*DeviceD-Vlanif11] mac-address 0000-5e00-0110
      [*DeviceD-Vlanif11] quit
      [*DeviceD] commit
      ```
   4. Configure the egress network. Configure physical links of the peer-link as egress bypass links between DeviceC and DeviceD, and configure dedicated VLANIF interfaces for the peer-link for Layer 3 interconnection.
      
      
      
      # Configure DeviceC.
      
      ```
      [~DeviceC] interface 100ge 1/0/1
      [~DeviceC-100GE1/0/1] undo portswitch
      [*DeviceC-100GE1/0/1] ip address 10.4.1.1 24
      [*DeviceC-100GE1/0/1] quit
      [*DeviceC] interface 100ge 1/0/2
      [*DeviceC-100GE1/0/2] undo portswitch
      [*DeviceC-100GE1/0/2] ip address 10.5.1.1 24
      [*DeviceC-100GE1/0/2] quit
      [*DeviceC] vlan batch 100
      [*DeviceC] interface vlanif 100 
      [*DeviceC-Vlanif100] ip address 10.10.10.1 30
      [*DeviceC-Vlanif100] ospf cost 10000
      [*DeviceC-Vlanif100] quit
      [*DeviceC] ospf 1
      [*DeviceC-ospf-1] area 0
      [*DeviceC-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
      [*DeviceC-ospf-1-area-0.0.0.0] network 10.4.1.0 0.0.0.255
      [*DeviceC-ospf-1-area-0.0.0.0] network 10.5.1.0 0.0.0.255
      [*DeviceC-ospf-1-area-0.0.0.0] network 10.10.10.0 0.0.0.3
      [*DeviceC-ospf-1-area-0.0.0.0] quit
      [*DeviceC-ospf-1] quit
      [*DeviceC] commit
      ```
      
      # Configure DeviceD.
      
      ```
      [~DeviceD] interface 100ge 1/0/1
      [~DeviceD-100GE1/0/1] undo portswitch
      [*DeviceD-100GE1/0/1] ip address 10.6.1.1 24
      [*DeviceD-100GE1/0/1] quit
      [*DeviceD] interface 100ge 1/0/2
      [*DeviceD-100GE1/0/2] undo portswitch
      [*DeviceD-100GE1/0/2] ip address 10.7.1.1 24
      [*DeviceD-100GE1/0/2] quit
      [*DeviceD] vlan batch 100
      [*DeviceD] interface vlanif 100 
      [*DeviceD-Vlanif100] ip address 10.10.10.2 30
      [*DeviceD-Vlanif100] ospf cost 10000
      [*DeviceD-Vlanif100] quit
      [*DeviceD] ospf 1
      [*DeviceD-ospf-1] area 0
      [*DeviceD-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
      [*DeviceD-ospf-1-area-0.0.0.0] network 10.6.1.0 0.0.0.255
      [*DeviceD-ospf-1-area-0.0.0.0] network 10.7.1.0 0.0.0.255
      [*DeviceD-ospf-1-area-0.0.0.0] network 10.10.10.0 0.0.0.3
      [*DeviceD-ospf-1-area-0.0.0.0] quit
      [*DeviceD-ospf-1] quit
      [*DeviceD] commit
      ```
3. Configure DeviceE and DeviceF at the core layer.
   
   
   
   # Configure DeviceE.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceE
   [*HUAWEI] commit
   [~DeviceE] interface 100ge 1/0/1
   [~DeviceE-100GE1/0/1] undo portswitch
   [*DeviceE-100GE1/0/1] ip address 10.4.1.2 24
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100ge 1/0/2
   [*DeviceE-100GE1/0/2] undo portswitch
   [*DeviceE-100GE1/0/2] ip address 10.7.1.2 24
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] ospf 1
   [*DeviceE-ospf-1] area 0
   [*DeviceE-ospf-1-area-0.0.0.0] network 10.4.1.0 0.0.0.255
   [*DeviceE-ospf-1-area-0.0.0.0] network 10.7.1.0 0.0.0.255
   [*DeviceE-ospf-1-area-0.0.0.0] quit
   [*DeviceE-ospf-1] quit
   [*DeviceE] commit
   ```
   
   # Configure DeviceF.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceF
   [*HUAWEI] commit
   [~DeviceF] interface 100ge 1/0/1
   [~DeviceF-100GE1/0/1] undo portswitch
   [*DeviceF-100GE1/0/1] ip address 10.6.1.2 24
   [*DeviceF-100GE1/0/1] quit
   [*DeviceF] interface 100ge 1/0/2
   [*DeviceF-100GE1/0/2] undo portswitch
   [*DeviceF-100GE1/0/2] ip address 10.5.1.2 24
   [*DeviceF-100GE1/0/2] quit
   [*DeviceF] ospf 1
   [*DeviceF-ospf-1] area 0
   [*DeviceF-ospf-1-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   [*DeviceF-ospf-1-area-0.0.0.0] network 10.6.1.0 0.0.0.255
   [*DeviceF-ospf-1-area-0.0.0.0] quit
   [*DeviceF-ospf-1] quit
   [*DeviceF] commit
   ```

#### Verifying the Configuration

* Run the **display dfs-group 1 m-lag** command to check the M-LAG status. Under normal circumstances, the states of two member devices are displayed. One device is in Master state, and the other device is in Backup state.
  
  # Check the M-LAG status at the access layer.
  
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
  
  # Check the M-LAG status at the aggregation layer.
  
  ```
  [~DeviceC] display dfs-group 1 m-lag
  *                     : Local node
  Heart beat state      : OK
  Node 1 *                            
    Dfs-Group ID        : 1
    Priority            : 150
    Dual-active Address : 10.2.1.1
    VPN-Instance        : public net
    State               : Master
    Causation           : - 
    System ID           : 00e0-fc12-3459
    SysName             : DeviceC
    Version             : V300R023C00
    Device Type         : CE6860-SAN
  Node 2                            
    Dfs-Group ID        : 1
    Priority            : 120
    Dual-active Address : 10.2.1.2
    VPN-Instance        : public net
    State               : Backup
    Causation           : - 
    System ID           : 00e0-fc12-3460
    SysName             : DeviceD
    Version             : V300R023C00
    Device Type         : CE6860-SAN
  ```
* Run the **display dfs-group 1 node 1 m-lag** **brief** command to check the M-LAG Eth-Trunk status.
  
  # Check the M-LAG Eth-Trunk status on DeviceA.
  
  ```
  [~DeviceA] display dfs-group 1 node 1 m-lag brief
  * - Local node
  
  M-Lag ID     Interface      Port State    Status                Consistency-check
         1     Eth-Trunk 1    Up            active(*)-active      success
        10     Eth-Trunk 10   Up            active(*)-active      success
  ......
  ```
  
  # Check the M-LAG Eth-Trunk status on DeviceC.
  
  ```
  [~DeviceC] display dfs-group 1 node 1 m-lag brief
  * - Local node
  
  M-Lag ID     Interface      Port State    Status                Consistency-check
        10     Eth-Trunk 10   Up            active(*)-active      success
  ......
  ```

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
  stp mode rstp
  stp v-stp enable 
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 10
  #
  interface 100GE1/0/1
   eth-trunk 10
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/5
   eth-trunk 0
  #
  interface 100GE1/0/6
   eth-trunk 0
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
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%#
  #
  vlan batch 11
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 10
  #
  interface 100GE1/0/1
   eth-trunk 10
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/3
   eth-trunk 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/5
   eth-trunk 0
  #
  interface 100GE1/0/6
   eth-trunk 0
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  dfs-group 1
   priority 150
   dual-active detection source ip 10.2.1.1 peer 10.2.1.2
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%#
  #
  vlan batch 11 100
  #
  stp mode rstp
  stp v-stp enable 
  #
  interface Vlanif11
   ip address 10.3.1.1 255.255.255.0
   mac-address 0000-5e00-0110 
  #
  interface Vlanif100
   ip address 10.10.10.1 255.255.255.252
   ospf cost 10000
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.4.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.5.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 10
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/6
   eth-trunk 0
  #
  interface 100GE1/0/7
   eth-trunk 0
  #
  ospf 1
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.4.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
    network 10.10.10.0 0.0.0.3
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  dfs-group 1
   priority 120
   dual-active detection source ip 10.2.1.2 peer 10.2.1.1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%#
  #
  vlan batch 11 100
  #
  stp mode rstp
  stp v-stp enable 
  #
  interface Vlanif11
   ip address 10.3.1.1 255.255.255.0
   mac-address 0000-5e00-0110
  #
  interface Vlanif100
   ip address 10.10.10.2 255.255.255.252
   ospf cost 10000
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
   port vlan exclude 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 10
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.6.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.7.1.1 255.255.255.0
  #
  interface 100GE1/0/3
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 10
  #
  interface 100GE1/0/5
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/6
   eth-trunk 0
  #
  interface 100GE1/0/7
   eth-trunk 0
  #
  ospf 1
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
    network 10.10.10.0 0.0.0.3
  #
  return
  ```
* DeviceE
  ```
  #
  sysname DeviceE
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.4.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.7.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.4.1.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
  #
  return
  ```
* DeviceF
  ```
  #
  sysname DeviceF
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.5.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.6.1.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 10.5.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
  #
  return
  ```