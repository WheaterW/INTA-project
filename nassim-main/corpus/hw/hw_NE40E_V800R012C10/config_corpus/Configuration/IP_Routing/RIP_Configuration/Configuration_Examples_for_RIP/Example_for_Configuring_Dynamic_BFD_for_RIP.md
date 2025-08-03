Example for Configuring Dynamic BFD for RIP
===========================================

This section describes how to configure dynamic BFD on a RIP network to rapidly detect link faults and notify RIP of the faults to trigger service traffic switchover.

#### Networking Requirements

RIP periodically exchanges Update packets to monitor the status of neighbors. By default, if a local device does not receive any Update packets from its neighbor after six update intervals (180s) elapse, it considers the neighbor down.

Voice, video, and other VOD services are widely used and are sensitive to the packet loss and delay. Long-time fault detection will cause the loss of a large number of data packets. As a result, the requirement of carrier-class networks for high reliability cannot be met. BFD for RIP can be deployed to complete link fault detection within milliseconds, speeding up RIP convergence.

On the network shown in [Figure 1](#EN-US_TASK_0172365887__fig_dc_vrp_rip_cfg_005601), primary and backup links are deployed. The primary link is Device A -> Device B, and the backup link is Device A -> Device C -> Device B. In normal cases, service traffic is transmitted along the primary link. If the primary link fails, it is expected that the fault is rapidly detected and that service traffic is switched to the backup link in time. In this case, you can configure BFD for RIP to monitor the RIP neighbor relationship between DeviceA and DeviceB. If the link between DeviceA and DeviceB fails, BFD can rapidly detect the fault and notify RIP of the fault. Then service traffic is switched to the backup link for transmission.

**Figure 1** Network diagram of configuring dynamic BFD for RIP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0256711487.png)

