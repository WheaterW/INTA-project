Example for Associating EFM with IPv4 Static Routes
===================================================

After EFM is associated with IPv4 static routes, the system responds to EFM Up/Down events on a specified interface and determines whether to activate static routes. In this manner, route advertisement is controlled and remote traffic is forwarded.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365464__fig_dc_vrp_static-route_disjoin_cfg_004901), DeviceA and DeviceB are connected and are enabled with EFM OAM. In addition, a static route destined for 1.1.1.1/32 is configured on DeviceA and associated with EFM.

**Figure 1** Associating EFM with IPv4 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_004901.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable EFM OAM both globally and on the interfaces of DeviceA and DeviceB.
2. Configure a static route destined for 1.1.1.1/32 on DeviceA and associate EFM with this static route.

#### Data Preparation

To complete the configuration, you need the IP addresses of interfaces.


#### Procedure

1. Configure an IP address for each interface. For detailed configurations, see Configuration Files.
2. Enable EFM OAM on DeviceA and DeviceB.
   
   
   
   # Enable EFM OAM on DeviceA.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] efm enable
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] efm enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] quit
   ```
   
   # Enable EFM OAM on DeviceB.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] efm enable
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] efm enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Check EFM OAM session information on DeviceA.
   
   ```
   <DeviceA> display efm session all
   ```
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/0      detect                      -- 
   ```
   
   The command output shows that the EFM OAM protocol status of the interface is **detect**, indicating that the interface is in the handshake state.
3. Associate EFM with a specified static route.
   
   
   
   # Configure a static route destined for 1.1.1.1/32 on DeviceA and associate EFM with this static route.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 172.16.1.2 track efm-state GigabitEthernet0/1/0
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] quit
   ```
4. Verify the configuration.
   
   
   
   # Run the **display current-configuration | include efm** command on DeviceA. The following command output shows that the static route has been associated with EFM:
   
   ```
   <DeviceA> display current-configuration | include efm
   ```
   ```
   efm enable
   ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 172.16.1.2 track efm-state GigabitEthernet0/1/0
   ```
   
   # Check the IP routing table on DeviceA. The command output shows that the static route 1.1.1.1/32 exists in the IP routing table.
   
   ```
   <DeviceA> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 8        Routes : 8
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.1/32  Static  60   0             D  172.16.1.2      GigabitEthernet0/1/1
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D  172.16.1.1      GigabitEthernet0/1/1
        172.16.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
      172.16.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0  
   ```
   
   # Run the **shutdown** command on GE0/1/0 of DeviceA to change the status of the EFM OAM session.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] quit
   ```
   
   # Run the **display efm session all** command on DeviceA. The command output shows that the OAM protocol status is **discovery**, indicating that the interface is in the peer discovery state.
   
   ```
   <DeviceA> display efm session all
   ```
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/0      discovery                   --    
   ```
   
   # Check the routing table of DeviceA. The command output shows that the static route 1.1.1.1/32 no longer exists. The static route is unavailable because it has been associated with EFM and the EFM session has not been established.
   
   ```
   <DeviceA> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 7        Routes : 7
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D  172.16.1.1      GigabitEthernet0/1/1
        172.16.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
      172.16.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/1
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  efm enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   efm enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
   ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 172.16.1.2 track efm-state GigabitEthernet0/1/0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  efm enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   efm enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 172.16.1.2 255.255.255.0
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  return
  ```