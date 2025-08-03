Example for Configuring IPv4 Layer 3 Multicast over M-LAG
=========================================================

Example for Configuring IPv4 Layer 3 Multicast over M-LAG

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001699389541__fig_01), to ensure high IPv4 network reliability, the user-side device Device is dual-homed to the active-active VRRP gateways DeviceA and DeviceB through an M-LAG. The user Receiver connected to the Device wants to receive the multicast video program from the Source.

**Figure 1** Network diagram for IPv4 Layer 3 multicast over M-LAG configuration  
![](figure/en-us_image_0000001651309270.png)

**Table 1** Device configuration list
| Device | Interface | VLANIF interface | IP Address |
| --- | --- | --- | --- |
| DeviceA | 100GE1/0/1 represents interface1. | VLANIF 12 | 10.3.1.1/24 |
| 100GE 1/0/6 represents interface6. | VLANIF 13 | 10.5.1.1/24 |
| Eth-Trunk 10 | VLANIF 11 | 10.2.1.1/24 |
| MEth0/0/0 | â | 10.1.1.1/24 |
| DeviceB | 100GE1/0/1 represents interface1. | VLANIF 14 | 10.4.1.1/24 |
| 100GE 1/0/6 represents interface6. | VLANIF 13 | 10.5.1.2/24 |
| Eth-Trunk 10 | VLANIF 11 | 10.2.1.2/24 |
| MEth0/0/0 | â | 10.1.1.2/24 |
| DeviceC | 100GE1/0/1 represents interface1. | VLANIF 12 | 10.3.1.2/24 |
| 100GE1/0/2 represents interface2. | VLANIF 14 | 10.4.1.2/24 |
| 100GE1/0/3 represents interface3. | VLANIF 15 | 10.6.1.1/24 |



#### Configuration Roadmap

![](public_sys-resources/note_3.0-en-us.png) 

To meet the requirements, the M-LAG master and backup devices (DeviceA and DeviceB) must have both a peer link and a direct Layer 3 link between them, and they must have the same multicast configuration.

The configuration roadmap is as follows:

1. Configure M-LAG on DeviceA and DeviceB, and configure dual-homed access on Device to enhance high reliability of the network.
2. On DeviceA and DeviceB, configure IP and MAC addresses for VLANIF interfaces so that DeviceA and DeviceB function as active-active gateways for access devices.
3. Configure a unicast routing protocol on DeviceA, DeviceB, and DeviceC to implement IP interworking. Multicast routing protocols work depending on unicast routing protocols.
4. Enable PIM-SM and IGMP on VLANIF interfaces of DeviceA and DeviceB, and enable PIM-SM on VLANIF interfaces of DeviceC, so that multicast forwarding entries can be created.
5. Enable the PIM silent function on user-side VLANIF interfaces on DeviceA and DeviceB, to ensure that DeviceA and DeviceB both act as DRs and send Join messages to the RP.
6. On DeviceA and DeviceB, enable IGMP snooping in the VLANs corresponding to the VLANIF interfaces to implement accurate multicast forwarding on the Layer 2 network.
7. Disable STP on the interfaces at both sides of the Layer 3 link between the master and backup devices, and specify the VLAN that is not allowed on the peer-link. This ensures normal multicast forwarding on the M-LAG.

#### Procedure

