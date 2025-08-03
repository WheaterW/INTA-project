Example for Configuring BGP Auto FRR
====================================

BGP Auto FRR provides backup forwarding entries for routes, minimizing the delay for important services.

#### Networking Requirements

As networks evolve continuously, voice, on-line video, and financial services raise increasingly high requirements for real-time performance. Usually, primary and backup links are deployed on a network to ensure the stability of these services. If the primary link fails, the device needs to wait for route convergence to be completed. After that, the device reselects an optimal route and delivers this route to the FIB to start a link switchover. This is the traditional switchover mode. In this mode, service interruption lasts a long time, which does not meet the services' requirement.

BGP Auto FRR addresses this problem. After BGP Auto FRR is enabled on a device, the device selects the optimal route to forward packets. In addition, the device automatically adds information about the sub-optimal route to the backup forwarding entries of the optimal route and delivers the backup forwarding entries to the FIB. If the primary link fails, the device quickly switches traffic to the backup link. The switchover does not depend on route convergence and reduces service interruption time. The switchover can be performed within sub-seconds.

As shown in [Figure 1](#EN-US_TASK_0172366400__fig_dc_vrp_bgp_cfg_408401), Device A belongs to AS 100; Device B, Device C, and Device D belong to AS 200. BGP Auto FRR needs to be configured to ensure that the route from Device A to DeviceD has the backup route.

**Figure 1** Configuring BGP Auto FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and Loopback1, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_408401.png)  


#### Precautions

When configuring BGP Auto FRR, note the following rules:

* When configuring BGP FRR, ensure that there are at least two routes to the same destination network segment.
* The name of a route-policy is case sensitive.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure EBGP connections between Device A and Device B, and between Device A and Device C. Configure IBGP connections between Device D and Device B, and between Device D and Device C.
2. Configure route-policies on Device B and Device C to change the MED values of routes to Device D for route selection.
3. Configure BGP Auto FRR on Device A.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of Device A, Device B, Device C, and Device D
* Names of route-policies and MED values of routes on Device B and Device C

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366400__example882375506214038) in this section.
2. Configure EBGP connections between Device A and Device B, and between Device A and Device C, and configure IBGP connections between Device B and Device D, and between Device C and Device D.
   
   
   
   # Configure EBGP connections on Device A.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] peer 10.2.1.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations on Device B and Device C are similar to the configuration on Device A.
   
   # Configure IBGP connections on Device D.
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 10.3.1.1 as-number 200
   ```
   ```
   [*DeviceD-bgp] peer 10.4.1.1 as-number 200
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations on Device B and Device C are similar to the configuration on Device D.
3. Configure BFD for BGP on Device A, Device B, Device C and Device D.
   
   
   
   # Configure BFD for BGP on Device A.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 bfd enable
   ```
   ```
   [*DeviceA-bgp] peer 10.1.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   ```
   ```
   [*DeviceA-bgp] peer 10.2.1.2 bfd enable
   ```
   ```
   [*DeviceA-bgp] peer 10.2.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   ```
   [~DeviceA] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations on Device B, Device C and Device D are similar to the configuration on Device A.
4. Configure route-policies on Device B and Device C to ensure that the MED values of routes to Device D are different.
   
   
   
   # Configure a route-policy on Device B.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] route-policy rtb permit node 10
   ```
   ```
   [*DeviceB-route-policy] apply cost 80
   ```
   ```
   [*DeviceB-route-policy] quit
   ```
   ```
   [*DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] peer 10.1.1.1 route-policy rtb export
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   
   # Configure a route-policy on Device C.
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] route-policy rtc permit node 10
   ```
   ```
   [*DeviceC-route-policy] apply cost 120
   ```
   ```
   [*DeviceC-route-policy] quit
   ```
   ```
   [*DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv4] peer 10.2.1.1 route-policy rtc export
   ```
   ```
   [*DeviceC-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv4] quit
   ```
   
   # Advertise a route to 4.4.4.4/32 on Device D.
   
   ```
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceD-bgp] network 4.4.4.4 32
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   
   # Run the **display ip routing-table verbose** command on Device A to check detailed information about the route to 4.4.4.4/32 it learns.
   
   ```
   <DeviceA> display ip routing-table 4.4.4.4 32 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 4.4.4.4/32
        Protocol: EBGP            Process ID: 0
      Preference: 255                   Cost: 80
         NextHop: 10.1.1.2         Neighbour: 10.1.1.2
           State: Active Adv             Age: 00h00m12s
             Tag: 0                 Priority: low
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x4
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/1/0
        TunnelID: 0x0                  Flags:  D
   ```
   
   Because the MED value of the route learned from Device B is smaller, Device A selects the path Device AâDevice BâDevice D to transmit traffic to 4.4.4.4/32. Because FRR has not been configured yet, no information about the backup route is available.
5. Enable BGP Auto FRR on Device A, and check the routing information.
   
   
   
   # Enable BGP Auto FRR on Device A.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] auto-frr
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   
   # Run the **display ip routing-table verbose** command on Device A to check the routing information.
   
   ```
   <DeviceA> display ip routing-table 4.4.4.4 32 verbose
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 4.4.4.4/32
        Protocol: EBGP            Process ID: 0
      Preference: 255                   Cost: 80
         NextHop: 10.1.1.2         Neighbour: 10.1.1.2
           State: Active Adv             Age: 00h52m45s
             Tag: 0                 Priority: low
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x4
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/1/0
        TunnelID: 0x0                  Flags:  D
       BkNextHop: 10.2.1.2       BkInterface: GigabitEthernet0/2/0
         BkLabel: NULL           SecTunnelID: 0x0
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
    BkIndirectID: 0x2  
   ```
   
   The command output shows that DeviceA has a backup next hop and a backup outbound interface to 4.4.4.4/32.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  bgp 100
   router-id 1.1.1.1
   peer 10.1.1.2 as-number 200
   peer 10.1.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.1.1.2 bfd enable
   peer 10.2.1.2 as-number 200
   peer 10.2.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.2.1.2 bfd enable
  #
   ipv4-family unicast
    undo synchronization
    auto-frr
    peer 10.1.1.2 enable
    peer 10.2.1.2 enable
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  bgp 200
   router-id 2.2.2.2
   peer 10.1.1.1 as-number 100
   peer 10.1.1.1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.1.1.1 bfd enable
   peer 10.3.1.2 as-number 200
   peer 10.3.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.3.1.2 bfd enable
  #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.1 route-policy rtb export
    peer 10.1.1.1 enable
    peer 10.3.1.2 enable
  #
  route-policy rtb permit node 10
   apply cost 80
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
  #
  bgp 200
   router-id 3.3.3.3
   peer 10.2.1.1 as-number 100
   peer 10.2.1.1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.2.1.1 bfd enable
   peer 10.4.1.2 as-number 200
   peer 10.4.1.2 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.4.1.2 bfd enable
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.1 route-policy rtc export
    peer 10.2.1.1 enable
    peer 10.4.1.2 enable
  #
  route-policy rtc permit node 10
   apply cost 120
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  bfd
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
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   router-id 4.4.4.4
   peer 10.3.1.1 as-number 200
   peer 10.3.1.1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.3.1.1 bfd enable
   peer 10.4.1.1 as-number 200
   peer 10.4.1.1 bfd min-tx-interval 100 min-rx-interval 100 detect-multiplier 4
   peer 10.4.1.1 bfd enable
   #
   ipv4-family unicast
    undo synchronization
    network 4.4.4.4 255.255.255.255
    peer 10.3.1.1 enable
    peer 10.4.1.1 enable
  #
  return
  ```