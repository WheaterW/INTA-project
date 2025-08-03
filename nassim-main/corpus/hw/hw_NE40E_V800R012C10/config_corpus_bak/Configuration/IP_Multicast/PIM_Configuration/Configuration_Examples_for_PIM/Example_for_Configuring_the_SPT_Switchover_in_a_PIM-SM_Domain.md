Example for Configuring the SPT Switchover in a PIM-SM Domain
=============================================================

If a receiver wants to perform the SPT switchover only when the rate of multicast data packets reaches the threshold, you need to configure triggering conditions for the SPT switchover. By default, the Rendezvous Point (RP) and the DR at the group member side immediately perform the shortest path tree (SPT) switchover after they receive the first multicast data packet.

#### Networking Requirements

Receivers can receive the Video On Demand (VOD) information in multicast mode. The SM-single BootStrap router (BSR) administrative domain is adopted in the entire PIM network. By default, the DR at the receiver side and the RP perform the SPT switchover immediately after receiving the first multicast data packet, and choose the optimal path to receive information from the source. If a receiver wants to perform the SPT switchover after the traffic reaches the threshold, you need to configure the SPT switchover.

As shown in [Figure 1](#EN-US_TASK_0172366924__fig_dc_vrp_multicast_cfg_004001), it is required to perform proper configuration on Routers. Host A on the leaf network can receive multicast data from the RP (GE 0/1/0 of Device A). When the rate for forwarding multicast data reaches 1024 kbit/s, the SPT switchover is performed (After SPT switchover, the path used by Host A to receive multicast data is Source-Device B-Device C-Host A).

**Figure 1** Networking diagram for performing SPT switchover in a PIM-SM domain  
![](images/fig_dc_vrp_multicast_cfg_004001.png)  

| Device | Interface | IP address |
| --- | --- | --- |
| Device A | GE0/1/0 | 192.168.1.1/24 |
| GE0/2/0 | 192.168.3.1/24 |
| DeviceB | GE0/1/0 | 192.168.2.1/24 |
| GE0/2/0 | 192.168.3.2/24 |
| GE0/3/0 | 10.110.5.1/24 |
| DeviceC | GE0/1/0 | 192.168.1.2/24 |
| GE0/3/0 | 192.168.2.2/24 |
| GE0/2/0 | 10.110.2.1/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a unicast routing protocol for each Router interface.
2. Enable multicast on each Router, PIM-SM on each interface, and IGMP on the interface at the host side.
3. Configure the same static RP address on all the Routers.
4. Perform the SPT switchover on Device C.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast source address is 10.110.5.100/24.
* Group address is 225.1.1.1/24.
* The number of IGMP version running between Device C and the leaf network is 2.

#### Procedure

1. Configure an IP address and a unicast routing protocol for each Router interface.
   
   
   
   # Based on [Figure 1](#EN-US_TASK_0172366924__fig_dc_vrp_multicast_cfg_004001), configure an IP address and mask of each interface, interconnect Routers through OSPF, ensure that Device A, Device B, and Device C can interconnect at the network layer, and configure the three Routers to dynamically update routes through a unicast routing protocol. The configuration details are not mentioned here.
2. Enable multicast on each Router, PIM-SM on each interface, and IGMP on the interface at the host side.
   
   
   
   # Enable multicast on each Router, PIM-SM on each interface, and IGMP on the interfaces that connect Device C to the leaf network. The configurations of Device A and Device B are the same as the configuration of Device C, and are not mentioned here.
   
   ```
   [~DeviceC] multicast routing-enable
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] igmp version 2
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
3. Configure a static RP.
   
   
   
   # Configure the static RP on Device A, Device B, and Device C. The configurations on Device B and Device C are similar to those on Device A. The detailed configurations are not mentioned here.
   
   ```
   [~DeviceA] pim
   ```
   ```
   [*DeviceA-pim] static-rp 192.168.1.1
   ```
   ```
   [*DeviceA-pim] quit
   ```
   ```
   [*DeviceA] commit
   ```
4. Configure the threshold of the SPT switchover.
   
   
   
   # Perform the SPT switchover on Device C when the rate of multicast data packets reaches 1024 kbit/s.
   
   ```
   [~DeviceC] pim
   ```
   ```
   [*DeviceC-pim] spt-switch-threshold 1024 
   ```
   ```
   [*DeviceC-pim] quit
   ```
   ```
   [*DeviceC] commit
   ```
5. Verify the configuration.
   
   
   
   # The multicast source starts to send data to the group, and Host A can receive the data from the source. When the rate is less than 1024 kbit/s, run the **display pim routing-table** command on Device C to view the PIM multicast routing table on the Device. You can find that the upstream neighbor is Device A. The display is as follows:
   
   ```
   <DeviceC> display pim routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
   (*, 225.1.1.1)
   ```
   ```
        RP: 192.168.1.1
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:13:46
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:13:46 
   ```
   ```
            Upstream neighbor: 192.168.1.1
   ```
   ```
            RPF neighbor: 192.168.1.1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0,
   ```
   ```
                Protocol: igmp, UpTime: 00:13:46, Expires:-
   ```
   ```
   (10.110.5.100, 225.1.1.1)
   ```
   ```
        RP: 192.168.1.1
   ```
   ```
        Protocol: pim-sm, Flag: ACT
   ```
   ```
        UpTime: 00:00:42
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:00:42
   ```
   ```
            Upstream neighbor: 192.168.1.1
   ```
   ```
            RPF neighbor: 192.168.1.1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:00:42, Expires:-
   ```
   
   # When the rate is greater than 1024 kbit/s, run the **display pim routing-table** command to view the PIM multicast routing table on the Device. You can find that the upstream neighbor is Device B. The display is as follows:
   
   ```
   <DeviceC> display pim routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
   (*, 225.1.1.1)
   ```
   ```
        RP: 192.168.1.1
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:13:46
   ```
   ```
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 00:13:46
   ```
   ```
            Upstream neighbor: 192.168.2.1
   ```
   ```
            RPF neighbor: 192.168.2.1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0,
   ```
   ```
                Protocol: igmp, UpTime: 00:13:46, Expires:-
   ```
   ```
   (10.110.5.100, 225.1.1.1)
   ```
   ```
        RP: 192.168.1.1
   ```
   ```
        Protocol: pim-sm, Flag:RPT SPT ACT
   ```
   ```
        UpTime: 00:00:42
   ```
   ```
        Upstream interface: GigabitEthernet0/3/0, Refresh time: 00:00:42
   ```
   ```
            Upstream neighbor: 192.168.2.1
   ```
   ```
            RPF neighbor: 192.168.2.1
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/2/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:00:42, Expires:-
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
  multicast routing-enable
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
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   static-rp 192.168.1.1 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return  
  ```
* Device B configuration file
  
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
  multicast routing-enable
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
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.5.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   static-rp 192.168.1.1 
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.110.5.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 192.168.3.0 0.0.0.255 
  ```
  ```
  #
  ```
  ```
  return 
  ```
* Device C configuration file
  
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
  multicast routing-enable
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
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.2.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
   igmp version 2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   spt-switch-threshold 1024
  ```
  ```
   static-rp 192.168.1.1
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.110.2.0 0.0.0.255
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255 
  ```
  ```
  #
  ```
  ```
  return
  ```