1. Configure V-STP-based M-LAG and M-LAG active-active gateways.
   
   
   1. Configure a V-STP-based M-LAG.
      
      # On DeviceA, configure a DFS group, a peer-link, V-STP, an M-LAG, and the LACP M-LAG system priority and system ID, to set up a V-STP-based M-LAG. The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname DeviceA
      [*HUAWEI] commit
      [~DeviceA] interface meth 0/0/0
      [~DeviceA-MEth0/0/0] ip address 10.1.1.1 24
      [*DeviceA-MEth0/0/0] quit
      [*DeviceA] dfs-group 1
      [*DeviceA-dfs-group-1] dual-active detection source ip 10.1.1.1 peer 10.1.1.2
      [*DeviceA-dfs-group-1] priority 150
      [*DeviceA-dfs-group-1] authentication-mode hmac-sha256 password YsHsjx_202206
      [*DeviceA-dfs-group-1] quit
      [*DeviceA] interface eth-trunk 1
      [*DeviceA-Eth-Trunk1] trunkport 100ge 1/0/4 to 1/0/5
      [*DeviceA-Eth-Trunk1] mode lacp-static
      [*DeviceA-Eth-Trunk1] peer-link 1
      [*DeviceA-Eth-Trunk1] quit
      [*DeviceA] stp mode rstp
      [*DeviceA] stp v-stp enable
      [*DeviceA] vlan batch 11
      [*DeviceA] interface eth-trunk 10
      [*DeviceA-Eth-Trunk10] mode lacp-static
      [*DeviceA-Eth-Trunk10] port link-type trunk
      [*DeviceA-Eth-Trunk10] port trunk allow-pass vlan 11
      [*DeviceA-Eth-Trunk10] trunkport 100ge 1/0/2 to 1/0/3
      [*DeviceA-Eth-Trunk10] dfs-group 1 m-lag 1
      [*DeviceA-Eth-Trunk10] lacp m-lag priority 10
      [*DeviceA-Eth-Trunk10] lacp m-lag system-id 00e0-fc00-0000
      [*DeviceA-Eth-Trunk10] quit
      [*DeviceA] commit
      ```
      
      On Device, bind uplink interfaces to an Eth-Trunk interface.
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname Device
      [*HUAWEI] commit
      [~Device] vlan batch 11
      [*Device] interface eth-trunk 20
      [*Device-Eth-Trunk20] mode lacp-static
      [*Device-Eth-Trunk20] port link-type trunk
      [*Device-Eth-Trunk20] port trunk allow-pass vlan 11
      [*Device-Eth-Trunk20] trunkport 100ge 1/0/1 to 1/0/4
      [*Device-Eth-Trunk20] quit
      [*Device] commit
      ```
   2. On DeviceA and DeviceB, configure IP and MAC addresses for VLANIF interfaces so that DeviceA and DeviceB function as active-active gateways for access devices.
      
      DeviceA and DeviceB must be configured with the same virtual IP address and virtual MAC address.
      
      # Configure DeviceA.
      ```
      [~DeviceA] interface vlanif 11
      [*DeviceA-Vlanif11] ip address 10.2.1.1 24
      [*DeviceA-Vlanif11] mac-address 0000-5e00-0101
      [*DeviceA-Vlanif11] quit
      [*DeviceA] commit
      ```
      
      # Configure DeviceB.
      ```
      [~DeviceB] interface vlanif 11
      [*DeviceB-Vlanif11] ip address 10.2.1.1 24
      [*DeviceB-Vlanif11] mac-address 0000-5e00-0101
      [*DeviceB-Vlanif11] quit
      [*DeviceB] commit
      ```
2. Configure OSPF to implement IP interworking.
   
   
   
   # Configure DeviceA. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] vlan batch 12 13
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 12
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/6
   [*DeviceA-100GE1/0/6] port link-type trunk
   [*DeviceA-100GE1/0/6] port trunk allow-pass vlan 13
   [*DeviceA-100GE1/0/6] quit
   [*DeviceA] interface vlanif 12
   [*DeviceA-Vlanif12] ip address 10.3.1.1 24
   [*DeviceA-Vlanif12] quit
   [*DeviceA] interface vlanif 13
   [*DeviceA-Vlanif13] ip address 10.5.1.1 24
   [*DeviceA-Vlanif13] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.1 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If the peer-link is selected as the optimal link to the RP or multicast source by the unicast routing protocol, multicast traffic with the peer-link interface as the outbound interface may fail to be forwarded. To prevent this problem, ensure that the Layer 3 link between the M-LAG master and backup devices has a route cost less than or equal to the route cost of the peer-link, so that the Layer 3 link is selected as the optimal route by the unicast routing protocol.
