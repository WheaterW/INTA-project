Example for Configuring PIM FRR and M-LAG for Protection
========================================================

Example for Configuring PIM FRR and M-LAG for Protection

#### Networking Requirements

Multicast services are deployed on the ISP network shown in [Figure 1](#EN-US_TASK_0000001315452113__fig_dc_vrp_multicast_cfg_003701). DeviceB and DeviceC are the first-hop PIM devices connected to the multicast source, and they are responsible for forwarding multicast data from the multicast source. DeviceA is the last-hop PIM device connected to a multicast group member, and it is responsible for forwarding multicast data to the member.

To ensure high reliability of multicast services, M-LAG is deployed between DeviceB and DeviceC. When the two devices are working properly, links work in load balancing mode. If either fails, services are not affected. In addition, PIM FRR is deployed on DeviceA, DeviceB, and DeviceC. In normal cases, DeviceA accepts traffic from the primary link. If the primary link fails, traffic is immediately switched to the backup link.

**Figure 1** Configuring PIM FRR and M-LAG for protection![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, interface4, and interface5 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, 100GE1/0/4, and 100GE1/0/5, respectively.

![](figure/en-us_image_0000001318137805.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create Eth-Trunk interfaces on DeviceB and DeviceC, and add Ethernet physical interfaces to the Eth-Trunk interfaces.
2. Configure V-STP on DeviceB and DeviceC.
3. Configure IP addresses for the management network ports on DeviceB and DeviceC.
4. Configure a DFS group on DeviceB and DeviceC, and bind the IP address of the corresponding management network port to the DFS group.
5. Configure the links between DeviceB and DeviceC as peer-links.
6. Bind the DFS group to the user-side Eth-Trunk interfaces on DeviceB and DeviceC, and enable STP edge ports on the Eth-Trunk interfaces to speed up network convergence.
7. Configure IP addresses and MAC addresses for VLANIF interfaces on DeviceB and DeviceC, and enable PIM-SM and IGMP.
8. Enable IGMP snooping in the VLAN on DeviceB and DeviceC.
9. Assign an IP address to each device interface and configure OSPF to implement IP interworking. Enable multicast and public network FRR, and enable PIM-SM on each interface.
10. Enable IGMP on the interface connecting DeviceA to the host and configure a static multicast group on the interface.
11. Configure a static RP on all devices.
12. Enable OSPF IP FRR on DeviceA.
13. Enable PIM FRR on all devices.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: 225.1.0.0
* Multicast source address: 10.0.5.100

#### Procedure

1. Create Eth-Trunk interfaces on DeviceB and DeviceC, and add Ethernet physical interfaces to the Eth-Trunk interfaces.
   
   
   
   # Create Eth-Trunk interfaces in LACP mode on DeviceB and add member interfaces to the Eth-Trunk interfaces. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 0
   [*DeviceB-Eth-Trunk0] mode lacp-static
   [*DeviceB-Eth-Trunk0] trunkport 100ge1/0/3
   [*DeviceB-Eth-Trunk0] trunkport 100ge 1/0/5
   [*DeviceB-Eth-Trunk0] quit
   [*DeviceB] vlan 100
   [*DeviceB-vlan100] quit
   [*DeviceB] interface eth-trunk 100
   [*DeviceB-Eth-Trunk100] port link-type trunk
   [*DeviceB-Eth-Trunk100] port trunk allow-pass vlan 100
   [*DeviceB-Eth-Trunk100] mode lacp-static
   [*DeviceB-Eth-Trunk100] lacp mixed-rate link enable
   [*DeviceB-Eth-Trunk100] trunkport 100ge1/0/1
   [*DeviceB-Eth-Trunk100] quit
   [*DeviceB] commit
   ```
2. Configure V-STP on DeviceB and DeviceC.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] stp mode rstp
   [*DeviceB] stp v-stp enable
   ```
3. Configure IP addresses for the management network ports on DeviceB and DeviceC.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface meth 0/0/0
   [~DeviceB-MEth0/0/0] ip address 10.1.1.1 24
   [*DeviceB-MEth0/0/0] quit
   [*DeviceB] commit
   ```
4. Configure a DFS group on DeviceB and DeviceC, and bind the IP address of the corresponding management network port to the DFS group.
   
   
   
   Ensure that DeviceB and DeviceC can communicate at Layer 3 through their management network ports.
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] dfs-group 1
   [*DeviceB-dfs-group-1] dual-active detection source ip 10.1.1.1 peer 10.1.1.2
   [*DeviceB-dfs-group-1] priority 120
   [*DeviceB-dfs-group-1] m-lag active-standby election arp
   [*DeviceB-dfs-group-1] dual-active detection delay 0
   [*DeviceB-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
   [*DeviceB-dfs-group-1] dual-active detection error-down mode routing-switch
   [*DeviceB-dfs-group-1] quit
   [*DeviceB] commit
   ```
5. Configure the links between DeviceB and DeviceC as peer-links.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 0
   [~DeviceB-Eth-Trunk0] peer-link 1
   [*DeviceB-Eth-Trunk0] quit
   [*DeviceB] commit
   ```
6. Bind the DFS group to the user-side Eth-Trunk interfaces on DeviceB and DeviceC, and enable STP edge ports on the Eth-Trunk interfaces to speed up network convergence.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface eth-trunk 100
   [~DeviceB-Eth-Trunk100] dfs-group 1 m-lag 1 active-standby
   [*DeviceB-Eth-Trunk100] stp edged-port enable
   [*DeviceB-Eth-Trunk100] quit
   [*DeviceB] commit
   ```
7. Configure IP addresses and MAC addresses for VLANIF interfaces on DeviceB and DeviceC, and enable PIM-SM and IGMP.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] interface vlanif 100
   [~DeviceB-Vlanif100] ip address 10.100.0.1 255.255.255.0
   [*DeviceB-Vlanif100] mac-address 0000-5e00-0101
   [*DeviceB-Vlanif100] pim sm
   [*DeviceB-Vlanif100] igmp enable
   [*DeviceB-Vlanif100] quit
   [*DeviceB] commit
   ```
8. Enable IGMP snooping in the VLAN on DeviceB and DeviceC.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   
   
   ```
   [~DeviceB] vlan 100
   [~DeviceB-vlan100] igmp snooping enable
   [*DeviceB-vlan100] quit
   [*DeviceB] commit
   ```
9. Assign an IP address to each device interface and configure OSPF to implement IP interworking. Enable multicast and public network FRR, and enable PIM-SM on each interface.
   
   
   
   # Configure DeviceB. The configuration of DeviceC is similar to that of DeviceB.
   
   ```
   [~DeviceB] multicast routing-enable
   [*DeviceB] ip frr
   [*DeviceB] interface 100ge 1/0/4
   [*DeviceB-100GE1/0/4] undo portswitch
   [*DeviceB-100GE1/0/4] ip address 10.10.1.1 24
   [*DeviceB-100GE1/0/4] ospf enable 1 area 0
   [*DeviceB-100GE1/0/4] pim sm
   [*DeviceB-100GE1/0/4] m-lag unpaired-port reserved
   [*DeviceB-100GE1/0/4] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 10.9.7.1 24
   [*DeviceB-100GE1/0/2] ospf enable 1 area 0
   [*DeviceB-100GE1/0/2] pim sm
   [*DeviceB-100GE1/0/2] m-lag unpaired-port reserved
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] ospf 1 
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.9.7.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] import-route direct type 1
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] multicast routing-enable
   [*DeviceC] ip frr
   [*DeviceC] interface 100ge 1/0/4
   [*DeviceC-100GE1/0/4] undo portswitch
   [*DeviceC-100GE1/0/4] ip address 10.10.1.2 24
   [*DeviceC-100GE1/0/4] ospf enable 1 area 0
   [*DeviceC-100GE1/0/4] pim sm
   [*DeviceC-100GE1/0/4] m-lag unpaired-port reserved
   [*DeviceC-100GE1/0/4] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] ip address 10.6.1.1 24
   [*DeviceC-100GE1/0/2] ospf enable 1 area 0
   [*DeviceC-100GE1/0/2] pim sm
   [*DeviceC-100GE1/0/2] m-lag unpaired-port reserved
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface loopback 0
   [*DeviceC-LoopBack0] ip address 10.6.6.6 32
   [*DeviceC-LoopBack0] pim sm
   [*DeviceC-LoopBack0] quit
   [*DeviceC] ospf 1 
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.6.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.6.6.6 0.0.0.0
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] import-route direct type 1
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.6.1.9 24
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] ospf enable 1 area 0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.9.7.9 24
   [*DeviceA-100GE1/0/2] ospf enable 1 area 0
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.9.1.1 24
   [*DeviceA-100GE1/0/3] ospf enable 1 area 0
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] ospf 1 
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.6.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.9.7.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.9.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
10. Enable IGMP on the interface connecting DeviceA to the host and configure a static multicast group on the interface.
    
    
    ```
    [~DeviceA] interface 100ge1/0/3
    [*DeviceA-100GE1/0/3] igmp enable
    [*DeviceA-100GE1/0/3] igmp static-group 225.1.0.0 source 10.100.0.2
    [*DeviceA-100GE1/0/3] quit
    [*DeviceA] commit
    ```
