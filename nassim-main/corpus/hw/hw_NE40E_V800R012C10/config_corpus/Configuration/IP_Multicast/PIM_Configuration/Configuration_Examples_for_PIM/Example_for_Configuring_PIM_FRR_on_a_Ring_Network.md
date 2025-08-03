Example for Configuring PIM FRR on a Ring Network
=================================================

This section provides an example for configuring PIM FRR on a ring network. PIM FRR relies on IGP FRR to compute primary and backup routes. IGP FRR can generally compute out both primary and backup routes on a node. However, a live network easily encounters backup route computation failures on some nodes due to the increase of nodes on the network. To resolve this issue, IP FRR needs to be deployed to work together with IGP FRR for route computation.

#### Networking Requirements

On the ring network shown in [Figure 1](#EN-US_TASK_0172366951__fig_dc_vrp_multicast_cfg_228001), Device C connects to a multicast receiver, and the primarily multicast traffic link for this receiver is Device C -> Device B -> Device A. To compute a backup route for the link Device C -> Device B, IGP FRR requires that the cost of the link Device D -> Device A be less than the cost of the link Device C -> Device A plus the cost of the link Device D -> Device C. However, this ring network does not meet this requirement; therefore, IGP FRR cannot compute a backup route for the link Device C -> Device B. Configure a static route and IP FRR. Specifically, configure a static route of which the destination is the multicast source, the next hop is Device D, and the preference is lower than that of the IGP route. In addition, configure IP FRR.

* The IGP route is Device C -> Device B -> Device A, which has a higher preference and functions as the primary link.
* The static route is Device C -> Device D -> Device E -> Device F -> Device A, which has a lower preference and functions as the backup link.

If the primary link works properly, Device C permits the multicast traffic on the primary link and discards that on the backup link. If the primary link (for example, the link Device B -> Device C) fails, Device C permits the multicast traffic on the backup link immediately after detecting the failure.

**Figure 1** Configuring PIM FRR on a ring network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/1, GE 0/1/2, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_228001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each Router interface and configure a unicast routing protocol. Configure a dynamic routing protocol on each Router. Configure a static route on RouterC, with the destination being the multicast source and next hop being RouterD.
2. Configure IS-IS FRR and IP FRR on RouterC.
3. Enable multicast routing and PIM-SM on all Routers that provide the multicast service.
4. Configure a static IGMP group on the Router interface connected to hosts.
5. Configure a rendezvous point (RP).
6. Enable PIM FRR on RouterC.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: 225.1.0.0
* Multicast source address: 11.11.11.11

#### Procedure

1. Assign IP addresses to interfaces and configure a dynamic unicast routing protocol. For configuration details, see [Configuration Files](#EN-US_TASK_0172366951__section_dc_vrp_cfg_01718405) in this section.
2. Configure a static unicast route on RouterC.
   
   
   ```
   [~Device C] ip route-static 10.0.5.0 24 192.168.10.2 
   ```
   ```
   [*Device C] commit
   ```
3. Enable RouterC to calculate loop-free backup routes by using the LFA algorithm.
   
   
   ```
   [~Device C] ip frr
   ```
   ```
   [*Device C] commit
   ```
   ```
   [~Device C] isis 1
   ```
   ```
   [*Device C-isis-1] frr
   ```
   ```
   [*Device C-isis-1-frr] loop-free-alternate level-1
   ```
   ```
   [*Device C-isis-1-frr] commit
   ```
4. Enable multicast routing on each Router and PIM-SM on each interface.
   
   
   
   # Enable multicast routing on each Router and PIM-SM on each interface of the Routers.
   
   ```
   [~Device C] multicast routing-enable
   ```
   ```
   [*Device C] interface gigabitethernet 0/1/1
   ```
   ```
   [*Device C-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*Device C-GigabitEthernet0/1/1] quit
   ```
   ```
   [*Device C] interface gigabitethernet 0/1/2
   ```
   ```
   [*Device C-Gigabitethernet0/1/2] pim sm
   ```
   ```
   [*Device C-Gigabitethernet0/1/2] quit
   ```
   ```
   [*Device C] interface gigabitethernet 0/1/3
   ```
   ```
   [*Device C-GigabitEthernet0/1/3] pim sm
   ```
   ```
   [*Device C-GigabitEthernet0/1/3] quit
   ```
   ```
   [*Device C] commit
   ```
   
   The configurations on Devices A, B, D, E, and F are similar to the configuration of DeviceC. For configuration details, see [Configuration Files](#EN-US_TASK_0172366951__section_dc_vrp_cfg_01718405) in this section.
5. Configure a static IGMP group on the Device interface connected to hosts to simulate a user join.
   
   
   
   # Configure a static IGMP group on the DeviceC interface connected to hosts.
   
   ```
   [~Device C] interface gigabitethernet 0/1/3
   ```
   ```
   [~Device C-GigabitEthernet0/1/3] igmp static-group 225.1.0.0 source 11.11.11.11
   [*Device C-GigabitEthernet0/1/3] quit
   [*Device C] commit
   ```
6. Configure an RP.
   
   
   
   # Configure a candidate-BSR (C-BSR) and candidate-RP (C-RP) on DeviceC.
   
   ```
   [~Device C] pim
   ```
   ```
   [*Device C-pim] c-bsr gigabitethernet 0/1/1
   ```
   ```
   [*Device C-pim] c-rp gigabitethernet 0/1/1
   ```
   ```
   [*Device C-pim] quit
   ```
   ```
   [*Device C] commit
   ```
   
   # Check the PIM routing table of DeviceC. The command output does not show backup inbound or outbound interface information.
   
   ```
   [~Device C] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (11.11.11.11, 225.1.0.0)
        RP: 192.168.8.2 (local)
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:21:36
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 01:21:36
            Upstream neighbor: 192.168.9.1
            RPF prime neighbor: 192.168.9.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/3
                Protocol: static, UpTime: 01:05:00, Expires: -
   ```
7. Enable PIM FRR on DeviceC.
   
   
   ```
   [~Device C] pim
   ```
   ```
   [~Device C-pim] rpf-frr
   ```
   ```
   [*Device C-pim] quit
   ```
   ```
   [*Device C] commit
   ```
   
   # Check the PIM routing table of DeviceC. The command output shows backup inbound interface information.
   
   ```
   [Device C] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (11.11.11.11, 225.1.0.0)
        RP: 192.168.8.2 (local)
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:22:40
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 01:22:40
            Upstream neighbor: 192.168.9.1
            RPF prime neighbor: 192.168.9.1
        Backup upstream interface: GigabitEthernet0/1/2
            Backup upstream neighbor: 192.168.10.2
            Backup RPF prime neighbor: 192.168.10.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/3
                Protocol: static, UpTime: 01:06:04, Expires: -
   ```
8. Verify the configuration.
   
   
   
   # Run the **shutdown** command on GE 0/1/2 of DeviceB to simulate a link failure.
   
   ```
   [~Device B] interface gigabitethernet 0/1/2
   ```
   ```
   [*Device B-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [*Device B-GigabitEthernet0/1/2] commit
   ```
   
   # Run the **display pim routing-table** command on DeviceC immediately after the **shutdown** command is run.
   
   ```
   [~Device C] display pim routing-table
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (11.11.11.11, 225.1.0.0)
        RP: NULL
        Protocol: pim-sm, Flag: SPT SG_RCVR
        UpTime: 01:24:22
        Upstream interface: GigabitEthernet0/1/2, Refresh time: 01:24:22
            Upstream neighbor: 192.168.10.2
            RPF prime neighbor: 192.168.10.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/3
                Protocol: static, UpTime: 01:07:46, Expires: -
   ```
   
   The command output shows that the inbound interface of the forwarding route on DeviceC has been switched to GE 0/1/2 connected to DeviceD on the backup link.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname Device A
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0001.00
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
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 11.11.11.11 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.13.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.8.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
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
  sysname Device B
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0003.00
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.8.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.9.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
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
  sysname Device C
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   frr
  ```
  ```
    loop-free-alternate level-1
  ```
  ```
   network-entity 10.0000.0000.0001.00
  ```
  ```
  #
  ```
  ```
  ip route-static 10.0.5.0 255.255.255.0 192.168.10.2 
  ```
  ```
  #
  ```
  ```
  ip frr 
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
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.14.1 255.255.255.0 
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
   igmp static-group 225.1.0.0 source 11.11.11.11 
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.10.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.9.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   c-bsr Gigabitethernet0/1/1
  ```
  ```
   c-rp Gigabitethernet0/1/1
  ```
  ```
   rpf-frr
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
  sysname Device D
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0004.00
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.10.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.11.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
  sysname Device E
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0005.00
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.11.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.12.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceF configuration file
  
  ```
  #
  ```
  ```
  sysname Device F
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   network-entity 10.0000.0000.0006.00
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.12.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Gigabitethernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.13.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```