3. Enable PIM-SM and IGMP on VLANIF interfaces of DeviceA and DeviceB, and enable PIM-SM on VLANIF interfaces of DeviceC.
   
   # Configure DeviceA. The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface vlanif 11
   [*DeviceA-Vlanif11] pim sm
   [*DeviceA-Vlanif11] igmp enable
   [*DeviceA-Vlanif11] quit
   [*DeviceA] interface vlanif 12
   [*DeviceA-Vlanif12] pim sm
   [*DeviceA-Vlanif12] igmp enable
   [*DeviceA-Vlanif12] quit
   [*DeviceA] interface vlanif 13
   [*DeviceA-Vlanif13] pim sm
   [*DeviceA-Vlanif13] igmp enable
   [*DeviceA-Vlanif13] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceC. Configure VLANIF 15 of DeviceC as a C-BSR and C-RP.
   ```
   [~DeviceC] multicast routing-enable
   [*DeviceC] interface vlanif 12
   [*DeviceC-Vlanif12] pim sm
   [*DeviceC-Vlanif12] quit
   [*DeviceC] interface vlanif 14
   [*DeviceC-Vlanif14] pim sm
   [*DeviceC-Vlanif14] quit
   [*DeviceC] interface vlanif 15
   [*DeviceC-Vlanif15] pim sm
   [*DeviceC-Vlanif15] quit
   [*DeviceC] pim
   [*DeviceC-pim] c-bsr vlanif 15
   [*DeviceC-pim] c-rp vlanif 15
   [*DeviceC-pim] quit
   [*DeviceC] commit
   ```
4. Enable the PIM silent function on user-side VLANIF interfaces of DeviceA and DeviceB.
   
   # Configure DeviceA. The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
   ```
   [~DeviceA] interface vlanif 11
   [~DeviceA-Vlanif11] pim silent
   [*DeviceA-Vlanif11] quit
   [*DeviceA] commit
   ```
5. On DeviceA and DeviceB, enable IGMP snooping in the VLANs corresponding to the VLANIF interfaces.
   
   # Configure DeviceA. The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
   ```
   [~DeviceA] igmp snooping enable
   [*DeviceA] vlan 11
   [*DeviceA-vlan11] igmp snooping enable
   [*DeviceA-vlan11] quit
   [*DeviceA] vlan 12
   [*DeviceA-vlan12] igmp snooping enable
   [*DeviceA-vlan12] quit
   [*DeviceA] vlan 13
   [*DeviceA-vlan13] igmp snooping enable
   [*DeviceA-vlan13] quit
   [*DeviceA] commit
   ```
6. Disable STP on the interfaces at both sides of the Layer 3 link between the M-LAG master and backup devices, and specify the VLAN that is not allowed on the peer-link.
   
   # Configure DeviceA. The configuration on DeviceB is similar to the configuration on DeviceA. For detailed configurations, see Configuration Scripts.
   ```
   [~DeviceA] interface 100ge 1/0/6
   [~DeviceA-100GE1/0/6] stp disable
   [*DeviceA-100GE1/0/6] quit
   [*DeviceA] interface eth-trunk 1
   [*DeviceA-Eth-Trunk1] port vlan exclude 1 13
   [*DeviceA-Eth-Trunk1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display dfs-group**](cmdqueryname=display+dfs-group) command on DeviceA to check M-LAG information.

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

In the preceding command output, the **Heart beat state** field displays **OK**, indicating that the heartbeat status is normal. DeviceA is node 1 with a priority of 150, and its **State** is **Master**; DeviceB is node 2 with a priority of 120, and its **State** is **Backup**. The preceding information shows that DeviceA is the M-LAG master device, and DeviceB is the M-LAG backup device.

# Run the [**display pim interface**](cmdqueryname=display+pim+interface) command on DeviceA and DeviceB to check the PIM configuration and running status on interfaces.

```
[~DeviceA] display pim interface
 VPN-Instance: public net
 Interface           State NbrCnt HelloInt     DR-Pri     DR-Address
 Vlanif11            up         0       30          1     10.2.1.1 (local)
 Vlanif12            up         1       30          1     10.3.1.2
 Vlanif13            up         1       30          1     10.5.1.2 
