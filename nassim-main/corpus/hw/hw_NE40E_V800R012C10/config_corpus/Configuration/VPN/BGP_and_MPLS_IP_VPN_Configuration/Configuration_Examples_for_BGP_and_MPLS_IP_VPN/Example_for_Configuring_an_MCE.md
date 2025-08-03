Example for Configuring an MCE
==============================

OSPF multi-instance can be configured on a CE to isolate different types of services on a LAN.

#### Networking Requirements

Branch A at site 1 and branch B at site 2 need to communicate with the HQ over the carrier backbone network. Branches A and B are responsible for different types of services and need to access service-related departments or servers in different areas of the headquarters. In this example, the services in branches A and B need to be isolated. If the traditional BGP/MPLS IP VPN technology is used, branches A and B each require a CE to be deployed at the HQ. This deployment is expensive. To resolve this issue, deploy a multi-VPN-instance CE (MCE) at the HQ to connect to the sites of different VPNs, as shown in [Figure 1](#EN-US_TASK_0172369543__fig_dc_vrp_mpls-l3vpn-v4_cfg_012201).

* CE1 in branch A and CE2 in branch B belong to vpna and vpnb, respectively.
* The MCE connects to the sites on vpna and vpnb at the headquarters.
* vpna and vpnb use different VPN targets.
* The headquarters use Device A and Device B to communicate with branches A and B, respectively.

This configuration ensures that users on the same VPN can communicate with each other and that users on different VPNs cannot communicate with each other.

**Figure 1** Network diagram of configuring an MCE![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GE0/1/0, GE0/2/0, GE0/3/0, and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_012201.png)  


#### Precautions

When configuring an MCE, note the following:

* Different VPN instances must be configured on the MCE and bound to different interfaces.
* Routing loop detection must be disabled on the MCE so that the MCE exchanges routing information with the PEs using OSPF multi-instance.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on PEs and enable MP-IBGP on the PEs to exchange VPN routing information.
2. Establish EBGP peer relationships between PEs and CEs to import VPN routes into the PEs' VRF tables.
3. Configure OSPF multi-instance on the MCE and PE2 to exchange VPN routing information.
4. Configure RIPv2 on the MCE, DeviceA, and DeviceB to exchange VPN routing information.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configuring OSPF multi-instance on the MCE and PE2 includes the following configurations:

* Import BGP routes to PE2's OSPF process in which OSPF multi-instance is configured on the MCE and PE2. Then advertise PE1's VPN routes to the MCE.
* Import all routes to PE2's OSPF process in which OSPF multi-instance is configured on the MCE and PE2, in PE2's BGP-VPN instance IPv4 address family view. Then advertise MCE's VPN routes to PE1.


#### Data Preparation

To complete the configuration, you need the following data:

* VPN instances on PE1 and PE2 (vpna and vpnb), the MCE for each service, vpna's import and export VPN targets (111:1), and vpnb's import and export VPN targets (222:2)
* vpna's OSPF process ID (100) and vpnb's OSPF process ID (200)
* vpna's RIP process ID (100) and vpnb's RIP process ID (200) used for importing VPN routes of sites 3 and 4 on the MCE

#### Procedure

1. Enable OSPF on the PEs on the backbone network to ensure that the PEs interwork with each other.
   
   
   
   For configuration details, see the configuration files.
   
   After the configurations are complete, the PEs can learn the address of each other's Loopback1 interface.
   
   The following example uses the command output on PE2.
   
   ```
   <PE2> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 9        Routes : 9
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  OSPF   10   1             D  172.16.1.1      GigabitEthernet0/1/0
           2.2.2.2/32  Direct 0    0             D  127.0.0.1       LoopBack1
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct 0    0             D  172.16.1.2      GigabitEthernet0/1/0
        172.16.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
2. Configure MPLS and MPLS LDP both globally and per interface on each node of the backbone network. Then establish LDP LSPs between PEs.
   
   
   
   For configuration details, see the configuration files.
   
   After completing the configurations, run the **display mpls ldp session** command on PEs. The command output shows that an MPLS LDP session has been established between the PEs and its status is **Operational**.
   
   The following example uses the command output on PE2.
   
   ```
   <PE2> display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   --------------------------------------------------------------------------
    PeerID             Status       LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    1.1.1.1:0          Operational DU  Active  0001:16:01  9608/9608
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   ```
3. Configure VPN instances on PE1 and PE2, bind the VPN instances on PE1 to PE1's interfaces connected to CE1 and CE2, and bind the VPN instances on PE2 to PE2's interfaces connected to the MCE.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] ip vpn-instance vpnb
   ```
   ```
   [*PE1-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpnb] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] ip address 10.1.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpnb
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] ip vpn-instance vpnb
   ```
   ```
   [*PE2-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] route-distinguisher 200:2
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   ```
   ```
   [*PE2-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpnb] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.5.1.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2]interface gigabitethernet0/3/0
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] ip binding vpn-instance vpnb
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] ip address 10.5.2.1 24
   ```
   ```
   [*PE2-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure VPN instances on the MCE and bind the VPN instances to the MCE's interfaces connected to Site3, Site4, and PE2.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname MCE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~MCE] ip vpn-instance vpna
   ```
   ```
   [*MCE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*MCE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*MCE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*MCE-vpn-instance-vpna] quit
   ```
   ```
   [*MCE] ip vpn-instance vpnb
   ```
   ```
   [*MCE-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*MCE-vpn-instance-vpnb-af-ipv4] route-distinguisher 200:2
   ```
   ```
   [*MCE-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [*MCE-vpn-instance-vpnb] quit
   ```
   ```
   [*MCE] interface gigabitethernet0/3/0
   ```
   ```
   [*MCE-GigabitEthernet0/3/0] ip binding vpn-instance vpna
   ```
   ```
   [*MCE-GigabitEthernet0/3/0] ip address 10.3.1.2 24
   ```
   ```
   [*MCE-GigabitEthernet0/3/0] quit
   ```
   ```
   [*MCE] interface gigabitethernet0/1/1
   ```
   ```
   [*MCE-GigabitEthernet0/1/1] ip binding vpn-instance vpnb
   ```
   ```
   [*MCE-GigabitEthernet0/1/1] ip address 10.4.1.2 24
   ```
   ```
   [*MCE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*MCE] interface gigabitethernet0/1/0
   ```
   ```
   [*MCE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*MCE-GigabitEthernet0/1/0] ip address 10.5.1.2 24
   ```
   ```
   [*MCE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*MCE] interface gigabitethernet0/2/0
   ```
   ```
   [*MCE-GigabitEthernet0/2/0] ip binding vpn-instance vpnb
   ```
   ```
   [*MCE-GigabitEthernet0/2/0] ip address 10.5.2.2 24
   ```
   ```
   [*MCE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*MCE] commit
   ```
5. Establish an MP-IBGP peer relationship between the PEs, and establish EBGP peer relationships between PE1 and CE1 and between PE1 and CE2.
   
   
   
   For configuration details, see the configuration files.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on PE1. The command output shows that IBGP peer relationships have been established between PE1 and PE2 and that EBGP peer relationships have been established between PE1 and CE1 and between PE1 and CE2.
   
   ```
   [~PE1] display bgp vpnv4 all peer
   ```
   ```
    BGP local router ID : 172.16.1.1
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2.2.2.2         4         100       13       12     0 00:04:49 Established   4
   
     Peer of IPv4-family for vpn instance :
   
     VPN-Instance vpna, router ID 172.16.1.1:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.1        4       65410       12       13     0 00:06:00 Established   1
     VPN-Instance vpnb, router ID 172.16.1.1:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.2.1.1        4       65420       12       12     0 00:06:00 Established   1
   ```
6. Configure OSPF multi-instance on PE2 and the MCE.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] ospf 100 vpn-instance vpna
   ```
   ```
   [*PE2-ospf-100] area 0
   ```
   ```
   [*PE2-ospf-100-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-100-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-100] import-route bgp
   ```
   ```
   [*PE2-ospf-100] quit
   ```
   ```
   [*PE2] ospf 200 vpn-instance vpnb
   ```
   ```
   [*PE2-ospf-200] area 0
   ```
   ```
   [*PE2-ospf-200-area-0.0.0.0] network 10.5.2.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-200-area-0.0.0.0] quit
   ```
   ```
   [*PE2-ospf-200] import-route bgp
   ```
   ```
   [*PE2-ospf-200] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] import-route ospf 100
   ```
   ```
   [*PE2-bgp-vpna] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpnb
   ```
   ```
   [*PE2-bgp-vpnb] import-route ospf 200
   ```
   ```
   [*PE2-bgp-vpnb] commit
   ```
   ```
   [~PE2-bgp-vpnb] quit
   ```
   
   # Configure the MCE.
   
   ```
   [~MCE] ospf 100 vpn-instance vpna
   ```
   ```
   [*MCE-ospf-100] area 0
   ```
   ```
   [*MCE-ospf-100-area-0.0.0.0] network 10.5.1.0 0.0.0.255
   ```
   ```
   [*MCE-ospf-100-area-0.0.0.0] quit
   ```
   ```
   [*MCE-ospf-100] quit
   ```
   ```
   [*MCE] ospf 200 vpn-instance vpnb
   ```
   ```
   [*MCE-ospf-200] area 0
   ```
   ```
   [*MCE-ospf-200-area-0.0.0.0] network 10.5.2.0 0.0.0.255
   ```
   ```
   [*MCE-ospf-200-area-0.0.0.0] commit
   ```
   ```
   [~MCE-ospf-200-area-0.0.0.0] quit
   ```
   ```
   [~MCE-ospf-200] quit
   ```
7. Disable routing loop detection on the MCE and import RIP routes destined for the VPN sites.
   
   
   ```
   [~MCE] ospf 100 vpn-instance vpna
   ```
   ```
   [~MCE-ospf-100] vpn-instance-capability simple
   Warning: This operation may cause a routing loop. Continue? [Y/N]:Y
   ```
   ```
   [*MCE-ospf-100] import-route rip 100
   ```
   ```
   [*MCE-ospf-100] quit
   ```
   ```
   [*MCE] ospf 200 vpn-instance vpnb
   ```
   ```
   [*MCE-ospf-200] vpn-instance-capability simple
   Warning: This operation may cause a routing loop. Continue? [Y/N]:Y
   ```
   ```
   [*MCE-ospf-200] import-route rip 200
   ```
   ```
   [*MCE-ospf-200] commit
   ```
   ```
   [~MCE-ospf-200] quit
   ```
8. Configure RIPv2 on the MCE to import the VPN routes of sites 3 and 4.
   
   
   
   # Configure the MCE.
   
   ```
   [~MCE] rip 100 vpn-instance vpna
   ```
   ```
   [~MCE-rip-100] version 2
   ```
   ```
   [*MCE-rip-100] network 10.0.0.0
   ```
   ```
   [*MCE-rip-100] import-route ospf 100
   ```
   ```
   [*MCE-rip-100] quit
   ```
   ```
   [~MCE] rip 200 vpn-instance vpnb
   ```
   ```
   [~MCE-rip-200] version 2
   ```
   ```
   [*MCE-rip-200] network 10.0.0.0
   ```
   ```
   [*MCE-rip-200] import-route ospf 200
   ```
   ```
   [*MCE-rip-200] commit
   ```
   ```
   [~MCE-rip-200] quit
   ```
9. Configure RIPv2 on Device A and Device B to implement interworking with the MCE.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] rip 100
   ```
   ```
   [*DeviceA-rip-100] version 2
   ```
   ```
   [*DeviceA-rip-100] network 10.0.0.0
   ```
   ```
   [*DeviceA-rip-100] network 33.0.0.0
   ```
   ```
   [*DeviceA-rip-100] commit
   ```
   ```
   [~DeviceA-rip-100] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] rip 200
   ```
   ```
   [*DeviceB-rip-200] version 2
   ```
   ```
   [*DeviceB-rip-200] network 10.0.0.0
   ```
   ```
   [*DeviceB-rip-200] network 44.0.0.0
   ```
   ```
   [*DeviceB-rip-200] commit
   ```
   ```
   [~DeviceB-rip-200] quit
   ```
