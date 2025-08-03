Example for Configuring VPN IP FRR
==================================

If multiple CEs at a VPN site connect to the same PE and VPN IP FRR is configured on the PE, the PE can rapidly switch traffic to a link between another CE and the PE if a link between one CE and the PE fails.

#### Networking Requirements

At a VPN site, different CEs use BGP to access the same PE. The PE learns multiple IP VPN routes with the same VPN prefix from the CEs. To enable the PE to select a pair of primary and backup routes, deploy VPN IP FRR. After this feature is deployed, the PE generates a pair of primary and backup routes destined for the VPN prefix. If the primary route fails, the PE quickly switches VPN IP traffic to the backup route.

On the network shown in [Figure 1](#EN-US_TASK_0172369561__fig_dc_vrp_mpls-l3vpn-v4_cfg_201401), an EBGP peer relationship is established between the PE and each CE. There are two BGP routes from the PE to Loopback 1 on DeviceA. The optimal route resides on Link\_A, and the second optimal route resides on Link\_B. VPN IP FRR must be deployed on the PE to enable traffic to be quickly switched to Link\_B when Link\_A fails.

**Figure 1** Configuring VPN IP FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_201401.png "Click to enlarge")  


#### Precautions

In a VPN FRR scenario, after the primary path recovers, traffic is switched back to this path. Because the order in which nodes undergo IGP convergence differs, packet loss may occur during the switchback. To resolve this problem, run the [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* command to configure a route selection delay so that traffic is switched back only after forwarding entries on the devices along the primary path are updated. The delay specified using *delay-value* depends on various factors, such as the number of routes on the devices. Set an appropriate delay as needed.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP at the VPN site, so that the route to Loopback 1 on DeviceA can be advertised to CE1 and CE2.
2. Configure a VPN instance named vpna on the PE and bind GE 0/1/0 and GE 0/2/0 to vpna.
3. Establish an EBGP peer relationship between the PE and CE1, and between the PE and CE2. On CE1 and CE2, configure IGP and BGP to import routes from each other.
4. Enable BGP VPN auto FRR on the PE.

#### Data Preparation

To complete the configuration, you need the following data:

* VPN instance name (vpna) and attributes of the VPN instance IPv4 address family, for example, the RD (100:1) and VPN targets (100:100), on the PE
* MEDs configured for the IGP routes imported into BGP on CE1 and CE2

#### Procedure

1. Configure IP addresses for the interfaces on the Routers at the VPN site.
   
   
   
   For configuration details, see the configuration files.
2. Configure IGP at the VPN site, so that the route to Loopback 1 on DeviceA can be advertised to CE1 and CE2. This example uses OSPF as IGP.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] ospf 1
   ```
   ```
   [*CE1-ospf] area 0
   ```
   ```
   [*CE1-ospf-1-area-0.0.0.0] network 10.3.1.0 0.0.0.255
   ```
   ```
   [*CE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [*CE1-ospf] quit
   ```
   ```
   [*CE1] commit
   ```
   
   The configurations of CE2 and DeviceA are similar to the configuration of CE1. For configuration details, see the configuration files.
   
   After completing the configurations, run the **display ip routing-table** command on the CEs. The command output shows that CE1 and CE2 have learned the route to Loopback 1 on DeviceA. The following example uses the command output on CE1.
   
   ```
   <CE1> display ip routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 12       Routes : 12        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct 0    0             D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       11.11.11.11/32  OSPF   10   1             D  10.3.1.2        GigabitEthernet0/2/0
          10.3.1.0/24  Direct 0    0             D  10.3.1.1        GigabitEthernet0/2/0
          10.3.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
        10.3.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
          10.4.1.0/24  OSPF   10   2             D  10.3.1.2        GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
3. Configure a VPN instance on the PE and bind the interfaces connecting the PE to CEs to the VPN instance.
   
   
   
   # Configure a VPN instance named vpna on the PE, and bind GE0/1/0 and GE0/2/0 to the instance.
   
   ```
   <PE> system-view
   ```
   ```
   [~PE] ip vpn-instance vpna
   ```
   ```
   [*PE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] vpn-target 100:100
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE-vpn-instance-vpna] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*PE-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE] quit
   ```
4. Establish EBGP peer relationships between the PE and CEs.
   
   
   
   # Configure the PE.
   
   ```
   [~PE] bgp 100
   ```
   ```
   [*PE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE-bgp-vpna] peer 10.1.1.2 as-number 65410
   ```
   ```
   [*PE-bgp-vpna] peer 10.2.1.2 as-number 65410
   ```
   ```
   [*PE-bgp-vpna] quit
   ```
   ```
   [*PE-bgp] commit
   ```
   ```
   [~PE-bgp] quit
   ```
   
   # Configure CE1.
   
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] peer 10.1.1.1 as-number 100
   ```
   ```
   [*CE1-bgp] commit
   ```
   ```
   [~CE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [*CE2] bgp 65410
   ```
   ```
   [*CE2-bgp] peer 10.2.1.1 as-number 100
   ```
   ```
   [*CE2-bgp] commit
   ```
   ```
   [~CE2-bgp] quit
   ```
   
   After completing the configurations, run the **display bgp vpnv4 vpn-instance vpna peer** command on the PE. The command output shows that the status of the EBGP peer relationship between the PE and CEs is **Established**.
   
   ```
   <PE> display bgp vpnv4 vpn-instance vpna peer
    
    BGP local router ID : 1.1.1.9
    Local AS number : 100
    Total number of peers : 2         Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.2        4       65410       21       23     0 00:17:47 Established        1
     10.2.1.2        4       65410       51       64     0 00:15:03 Established        1
   ```
5. Configure OSPF and BGP to import routes from each other on the CEs.
   
   
   
   # Configure CE1.
   
   ```
   [*CE1] bgp 65410
   ```
   ```
   [*CE1-bgp] network 11.11.11.11 32
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] ospf 1
   ```
   ```
   [*CE1-ospf-1] import-route bgp
   ```
   ```
   [*CE1-ospf-1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [*CE2] bgp 65410
   ```
   ```
   [*CE2-bgp] network 11.11.11.11 32
   ```
   ```
   [*CE2-bgp] quit
   ```
   ```
   [*CE2] ospf 1
   ```
   ```
   [*CE2-ospf-1] import-route bgp
   ```
   ```
   [*CE2-ospf-10] quit
   ```
   ```
   [*CE2] commit
   ```
   
   After completing the configurations, run the **display ip routing-table vpn-instance** command on the PE. The command output shows the route to the loopback interface on DeviceA.
   
   ```
   <PE> display ip routing-table vpn-instance vpna
   display ip routing-table  vpn-instance vpna
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
            Destinations : 8        Routes : 8         
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
          10.1.1.0/24  Direct 0    0             D  10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
       11.11.11.11/32  EBGP   255  1             RD 10.1.1.2        GigabitEthernet0/1/0
          10.2.1.0/24  Direct 0    0             D  10.2.1.1        GigabitEthernet0/2/0
          10.2.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
        10.2.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
6. Enable VPN BGP auto FRR on the PE.
   
   
   
   # Configure the PE.
   
   ```
   [~PE] bgp 100
   ```
   ```
   [~PE-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE-bgp-vpna] auto-frr
   ```
   ```
   [*PE-bgp-vpna] route-select delay 300
   ```
   ```
   [*PE-bgp-vpna] quit
   ```
   ```
   [*PE-bgp] quit
   ```
   ```
   [*PE] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**auto-frr**](cmdqueryname=auto-frr) command configured in the BGP-VPN instance IPv4 address family view is valid only for the networking where BGP runs between the PE and CEs.
7. Verify the configuration.
   
   
   
   Run the **display ip routing-table vpn-instance** command on the PE. The command output shows that the next hop to 11.11.11.11/32 is **10.1.1.2**, and the PE has a backup next hop and a backup outbound interface.
   
   ```
   <PE> display ip routing-table vpn-instance vpna 11.11.11.11 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
   Summary Count : 1
   
   Destination: 11.11.11.11/32          
        Protocol: EBGP            Process ID: 0              
      Preference: 255                   Cost: 1              
         NextHop: 10.1.1.2         Neighbour: 0.0.0.0        
           State: Active Adv Relied      Age: 00h35m31s           
             Tag: 0                 Priority: low            
           Label: NULL               QoSInfo: 0x0            
      IndirectID: 0xc7          
    RelayNextHop: 10.1.1.2         Interface: GigabitEthernet0/1/0
        TunnelID: 0x0                  Flags: RD             
       BkNextHop: 10.2.1.2       BkInterface: GigabitEthernet0/2/0
         BkLabel: NULL           SecTunnelID: 0x0              
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0              
    BkIndirectID: 0xc8
   ```
   
   Run the [**shutdown**](cmdqueryname=shutdown) command on GE 0/2/0 of CE1 to simulate a link fault.
   
   ```
   [~CE1] interface Gigabitethernet0/2/0
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~CE1] quit
   ```
   
   Run the **display ip routing-table vpn-instance** command on the PE. The command output shows that the next hop to 11.11.11.11/32 is 10.2.1.2, and the PE does not have a backup next hop or a backup outbound interface.
   
   ```
   <PE> display ip routing-table vpn-instance vpna 11.11.11.11 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpna
   Summary Count : 1
   
   Destination: 11.11.11.11/32          
        Protocol: EBGP            Process ID: 0              
      Preference: 255                   Cost: 1              
         NextHop: 10.2.1.2         Neighbour: 0.0.0.0        
           State: Active Adv Relied      Age: 00h00m04s           
             Tag: 0                 Priority: low            
           Label: NULL               QoSInfo: 0x0            
      IndirectID: 0xc8          
    RelayNextHop: 10.2.1.2         Interface: GigabitEthernet0/2/0
        TunnelID: 0x0                  Flags: RD  
   ```
   
   Private network IP FRR has taken effect.

#### Configuration Files

* PE configuration file
  ```
  #
  sysname PE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 100:100 export-extcommunity
    vpn-target 100:100 import-extcommunity
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.1 255.255.255.0
  #
  bgp 100
   #
   ipv4-family unicast
    undo synchronization
    #
   ipv4-family vpn-instance vpna
    auto-frr
    route-select delay 300
    peer 10.1.1.2 as-number 65410
    peer 10.2.1.2 as-number 65410
  #
  return
  
  ```
* CE1 configuration file
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  bgp 65410
   peer 10.1.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.1 enable
  #
  ospf 1 
   import-route bgp
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  return
  ```
* CE2 configuration file
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
  #
  bgp 65410
   peer 10.2.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.2.1.1 enable
  #
  ospf 1 
    import-route bgp
    area 0.0.0.0
     network 10.4.1.0 0.0.0.255
  #
  return
  ```
* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #
  ospf 1 
   area 0.0.0.0
    network 11.11.11.11 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.4.1.0 0.0.0.255
  #
  return
  ```