```
```
[~DeviceB] display pim interface
 VPN-Instance: public net
 Interface           State NbrCnt HelloInt     DR-Pri     DR-Address
 Vlanif11            up         0       30          1     10.2.1.2 (local)
 Vlanif14            up         1       30          1     10.4.1.2 
 Vlanif13            up         1       30          1     10.5.1.2 (local)
```

According to the preceding information, VLANIF 11 of DeviceA and VLANIF 11 of DeviceB are both DRs; therefore, both DeviceA and DeviceB will send Join messages to the upstream RP.

# Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on DeviceA, DeviceB, and DeviceC to check the PIM-SM routing tables on them.

```
[~DeviceC] display pim routing-table
 VPN-Instance: public net                                          
 Total 1 (*, G) entry; 1 (S, G) entry                              

 (*, 225.1.1.1)                                                    
     RP: 10.6.1.1 (local)                                          
     Protocol: pim-sm, Flag: WC                                    
     UpTime: 00:14:45                                              
     Upstream interface: Register                                  
         Upstream neighbor: NULL                                   
         RPF prime neighbor: NULL                                  
     Downstream interface(s) information:                          
     Total number of downstreams: 2
        1: Vlanif12
             Protocol: pim-sm, UpTime: 00:14:45, Expires: 00:02:45 
        2: Vlanif14
             Protocol: pim-sm, UpTime: 00:14:45, Expires: 00:02:45 

 (10.6.1.2, 225.1.1.1)                                             
     RP: 10.6.1.1 (local)                                          
     Protocol: pim-sm, Flag: SPT LOC ACT                     
     UpTime: 00:15:47                                              
     Upstream interface: Vlanif15                                  
         Upstream neighbor: NULL                                   
         RPF prime neighbor: NULL                                  
     Downstream interface(s) information:                          
     Total number of downstreams: 2
        1: Vlanif12
             Protocol: pim-sm, UpTime: 00:14:45, Expires: 00:02:45 
        2: Vlanif14
             Protocol: pim-sm, UpTime: 00:14:45, Expires: 00:02:45 

```

According to the preceding information, DeviceC has two downstream interfaces VLANIF 12 and VLANIF 14. Because both DeviceA and DeviceB are DRs, data sent from the multicast source is forwarded to the two devices through the two downstream interfaces. In real-world application, the downstream interfaces on DeviceC are determined by the unicast routes from the DRs to the RP.

```
[~DeviceA] display pim routing-table
 VPN-Instance: public net                                 
 Total 1 (*, G) entry; 1 (S, G) entry                     

 (*, 225.1.1.1)                                           
     RP: 10.6.1.1                                         
     Protocol: pim-sm, Flag: WC                           
     UpTime: 00:18:31                                     
     Upstream interface: Vlanif12                         
         Upstream neighbor: 10.3.1.2                      
         RPF prime neighbor: 10.3.1.2                     
     Downstream interface(s) information:                 
     Total number of downstreams: 1                       
        1: Vlanif11
             Protocol: igmp, UpTime: 00:18:31, Expires: - 

 (10.6.1.2, 225.1.1.1)                                    
     RP: 10.6.1.1                                         
     Protocol: pim-sm, Flag: SPT ACT                      
     UpTime: 00:17:31                                     
     Upstream interface: Vlanif12                         
         Upstream neighbor: 10.3.1.2                      
         RPF prime neighbor: 10.3.1.2                     
     Downstream interface(s) information:                 
     Total number of downstreams: 1                       
        1: Vlanif11
             Protocol: pim-sm, UpTime: 00:17:31, Expires: - 
```
```
[~DeviceB] display pim routing-table
 VPN-Instance: public net                                 
 Total 1 (*, G) entry; 1 (S, G) entry                     

 (*, 225.1.1.1)                                           
     RP: 10.6.1.1                                         
     Protocol: pim-sm, Flag: WC                           
     UpTime: 00:18:59                                     
     Upstream interface: Vlanif14                         
         Upstream neighbor: 10.4.1.2                      
         RPF prime neighbor: 10.4.1.2                     
     Downstream interface(s) information:                 
     Total number of downstreams: 1                       
        1: Vlanif11
             Protocol: igmp, UpTime: 00:18:59, Expires: - 

 (10.6.1.2, 225.1.1.1)                                    
     RP: 10.6.1.1                                         
     Protocol: pim-sm, Flag: SPT ACT                      
     UpTime: 00:17:59                                     
     Upstream interface: Vlanif14                         
         Upstream neighbor: 10.4.1.2                      
         RPF prime neighbor: 10.4.1.2                     
     Downstream interface(s) information:                 
     Total number of downstreams: 1                       
        1: Vlanif11
             Protocol: pim-sm, UpTime: 00:17:59, Expires: - 
