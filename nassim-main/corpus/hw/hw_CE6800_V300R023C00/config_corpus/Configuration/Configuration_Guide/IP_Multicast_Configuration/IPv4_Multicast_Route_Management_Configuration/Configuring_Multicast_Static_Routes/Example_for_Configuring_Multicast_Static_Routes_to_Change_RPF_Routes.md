Example for Configuring Multicast Static Routes to Change RPF Routes
====================================================================

Example for Configuring Multicast Static Routes to Change RPF Routes

#### Networking Scenario

In [Figure 1](#EN-US_TASK_0000001130622984__fig125353144811), PIM-SM is running on the network, all devices support multicast, and the receiver can receive information from the multicast source. IS-IS is running on DeviceA, DeviceB, DeviceC, and DeviceD. To change the RPF route so that the source-to-receiver multicast path is different from the unicast path, configure a multicast static route on the multicast network.

**Figure 1** Network diagram of configuring a multicast static route to change the RPF route![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001130782790.png)
#### Precautions

Note the following during the configuration:

* When configuring a multicast static route, if the next hop is a P2P interface, you can specify the outbound interface number. If the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses and IS-IS on the devices.
2. Enable the multicast function on all the devices, enable PIM-SM on all the involved interfaces, and enable IGMP on the interface connecting to the host.
3. Configure a candidate-bootstrap router (C-BSR) and a candidate-rendezvous point (C-RP).
4. On DeviceB, configure a multicast static route that specifies DeviceC as the RPF neighbor to the source.


#### Procedure

1. Configure interface IPv4 addresses and IS-IS on the devices.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] isis 1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.4.1.1 255.255.255.0
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.5.1.1 255.255.255.0
   [*DeviceA-100GE1/0/2] isis enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 10.3.1.1 255.255.255.0
   [*DeviceA-100GE1/0/3] isis enable 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable IGMP on the interface connecting to the host.
   
   
   
   # Enable IGMP on the interface connecting DeviceD to the host.
   
   ```
   [~DeviceD] interface 100GE 1/0/2
   [*DeviceD-100GE1/0/2] igmp enable
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```
4. Configure a C-BSR and a C-RP.
   
   
   
   # Configure 100GE1/0/3 on DeviceC as the C-BSR and C-RP.
   
   ```
   [~DeviceC] pim
   [*DeviceC-pim] c-bsr 100GE 1/0/3
   [*DeviceC-pim] c-rp 100GE 1/0/3
   [*DeviceC-pim] commit
   ```
   
   
   
   # Run the [**display multicast rpf-info**](cmdqueryname=display+multicast+rpf-info) command on DeviceB to check the RPF route information of the source. The command output shows that the RPF route is a unicast route and the RPF neighbor is DeviceA. The displayed information is as follows:
   
   ```
   [~DeviceB] display multicast rpf-info 10.5.1.0
   VPN-Instance: public net
   RPF information about source 10.5.1.2:
        RPF interface: 100GE1/0/1, RPF neighbor: 10.4.1.1
        Referenced route/mask: 10.5.1.0/24
        Referenced route type: unicast
        Route selection rule: preference-preferred
        Load splitting rule: disable
   ```
5. Configure a multicast static route.
   
   
   
   # On DeviceB, configure a multicast static route that specifies DeviceC as the RPF neighbor to the source.
   
   ```
   [~DeviceB] ip rpf-route-static 10.5.1.0 255.255.255.0 10.2.1.2
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Run the [**display multicast rpf-info**](cmdqueryname=display+multicast+rpf-info) command on DeviceB to check the RPF route information of the source. The command output shows that the RPF route and the RPF neighbor have been updated according to the multicast static route. The displayed information is as follows:

```
[~DeviceB] display multicast rpf-info 10.5.1.0
VPN-Instance: public net
RPF information about source 10.5.1.2:
     RPF interface: 100GE1/0/2, RPF neighbor: 10.2.1.2
     Referenced route/mask: 10.5.1.0/24
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
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.4.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.5.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.3.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.4.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  ip rpf-route-static 10.5.1.0 255.255.255.0 10.2.1.2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.2.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.3.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   c-bsr 100GE1/0/3
   c-rp 100GE1/0/3
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.6.1.1 255.255.255.0
   pim sm
   igmp enable
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```