11. Configure a static RP on all devices.
    
    
    
    # Configure DeviceB. The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB.
    
    
    
    ```
    [~DeviceB] pim
    [*DeviceB-pim] static-rp 10.6.6.6
    [*DeviceB-pim] quit
    [*DeviceB-pim] commit
    ```
12. Enable OSPF IP FRR on DeviceA.
    
    
    ```
    [~DeviceA] ospf 1 
    [~DeviceA-ospf-1] frr 
    [*DeviceA-ospf-1] loop-free-alternate
    [*DeviceA-ospf-1] quit
    [*DeviceA] commit
    ```
13. Enable PIM FRR on all devices.
    
    
    
    # Configure DeviceB. The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB.
    
    ```
    [~Device B] pim
    [*Device B-pim] rpf-frr
    [*Device B-pim] quit
    [*Device B] commit
    ```

#### Verifying the Configuration

# Run the **display pim routing-table** command on DeviceC to check the PIM routing table.

```
[*Device C] display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.100.0.2, 225.1.0.0)
     RP: 10.6.6.6 (local)
     Protocol: pim-sm, Flag: SPT SG_RCVR
     UpTime: 01:22:40
     Upstream interface: Vlanif100, Refresh time: 01:22:40
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Backup upstream interface: 100GE1/0/4
        Backup upstream neighbor: 10.10.1.2
        Backup RPF prime neighbor: 10.10.1.2     
     Downstream interface(s) information:
     Total number of downstreams: 2
        1: 100GE1/0/2
             Protocol: pim-sm, UpTime: 01:06:04, Expires: -
        2: 100GE1/0/4
             Protocol: pim-sm, UpTime: 01:06:04, Expires: -
```