10. Verify the configuration.
    
    
    
    # Run the **display ip routing-table** **vpn-instance** command on the MCE to view the routes to the peer CEs.
    
    The following example uses vpna.
    
    ```
    [~MCE] display ip routing-table vpn-instance vpna
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpna
             Destinations : 12       Routes : 12
    
    Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
    
           10.1.1.0/24  O_ASE  150  1             D  10.5.1.1        GigabitEthernet0/1/0
           10.3.1.0/24  Direct 0    0             D  10.3.1.2        GigabitEthernet0/3/0
           10.3.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
         10.3.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/3/0
        11.11.11.11/32  O_ASE  150  1             D  10.5.1.1        GigabitEthernet0/1/0
        33.33.33.33/32  RIP    100  1             D  10.3.1.1        GigabitEthernet0/3/0
           10.5.1.0/24  Direct 0    0             D  10.5.1.2        GigabitEthernet0/1/0
           10.5.1.1/32  Direct 0    0             D  10.5.1.1        GigabitEthernet0/1/0
           10.5.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         10.5.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
    255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    ```
    
    # Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** command on the PEs to view the routes to the peer sites.
    
    The following example uses vpna on PE1.
    
    ```
    [~PE1] display ip routing-table vpn-instance vpna
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpna
             Destinations : 9        Routes : 9
    
    Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
    
           10.1.1.0/24  Direct 0    0             D  10.1.1.2        GigabitEthernet0/1/0
           10.1.1.2/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
           10.3.1.0/24  IBGP   255  3             RD 2.2.2.2         GigabitEthernet0/3/0
           10.4.1.0/24  IBGP   255  2             RD 2.2.2.2         GigabitEthernet0/3/0
        11.11.11.11/32  EBGP   255  0             RD 10.1.1.1        GigabitEthernet0/1/0
        33.33.33.33/32  IBGP   255  2             RD 2.2.2.2         GigabitEthernet0/3/0
           10.5.1.0/24  IBGP   255  2             RD 2.2.2.2         GigabitEthernet0/3/0
    255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
    ```
    
    # Run the [**ping**](cmdqueryname=ping) command on CEs to check the connectivity between CE1 and DeviceA, and between CE2 and DeviceB. The ping operations are successful.
    
    The following example uses the command output on CE1.
    
    ```
    [~CE1] ping -a 11.11.11.11 33.33.33.33
    ```
    ```
      PING 33.33.33.33: 56  data bytes, press CTRL_C to break
        Reply from 33.33.33.33: bytes=56 Sequence=1 ttl=252 time=4 ms
        Reply from 33.33.33.33: bytes=56 Sequence=2 ttl=252 time=2 ms
        Reply from 33.33.33.33: bytes=56 Sequence=3 ttl=252 time=2 ms
        Reply from 33.33.33.33: bytes=56 Sequence=4 ttl=252 time=2 ms
        Reply from 33.33.33.33: bytes=56 Sequence=5 ttl=252 time=2 ms
    
      --- 33.33.33.33 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 2/2/4 ms
    ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 11.11.11.11 255.255.255.255
  #
  bgp 65410
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 11.11.11.11 255.255.255.255
    peer 10.1.1.2 enable
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
   ip address 10.2.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65420
   peer 10.2.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 22.22.22.22 255.255.255.255
    peer 10.2.1.2 enable
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv4-family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.2.1.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance vpna
    network 10.1.1.0 255.255.255.0
    peer 10.1.1.1 as-number 65410
   #
   ipv4-family vpn-instance vpnb
    network 10.2.1.0 255.255.255.0
    peer 10.2.1.1 as-number 65420
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  ip vpn-instance vpnb
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.5.1.1 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.5.2.1 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance vpna
    import-route ospf 100
   #
   ipv4-family vpn-instance vpnb
    import-route ospf 200
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  ospf 100 vpn-instance vpna
   import-route bgp
   area 0.0.0.0
    network 10.5.1.0 0.0.0.255
  #
  ospf 200 vpn-instance vpnb
   import-route bgp
   area 0.0.0.0
    network 10.5.2.0 0.0.0.255
  #
  return
  ```