#### Precautions

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic RIP functions on each Router and ensure that RIP neighbor relationships are established.
2. Enable global BFD.
3. Enable BFD on the interfaces of the link between DeviceA and DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA: RIP process ID (1), RIP version number (2), IP address of GE 0/1/0 (2.2.2.1/24), and IP address of GE 0/2/0 (3.3.3.1/24)
* DeviceB: RIP process ID (1), RIP version number (2), IP address of GE 0/1/0 (2.2.2.2/24), IP address of GE 0/2/0 (4.4.4.1/24), and IP address of GE 0/3/0 (172.16.1.1/24)
* DeviceC: RIP process ID (1), RIP version number (2), IP address of GE 0/1/0 (4.4.4.2/24), and IP address of GE 0/2/0 (3.3.3.2/24)
* DeviceD: RIP process ID (1), RIP version number (2), and IP address of GE 0/1/0 (172.16.1.2/24)
* Minimum interval at which BFD packets are sent (100 ms), minimum interval at which BFD packets are received (100 ms), and local detection multiplier (10) on DeviceA and DeviceB

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0172365887__fig_dc_vrp_rip_cfg_005601) and [Data Preparation](#EN-US_TASK_0172365887__section_dc_vrp_rip_cfg_005603). For configuration details, see configuration files in this section.
2. Configure basic RIP functions.
   
   
   
   # Configure DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] rip 1
   ```
   ```
   [*DeviceA-rip-1] version 2
   ```
   ```
   [*DeviceA-rip-1] network 2.0.0.0
   ```
   ```
   [*DeviceA-rip-1] network 3.0.0.0
   ```
   ```
   [*DeviceA-rip-1] commit
   ```
   ```
   [~DeviceA-rip-1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] rip 1
   ```
   ```
   [*DeviceB-rip-1] version 2
   ```
   ```
   [*DeviceB-rip-1] network 2.0.0.0
   ```
   ```
   [*DeviceB-rip-1] network 4.0.0.0
   ```
   ```
   [*DeviceB-rip-1] network 172.16.0.0
   ```
   ```
   [*DeviceB-rip-1] commit
   ```
   ```
   [~DeviceB-rip-1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] rip 1
   ```
   ```
   [*DeviceC-rip-1] version 2
   ```
   ```
   [*DeviceC-rip-1] network 3.0.0.0
   ```
   ```
   [*DeviceC-rip-1] network 4.0.0.0
   ```
   ```
   [*DeviceC-rip-1] commit
   ```
   ```
   [~DeviceC-rip-1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] rip 1
   ```
   ```
   [*DeviceD-rip-1] version 2
   ```
   ```
   [*DeviceD-rip-1] network 172.16.0.0
   ```
   ```
   [*DeviceD-rip-1] commit
   ```
   ```
   [~DeviceD-rip-1] quit
   ```
   
   # After completing the preceding configurations, run the [**display rip neighbor**](cmdqueryname=display+rip+neighbor) command. The command output shows that DeviceA has established neighbor relationships with DeviceB and DeviceC. Use the command output on DeviceA as an example.
   
   ```
   [~DeviceA] display rip 1 neighbor
   ```
   ```
   ---------------------------------------------------------------------
   ```
   ```
   IP Address         Interface Type          Type       Last-Heard-Time 
   ```
   ```
   ---------------------------------------------------------------------
    3.3.3.2         GigabitEthernet0/2/0        RIP    0:0:5
    Number of RIP routes  :2
    2.2.2.2         GigabitEthernet0/1/0        RIP    0:0:5
    Number of RIP routes  :4
   ```
   
   # Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command. The command output shows that Routers can import routes from each other. Take the command output on DeviceA as an example.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 15       Routes : 15        
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           3.0.0.0/8   RIP    100  3             D  3.3.3.2         GigabitEthernet0/2/0
           3.3.3.0/24  Direct 0    0             D  3.3.3.1         GigabitEthernet0/2/0
           3.3.3.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
         3.3.3.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
           2.0.0.0/8   RIP    100  3             D  2.2.2.2         GigabitEthernet0/1/0
           2.2.2.0/24  Direct 0    0             D  2.2.2.1         GigabitEthernet0/1/0
           2.2.2.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         2.2.2.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
        172.16.0.0/16  RIP    100  4             D  2.2.2.2         GigabitEthernet0/1/0
        172.16.1.0/24  RIP    100  1             D  2.2.2.2         GigabitEthernet0/1/0
           4.4.4.0/24  RIP    100  1             D  3.3.3.2         GigabitEthernet0/2/0
                       RIP    100  1             D  2.2.2.2         GigabitEthernet0/1/0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   The routing table shows that the next-hop address of the route destined for 172.16.1.0/24 is 2.2.2.2 and that the outbound interface is GigabitEthernet 0/1/0. This indicates that traffic is transmitted on the primary link DeviceA -> DeviceB.
3. Configure BFD for RIP.
   
   
   
   # Configure BFD on all interfaces of DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] rip 1
   ```
   ```
   [*DeviceA-rip-1] bfd all-interfaces enable
   ```
   ```
   [*DeviceA-rip-1] bfd all-interfaces min-rx-interval 100 min-tx-interval 100 detect-multiplier 10
   ```
   ```
   [*DeviceA-rip-1] commit
   ```
   ```
   [~DeviceA-rip-1] quit
   ```
   
   The configuration on DeviceB is similar to the preceding configuration. For details, see configuration files.
   
   # After completing the configurations, run the [**display rip bfd session**](cmdqueryname=display+rip+bfd+session) command. The command output shows that a BFD session has been established between DeviceA and DeviceB and that the BFD State is Up. Use the command output on DeviceA as an example.
   
   ```
   [~DeviceA] display rip 1 bfd session all
   ```
   ```
    Interface  :GigabitEthernet0/1/0
    LocalIp      :2.2.2.1         RemoteIp   :2.2.2.2        BFDState :Up
   
    Interface :GigabitEthernet0/2/0
    LocalIp      :3.3.3.1         RemoteIp  :3.3.3.2         BFDState :Down
   ```
4. Verifying the Configuration
   
   
   
   # Run the [**shutdown**](cmdqueryname=shutdown) command on GigabitEthernet 0/1/0 of DeviceB to simulate a fault on the primary link.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Link fault simulation is required for verification and does not need to be performed in actual applications.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   
   # Check information about the BFD session on DeviceA. The command output shows that no BFD session exists between DeviceA and DeviceB.
   
   ```
   [~DeviceA] display rip 1 bfd session all
   ```
   ```
    Interface :GigabitEthernet0/2/0
    LocalIp      :3.3.3.1         RemoteIp  :3.3.3.2         BFDState :Down
   ```
   
   # Check the routing table of DeviceA.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 8        Routes : 8         
   
   Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface
   
           3.3.3.0/24  Direct 0    0             D  3.3.3.1         GigabitEthernet0/2/0
           3.3.3.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
         3.3.3.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/2/0
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  RIP    100  2             D  3.3.3.2         GigabitEthernet0/2/0
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   The routing table shows that the backup link DeviceA -> DeviceC -> DeviceB is used after the primary link fails. The next hop address of the route to 172.16.1.0/24 is 3.3.3.2, and the outbound interface is GigabitEthernet 0/2/0.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 2.2.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 3.3.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 1 
  ```
  ```
   version 2 
  ```
  ```
   network 2.0.0.0
  ```
  ```
   network 3.0.0.0
  ```
  ```
   bfd all-interfaces enable 
  ```
  ```
   bfd all-interfaces min-tx-interval 100 min-rx-interval 100 detect-multiplier 10 
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
  bfd
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 2.2.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 4.4.4.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
  rip 1 
  ```
  ```
   version 2 
  ```
  ```
   network 2.0.0.0
  ```
  ```
   network 4.0.0.0
  ```
  ```
   network 172.16.0.0
  ```
  ```
   bfd all-interfaces enable 
  ```
  ```
   bfd all-interfaces min-tx-interval 100 min-rx-interval 100 detect-multiplier 10 
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 4.4.4.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 3.3.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 1 
  ```
  ```
   version 2 
  ```
  ```
   network 3.0.0.0
  ```
  ```
   network 4.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceD
  ```
  ```
  #
  ```
  ```
  interface gigabitethernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  rip 1 
  ```
  ```
   version 2 
  ```
  ```
   network 172.16.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```