```

The preceding information shows that both DeviceA and DeviceB have a downstream interface VLANIF 11. When the M-LAG is functioning normally, both the master and backup M-LAG member interfaces can forward multicast data traffic to the receiver, implementing load sharing. The load balancing rule is as follows: If the last decimal number of a multicast group address is an odd number (for example, 225.1.1.1), traffic is forwarded by the M-LAG master member interface. If the last decimal number of a multicast group address is an even number (for example, 225.1.1.2), traffic is forwarded by the M-LAG backup member interface. In this example, the M-LAG master device forwards data traffic to the multicast group address 225.1.1.1.


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
  vlan batch 11 to 13
  #
  stp mode rstp
  stp v-stp enable
  #
  multicast routing-enable
  #
  igmp snooping enable
  #
  vlan 11
   igmp snooping enable
  #
  vlan 12
   igmp snooping enable
  #
  vlan 13
   igmp snooping enable
  #
  interface Vlanif11
   ip address 10.2.1.1 255.255.255.0
   mac-address 0000-5e00-0101  
   pim silent
   pim sm
   igmp enable
  #
  interface Vlanif12
   ip address 10.3.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface Vlanif13
   ip address 10.5.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface MEth0/0/0
   ip address 10.1.1.1 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1 13
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
   lacp m-lag priority 10
   lacp m-lag system-id 00e0-fc00-0000
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 12
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
  interface 100GE1/0/6
   port link-type trunk
   port trunk allow-pass vlan 13
   stp disable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
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
  vlan batch 11 13 to 14
  #
  stp mode rstp
  stp v-stp enable
  #
  multicast routing-enable
  #
  igmp snooping enable
  #
  vlan 11
   igmp snooping enable
  #
  vlan 13
   igmp snooping enable
  #
  vlan 14
   igmp snooping enable
  #
  interface Vlanif11
   ip address 10.2.1.1 255.255.255.0
   mac-address 0000-5e00-0101  
   pim silent
   pim sm
   igmp enable
  #
  interface Vlanif13
   ip address 10.5.1.2 255.255.255.0
   pim sm
   igmp enable
  #
  interface Vlanif14
   ip address 10.4.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface MEth0/0/0
   ip address 10.1.1.2 255.255.255.0
  #
  interface Eth-Trunk1
   mode lacp-static
   peer-link 1
   port vlan exclude 1 13
  #
  interface Eth-Trunk10
   port link-type trunk
   port trunk allow-pass vlan 11
   mode lacp-static
   dfs-group 1 m-lag 1
   lacp m-lag priority 10
   lacp m-lag system-id 00e0-fc00-0000
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 14
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
  interface 100GE1/0/6
   port link-type trunk
   port trunk allow-pass vlan 13
   stp disable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.4.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 12 14 to 15
  #
  multicast routing-enable
  #
  interface Vlanif12
   ip address 10.3.1.2 255.255.255.0
   pim sm
  #
  interface Vlanif14
   ip address 10.4.1.2 255.255.255.0
   pim sm
  #
  interface Vlanif15
   ip address 10.6.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/1
   port link-type trunk
   port trunk allow-pass vlan 12
  #
  interface 100GE1/0/2
   port link-type trunk
   port trunk allow-pass vlan 14
  #
  interface 100GE1/0/3
   port default vlan 15
  #
  ospf 1
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.4.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
  #
  pim
   c-bsr Vlanif15
   c-rp Vlanif15
  #
  return
  ```
* Device
  
  ```
  #
  sysname Device
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