Example for Configuring IPv6 Multicast Static Routes to Connect RPF Routes
==========================================================================

Example for Configuring IPv6 Multicast Static Routes to Connect RPF Routes

#### Networking Scenario

In [Figure 1](#EN-US_TASK_0000001533240822__fig1912652714446), IPv6 PIM-SM is running on the network, all devices support multicast, and the receiver can receive information from the multicast source Source1. DeviceB and DeviceC run OSPFv3, and no unicast routes are available for communication between DeviceA and DeviceB or between DeviceA and DeviceC. To enable the receiver to receive multicast data from multicast source Source2 that is not in the OSPF domain, configure multicast static routes to connect the RPF routes.

**Figure 1** Network diagram of configuring IPv6 multicast static routes to connect RPF routes![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001583640761.png)
#### Precautions

Note the following during the configuration:

* When configuring a multicast static route, if the next hop is a P2P interface, you can specify the next hop through the outbound interface number. If the next hop is not a P2P interface, you must specify the next hop through the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IPv6 addresses to interfaces and configure OSPFv3 as the unicast routing protocol.
2. Enable multicast routing on each device, enable IPv6 PIM-SM on each interface, and enable MLD on interfaces connected to hosts.
3. Configure a C-BSR and a C-RP.
4. Configure an IPv6 multicast static route on DeviceB and DeviceC.


#### Procedure

1. Assign IPv6 addresses to interfaces and configure OSPFv3 as the unicast routing protocol.
   
   
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:2::2 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100GE 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ipv6 enable
   [*DeviceB-100GE1/0/2] ipv6 address 2001:db8:3::1 64
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100GE 1/0/3
   [*DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ipv6 enable
   [*DeviceB-100GE1/0/3] ipv6 address 2001:db8:4::1 64
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   [*DeviceB-ospfv3-1] area 0.0.0.0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   ```
   
   The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] multicast ipv6 routing-enable
   [*DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] pim ipv6 sm
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100GE 1/0/2
   [*DeviceB-100GE1/0/2] pim ipv6 sm
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100GE 1/0/3
   [*DeviceB-100GE1/0/3] pim ipv6 sm
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceC to the host.
   
   ```
   [~DeviceC] interface 100GE 1/0/2
   [*DeviceC-100GE1/0/2] mld enable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
4. Configure a C-BSR and a C-RP.
   
   
   
   # Configure interface1 on DeviceB as the C-BSR and C-RP.
   
   ```
   [~DeviceB] pim ipv6
   [*DeviceB-pim6] c-bsr 2001:db8:2::2
   [*DeviceB-pim6] c-rp 2001:db8:2::2
   [*DeviceB-pim6] commit
   ```
   
   Both Source1 (2001:db8:3::1/64) and Source2 (2001:db8:5::2/64) send multicast data to multicast group G (FF13::1). After Receiver joins group G, it can receive multicast data from Source1 but not from Source2. After the **display multicast ipv6 rpf-info 2001:db8:5::** command is run on DeviceB and DeviceC, no command output is displayed, indicating that the devices have no RPF routes to Source2.
5. Configure multicast static routes.
   
   
   
   # Configure a multicast static route on DeviceB, and specify DeviceA as the RPF neighbor to Source2.
   
   ```
   [~DeviceB] ipv6 rpf-route-static 2001:db8:5::2 64 2001:db8:4::2
   [*DeviceB] commit
   ```
   
   # Configure a multicast static route on DeviceC, and specify DeviceB as the RPF neighbor to Source2.
   
   ```
   [~DeviceC] ipv6 rpf-route-static 2001:db8:5::2 64 2001:db8:2::2
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) command on DeviceB and DeviceC to check the RPF routes to Source2. The displayed information is as follows:

```
[~DeviceB] display multicast ipv6 rpf-info 2001:db8:5::
VPN-Instance: public net
RPF information about source 2001:db8:5::2
     RPF interface: 100GE1/0/3, RPF neighbor: 2001:db8:4::2
     Referenced route/mask: 2001:db8:5::/64
     Referenced route type:mstatic
     Route selection rule: preference-preferred
     Load splitting rule: disable
```
```
[~DeviceC] display multicast ipv6 rpf-info 2001:db8:5::
VPN-Instance: public net
RPF information about source 2001:db8:5::2
     RPF interface: 100GE1/0/1, RPF neighbor: 2001:db8:2::2
     Referenced route/mask: 2001:db8:5::/64
     Referenced route type:mstatic
     Route selection rule: preference-preferred
     Load splitting rule: disable
```

# Run the **display pim ipv6 routing-table** command on DeviceC to check the routing table information. DeviceC has the multicast entry of Source2. The receiver can receive multicast data from Source2.

```
[~DeviceC] display pim ipv6 routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 2 (S, G) entries

 (*, FF13::1)
     RP: 2001:db8:2::2
     Protocol: PIM-SM, Flag: WC
     UpTime: 03:54:19
     Upstream interface: NULL, Refresh time: 03:54:19
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/2
             Protocol: PIM-SM, UpTime: 01:38:19, Expires: never

(2001:db8:3::2, FF13::1)     
     RP: 2001:db8:2::2
     Protocol: PIM-SM, Flag: ACT
     UpTime: 00:00:44
     Upstream interface: 100GE1/0/1, Refresh time: 00:00:44
         Upstream neighbor: 2001:db8:2::2
         RPF prime neighbor: 2001:db8:2::2
     Downstream interface(s) information:
     Total number of downstreams: 1
          1: 100GE1/0/2
              Protocol: PIM-SM, UpTime: 00:00:44, Expires: never

(2001:db8:5::2, FF13::1)     
     RP: 2001:db8:2::2
     Protocol: PIM-SM, Flag: ACT
     UpTime: 00:00:44
     Upstream interface: 100GE1/0/1, Refresh time: 00:00:44
         Upstream neighbor: 2001:db8:2::2
         RPF prime neighbor: 2001:db8:2::2
     Downstream interface(s) information:
     Total number of downstreams: 1
          1: 100GE1/0/2
              Protocol: PIM-SM, UpTime: 00:00:44, Expires: never
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
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
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:2::2
   c-rp 2001:db8:2::2
  #
  ipv6 rpf-route-static 2001:db8:5:: 64 2001:db8:4::2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  ipv6 rpf-route-static 2001:db8:5:: 64 2001:db8:2::2
  #
  return
  ```