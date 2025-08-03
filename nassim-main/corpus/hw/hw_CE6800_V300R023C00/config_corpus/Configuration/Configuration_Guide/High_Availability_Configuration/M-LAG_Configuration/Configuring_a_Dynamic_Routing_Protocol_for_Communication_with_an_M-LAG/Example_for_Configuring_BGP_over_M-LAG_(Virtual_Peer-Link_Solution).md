Example for Configuring BGP over M-LAG (Virtual Peer-Link Solution)
===================================================================

Example for Configuring BGP over M-LAG (Virtual Peer-Link Solution)

#### Networking Requirements

![](../public_sys-resources/note_3.0-en-us.png) 

This configuration example is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ.

On the network shown in [Figure 1](#EN-US_TASK_0000001512849250__en-us_task_0241512178_en-us_task_0141119105_fig_dc_cfg_vxlan_cfgcase_000601), DeviceA, DeviceB, and DeviceC constitute an M-LAG. The M-LAG member interfaces on DeviceB and DeviceC support dynamic routing protocols. A dynamic routing protocol is configured on DeviceA so that it can communicate with the M-LAG through Layer 3 routes.

**Figure 1** Configuring BGP over M-LAG (virtual peer-link solution)![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001512689882.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure DeviceA, DeviceB, and DeviceC to establish an M-LAG.
   * Configure V-STP on DeviceB and DeviceC.
   * Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group.
   * Configure BGP on DeviceB, DeviceC, and DeviceD so that EBGP peer relationships can be established between DeviceD and DeviceB and between DeviceD and DeviceC. BGP is used to advertise dedicated routing information for establishing a bypass VXLAN tunnel.
   * Configure a virtual peer-link between DeviceB and DeviceC.
   * Configure a reserved VNI for the M-LAG, and configure a bypass VXLAN tunnel.
   * Configure M-LAG member interfaces on DeviceB and DeviceC and an Eth-Trunk interface on DeviceA.
   * Configure Monitor Link on DeviceB and DeviceC.
2. Configure BGP over M-LAG.
   * Configure IPv4 addresses for BGP over M-LAG on DeviceB and DeviceC.
   * Configure DeviceA to establish BGP peer relationships with M-LAG member devices (DeviceB and DeviceC).

![](../public_sys-resources/note_3.0-en-us.png) 

* DeviceB and DeviceC have the same AS number. To ensure that M-LAG devices advertise bypass VXLAN tunnel information, disable the function of checking duplicate AS numbers on DeviceB for the BGP peer relationship with DeviceD. The configuration on DeviceC is similar.
* To prevent the backup device from shutting down the outbound interface of the bypass VXLAN tunnel due to a negotiation exception on M-LAG devices, the outbound interface of the bypass VXLAN tunnel must be configured as an M-LAG reserved interface.
* Configure different M-LAG IPv4 addresses on DeviceB and DeviceC. Otherwise, peer relationships of the routing protocol cannot be established.


#### Procedure

1. Configure DeviceA, DeviceB, and DeviceC to establish an M-LAG.
   
   
   1. Configure V-STP.
      
      # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceB
      [*HUAWEI] commit
      [~DeviceB] stp mode rstp
      [*DeviceB] stp v-stp enable
      [*DeviceB] commit
      ```
   2. Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group. Ensure that DeviceB and DeviceC can communicate at Layer 3 through their management interfaces.# Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
      ```
      [~DeviceB] interface meth 0/0/0
      [~DeviceB-MEth0/0/0] ip address 10.200.1.1 24
      [*DeviceB-MEth0/0/0] quit
      [*DeviceB] dfs-group 1
      [*DeviceB-dfs-group-1] dual-active detection source ip 10.200.1.1 peer 10.200.2.1
      [*DeviceB-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceB-dfs-group-1] quit
      [*DeviceB] commit
      ```
   3. Configure BGP on DeviceB, DeviceC, and DeviceD so that EBGP peer relationships can be established between DeviceD and DeviceB and between DeviceD and DeviceC. BGP is used to advertise dedicated routing information for establishing a bypass VXLAN tunnel.
      
      # Configure a BGP peer for DeviceB and disable the function of checking duplicate AS numbers.
      
      ```
      [~DeviceB] interface loopback 1
      [*DeviceB-LoopBack1] ip address 10.1.1.1 32
      [*DeviceB-LoopBack1] quit
      [*DeviceB] commit
      [~DeviceB] bgp 100
      [*DeviceB-bgp] router-id 10.111.12.12 
      [*DeviceB-bgp] peer 192.168.1.2 as-number 200 
      [*DeviceB-bgp] peer 192.168.1.2 allow-as-loop
      [*DeviceB-bgp] network 10.1.1.1 255.255.255.255
      [*DeviceB-bgp] quit 
      [*DeviceB] commit
      ```
      
      # Configure a BGP peer for DeviceC and disable the function of checking duplicate AS numbers.
      
      ```
      [~DeviceC] interface loopback 1
      [*DeviceC-LoopBack1] ip address 10.1.1.2 32
      [*DeviceC-LoopBack1] quit
      [*DeviceC] commit
      [~DeviceC] bgp 100
      [*DeviceC-bgp] router-id 10.114.14.14 
      [*DeviceC-bgp] peer 192.168.2.2 as-number 200 
      [*DeviceC-bgp] peer 192.168.2.2 allow-as-loop
      [*DeviceC-bgp] network 10.1.1.2 255.255.255.255
      [*DeviceC-bgp] quit 
      [*DeviceC] commit
      ```
      
      # Configure BGP peers for DeviceD.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceD
      [*HUAWEI] commit
      [~DeviceD] interface loopback 1
      [*DeviceD-LoopBack1] ip address 10.1.1.3 32
      [*DeviceD-LoopBack1] quit
      [*DeviceD] commit
      [~DeviceD] bgp 200
      [*DeviceD-bgp] router-id 10.113.13.13 
      [*DeviceD-bgp] peer 192.168.1.1 as-number 100 
      [*DeviceD-bgp] peer 192.168.2.1 as-number 100
      [*DeviceD-bgp] quit 
      [*DeviceD] commit
      ```
   4. Configure a virtual peer-link between DeviceB and DeviceC.
      
      # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
      
      ```
      [~DeviceB] interface eth-trunk 1 
      [*DeviceB-Eth-Trunk1] peer-link 1 virtual-link
      [*DeviceB-Eth-Trunk1] quit 
      [*DeviceB] commit
      ```
   5. Configure a reserved VNI for the M-LAG, and configure a bypass VXLAN tunnel.
      
      # Configure the uplink interface of the bypass VXLAN tunnel as an M-LAG reserved interface on DeviceB.
      
      ```
      [~DeviceB] interface 100ge 1/0/1                                         
      [*DeviceB-100GE1/0/1] m-lag unpaired-port reserved
      [*DeviceB-100GE1/0/1] quit
      [*DeviceB] commit
      ```
      
      # Configure the uplink interface of the bypass VXLAN tunnel as an M-LAG reserved interface on DeviceC.
      
      ```
      [~DeviceC] interface 100ge 1/0/1                                         
      [*DeviceC-100GE1/0/1] m-lag unpaired-port reserved
      [*DeviceC-100GE1/0/1] quit
      [*DeviceC] commit
      ```
      
      # Configure a reserved VNI for the virtual peer-link solution and configure a bypass VXLAN tunnel on DeviceB.
      
      ```
      [~DeviceB] interface nve 1                                         
      [*DeviceB-Nve1] pip-source 10.1.1.1 peer 10.1.1.2 bypass
      [*DeviceB-Nve1] vni 10000 reserved for m-lag
      [*DeviceB-Nve1] quit
      [*DeviceB] commit
      ```
      
      # Configure a reserved VNI for the virtual peer-link solution and configure a bypass VXLAN tunnel on DeviceC.
      
      ```
      [~DeviceC] interface nve 1                                         
      [*DeviceC-Nve1] pip-source 10.1.1.2 peer 10.1.1.1 bypass
      [*DeviceC-Nve1] vni 10000 reserved for m-lag
      [*DeviceC-Nve1] quit
      [*DeviceC] commit
      ```
   6. Configure M-LAG member interfaces on DeviceB and DeviceC and an Eth-Trunk interface on DeviceA.
      
      # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
      
      ```
      [~DeviceB] interface eth-trunk 10 
      [*DeviceB-Eth-Trunk10] mode lacp-static 
      [*DeviceB-Eth-Trunk10] port link-type trunk 
      [*DeviceB-Eth-Trunk10] lacp mixed-rate link enable 
      [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/2 
      [*DeviceB-Eth-Trunk10] dfs-group 1 m-lag 1 
      [*DeviceB-Eth-Trunk10] quit 
      [*DeviceB] commit
      ```
      
      # Configure DeviceA.
      
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceA
      [*HUAWEI] commit
      [~DeviceA] interface eth-trunk 10 
      [*DeviceA-Eth-Trunk10] mode lacp-static 
      [*DeviceA-Eth-Trunk10] port link-type trunk 
      [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/1
      [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2
      [*DeviceA-Eth-Trunk10] quit 
      [*DeviceA] commit
      ```
   7. Configure Monitor Link on DeviceB and DeviceC.
      
      # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
      
      ```
      [~DeviceB] monitor-link group 1 
      [*DeviceB-mtlk-group1] port 100ge 1/0/1 uplink 
      [*DeviceB-mtlk-group1] port eth-trunk 10 downlink 1 
      [*DeviceB-mtlk-group1] quit 
      [*DeviceB] commit
      ```
2. Configure BGP over M-LAG.
   
   
   1. Configure IPv4 addresses for BGP over M-LAG on DeviceB, DeviceC, and DeviceA.
      
      # Configure DeviceA.
      
      ```
      [~DeviceA] vlan batch 102
      [*DeviceA] interface vlanif 102
      [*DeviceA-Vlanif102] ip address 10.102.0.2 255.255.255.0
      [*DeviceA-Vlanif102] quit
      [*DeviceA] commit
      [~DeviceA] interface eth-trunk 10
      [~DeviceA-Eth-Trunk10] port trunk allow-pass vlan 102
      [*DeviceA-Eth-Trunk10] quit
      [*DeviceA] commit
      ```
      
      # Configure DeviceB.
      
      ```
      [~DeviceB] vlan batch 102
      [*DeviceB] interface vlanif 102
      [*DeviceB-Vlanif102] ip address 10.102.0.1 255.255.255.0
      [*DeviceB-Vlanif102] m-lag ip address 10.102.0.3 255.255.255.0
      [*DeviceB-Vlanif102] mac-address 0000-5e00-0101
      [*DeviceB-Vlanif102] arp proxy enable
      [*DeviceB-Vlanif102] quit
      [*DeviceB] commit
      [~DeviceB] interface eth-trunk 10
      [~DeviceB-Eth-Trunk10] port trunk allow-pass vlan 102
      [*DeviceB-Eth-Trunk10] quit
      [*DeviceB] commit
      ```
      
      # Configure DeviceC.
      
      ```
      [~DeviceC] vlan batch 102
      [*DeviceC] interface vlanif 102
      [*DeviceC-Vlanif102] ip address 10.102.0.1 255.255.255.0
      [*DeviceC-Vlanif102] m-lag ip address 10.102.0.4 255.255.255.0
      [*DeviceC-Vlanif102] mac-address 0000-5e00-0101
      [*DeviceC-Vlanif102] arp proxy enable
      [*DeviceC-Vlanif102] quit
      [*DeviceC] commit
      [~DeviceC] interface eth-trunk 10
      [~DeviceC-Eth-Trunk10] port trunk allow-pass vlan 102
      [*DeviceC-Eth-Trunk10] quit
      [*DeviceC] commit
      ```
   2. Configure DeviceA to establish BGP peer relationships with M-LAG member devices (DeviceB and DeviceC).# Configure DeviceA.
      ```
      [~DeviceA] bgp 100
      [*DeviceA-bgp] router-id 10.115.15.15 
      [*DeviceA-bgp] peer 10.102.0.3 as-number 100  
      [*DeviceA-bgp] peer 10.102.0.4 as-number 100
      [*DeviceA-bgp] quit
      [*DeviceA] commit
      ```
      
      # Configure DeviceB.
      ```
      [~DeviceB] bgp 100  
      [~DeviceB-bgp] peer 10.102.0.2 as-number 100 
      [*DeviceB-bgp] peer 10.102.0.2 connect-interface Vlanif102 10.102.0.3  
      [*DeviceB-bgp] quit
      [*DeviceB] commit
      ```
      
      # Configure DeviceC.
      ```
      [~DeviceC] bgp 100  
      [~DeviceC-bgp] peer 10.102.0.2 as-number 100 
      [*DeviceC-bgp] peer 10.102.0.2 connect-interface Vlanif102 10.102.0.4  
      [*DeviceC-bgp] quit
      [*DeviceC] commit
      ```

#### Verifying the Configuration

# Run the **display dfs-group 1 m-lag** command to check M-LAG information.

```
[~DeviceB] display dfs-group 1 m-lag
*                     : Local node
Heart beat state      : OK
Node 1 *
  Dfs-Group ID        : 1
  Priority            : 100
  Dual-active Address : 10.200.1.1
  VPN-Instance        : public net
  State               : Master
  Causation           : -
  System ID           : 00e0-fc12-3457
  SysName             : DeviceB
  Version             : V300R023C00
  Device Type         : CE6860-SAN
Node 2
  Dfs-Group ID        : 1
  Priority            : 100
  Dual-active Address : 10.200.2.1
  VPN-Instance        : public net
  State               : Backup
  Causation           : -
  System ID           : 00e0-fc12-3458
  SysName             : DeviceC
  Version             : V300R023C00
  Device Type         : CE6860-SAN
```

# Check M-LAG information on DeviceB.

```
[~DeviceB] display dfs-group 1 node 1 m-lag brief
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

# Check M-LAG information on DeviceC.

```
[~DeviceC] display dfs-group 1 node 2 m-lag brief
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

Run the **display bgp peer** command on DeviceB, DeviceC, and DeviceA to check BGP peer information.

# Check BGP peer information on DeviceB.

```
[~DeviceB] display bgp peer                                          
Status codes: * - Dynamic 
BGP local router ID        : 10.111.12.12 
Local AS number            : 100 
Total number of peers      : 2 
Peers in established state : 2 
Total number of dynamic peers : 0 
  
 Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv            
 10.102.0.2      4         100        6        8     0 00:00:45  Established    0             
 192.168.1.2     4         200       26       25     0 00:03:52  Established    0
```

# Check BGP peer information on DeviceC.

```
[~DeviceC] display bgp peer                                          
Status codes: * - Dynamic 
BGP local router ID        : 10.114.14.14 
Local AS number            : 100 
Total number of peers      : 2 
Peers in established state : 2 
Total number of dynamic peers : 0 
  
 Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv            
 10.102.0.2      4         100        7        9     0 00:00:45  Established    0             
 192.168.2.2     4         200       26       24     0 00:03:52  Established    0
```

# Check BGP peer information on DeviceA.

```
[~DeviceA] display bgp peer                                          
Status codes: * - Dynamic 
BGP local router ID        : 10.115.15.15 
Local AS number            : 100 
Total number of peers      : 2 
Peers in established state : 2 
Total number of dynamic peers : 0 
  
 Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv            
 10.102.0.3      4         100        6        0     0 00:00:45  Established    0             
 10.102.0.4      4         100        7        0     0 00:03:52  Established    0
```

After BGP is configured successfully, run the **display bgp peer** command on DeviceD to check BGP peer information.

```
[~DeviceD] display bgp peer                                          
Status codes: * - Dynamic 
BGP local router ID        : 10.113.13.13 
Local AS number            : 200 
Total number of peers      : 2 
Peers in established state : 2 
Total number of dynamic peers : 0 
  
 Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv            
 192.168.1.1     4         100        3        3     0 00:00:45  Established    0             
 192.168.2.1     4         100        7        7     0 00:03:52  Established    0
```

After the bypass VXLAN tunnel is established successfully, check tunnel information. The command outputs on DeviceB and DeviceC are as follows:

# Check bypass VXLAN tunnel information on DeviceB.

```
[~DeviceB] display vxlan tunnel 
                                         
Number of vxlan tunnel : 1  
                                                                                                    
Tunnel ID   Source                        Destination                  State  Type     Uptime

----------------------------------------------------------------------------------------------------

4026533892  10.1.1.1                      10.1.1.2                       up     static   00:32:34
```

# Check bypass VXLAN tunnel information on DeviceC.

```
[~DeviceC] display vxlan tunnel  
                                                                                                           
Number of vxlan tunnel : 1                                                                                                          
Tunnel ID   Source                         Destination                  State  Type     Uptime

----------------------------------------------------------------------------------------------------

4026531845  10.1.1.2                       10.1.1.1                       up     static   00:17:55
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 102
  #
  interface Vlanif102
   ip address 10.102.0.2 255.255.255.0
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 102
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 10
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  bgp 100
   router-id 10.115.15.15 
   peer 10.102.0.3 as-number 100 
   peer 10.102.0.4 as-number 100 
   private-4-byte-as enable
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  dfs-group 1
   dual-active detection source ip 10.200.1.1 peer 10.200.2.1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%# 
  #
  vlan batch 102
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif102
   ip address 10.102.0.1 255.255.255.0
   mac-address 0000-5e00-0101
   m-lag ip address 10.102.0.3 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
    peer-link 1 virtual-link
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 102
   mode lacp-static
   lacp mixed-rate link enable
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ip address 10.200.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  interface nve 1
   pip-source 10.1.1.1 peer 10.1.1.2 bypass
   vni 10000 reserved for m-lag
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port Eth-Trunk10 downlink 1
  #
  bgp 100
   router-id 10.111.12.12 
   peer 192.168.1.2 as-number 200 
   peer 192.168.1.2 allow-as-loop
   peer 10.102.0.2 as-number 100 
   peer 10.102.0.2 connect-interface Vlanif102 10.102.0.3 
   network 10.1.1.1 255.255.255.255
   private-4-byte-as enable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  dfs-group 1
   dual-active detection source ip 10.200.2.1 peer 10.200.1.1
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!=I9f8>C{!P_bhB31@7r-=jrS8c|_"(Bn~#=!!!!!!!!!!!!!!!9!!!!kx-6@.tGA(wAt/IQXl6>[g{6YlOi9$!!!!!!!!!!%+%#
  #
  vlan batch 102
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif102
   ip address 10.102.0.1 255.255.255.0
   mac-address 0000-5e00-0101
   m-lag ip address 10.102.0.4 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
   peer-link 1 virtual-link
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 102
   mode lacp-static
   lacp mixed-rate link enable
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ip address 10.200.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface LoopBack1
   ip address 10.1.1.2 255.255.255.255
  #
  interface nve 1
   pip-source 10.1.1.2 peer 10.1.1.1 bypass
   vni 10000 reserved for m-lag
  #
  monitor-link group 1
   port 100GE1/0/1 uplink
   port Eth-Trunk10 downlink 1
  #
  bgp 100
   router-id 10.114.14.14 
   peer 192.168.2.2 as-number 200 
   peer 192.168.2.2 allow-as-loop
   peer 10.102.0.2 as-number 100 
   peer 10.102.0.2 connect-interface Vlanif102 10.102.0.4
   network 10.1.1.2 255.255.255.255
   private-4-byte-as enable
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface LoopBack1
   ip address 10.1.1.3 255.255.255.255
  #
  bgp 200
   router-id 10.113.13.13 
   peer 192.168.1.1 as-number 100 
   peer 192.168.2.1 as-number 100 
   private-4-byte-as enable
  #
  return
  ```