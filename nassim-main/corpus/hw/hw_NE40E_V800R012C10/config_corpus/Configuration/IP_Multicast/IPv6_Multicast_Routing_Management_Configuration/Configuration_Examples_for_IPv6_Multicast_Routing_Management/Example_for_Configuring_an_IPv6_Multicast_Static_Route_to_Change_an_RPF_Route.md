Example for Configuring an IPv6 Multicast Static Route to Change an RPF Route
=============================================================================

By configuring a multicast static route on a multicast network, you can change a reverse path forwarding (RPF) route so that the source-to-receiver multicast path is different from the unicast path.

#### Networking Requirements

The network shown in [Figure 1](#EN-US_TASK_0000001533377298__fig_dc_vrp_multicast_cfg_009401) runs IPv6 PIM-SM, all Routers support multicast, and the receiver can receive information from the multicast source. IS-IS runs on DeviceA, DeviceB, DeviceC, and DeviceD. It is required that a multicast static route be used to ensure that the source-to-receiver multicast path is different from the unicast path.

**Figure 1** Network diagram of configuring an IPv6 multicast static route to change an RPF route![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/0, GE 0/2/1, and GE 0/2/2, respectively.


  
![](figure/en-us_image_0000001533537246.png)

#### Precautions

During the configuration process, note the following:

* When configuring a multicast static route, if the next hop is a point-to-point (P2P) interface, you can specify the outbound interface number instead. If the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each Router interface and configure IPv6 IS-IS as the unicast routing protocol.
2. Enable multicast routing on each Router, enable IPv6 PIM-SM on each interface, and enable MLD on interfaces connected to hosts.
3. Configure the candidate-bootstrap router (C-BSR) and candidate rendezvous point (C-RP).
4. Configure an IPv6 multicast static route on DeviceB and specify DeviceC as the RPF neighbor to the source.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the source
* Outbound interface from DeviceB to the source

#### Procedure

1. Assign an IPv6 address to each Router interface and configure a unicast routing protocol. For detailed configurations, see the configuration files.
2. Enable multicast routing on all Routers and enable IPv6 PIM-SM on each interface.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see the configuration files.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/1] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/2/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/2] quit
   ```
3. Enable MLD on the interfaces connected to hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceD to hosts.
   
   ```
   [~DeviceD] interface gigabitethernet 0/2/1
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/1] mld enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/1] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/2/1] quit
   ```
4. Configure the C-BSR and C-RP.
   
   
   
   # Configure GE 0/2/2 on DeviceC as the C-BSR and C-RP.
   
   ```
   [~DeviceC] pim-ipv6
   ```
   ```
   [*DeviceC-pim6] c-bsr GigabitEthernet 0/2/2
   ```
   ```
   [*DeviceC-pim6] c-rp GigabitEthernet 0/2/2
   ```
   ```
   [*DeviceC-pim6] commit
   ```
   ```
   [~DeviceC-pim6] quit
   ```
   
   # Run the **display multicast ipv6 rpf-info** command on DeviceB to check the RPF route to the source. According to the following command output, the RPF route is a unicast route, and the RPF neighbor is DeviceA.
   
   ```
   <DeviceB> display multicast ipv6 rpf-info 2001:db8:5::2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 2001:db8:5::2:
   ```
   ```
        RPF interface: GigabitEthernet0/1/0, RPF neighbor: 2001:db8:4::1
   ```
   ```
        Referenced route/mask: 2001:db8:5::2/64
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
5. Configure a multicast static route.
   
   
   
   # Configure a multicast static route on DeviceB, and specify DeviceC as the RPF neighbor to the source.
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:2::2
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display multicast ipv6 rpf-info** command on DeviceB to check the RPF route to the source. According to the following command output, the RPF route and the RPF neighbor have been updated according to the multicast static route.
   
   ```
   <DeviceB> display multicast ipv6 rpf-info 2001:db8:5::2
   ```
   ```
   VPN-Instance: public net
   ```
   ```
   RPF information about source 2001:db8:5::2:
   ```
   ```
        RPF interface: GigabitEthernet0/2/1, RPF neighbor: 2001:db8:2::2
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

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm 
   isis ipv6 enable 1 
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
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
  isis 1
   ipv6 enable
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  ipv6 rpf-route-static 2001:db8:5::0 64 2001:db8:2::2
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
  isis 1
   ipv6 enable
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  pim-ipv6
   c-bsr GigabitEthernet0/2/2
   c-rp GigabitEthernet0/2/2
  #
  return
  
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
   pim ipv6 sm 
   mld enable
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  return
  
  ```