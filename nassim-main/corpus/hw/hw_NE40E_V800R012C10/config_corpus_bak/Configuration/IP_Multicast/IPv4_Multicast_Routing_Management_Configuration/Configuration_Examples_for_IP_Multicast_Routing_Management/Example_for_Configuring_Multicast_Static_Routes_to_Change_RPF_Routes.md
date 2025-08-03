Example for Configuring Multicast Static Routes to Change RPF Routes
====================================================================

To change the Reverse Path Forwarding (RPF) route and create a multicast path different from the source-to-receiver unicast path, configure multicast static routes on the multicast network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172367127__fig_dc_vrp_multicast_cfg_009401), the network runs PIM-SM, all Routers support multicast, and the receiver can receive information from the multicast source. IS-IS is run between Routers. Configure a multicast static route to create a multicast path from the source to the receiver different from the unicast path from the source to the receiver.

**Figure 1** Configuring multicast static routes to change RPF routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_009401.png)

#### Precautions

During the configuration, pay attention to the following points:

* When configuring a multicast static route, if the next hop is a P2P interface, you can specify the outbound interface number. If the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each Router interface and configure IS-IS on Routers.
2. Enable multicast routing on each Router, enable PIM-SM on each interface, and enable IGMP on interfaces connecting Routers to hosts.
3. Configure Candidate-BootStrap Routers (C-BSRs) and Candidate-Rendezvous Points (C-RPs).
4. Configure multicast static routes on Device B and specify Device C as an RPF neighbor to the source.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the source
* Outbound interface of Device B to the source

#### Procedure

1. Configure an IP address for each Router interface and a unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Configure Device A. The configurations of Device B, Device C, and Device D are similar to the configuration of Device A. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/3/0] quit
   ```
3. Enable IGMP on interfaces that connect to hosts.
   
   
   
   # Enable IGMP on the interface connecting Device D to hosts.
   
   ```
   [~DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/0] quit
   ```
4. Configure C-BSRs and C-RPs.
   
   
   
   # Configure GE 0/3/0 on Device C as both a C-BSR and a C-RP.
   
   ```
   [~DeviceC] pim
   ```
   ```
   [*DeviceC-pim] c-bsr GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceC-pim] c-rp GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceC-pim] commit
   ```
   ```
   [~DeviceC-pim] quit
   ```
   
   # Run the **display multicast rpf-info** command on DeviceB to view the RPF route information of the source. The command output shows that the RPF route is a unicast route and the RPF neighbor is DeviceA.
   
   ```
   <DeviceB> display multicast rpf-info 10.5.1.2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 10.5.1.2:
   ```
   ```
        RPF interface: GigabitEthernet0/1/0, RPF neighbor: 10.4.1.1
   ```
   ```
        Referenced route/mask: 10.5.1.0/24
   ```
   ```
        Referenced route type: unicast
   ```
   ```
        Route selection rule: preference-preferred
   ```
   ```
        Load splitting rule: disable
   ```
5. Configure multicast static routes.
   
   
   
   # Configure a multicast static route on Device B and specify Device C as an RPF neighbor to the source.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ip rpf-route-static 10.5.1.0 255.255.255.0 10.2.1.2
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display multicast rpf-info** command on DeviceB to view the RPF route information of the source. The command output shows that the RPF route and the RPF neighbor have been updated according to the multicast static route. The command output is as follows.
   
   ```
   <DeviceB> display multicast rpf-info 10.5.1.2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 10.5.1.2:
   ```
   ```
        RPF interface: GigabitEthernet0/2/0, RPF neighbor: 10.2.1.2
   ```
   ```
        Referenced route/mask: 10.5.1.0/24
   ```
   ```
        Referenced route type: mstatic
   ```
   ```
        Route selection rule: preference-preferred
   ```
   ```
        Load splitting rule: disable 
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.5.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.4.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  ip rpf-route-static 10.5.1.0 255.255.255.0 10.2.1.2
  #
  return
  
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   c-bsr GigabitEthernet0/3/0
   c-rp GigabitEthernet0/3/0
  #
  return
  
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.6.1.1 255.255.255.0
   pim sm
   igmp enable
   isis enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  
  ```