Example for Configuring IPv6 Multicast Static Routes to Connect RPF Routes
==========================================================================

After multicast static routes are configured on a multicast network, receivers in an area can receive data from a multicast source outside the area.

#### Networking Requirements

The network shown in [Figure 1](#EN-US_TASK_0000001583617441__fig_dc_vrp_multicast_cfg_009501) runs IPv6 PIM-SM, all Routers support multicast, and Receiver can receive information from Source1. DeviceB and DeviceC run OSPFv3, and no unicast routes are available for communication between DeviceA and DeviceB and between DeviceA and DeviceC. It is required that multicast static routes be configured so that Receiver can receive information from Source2 outside the OSPF area.

**Figure 1** Network diagram of configuring IPv6 multicast static routes to connect RPF routes  
![](figure/en-us_image_0000001533058090.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | interface1, GE0/1/0 | 2001:db8:5::1/64 |
| interface3, GE0/2/2 | 2001:db8:4::2/64 |
| DeviceB | interface1, GE0/1/0 | 2001:db8:2::2/64 |
| interface2, GE0/2/1 | 2001:db8:3::1/64 |
| interface3, GE0/2/2 | 2001:db8:4::1/64 |
| DeviceC | interface1, GE0/1/0 | 2001:db8:2::1/64 |
| interface2, GE0/2/1 | 2001:db8:1::1/64 |



#### Precautions

During the configuration process, note the following:

* When configuring a multicast static route, if the next hop is a point-to-point (P2P) interface, you can specify the outbound interface number instead. If the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv6 addresses to Router interfaces and configure OSPFv3 as the unicast routing protocol.
2. Enable multicast routing on each Router, enable IPv6 PIM-SM on each interface, and enable MLD on interfaces connected to hosts.
3. Configure the candidate-bootstrap router (C-BSR) and candidate rendezvous point (C-RP).
4. Configure multicast static routes on DeviceB and DeviceC.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of Source2
* DeviceB's RPF interface and RPF neighbor to Source2
* DeviceC's RPF interface and RPF neighbor to Source2

#### Procedure

1. Assign an IPv6 address to each Router interface and configure an IPv6 unicast routing protocol. For detailed configurations, see the configuration files.
2. Enable multicast routing on all Routers and enable IPv6 PIM-SM on each interface.
   
   
   
   # Configure DeviceB. The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB. For configuration details, see the configuration files.
   
   ```
   [~DeviceB] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] pim ipv6 sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/1] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/2/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/2] pim ipv6 sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/2] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/2] quit
   ```
3. Enable MLD on the interfaces connected to hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceC to hosts.
   
   ```
   [~DeviceC] interface gigabitethernet 0/2/1
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/1] mld enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/1] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/1] quit
   ```
4. Configure the C-BSR and C-RP.
   
   
   
   # Configure GE 0/1/0 on DeviceB as the C-BSR and C-RP.
   
   ```
   [~DeviceB] pim-ipv6
   ```
   ```
   [*DeviceB-pim6] c-bsr GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-pim6] c-rp GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-pim6] commit
   ```
   ```
   [~DeviceB-pim6] quit
   ```
   
   Both Source1 (2001:db8:3::2/64/64) and Source2 (2001:db8:5::2/64/64) send multicast data to multicast group G (FF13::1). After Receiver joins group G, it can receive multicast data from Source1 but not from Source2.
   
   # Run the **display multicast ipv6 rpf-info 2001:db8:5::2/64** command on DeviceB and DeviceC. No information is displayed, indicating that they do not have an RPF route to Source2.
5. Configure IPv6 multicast static routes.
   
   
   
   # Configure an IPv6 multicast static route on DeviceB, and specify DeviceA as the RPF neighbor to Source2.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:4::2/64
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] quit
   ```
   
   # Configure an IPv6 multicast static route on DeviceC, and specify DeviceB as the RPF neighbor to Source2.
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:2::2/64
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display multicast ipv6 rpf-info 2001:db8:5::2** command on DeviceB and DeviceC to check information about the RPF route to Source2. The information is displayed as follows:
   
   ```
   <DeviceB> display multicast ipv6 rpf-info 2001:db8:5::2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about: 2001:db8:5::2
   ```
   ```
        RPF interface: GigabitEthernet0/2/2, RPF neighbor: 2001:db8:4::2/64
   ```
   ```
        Referenced route/mask: 2001:db8:5::0/64
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
   <DeviceC> display multicast ipv6 rpf-info 2001:db8:5::2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 2001:db8:5::2:
   ```
   ```
        RPF interface: GigabitEthernet0/1/0, RPF neighbor: 2001:db8:2::2/64
   ```
   ```
        Referenced route/mask: 2001:db8:5::0/64
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
   
   # Run the **display pim ipv6 routing-table** command on DeviceC to check the routing table. According to the following command output, DeviceC has a multicast entry related to Source2, indicating that Receiver can receive multicast data from Source2.
   
   ```
   <DeviceC> display pim ipv6 routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 2 (S, G) entries
   ```
   ```
    (*,FF13::1)
   ```
   ```
        RP: 2001:db8:2::2/64
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
            1: GigabitEthernet0/2/1
   ```
   ```
                Protocol: PIM-SM, UpTime: 01:38:19, Expires: never
   ```
   ```
   (2001:db8:3::2/64, FF13::1)  
   ```
   ```
        RP: 2001:db8:2::2/64
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
            Upstream neighbor: 2001:db8:2::2/64
   ```
   ```
            RPF prime neighbor: 2001:db8:2::2/64
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
             1: GigabitEthernet0/2/1
   ```
   ```
                 Protocol: PIM-SM, UpTime: 00:00:44, Expires: never
   ```
   ```
   (2001:db8:5::2/64, FF13::1)   
   ```
   ```
        RP: 2001:db8:2::2/64
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
            Upstream neighbor: 2001:db8:2::2/64
   ```
   ```
            RPF prime neighbor: 2001:db8:2::2/64
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
             1: GigabitEthernet0/2/1
   ```
   ```
                 Protocol: PIM-SM, UpTime: 00:00:44, Expires: never
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  pim-ipv6
   c-bsr GigabitEthernet0/1/0
   c-rp GigabitEthernet0/1/0
  #
  ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:4::2/64
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:2::2/64
  #
  return
  ```