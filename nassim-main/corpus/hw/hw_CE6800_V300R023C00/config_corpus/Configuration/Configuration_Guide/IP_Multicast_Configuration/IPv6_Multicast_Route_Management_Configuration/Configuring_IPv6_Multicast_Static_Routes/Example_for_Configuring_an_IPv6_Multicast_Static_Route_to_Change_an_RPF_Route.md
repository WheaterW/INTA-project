Example for Configuring an IPv6 Multicast Static Route to Change an RPF Route
=============================================================================

Example for Configuring an IPv6 Multicast Static Route to Change an RPF Route

#### Networking Scenario

In [Figure 1](#EN-US_TASK_0000001583800489__fig125353144811), IPv6 PIM-SM is running on the network, all devices support multicast, and the receiver can receive information from the multicast source. IPv6 IS-IS is running on DeviceA, DeviceB, DeviceC, and DeviceD. To change the RPF route so that the source-to-receiver multicast path is different from the unicast path, configure a multicast static route on the multicast network.

**Figure 1** Network diagram of configuring an IPv6 multicast static route to change an RPF route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001583680837.png)
#### Precautions

Note the following during the configuration:

* When configuring a multicast static route, if the next hop is a P2P interface, you can specify the next hop through the outbound interface number. If the next hop is not a P2P interface, you must specify the next hop through the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface and configure IPv6 IS-IS as the unicast routing protocol.
2. Enable multicast routing on each device, enable IPv6 PIM-SM on each interface, and enable MLD on interfaces connected to hosts.
3. Configure a candidate-bootstrap router (C-BSR) and a candidate-rendezvous point (C-RP).
4. On DeviceB, configure a multicast static route that specifies DeviceC as the RPF neighbor to the source.


#### Procedure

1. Configure interface IPv6 addresses and IS-IS on the devices.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] isis 1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] ipv6 enable
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:4::1 64
   [*DeviceA-100GE1/0/1] isis ipv6 enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:5::1 64
   [*DeviceA-100GE1/0/2] isis ipv6 enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ipv6 enable
   [*DeviceA-100GE1/0/3] ipv6 address 2001:db8:3::1 64
   [*DeviceA-100GE1/0/3] isis ipv6 enable 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] pim ipv6 sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceD to the host.
   
   ```
   [~DeviceD] interface 100GE 1/0/2
   [*DeviceD-100GE1/0/2] mld enable
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
4. Configure a C-BSR and a C-RP.
   
   
   
   # Configure interface3 on DeviceC as the C-BSR and C-RP.
   
   ```
   [~DeviceC] pim ipv6
   [*DeviceC-pim6] c-bsr 2001:db8:3::2
   [*DeviceC-pim6] c-rp 2001:db8:3::2
   [*DeviceC-pim6] commit
   ```
   
   
   
   # Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) command on DeviceB to check the RPF route to the source. The command output shows that the RPF route is a unicast route and the RPF neighbor is DeviceA. The displayed information is as follows:
   
   ```
   [~DeviceB] display multicast ipv6 rpf-info 2001:db8:5::
   VPN-Instance: public net
   RPF information about source 2001:db8:5::2:
        RPF interface: 100GE1/0/1, RPF neighbor: 2001:db8:4::1
        Referenced route/mask: 2001:db8:5::/64
        Referenced route type: unicast
        Route selection rule: preference-preferred
        Load splitting rule: disable
   ```
5. Configure a multicast static route.
   
   
   
   # Configure a multicast static route on DeviceB, and specify DeviceC as the RPF neighbor to the source.
   
   ```
   [~DeviceB] ipv6 rpf-route-static 2001:db8:5:: 64 2001:db8:2::2
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) command on DeviceB to check the RPF route to the source. The command output shows that the RPF route and the RPF neighbor have been updated according to the multicast static route. The displayed information is as follows:

```
[~DeviceB] display multicast ipv6 rpf-info 2001:db8:5::
VPN-Instance: public net
RPF information about source 2001:db8:5::2:
     RPF interface: 100GE1/0/2, RPF neighbor: 2001:db8:2::2
     Referenced route/mask: 2001:db8:5::/64
     Referenced route type:mstatic
     Route selection rule: preference-preferred
     Load splitting rule: disable
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
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
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  ipv6 rpf-route-static 2001:db8:5:: 64 2001:db8:2::2
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
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  pim ipv6
   c-bsr 2001:db8:3::2
   c-rp 2001:db8:3::2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
   pim ipv6 sm 
   mld enable
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm 
   isis ipv6 enable 1
  #
  return
  ```