# Run the **shutdown** command on 100GE1/0/3 of DeviceC to simulate a link fault.

```
[~DeviceC] interface Eth-trunk 0
[*DeviceC-Eth-trunk0] shutdown
[*DeviceC-Eth-trunk0] commit
```

# Run the **display pim routing-table** command on DeviceC immediately to check the PIM routing table.

```
[*Device C] display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.100.0.2, 225.1.0.0)
     RP: 10.6.6.6 (local)
     Protocol: pim-sm, Flag: SPT SG_RCVR
     UpTime: 01:22:40
     Upstream interface: 100GE1/0/4, Refresh time: 01:22:40
         Upstream neighbor: 10.10.1.2
         RPF prime neighbor: 10.10.1.2
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol: pim-sm, UpTime: 01:06:04, Expires: -
```

The command output shows that the inbound interface of the route on DeviceC has been changed to 100GE1/0/4, which was on the original backup link.

#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.6.1.9 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 10.9.7.9 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.9.1.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 225.1.0.0 source 10.100.0.2
   ospf enable 1 area 0.0.0.0
  #
  ospf 1
   frr
    loop-free-alternate 
   area 0.0.0.0
    network 10.6.1.0 0.0.0.255
    network 10.9.7.0 0.0.0.255
    network 10.9.1.0 0.0.0.255
  #
  pim
   static-rp 10.6.6.6
   rpf-frr
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  dfs-group 1   
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%# 
   dual-active detection source ip 10.1.1.1 peer 10.1.1.2
   priority 120
   m-lag active-standby election arp
   dual-active detection delay 0
   dual-active detection error-down mode routing-switch
  #
  stp mode rstp
  stp v-stp enable
  #
  ip frr 
  #
  multicast routing-enable
  #
  igmp snooping enable
  #
  vlan 100
   igmp snooping enable
  #
  interface Vlanif100
   ip address 10.100.0.1 255.255.255.0
   pim sm
   igmp enable
   mac-address 0000-5e00-0101
  #
  interface MEth0/0/0
   ip address 10.1.1.1 255.255.224.0
  #
  interface Eth-Trunk0
   peer-link 1
  # 
  interface Eth-Trunk100
   port link-type trunk
   port trunk allow-pass vlan 100
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1 active-standby
  #
  interface 100GE1/0/1
   eth-trunk 100
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 10.9.7.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/3
   eth-trunk 0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.10.1.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/5
   eth-trunk 0
  #
  ospf 1
   import-route direct type 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.9.7.0 0.0.0.255
  #
  pim
   static-rp 10.6.6.6
   rpf-frr
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  #
  dfs-group 1   
   authentication-mode hmac-sha256 password %+%##!!!!!!!!!"!!!!"!!!!*!!!!C+tR0CW9x*eB&pWp`t),Azgw-h\o8#4LZPD!!!!!!!!!!!!!!!9!!!!>fwJ)I0E{=:%,*,XRhbH&t0MCy_8=7!!!!!!!!!!%+%# 
   dual-active detection source ip 10.1.1.2 peer 10.1.1.1
   m-lag active-standby election arp
   dual-active detection delay 0
   dual-active detection error-down mode routing-switch
  #
  stp mode rstp
  stp v-stp enable
  #
  ip frr 
  #
  multicast routing-enable
  #
  igmp snooping enable
  #
  vlan 100
   igmp snooping enable
  #
  interface Vlanif100
   ip address 10.100.0.1 255.255.255.0
   pim sm
   igmp enable
   mac-address 0000-5e00-0101
  #
  interface MEth0/0/0
   ip address 10.1.1.2 255.255.224.0
  #
  interface loopback0
   ip address 10.6.6.6 255.255.255.255
   pim sm
  #
  interface Eth-Trunk0
   peer-link 1
  # 
  interface Eth-Trunk100
   port link-type trunk
   port trunk allow-pass vlan 100
   stp edged-port enable
   mode lacp-static
   dfs-group 1 m-lag 1 active-standby
  #
  interface 100GE1/0/1
   eth-trunk 100
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 10.6.1.1 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/3
   eth-trunk 0
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.10.1.2 255.255.255.0
   pim sm
   ospf enable 1 area 0.0.0.0
   m-lag unpaired-port reserved
  #
  interface 100GE1/0/5
   eth-trunk 0
  #
  ospf 1
   import-route direct type 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
    network 10.6.6.6 0.0.0.0
  #
  pim
   static-rp 10.6.6.6
   rpf-frr
  #
  return
  ```