* MCE configuration file
  
  ```
  #
  sysname MCE
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
  #
  ip vpn-instance vpnb
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.5.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.5.2.2 255.255.255.0
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.3.1.2 255.255.255.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.4.1.2 255.255.255.0
  #
  ospf 100 vpn-instance vpna
   import-route rip 100
   vpn-instance-capability simple
   area 0.0.0.0
    network 10.3.1.0 0.0.0.255
    network 10.5.1.0 0.0.0.255
  #
  ospf 200 vpn-instance vpnb
   import-route rip 200
   vpn-instance-capability simple
   area 0.0.0.0
    network 10.4.1.0 0.0.0.255
    network 10.5.2.0 0.0.0.255
  #
  rip 100 vpn-instance vpna
   version 2
   network 10.0.0.0
   import-route ospf 100
  #
  rip 200 vpn-instance vpnb
   version 2
   network 10.0.0.0
   import-route ospf 200
  #
  return
  ```
* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 33.33.33.33 255.255.255.255
  #
  rip 100
   version 2
   network 10.0.0.0
   network 33.0.0.0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
  #
  interface LoopBack1
   ip address 44.44.44.44 255.255.255.255
  #
  rip 200
   version 2
   network 10.0.0.0
   network 44.0.0.0
  #
  return
  ```