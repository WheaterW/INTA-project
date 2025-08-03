Example for Configuring Static BFD for IPv4 Static Routes
=========================================================

To improve network reliability, you can configure static BFD for IPv4 static routes to fast detect link failures and speed up route convergence.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365458__fig_dc_vrp_static-route_disjoin_cfg_002901), DeviceA is connected to DeviceB through Switch C. It is required that DeviceA communicate with other devices through static default routes and that a BFD session be set up between DeviceA and DeviceB to detect link faults.

**Figure 1** Configuring static BFD for IPv4 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_002901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BFD session between DeviceA and DeviceB to detect the link between the two devices.
2. Configure a default static route from DeviceA to the external network and bind the default static route to the BFD session.

#### Data Preparation

To complete the configuration, you need the following data:

* Peer IP address to be detected by BFD
* Local discriminator and remote discriminator of a BFD session
* Default values of the local detection multiplier and of the minimum intervals at which BFD Control packets are sent and received

#### Procedure

1. Configure an IP address for each interface.
   
   
   
   For configuration details, see "Configuration Files" in this section.
2. Configure a BFD session between DeviceA and DeviceB.
   
   
   
   # On DeviceA, configure a BFD session between DeviceA and DeviceB.
   
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
   [*DeviceA] bfd aa bind peer-ip 1.1.1.2
   ```
   ```
   [*DeviceA-bfd-session-aa] discriminator local 10
   ```
   ```
   [*DeviceA-bfd-session-aa] discriminator remote 20
   ```
   ```
   [*DeviceA-bfd-session-aa] commit
   ```
   ```
   [~DeviceA-bfd-session-aa] quit
   ```
   
   # On DeviceB, configure a BFD session between DeviceA and DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] bfd
   ```
   ```
   [*DeviceB-bfd] quit
   ```
   ```
   [*DeviceB] bfd bb bind peer-ip 1.1.1.1
   ```
   ```
   [*DeviceB-bfd-session-bb] discriminator local 20
   ```
   ```
   [*DeviceB-bfd-session-bb] discriminator remote 10
   ```
   ```
   [*DeviceB-bfd-session-bb] commit
   ```
   ```
   [~DeviceB-bfd-session-bb] quit
   ```
3. Configure a default static route and bind it to a BFD session.
   
   
   
   # On DeviceA, configure a default static route to the external network and bind it to BFD session named **aa**.
   
   ```
   [~DeviceA] ip route-static 0.0.0.0 0 1.1.1.2 track bfd-session aa
   ```
4. Verify the configuration.
   
   
   
   # Run the **display bfd session** **all** command on DeviceA and DeviceB. The command output shows that a BFD session has been established and is up. Then, run the **display current-configuration | include bfd** command in the system view. The command output shows that the static route has been bound to the BFD session.
   
   Use the command output on DeviceA as an example.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   --------------------------------------------------------------------------------
   Local  Remote PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   10     20     1.1.1.2         Up       S_IP_PEER   -
   --------------------------------------------------------------------------------
        Total UP/DOWN Session Number : 1/0
   ```
   ```
   [~DeviceA] display current-configuration | include bfd
   ```
   ```
    bfd
    bfd aa bind peer-ip 1.1.1.2
    ip route-static 0.0.0.0 0.0.0.0 1.1.1.2 track bfd-session aa
   ```
   
   # Check the IP routing table of DeviceA. The command output shows that the static route exists in the routing table.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 5        Routes : 5
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
           0.0.0.0/0   Static 60   0          RD  1.1.1.2         GigabitEthernet0/1/0
           1.1.1.0/24  Direct 0    0           D  1.1.1.1         GigabitEthernet0/1/0
           1.1.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
         1.1.1.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```
   
   # Run the **shutdown** command on GE 0/1/0 of DeviceB to simulate a link fault.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] shutdown
   ```
   
   # Check the IP routing table of DeviceA. The command output shows that the static default route 0.0.0.0/0 does not exist. This is because the default static route has become unavailable after the BFD session bound to the route detects the link fault.
   
   ```
   [~DeviceA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: Public
            Destinations : 4        Routes : 4
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
           1.1.1.0/24  Direct 0    0           D  1.1.1.1         GigabitEthernet0/1/0
           1.1.1.1/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
         1.1.1.255/32  Direct 0    0           D  127.0.0.1       GigabitEthernet0/1/0
   255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
   ```

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
   ip address 1.1.1.1 255.255.255.0
  #
   ip route-static 0.0.0.0 0.0.0.0 1.1.1.2 track bfd-session aa
  #
  bfd aa bind peer-ip 1.1.1.2
   discriminator local 10
   discriminator remote 20
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  bfd
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 1.1.1.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 2.2.2.2 255.255.255.0
  #
  bfd bb bind peer-ip 1.1.1.1
   discriminator local 20
   discriminator remote 10
  #
  return
  ```