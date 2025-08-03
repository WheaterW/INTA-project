Example for Configuring Static BFD for RIP
==========================================

This section provides an example for configuring static BFD for RIP.

#### Networking Requirements

RIP periodically exchanges Update packets to monitor the status of neighbors. By default, if a local device does not receive any Update packets from its neighbor after six update intervals (180s) elapse, it considers the neighbor down.

Voice, video, and other VOD services are widely used and are sensitive to the packet loss and delay. Long-time fault detection will cause the loss of a large number of data packets. As a result, the requirement of carrier-class networks for high reliability cannot be met. BFD for RIP can be deployed to complete link fault detection within milliseconds, speeding up RIP convergence.

On the network shown in [Figure 1](#EN-US_TASK_0172365889__fig_dc_vrp_rip_cfg_005701):

* DeviceA, DeviceB, DeviceC, and DeviceD run RIP.
* Traffic is transmitted along the primary link DeviceA -> DeviceB -> DeviceD. Static BFD is enabled on the interfaces connecting DeviceA and DeviceB. If the primary link fails, BFD can rapidly detect the fault and notify RIP of the fault, allowing service traffic to be rapidly switched to the backup link.

**Figure 1** Configuring static BFD for RIP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_rip_cfg_005601.png)

#### Precautions

To improve security, you are advised to configure RIP-2 packet authentication. For details, see "Improving RIP Network Security." The following example describes how to configure an authentication mode for RIP-2 packets. For details, see "Example for Configuring Basic RIP Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic RIP functions on each Router to establish RIP neighbor relationships.
2. Enable BFD globally.
3. Enable static BFD on the interfaces connecting DeviceA and DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* DeviceA: RIP process ID (1), RIP version number (2), IP address of GE 0/1/0 (2.2.2.1/24), and IP address of GE 0/2/0 (3.3.3.1/24)
* DeviceB: RIP process ID (1), RIP version number (2), and IP addresses of GE 0/1/0, GE 0/2/0, and GE0/3/0 (2.2.2.2/24, 4.4.4.1/24, and 172.16.1.1/24, respectively)
* DeviceC: RIP process ID (1), RIP version number (2), IP address of GE 0/1/0 (4.4.4.2/24), and IP address of GE 0/2/0 (3.3.3.2/24)
* DeviceD: RIP process ID (1), RIP version number (2), and IP address of GE 0/1/0 (172.16.1.2/24)
* Local and remote discriminators of the BFD session established between DeviceA and DeviceB

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0172365889__fig_dc_vrp_rip_cfg_005701) and [Data Preparation](#EN-US_TASK_0172365889__section_dc_vrp_rip_cfg_005703). For configuration details, see configuration files in this section.
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
    IP Address      Interface                   Type   Last-Heard-Time
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
   
   The routing table shows that the next-hop address of the route destined for 172.16.0.0/16 is 2.2.2.2 and that the outbound interface is GigabitEthernet 0/1/0. This indicates that traffic is transmitted on the primary link DeviceA -> DeviceB.
3. Configure static BFD.
   
   
   
   # Configure static BFD on DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] bfd 1 bind peer-ip 2.2.2.2 interface gigabitethernet0/1/0 source-ip 2.2.2.1
   ```
   ```
   [*DeviceA-bfd-session-1] discriminator local 1
   ```
   ```
   [*DeviceA-bfd-session-1] discriminator remote 2
   ```
   ```
   [*DeviceA-bfd-session-1] commit
   ```
   ```
   [~DeviceA-bfd-session-1] quit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] rip bfd static
   ```
   
   # Configure static BFD on DeviceB.
   
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd 1 bind peer-ip 2.2.2.1 interface gigabitethernet0/1/0 source-ip 2.2.2.2
   ```
   ```
   [*DeviceB-bfd-session-1] discriminator local 2
   ```
   ```
   [*DeviceB-bfd-session-1] discriminator remote 1
   ```
   ```
   [*DeviceB-bfd-session-1] commit
   ```
   ```
   [~DeviceB-bfd-session-1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] rip bfd static
   ```
   
   # After completing the configurations, run the [**display bfd session**](cmdqueryname=display+bfd+session) **all** command on DeviceA. The command output shows that a static BFD session has been established.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR 
   (*): State is invalid
   ------------------------------------------------------------------------------
   Local  Remote  PeerIpAddr      State     Type        InterfaceName                
   ------------------------------------------------------------------------------
   1      2       2.2.2.2         Up        S_IP_IF     GigabitEthernet0/1/0
   ------------------------------------------------------------------------------
       Total UP/DOWN Session Number : 1/0
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
   rip bfd static
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
  #
  ```
  ```
  bfd 1 bind peer-ip 2.2.2.2 interface gigabitethernet0/1/0 source-ip 2.2.2.1
  ```
  ```
   discriminator local 1  
  ```
  ```
   discriminator remote 2
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
   rip bfd static
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
   network 4.0.0.0
  ```
  ```
   network 172.16.0.0
  ```
  ```
  #
  ```
  ```
  bfd 1 bind peer-ip 2.2.2.1 interface gigabitethernet0/1/0 source-ip 2.2.2.2
  ```
  ```
   discriminator local 2  
  ```
  ```
   discriminator remote 1
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