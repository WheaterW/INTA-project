Example for Configuring Multicast Static Routes to Connect RPF Routes
=====================================================================

After multicast static routes are configured, a receiver can receive multicast data from a multicast source in another area that is unreachable with unicast routes.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172367130__fig_dc_vrp_multicast_cfg_009501), the network runs PIM-SM, all Routers support multicast, and the receiver can receive information from Source1. Device B and Device C run OSPF. There is no unicast route between Device A and Device B. To enable the receiver to receive information sent from Source 2, configure a multicast static route.

**Figure 1** Configuring multicast static routes to connect RPF routes  
![](images/fig_dc_vrp_multicast_cfg_009501.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | interface1, GE0/1/0 | 10.1.5.1/24 |
| interface3, GE0/3/0 | 10.1.4.2/24 |
| DeviceB | interface1, GE0/1/0 | 10.1.2.2/24 |
| interface2, GE0/2/0 | 10.1.3.1/24 |
| interface3, GE0/3/0 | 10.1.4.1/24 |
| DeviceC | interface1, GE0/1/0 | 10.1.2.1/24 |
| interface2, GE0/2/0 | 10.1.1.1/24 |



#### Precautions

When configuring multicast static routes to connect RPF routes, note the following precautions:

* When configuring a multicast static route, if the next hop is a Point-to-point (P2P) interface, you must specify the outbound interface number; if the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each Router interface and configure OSPF on Routers.
2. Enable multicast routing on each Router, enable PIM-SM on each interface, and enable IGMP on interfaces connecting Routers to hosts.
3. Configure candidate-bootstrap routers (C-BSRs) and candidate-rendezvous points (C-RPs).
4. Configure multicast static routes on Device B and Device C.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of Source 2
* RPF interface connecting Device B to Source 2 and the RPF neighbor of Device B
* RPF interface connecting Device C to Source 2 and the RPF neighbor of Device C

#### Procedure

1. Configure an IP address for each Router interface and a unicast routing protocol. For configuration details, see Configuration Files in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Configure Device B. The configurations of Device A and Device C are similar to the configuration of Device B. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceB] multicast routing-enable
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/3/0] quit
   ```
3. Enable IGMP on interfaces that connect to hosts.
   
   
   
   # Enable IGMP on the interface connecting Device C to hosts.
   
   ```
   [~DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
4. Configure C-BSRs and C-RPs.
   
   
   
   # Configure GE 0/1/0 on Device B as both a C-BSR and a C-RP.
   
   ```
   [~DeviceB] pim
   ```
   ```
   [*DeviceB-pim] c-bsr GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-pim] c-rp GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-pim] commit
   ```
   ```
   [~DeviceB-pim] quit
   ```
   
   Source 1 (10.1.3.2/24) and Source2 (10.1.5.2/24) both send multicast data to G (225.1.1.1). The receiver joins G and can receive multicast data sent from Source 1 and Source 2.
   
   # Run the **display multicast rpf-info 10.1.5.2** command on Device B and Device C. There is no command output. This indicates that Devices have no RPF routes to Source 2.
5. Configure multicast static routes.
   
   
   
   # Configure a multicast static route on Device B and specify Device A as an RPF neighbor to Source 2.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ip rpf-route-static 10.1.5.0 255.255.255.0 10.1.4.2
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Configure a multicast static route on Device C and specify Device B as an RPF neighbor to Source2.
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] ip rpf-route-static 10.1.5.0 255.255.255.0 10.1.2.2
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display multicast rpf-info 10.1.5.2** command again on Device B and Device C. The command output shows RPF information of Source 2.
   
   ```
   <DeviceB> display multicast rpf-info 10.1.5.2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about: 10.1.5.2
   ```
   ```
        RPF interface: GigabitEthernet0/3/0, RPF neighbor: 10.1.4.2
   ```
   ```
        Referenced route/mask: 10.1.5.0/24
   ```
   ```
        Referenced route type: mstatic
   ```
   ```
        Route selecting rule: preference-preferred
   ```
   ```
        Load splitting rule: disable 
   ```
   ```
   <DeviceC> display multicast rpf-info 10.1.5.2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 10.1.5.2:
   ```
   ```
        RPF interface: GigabitEthernet0/1/0, RPF neighbor: 10.1.2.2
   ```
   ```
        Referenced route/mask: 10.1.5.0/24
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
   
   # Run the **display pim routing-table** command on Device C to view information about PIM routing tables. Device C has multicast entries related to Source 2 and the receiver can receive multicast data from Source 2.
   
   ```
   <DeviceC> display pim routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (*, 225.1.1.1)
   ```
   ```
        RP: 10.1.2.2
   ```
   ```
        Protocol: PIM-SM, Flag: WC
   ```
   ```
        UpTime: 03:54:19
   ```
   ```
        Upstream interface: NULL, Refresh time: 03:54:19
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
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
                Protocol: PIM-SM, UpTime: 01:38:19, Expires: never
   ```
   ```
   (10.1.3.2, 225.1.1.1)     
   ```
   ```
        RP: 10.1.2.2
   ```
   ```
        Protocol: PIM-SM, Flag: ACT
   ```
   ```
        UpTime: 00:00:44
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:00:44
   ```
   ```
            Upstream neighbor: 10.1.2.2
   ```
   ```
            RPF prime neighbor: 10.1.2.2
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
                 Protocol: PIM-SM, UpTime: 00:00:44, Expires: never
   ```
   ```
   (10.1.5.2, 225.1.1.1)     
   ```
   ```
        RP: 10.1.2.2
   ```
   ```
        Protocol: PIM-SM, Flag: ACT
   ```
   ```
        UpTime: 00:00:44
   ```
   ```
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:00:44
   ```
   ```
            Upstream neighbor: 10.1.2.2
   ```
   ```
            RPF prime neighbor: 10.1.2.2
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
                 Protocol: PIM-SM, UpTime: 00:00:44, Expires: never
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.5.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.5.0 0.0.0.255
     network 10.1.4.0 0.0.0.255
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
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  pim
   c-bsr GigabitEthernet0/3/0
   c-rp GigabitEthernet0/3/0
  #
  ip rpf-route-static 10.1.5.0 24 10.1.4.2
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
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  ip rpf-route-static 10.1.5.0 24 10.1.2.2
  #
  return
  
  ```