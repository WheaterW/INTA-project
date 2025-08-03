Example for Configuring M-LAG Devices as DHCP Servers
=====================================================

Example for Configuring M-LAG Devices as DHCP Servers

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564126225__fig_dc_cfg_dhcp_009201), DeviceA and DeviceB form an M-LAG, which functions as a dual-active gateway for downstream servers. You need to enable the DHCP server function on both DeviceA and DeviceB to dynamically allocate IP addresses to the servers.

**Figure 1** Network diagram of configuring M-LAG devices as DHCP servers![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5, respectively.


  
![](figure/en-us_image_0000001513166166.png)

#### Precautions

This example applies only to ZTP deployment. For detailed configuration precautions when both the M-LAG and DHCP server are used, see "Configuration Precautions for DHCPv4."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure routes on DeviceA, DeviceB, and DeviceD to ensure Layer 3 connectivity.
2. Configure DeviceA and DeviceB to set up an M-LAG.
3. Configure an interconnection VLAN.
4. Configure IP and MAC addresses for VLANIF interfaces on DeviceA and DeviceB so that these devices function as dual-active gateways for access devices, and configure the DHCP server function on DeviceA and DeviceB.

#### Procedure

1. Configure routes on DeviceA, DeviceB, and DeviceD to ensure Layer 3 connectivity. OSPF is used as an example.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] ip address 10.1.1.1 32
   [*DeviceA-LoopBack0] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.1 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.1 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface loopback 0
   [*DeviceB-LoopBack0] ip address 10.1.1.2 32
   [*DeviceB-LoopBack0] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 192.168.2.1 24
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.2 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] interface 100ge 1/0/1
   [*DeviceD-100GE1/0/1] undo portswitch
   [*DeviceD-100GE1/0/1] ip address 192.168.1.2 24
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] ip address 192.168.2.2 24
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] ospf 1
   [*DeviceD-ospf-1] area 0
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*DeviceD-ospf-1-area-0.0.0.0] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
2. Configure DeviceA and DeviceB to set up an M-LAG.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] stp mode rstp
   [*DeviceA] stp v-stp enable
   [*DeviceA] dfs-group 1
   [*DeviceA-dfs-group-1] dual-active detection source ip 10.1.1.1 peer 10.1.1.2
   [*DeviceA-dfs-group-1] priority 150
   [*DeviceA-dfs-group-1] quit
   [*DeviceA] interface eth-trunk 0
   [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/4
   [*DeviceA-Eth-Trunk0] trunkport 100ge 1/0/5
   [*DeviceA-Eth-Trunk0] mode lacp-static
   [*DeviceA-Eth-Trunk0] peer-link 1
   [*DeviceA-Eth-Trunk0] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] stp mode rstp  
   [*DeviceB] stp v-stp enable
   [*DeviceB] dfs-group 1
   [*DeviceB-dfs-group-1] dual-active detection source ip 10.1.1.2 peer 10.1.1.1
   [*DeviceB-dfs-group-1] quit
   [*DeviceB] interface eth-trunk 0
   [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/4
   [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/5
   [*DeviceB-Eth-Trunk0] mode lacp-static
   [*DeviceB-Eth-Trunk0] peer-link 1
   [*DeviceB-Eth-Trunk0] quit
   [*DeviceB] commit
   ```
3. Configure an interconnection VLAN.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] vlan batch 10
   [*DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] mode lacp-static
   [*DeviceA-Eth-Trunk1] port link-type trunk
   [*DeviceA-Eth-Trunk1] undo port trunk allow-pass vlan 1
   [*DeviceA-Eth-Trunk1] port trunk allow-pass vlan 10
   [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/1
   [*DeviceA-Eth-Trunk1] dfs-group 1 m-lag 1
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] vlan batch 10
   [*DeviceB] interface eth-trunk 1
   [*SwitchB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] port link-type trunk
   [*DeviceB-Eth-Trunk1] undo port trunk allow-pass vlan 1
   [*DeviceB-Eth-Trunk1] port trunk allow-pass vlan 10
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/1
   [*DeviceB-Eth-Trunk1] dfs-group 1 m-lag 1
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceC
   [*HUAWEI] commit
   [~DeviceC] vlan batch 10
   [*DeviceC] interface eth-trunk 1
   [*DeviceC-Eth-Trunk1] mode lacp-static
   [*DeviceC-Eth-Trunk1] port link-type trunk
   [*DeviceC-Eth-Trunk1] undo port trunk allow-pass vlan 1
   [*DeviceC-Eth-Trunk1] port trunk allow-pass vlan 10
   [*DeviceC-Eth-Trunk1] trunkport 100ge 1/0/1
   [*DeviceC-Eth-Trunk1] trunkport 100ge 1/0/2
   [*DeviceC-Eth-Trunk1] quit
   [*DeviceC] interface 100ge 1/0/3
   [*DeviceC-100GE1/0/3] port link-type access
   [*DeviceC-100GE1/0/3] port default vlan 10
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
4. Configure IP and MAC addresses for VLANIF interfaces on DeviceA and DeviceB so that these devices function as dual-active gateways for access devices, and configure the DHCP server function on DeviceA and DeviceB. DeviceA and DeviceB must be configured with the same virtual IP address and virtual MAC address.
   
   
   
   # Configure DeviceA as the active-active gateway for access devices, enable the DHCP server function for the interface address pool, and assign an address range to the interface address pool.
   
   ```
   [~DeviceA] dhcp enable
   [*DeviceA] commit
   [~DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.2.1.1 24
   [*DeviceA-Vlanif10] mac-address 0000-5e00-0101
   [*DeviceA-Vlanif10] dhcp select interface
   [*DeviceA-Vlanif10] dhcp server ip-range 10.2.1.1 10.2.1.128
   [*DeviceA-Vlanif10] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB as the active-active gateway for access devices, enable the DHCP server function for the interface address pool, and assign an address range to the interface address pool.
   
   ```
   [~DeviceB] dhcp enable
   [*DeviceB] commit
   [~DeviceB] interface vlanif 10
   [*DeviceB-Vlanif10] ip address 10.2.1.1 24
   [*DeviceB-Vlanif10] mac-address 0000-5e00-0101
   [*DeviceB-Vlanif10] dhcp select interface
   [*DeviceB-Vlanif10] dhcp server ip-range 10.2.1.129 10.2.1.254
   [*DeviceB-Vlanif10] quit
   [*DeviceB] commit
   ```
5. Verify the configuration.
   
   
   
   Run the **display ip pool** command on DeviceA to check the IP address pool configuration.
   
   ```
   [~DeviceA] display ip pool
    -----------------------------------------------------------------------------
     Pool name      : pool1
     Pool number    : 0
     Position       : Local
     Status         : Unlocked
     Gateway        : 10.0.0.1
     Mask           : 255.255.255.0
     VPN instance   : --
   
     All IP pool address statistic
       Total       :253
       Used        :0          Idle        :125        Expired     :0
       Conflict    :0          Disable     :128
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
  #
  vlan batch 10
  #
  stp mode rstp
  stp v-stp enable
  #
  dhcp enable
  #
  interface Vlanif10
   ip address 10.2.1.1 255.255.255.0
   mac-address 0000-5e00-0101
   dhcp select interface
   dhcp server ip-range 10.2.1.1 10.2.1.128
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/4
    eth-trunk 0
  #
  interface 100GE1/0/5
    eth-trunk 0
  #
  interface LoopBack0
   ip address 10.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  dfs-group 1
   dual-active detection source ip 10.1.1.2 peer 10.1.1.1 
  #
  vlan batch 10
  #
  stp mode rstp
  stp v-stp enable
  #
  dhcp enable
  #
  interface Vlanif10
   ip address 10.2.1.1 255.255.255.0
   mac-address 0000-5e00-0101
   dhcp select interface
   dhcp server ip-range 10.2.1.129 10.2.1.254
  #
  interface Eth-Trunk0
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10
   mode lacp-static
   dfs-group 1 m-lag 1
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/4
    eth-trunk 0
  #
  interface 100GE1/0/5
    eth-trunk 0
  #
  interface LoopBack0
   ip address 10.1.1.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.2 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* DeviceC
  ```
  #
  sysname DeviceC
  #
  vlan batch 10
  #
  interface Eth-Trunk1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 1
  #
  interface 100GE1/0/2
   eth-trunk 1
  #
  interface 100GE1/0/3
    port default vlan 10
  #
  return
  ```
* DeviceD
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```