Example for Configuring OSPF over M-LAG (Virtual Peer-Link Solution)
====================================================================

Example for Configuring OSPF over M-LAG (Virtual Peer-Link Solution)

#### Networking Requirements

![](../public_sys-resources/note_3.0-en-us.png) 

This configuration example is supported only by the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ.

On the network shown in [Figure 1](#EN-US_TASK_0000001513048790__en-us_task_0241512178_en-us_task_0141119105_fig_dc_cfg_vxlan_cfgcase_000601), DeviceA, DeviceB, and DeviceC constitute an M-LAG. The M-LAG member interfaces on DeviceB and DeviceC support OSPF. OSPF is configured on DeviceA so that it can communicate with the M-LAG through Layer 3 routes.

**Figure 1** Configuring OSPF over M-LAG (virtual peer-link solution)![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001513048830.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on DeviceB, DeviceC, and DeviceD to implement Layer 3 connectivity.
2. Create a bypass VXLAN tunnel between DeviceB and DeviceC.
3. Configure a routing policy to filter routing information of the bypass VXLAN tunnel on DeviceB and DeviceC, respectively.
4. Configure the uplink interface of the bypass VXLAN tunnel as an M-LAG reserved interface on DeviceB and DeviceC, respectively.
5. Configure V-STP.
6. Configure an M-LAG.
   1. Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group.
   2. Configure a virtual peer-link between DeviceB and DeviceC.
   3. Configure a reserved VNI for the virtual peer-link solution on DeviceB and DeviceC, respectively.
   4. Bind the user-side Eth-Trunk interface to the DFS group on DeviceB and DeviceC, respectively.
7. Configure an IP address for OSPF over M-LAG.
8. Configure M-LAG member devices to use the specified IP address to establish OSPF neighbor relationships with DeviceA. Configure different OSPF areas for the access side and network side.


#### Procedure

1. Configure a routing protocol.
   
   
   
   # Configure DeviceB. The configurations of DeviceC and DeviceD are similar to the configuration of DeviceB. When configuring OSPF, configure the devices to advertise the 32-bit IP addresses of loopback interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 10.0.0.2 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface loopback 0
   [*DeviceB-LoopBack0] ip address 10.5.5.5 32
   [*DeviceB-LoopBack0] quit
   [*DeviceB] commit
   [~DeviceB] ospf 1 router-id 192.168.1.2
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.5.5.5 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.0.0.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   After OSPF is configured successfully, DeviceB, DeviceC, and DeviceD can learn the IP address of each other's loopback interface through OSPF and successfully ping each other.
2. Create a static bypass VXLAN tunnel.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface nve 1
   [*DeviceB-Nve1] pip-source 10.5.5.5 peer 10.6.6.6 bypass
   [*DeviceB-Nve1] quit
   [*DeviceB] commit
   ```
3. Configure a routing policy to filter routing information of the bypass VXLAN tunnel.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] ip ip-prefix bypsssIp index 10 permit 10.5.5.5 32
   [*DeviceB] ip ip-prefix bypsssIp index 11 permit 10.6.6.6 32
   [*DeviceB] commit
   [~DeviceB] route-policy loopBackLimit deny node 10
   [*DeviceB-route-policy] if-match ip-prefix bypsssIp
   [*DeviceB-route-policy] quit
   [*DeviceB] route-policy loopBackLimit permit node 11
   [*DeviceB-route-policy] quit
   [*DeviceB] commit
   [~DeviceB] ospf 1
   [~DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] filter route-policy loopBackLimit export
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
4. Configure the uplink interface of the bypass VXLAN tunnel as an M-LAG reserved interface on DeviceB and DeviceC, respectively.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface 100ge 1/0/1                                         
   [*DeviceB-100GE1/0/1] m-lag unpaired-port reserved
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
5. Configure V-STP.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] stp mode rstp
   [*DeviceB] stp v-stp enable
   [*DeviceB] commit
   ```
6. Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group. Ensure that DeviceB and DeviceC can communicate at Layer 3 through their management interfaces.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
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
7. Configure a virtual peer-link between DeviceB and DeviceC.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 1
   [~DeviceB-Eth-Trunk1] peer-link 1 virtual-link
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
8. Configure a reserved VNI for the virtual peer-link solution on DeviceB and DeviceC, respectively.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   
   
   ```
   [~DeviceB] interface nve 1
   [~DeviceB-Nve1] vni 10000 reserved for m-lag
   [*DeviceB-Nve1] quit
   [*DeviceB] commit
   ```
9. Bind the user-side Eth-Trunk interface to the DFS group on DeviceB and DeviceC, respectively.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] vlan batch 100
   [*DeviceB] interface eth-trunk 10
   [*DeviceB-Eth-Trunk10] mode lacp-static
   [*DeviceB-Eth-Trunk10] port link-type trunk 
   [*DeviceB-Eth-Trunk10] port trunk allow-pass vlan 100
   [*DeviceB-Eth-Trunk10] lacp mixed-rate link enable
   [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/2
   [~DeviceB-Eth-Trunk10] dfs-group 1 m-lag 1
   [*DeviceB-Eth-Trunk10] quit
   [*DeviceB] commit
   ```
10. Configure an Eth-Trunk interface on DeviceA.
    
    
    
    # Configure DeviceA.
    
    ```
    <HUAWEI> system-view
    [~HUAWEI] sysname DeviceA
    [*HUAWEI] commit
    [~DeviceA] vlan batch 100
    [*DeviceA] interface eth-trunk 10 
    [*DeviceA-Eth-Trunk10] mode lacp-static 
    [*DeviceA-Eth-Trunk10] port link-type trunk 
    [*DeviceA-Eth-Trunk10] port trunk allow-pass vlan 100
    [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/1
    [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2
    [*DeviceA-Eth-Trunk10] quit 
    [*DeviceA] commit
    ```
11. Configure an IP address for OSPF over M-LAG on DeviceB and DeviceC, respectively.
    
    
    
    # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
    
    ```
    [~DeviceB] interface vlanif 100
    [*DeviceB-Vlanif100] ip address 10.100.0.1 255.255.255.0
    [*DeviceB-Vlanif100] ospf source sub-address 10.100.0.3
    [*DeviceB-Vlanif100] ospf enable 1 area 0.0.0.1
    [*DeviceB-Vlanif100] m-lag ip address 10.100.0.3 255.255.255.0
    [*DeviceB-Vlanif100] mac-address 0000-5e00-0101
    [*DeviceB-Vlanif100] arp proxy enable
    [*DeviceB-Vlanif100] quit
    [*DeviceB] commit
    ```
12. Configure M-LAG member devices to use the specified IP address to establish OSPF neighbor relationships with DeviceA. The ID of the OSPF area to which DeviceA, DeviceB, and DeviceC belong must be different from the ID of the OSPF area to which DeviceB, DeviceC, and DeviceD belong.
    
    # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
    ```
    [~DeviceB] ospf 1
    [*DeviceB-ospf-1] area 1
    [*DeviceB-ospf-1-area-0.0.0.1] network 10.100.0.0 0.0.0.255
    [*DeviceB-ospf-1-area-0.0.0.1] quit
    [*DeviceB-ospf-1] quit
    [*DeviceB] commit
    ```
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] interface vlanif 100
    [~DeviceA-Vlanif100] ip address 10.100.0.2 255.255.255.0
    [*DeviceA-Vlanif100] quit
    [*DeviceA] commit
    [~DeviceA] ospf 1
    [*DeviceA-ospf-1] area 1
    [*DeviceA-ospf-1-area-0.0.0.1] network 10.100.0.0 0.0.0.255
    [*DeviceA-ospf-1-area-0.0.0.1] quit
    [*DeviceA-ospf-1] quit
    [*DeviceA] commit
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

Run the [**display ospf peer brief**](cmdqueryname=display+ospf+peer+brief) command on DeviceB, DeviceC, and DeviceA to check OSPF neighbor information.

# Check OSPF neighbor information on DeviceB.

```
[~DeviceB] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 192.168.1.2                    
                  Peer Statistic Information   
  Total number of peer(s): 3                                                       
  Peer(s) in full state: 3   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.0         100GE1/0/1                  192.168.1.1         Full
  0.0.0.1         Vlanif100                  192.168.1.3         Full  
  0.0.0.1         Vlanif100                  192.168.1.4         Full
```

# Check OSPF neighbor information on DeviceC.

```
[~DeviceC] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 192.168.1.3                    
                  Peer Statistic Information   
  Total number of peer(s): 3                                                       
  Peer(s) in full state: 3   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.0         100GE1/0/1                  192.168.1.1         Full
  0.0.0.1         Vlanif100                  192.168.1.2         Full  
  0.0.0.1         Vlanif100                  192.168.1.4         Full
```

# Check OSPF neighbor information on DeviceA.

```
[~DeviceA] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 192.168.1.4                    
                  Peer Statistic Information   
  Total number of peer(s): 2                                                       
  Peer(s) in full state: 2   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.1         Vlanif100                  192.168.1.2         Full  
  0.0.0.1         Vlanif100                  192.168.1.3         Full
```

After OSPF is configured successfully, run the [**display ospf peer brief**](cmdqueryname=display+ospf+peer+brief) command on DeviceD to check OSPF neighbor information.

# Check OSPF neighbor information on DeviceD.

```
[~DeviceD] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 192.168.1.1                    
                  Peer Statistic Information   
  Total number of peer(s): 2                                                       
  Peer(s) in full state: 2   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.0         Vlanif100                  192.168.1.2         Full  
  0.0.0.0         Vlanif100                  192.168.1.3         Full
```

After the bypass VXLAN tunnel is established successfully, check tunnel information. The command outputs on DeviceB and DeviceC are as follows:

# Check bypass VXLAN tunnel information on DeviceB.

```
[~DeviceB] [display vxlan tunnel](cmdqueryname=display+vxlan+tunnel)  
                                                                                                           
Number of vxlan tunnel : 1                                                                                                          
Tunnel ID   Source                         Destination                    State  Type     Uptime

----------------------------------------------------------------------------------------------------                                
4026531844  10.5.5.5                       10.6.6.6                       up     static   00:30:48   
```

# Check bypass VXLAN tunnel information on DeviceC.

```
[~DeviceC] display vxlan tunnel  
                                                                                                           
Number of vxlan tunnel : 1                                                                                                          
Tunnel ID   Source                         Destination                    State  Type     Uptime

----------------------------------------------------------------------------------------------------                                
4026531845  10.6.6.6                       10.5.5.5                       up     static   00:30:48   
```

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  vlan batch 100
  #
  interface Vlanif100
   ip address 10.100.0.2 255.255.255.0
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 100
   mode lacp-static
  #
  interface 100GE1/0/1
   eth-trunk 10
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  ospf 1 router-id 192.168.1.4
   area 0.0.0.1
    network 10.100.0.0 0.0.0.255
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
  vlan batch 100
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif100
   ip address 10.100.0.1 255.255.255.0
   ospf source sub-address 10.100.0.3
   ospf enable 1 area 0.0.0.1
   mac-address 0000-5e00-0101
   m-lag ip address 10.100.0.3 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
    peer-link 1 virtual-link
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 100
   mode lacp-static
   lacp mixed-rate link enable
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ip address 10.200.1.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.0.0.2 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface LoopBack0
   ip address 10.5.5.5 255.255.255.255
  #
  interface nve 1
   pip-source 10.5.5.5 peer 10.6.6.6 bypass
   vni 10000 reserved for m-lag
  #
  ip ip-prefix bypsssIp index 10 permit 10.5.5.5 32
  ip ip-prefix bypsssIp index 11 permit 10.6.6.6 32
  #
  route-policy loopBackLimit deny node 10
   if-match ip-prefix bypsssIp
  #
  route-policy loopBackLimit permit node 11
  #
  ospf 1 router-id 192.168.1.2
   area 0.0.0.0
    filter route-policy loopBackLimit export
    network 10.5.5.5 0.0.0.0
    network 10.0.0.0 0.0.0.255
   area 0.0.0.1
    network 10.100.0.0 0.0.0.255
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
  vlan batch 100
  #
  stp mode rstp
  stp v-stp enable
  #
  interface Vlanif100
   ip address 10.100.0.1 255.255.255.0
   ospf source sub-address 10.100.0.4
   ospf enable 1 area 0.0.0.1
   mac-address 0000-5e00-0101
   m-lag ip address 10.100.0.4 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
   peer-link 1 virtual-link
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 100
   mode lacp-static
   lacp mixed-rate link enable
   dfs-group 1 m-lag 1
  #
  interface MEth0/0/0
   ip address 10.200.2.1 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.0.2 255.255.255.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface LoopBack0
   ip address 10.6.6.6 255.255.255.255
  #
  interface nve 1
   pip-source 10.6.6.6 peer 10.5.5.5 bypass
   vni 10000 reserved for m-lag
  #
  ip ip-prefix bypsssIp index 10 permit 10.6.6.6 32
  ip ip-prefix bypsssIp index 11 permit 10.5.5.5 32
  #
  route-policy loopBackLimit deny node 10
   if-match ip-prefix bypsssIp
  #
  route-policy loopBackLimit permit node 11
  #
  ospf 1 router-id 192.168.1.3
   area 0.0.0.0
    filter route-policy loopBackLimit export
    network 10.6.6.6 0.0.0.0
    network 10.1.0.0 0.0.0.255
   area 0.0.0.1
    network 10.100.0.0 0.0.0.255
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
   ip address 10.0.0.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.0.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  ospf 1 router-id 192.168.1.1
   area 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 10.0.0.0 0.0.0.255
    network 10.1.0.0 0.0.0.255
  #
  return
  ```