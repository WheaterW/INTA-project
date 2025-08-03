Example for Configuring OSPF Fast Convergence
=============================================

This section describes how to configure OSPF fast convergence by adjusting the timer parameter and configuring BFD.

#### Networking Requirements

On the broadcast network shown in [Figure 1](#EN-US_TASK_0172365664__fig_dc_vrp_ospf_cfg_010101), OSPF runs on the four devices, which belong to the same OSPF area.

**Figure 1** Networking for configuring OSPF fast convergence![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE0/1/0.


  
![](images/fig_dc_vrp_ospf_cfg_009701.png)  


#### Precautions

When configuring OSPF fast convergence, note the following rules:

* You can decrease the interval at which Hello packets are sent and values of the Dead, Poll, and Wait timers for fast OSPF network convergence. Frequent packet transmission, however, may overload the device. In addition, the OSPF network convergence slows down if the values of these timers are too large. Therefore, set values based on the network stability.
* The intervals at which Hello packets are sent and values of the Dead, Poll, and Wait timers at both ends must be the same. Otherwise, the OSPF neighbor relationship cannot be established.
* To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security". OSPF area authentication is used as an example. For details, see Example for Configuring Basic OSPF Functions.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPF functions on each Router for interconnection.
2. Configure the BFD function on each Router.
3. Adjust the holddown time of the OSPF neighbors on each Router.
4. Configure the Smart-discover function on each Router.
5. Adjust the intervals for configuration update, LSA reception, and SPF calculation through an intelligent timer on each Router.

#### Data Preparation

To complete the configuration, you need the following data:

* Holddown time of the OSPF neighbors
* Intervals for LSA update, LSA reception, and SPF calculation

#### Procedure

1. Assign an IP address to each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365664__section_dc_vrp_ospf_cfg_010106) in this section.
2. Configure basic OSPF functions. For details, see [Example for Configuring Basic OSPF Functions](dc_vrp_ospf_cfg_0094.html).
3. Adjust the holddown time of the OSPF neighbors on each Router.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospf timer dead 30
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The holddown time of neighbors of the OSPF-capable interfaces must be longer than the interval at which Hello packets are sent, and the values of **dead** *interval* on the routers in the same network segment must be the same.
   * In this configuration example, the following configurations on each Router are the same as that on DeviceA. For configuration details, see Configuration Files in this section.
     
     + Adjust the holddown time of the OSPF neighbors on each Router.
     + Configure the Smart-discover function on each Router.
     + Adjust the intervals for configuration update, LSA reception, and SPF calculation through an intelligent timer on the Router.
4. Configure the Smart-discover function on each Router.
   
   
   
   # Configure DeviceA.
   
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospf smart-discover
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
5. Configure the BFD function on each Router.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] ospf
   ```
   ```
   [*DeviceA-ospf-1] bfd all-interfaces enable
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
   ```
   [~DeviceA-ospf-1] quit
   ```
6. Adjust the intervals for configuration update, LSA reception, and SPF calculation through an intelligent timer on each Router.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   ```
   ```
   [~DeviceA-ospf-1] lsa-arrival-interval intelligent-timer 3000 200 500
   ```
   ```
   [*DeviceA-ospf-1] lsa-originate-interval intelligent-timer 3000 200 500
   ```
   ```
   [*DeviceA-ospf-1] spf-schedule-interval intelligent-timer 3000 200 500
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the [**display ospf brief**](cmdqueryname=display+ospf+brief) command on each Router to view the brief information about OSPF. Use Router A as an example. You can view the values of timers.
   
   ```
   [~DeviceA] display ospf brief
   ```
   ```
             OSPF Process 1 with Router ID 9.9.9.9
                     OSPF Protocol Information
   RouterID: 9.9.9.9          Border Router: AREA 
   Multi-VPN-Instance is not enabled 
   Global DS-TE Mode: Non-Standard IETF Mode 
   Graceful-restart capability: disabled 
   Helper support capability  : not configured 
   OSPF Stub Router State Reason: Startup Synchronize
       Router LSA stub links with cost 65535
       Summary LSA with cost 16777214 
       External LSA with cost 16777214 
   Applications Supported: MPLS Traffic-Engineering 
   Spf-schedule-interval: max 10000ms, start 500ms, hold 1000ms 
   Default ASE parameters: Metric: 1 Tag: 1 Type: 2 
   Route Preference: 10 
   ASE Route Preference: 150 
   Intra Route Preference: 50 
   Inter Route Preference: 50 
   SPF Computation Count: 56 
   RFC 1583 Compatible 
   Retransmission limitation is disabled 
   bfd enabled 
   BFD Timers: Tx-Interval 10 , Rx-Interval 10 , Multiplier 3 
   Area Count: 2   Nssa Area Count: 0 
   ExChange/Loading Neighbors: 0
   
    Area: 0.0.0.0             MPLS TE not enabled
    Authtype: None   Area flag: Normal
    SPF scheduled count: 2
    Exchange/Loading neighbors: 0
    Router ID conflict state: Normal
   
    Interface: 1.1.1.1 (GE0/3/1)
    Cost: 1       State: DR      Type: Broadcast      MTU: 1500
    Priority: 1
    Designated Router: 1.1.1.1
    Backup Designated Router: 0.0.0.0
    Timers: Hello 10, Dead 40, Wait 40, Poll 120, Retransmit 5, Transmit Delay 1
   ```

#### Configuration Files

* Device A configuration file
  
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
  router id 1.1.1.1
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.1 255.255.255.0
  ```
  ```
   ospf timer dead 30
  ```
  ```
   ospf smart-discover 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   bfd all-interfaces enable
  ```
  ```
   spf-schedule-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-arrival-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-originate-interval intelligent-timer 3000 200 500
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
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
  router id 2.2.2.2
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
   ospf timer dead 30
  ```
  ```
   ospf smart-discover 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   bfd all-interfaces enable
  ```
  ```
   spf-schedule-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-arrival-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-originate-interval intelligent-timer 3000 200 500
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
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
  router id 3.3.3.3
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.3 255.255.255.0
  ```
  ```
   ospf timer dead 30
  ```
  ```
   ospf smart-discover 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   bfd all-interfaces enable
  ```
  ```
   spf-schedule-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-arrival-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-originate-interval intelligent-timer 3000 200 500
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
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
  router id 4.4.4.4
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.4 255.255.255.0
  ```
  ```
   ospf timer dead 30
  ```
  ```
   ospf smart-discover 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   bfd all-interfaces enable
  ```
  ```
   spf-schedule-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-arrival-interval intelligent-timer 3000 200 500
  ```
  ```
   lsa-originate-interval intelligent-timer 3000 200 500
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```