Example for Configuring a Dynamic Routing Protocol for Communication with an M-LAG in V-STP Mode
================================================================================================

Example for Configuring a Dynamic Routing Protocol for Communication with an M-LAG in V-STP Mode

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001513168790__fig7533163320230), DeviceA, DeviceB, and DeviceC constitute an M-LAG. The M-LAG member interfaces on DeviceB and DeviceC support dynamic routing protocols. A dynamic routing protocol is configured on DeviceA so that it can communicate with the M-LAG through Layer 3 routes.

**Figure 1** Network diagram for configuring a dynamic routing protocol for communication with an M-LAG![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 on DeviceA represent 100GE 1/0/1 and 100GE 1/0/2, respectively.

In this example, interface 1, interface 2, interface 4, interface 5, and interface 6 on DeviceB represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/4, 100GE 1/0/5, and MEth0/0/0, respectively.

In this example, interface 1, interface 2, interface 4, interface 5, and interface 6 on DeviceC represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/4, 100GE 1/0/5, and MEth0/0/0, respectively.

In this example, interface 1 and interface 2 on DeviceD represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001913177116.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a routing protocol on DeviceB, DeviceC, and DeviceD to implement Layer 3 connectivity.
2. Create Eth-Trunk interfaces.
3. Configure V-STP.
4. Configure an M-LAG.
   * Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group.
   * Configure the link between DeviceB and DeviceC as the peer-link.
   * Bind the user-side Eth-Trunk interface to the DFS group on DeviceB and DeviceC, respectively.
5. Configure an IP address for OSPF over M-LAG. Configure different M-LAG IP addresses on DeviceB and DeviceC. Otherwise, neighbor relationships of the routing protocol cannot be established.
6. Configure M-LAG member devices to use the specified IP address to establish OSPF neighbor relationships with DeviceA.


#### Procedure

1. Configure a routing protocol.
   
   
   
   # Configure DeviceB. The configurations of DeviceC and DeviceD are similar to the configuration of DeviceB. When configuring OSPF, configure the devices to advertise the 32-bit IP addresses of loopback interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface loopback 2
   [*DeviceB-LoopBack2] ip address 10.3.3.3 32
   [*DeviceB-LoopBack2] quit
   [*DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ip address 192.168.1.1 24
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] ospf 1 router-id 10.11.1.1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.3.3.3 0.0.0.0
   [*DeviceB-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   After OSPF is configured successfully, DeviceB, DeviceC, and DeviceD can learn the IP address of each other's loopback interface through OSPF and successfully ping each other.
2. Create Eth-Trunk interfaces and add physical Ethernet interfaces to them.
   
   
   
   The uplink interfaces that connect a server to two switches must be added to an Eth-Trunk interface, and the working mode of the Eth-Trunk interface must be the same as that of the Eth-Trunk interfaces on both switches.
   
   # Create Eth-Trunk interfaces in LACP mode on DeviceB and add member interfaces to the Eth-Trunk interfaces. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 1
   [*DeviceB-Eth-Trunk1] mode lacp-static
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/4
   [*DeviceB-Eth-Trunk1] trunkport 100ge 1/0/5
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] vlan batch 100
   [*DeviceB] interface eth-trunk 10
   [*DeviceB-Eth-Trunk10] mode lacp-static
   [*DeviceB-Eth-Trunk10] port link-type trunk
   [*DeviceB-Eth-Trunk10] undo port trunk allow-pass vlan 1
   [*DeviceB-Eth-Trunk10] port trunk allow-pass vlan 100
   [*DeviceB-Eth-Trunk10] lacp mixed-rate link enable
   [*DeviceB-Eth-Trunk10] trunkport 100ge 1/0/2
   [*DeviceB-Eth-Trunk10] quit
   [*DeviceB] commit
   ```
3. Configure V-STP.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] stp mode rstp
   [*DeviceB] stp v-stp enable
   [*DeviceB] commit
   ```
4. Configure a DFS group on DeviceB and DeviceC, and bind IP addresses of their management interfaces to the DFS group. Ensure that DeviceB and DeviceC can communicate at Layer 3 through their management interfaces.
   
   
   
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
5. Configure the link between DeviceB and DeviceC as the peer-link.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 1
   [~DeviceB-Eth-Trunk1] peer-link 1
   [*DeviceB-Eth-Trunk1] quit
   [*DeviceB] commit
   ```
6. Bind the user-side Eth-Trunk interface to the DFS group on DeviceB and DeviceC, respectively.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 10
   [~DeviceB-Eth-Trunk10] dfs-group 1 m-lag 1
   [*DeviceB-Eth-Trunk10] quit
   [*DeviceB] commit
   ```
7. Configure an IP address for OSPF over M-LAG on DeviceB and DeviceC, respectively.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface vlanif 100
   [*DeviceB-Vlanif100] ip address 10.100.0.1 255.255.255.0
   [*DeviceB-Vlanif100] ospf source sub-address 10.100.0.3
   [*DeviceB-Vlanif100] m-lag ip address 10.100.0.3 255.255.255.0
   [*DeviceB-Vlanif100] mac-address 0000-5e00-0101
   [*DeviceB-Vlanif100] arp proxy enable
   [*DeviceB-Vlanif100] quit
   [*DeviceB] commit
   ```
8. Configure M-LAG member devices to use the specified IP address to establish OSPF neighbor relationships with DeviceA. The ID of the OSPF area to which DeviceA, DeviceB, and DeviceC belong must be different from the ID of the OSPF area to which DeviceB, DeviceC, and DeviceD belong.
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   ```
   [~DeviceB] ospf
   [~DeviceB-ospf-1] area 1
   [*DeviceB-ospf-1-area-0.0.0.1] network 10.100.0.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.1] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 100
   [*DeviceA] interface eth-trunk 10
   [*DeviceA-Eth-Trunk10] mode lacp-static
   [*DeviceA-Eth-Trunk10] port link-type trunk
   [*DeviceA-Eth-Trunk10] undo port trunk allow-pass vlan 1
   [*DeviceA-Eth-Trunk10] port trunk allow-pass vlan 100
   [*DeviceA-Eth-Trunk10] lacp mixed-rate link enable
   [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/1
   [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2
   [*DeviceA-Eth-Trunk10] quit
   [*DeviceA] commit
   [*DeviceA] interface vlanif 100
   [*DeviceA-Vlanif100] ip address 10.100.0.2 255.255.255.0
   [*DeviceA-Vlanif100] quit
   [*DeviceA] commit
   [~DeviceA] ospf 1 router-id 10.11.4.4
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
        OSPF Process 1 with Router ID 10.11.1.1                    
                  Peer Statistic Information   
  Total number of peer(s): 3                                                       
  Peer(s) in full state: 3   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.0         100GE1/0/1                  10.11.3.3         Full
  0.0.0.1         Vlanif100                  10.11.2.2         Full  
  0.0.0.1         Vlanif100                  10.11.4.4         Full
```

# Check OSPF neighbor information on DeviceC.

```
[~DeviceC] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 10.11.2.2                    
                  Peer Statistic Information   
  Total number of peer(s): 3                                                       
  Peer(s) in full state: 3   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.0         100GE1/0/1                  10.11.3.3         Full
  0.0.0.1         Vlanif100                  10.11.1.1         Full  
  0.0.0.1         Vlanif100                  10.11.4.4         Full
```

# Check OSPF neighbor information on DeviceA.

```
[~DeviceA] [display ospf peer brief](cmdqueryname=display+ospf+peer+brief)
(M) Indicates MADJ interface
        OSPF Process 1 with Router ID 10.11.4.4                    
                  Peer Statistic Information   
  Total number of peer(s): 2                                                       
  Peer(s) in full state: 2   
  ----------------------------------------------------------------------------
  Area Id         Interface                  Neighbor id      State
  0.0.0.1         Vlanif100                  10.11.1.1         Full  
  0.0.0.1         Vlanif100                  10.11.2.2         Full
```

#### Configuration Scripts

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
   mac-address 0000-5e00-0101
   m-lag ip address 10.100.0.3 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
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
   ip address 192.168.1.1 255.255.255.0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface LoopBack2
   ip address 10.3.3.3 255.255.255.255
  #
  ospf 1 router-id 10.11.1.1
   area 0.0.0.0
    network 10.3.3.3 0.0.0.0
    network 192.168.1.0 0.0.0.255
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
   mac-address 0000-5e00-0101
   m-lag ip address 10.100.0.4 255.255.255.0
   arp proxy enable
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
  #
  interface Eth-Trunk10
   port link-type trunk
   undo port trunk allow-pass vlan 1
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
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  interface 100GE1/0/4
   eth-trunk 1
  #
  interface 100GE1/0/5
   eth-trunk 1
  #
  interface LoopBack2
   ip address 10.4.4.4 255.255.255.255
  #
  ospf 1 router-id 10.11.2.2
   area 0.0.0.0
    network 10.4.4.4 0.0.0.0
    network 192.168.2.0 0.0.0.255
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
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  ospf 1 router-id 10.11.3.3
   area 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
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
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 100
   mode lacp-static
   lacp mixed-rate link enable
  #
  interface 100GE1/0/1
   eth-trunk 10
  #
  interface 100GE1/0/2
   eth-trunk 10
  #
  ospf 1 router-id 10.11.4.4
   area 0.0.0.1
    network 10.100.0.0 0.0.0.255
  #
  return
  ```