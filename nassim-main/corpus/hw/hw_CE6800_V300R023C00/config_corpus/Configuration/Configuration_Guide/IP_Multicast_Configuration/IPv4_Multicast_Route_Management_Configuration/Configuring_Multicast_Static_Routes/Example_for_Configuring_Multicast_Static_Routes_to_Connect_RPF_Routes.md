Example for Configuring Multicast Static Routes to Connect RPF Routes
=====================================================================

Example for Configuring Multicast Static Routes to Connect RPF Routes

#### Networking Scenario

In [Figure 1](#EN-US_TASK_0000001176742427__fig1912652714446), PIM-SM is running on the network, all devices support multicast, and the receiver can receive information from multicast source Source1. OSPF is running on DeviceB and DeviceC and is isolated from the unicast route of DeviceA. To enable the receiver to receive multicast data from multicast source Source2 that is not in the OSPF domain, configure multicast static routes to connect the RPF routes.

**Figure 1** Network diagram of configuring multicast static routes to connect the RPF routes![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001216726716.png)
#### Precautions

Note the following during the configuration:

* When configuring a multicast static route, if the next hop is a P2P interface, you can specify the outbound interface number. If the next hop is not a P2P interface, you must specify the next-hop address.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses and OSPF on the devices.
2. Enable the multicast function on all the devices, enable PIM-SM on all the involved interfaces, and enable IGMP on the interface connecting to the host.
3. Configure a C-BSR and a C-RP.
4. Configure a multicast static route on DeviceB and DeviceC.


#### Procedure

1. Configure interface IPv4 addresses and OSPF on the devices.
   
   
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface 100GE 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [~DeviceB-100GE1/0/1] ip address 10.1.2.2 255.255.255.0
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100GE 1/0/2
   [*DeviceB-100GE1/0/2] undo portswitch
   [*DeviceB-100GE1/0/2] ip address 10.1.3.1 255.255.255.0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100GE 1/0/3
   [*DeviceB-100GE1/0/3] undo portswitch
   [*DeviceB-100GE1/0/3] ip address 10.1.4.1 255.255.255.0
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] multicast routing-enable
   [*DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] pim sm
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100GE 1/0/2
   [*DeviceB-100GE1/0/2] pim sm
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100GE 1/0/3
   [*DeviceB-100GE1/0/3] pim sm
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   The configurations of DeviceA and DeviceC are similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
3. Enable IGMP on the interface connecting to the host.
   
   
   
   # Enable IGMP on the interface connecting DeviceC to the host.
   
   ```
   [~DeviceC] interface 100GE 1/0/2
   [*DeviceC-100GE1/0/2] igmp enable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
4. Configure a C-BSR and a C-RP.
   
   
   
   # Configure 100GE1/0/1 on DeviceB as the C-BSR and C-RP.
   
   ```
   [~DeviceB] pim
   [*DeviceB-pim] c-bsr 100GE 1/0/1
   [*DeviceB-pim] c-rp 100GE 1/0/1
   [*DeviceB-pim] commit
   ```
   
   Source1 (10.1.3.0/24) and Source2 (10.1.5.0/24) both send multicast data to multicast group G (225.1.1.1). After the receiver joins group G, it can receive multicast data from Source1 but cannot receive multicast data from Source2. After the **display multicast rpf-info 10.1.5.0** command is run on DeviceB and DeviceC, no command output is displayed, indicating that the devices have no RPF routes to Source2.
5. Configure multicast static routes.
   
   
   
   # On DeviceB, configure a multicast static route that specifies DeviceA as the RPF neighbor to Source2.
   
   ```
   [~DeviceB] ip rpf-route-static 10.1.5.0 255.255.255.0 10.1.4.2
   [*DeviceB] commit
   ```
   
   # On DeviceC, configure a multicast static route that specifies DeviceB as the RPF neighbor to Source2.
   
   ```
   [~DeviceC] ip rpf-route-static 10.1.5.0 255.255.255.0 10.1.2.2
   [*DeviceC] commit
   ```

#### Verifying the Configuration

# Run the [**display multicast rpf-info**](cmdqueryname=display+multicast+rpf-info) command on DeviceB and DeviceC to check the RPF route information to Source2. The displayed information is as follows:

```
[~DeviceB] display multicast rpf-info 10.1.5.0
VPN-Instance: public net
RPF information about source 10.1.5.2:
     RPF interface: 100GE1/0/3, RPF neighbor: 10.1.4.2
     Referenced route/mask: 10.1.5.0/24
     Referenced route type:mstatic
     Route selection rule: preference-preferred
     Load splitting rule: disable
```
```
[~DeviceC] display multicast rpf-info 10.1.5.0
VPN-Instance: public net
RPF information about source 10.1.5.2:
     RPF interface: 100GE1/0/1, RPF neighbor: 10.1.2.2
     Referenced route/mask: 10.1.5.0/24
     Referenced route type:mstatic
     Route selection rule: preference-preferred
     Load splitting rule: disable
```

# Run the **display pim routing-table** command on DeviceC to check the routing table information. DeviceC has the multicast entry of Source2. The receiver can receive multicast data from Source2.

```
[~DeviceC] display pim routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 2 (S, G) entries

 (*, 225.1.1.1)
     RP: 10.1.2.2
     Protocol: PIM-SM, Flag: WC
     UpTime: 03:54:19
     Upstream interface: NULL, Refresh time: 03:54:19
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/2
             Protocol: PIM-SM, UpTime: 01:38:19, Expires: never

(10.1.3.0, 225.1.1.1)     
     RP: 10.1.2.2
     Protocol: PIM-SM, Flag: ACT
     UpTime: 00:00:44
     Upstream interface: 100GE1/0/1, Refresh time: 00:00:44
         Upstream neighbor: 10.1.2.2
         RPF prime neighbor: 10.1.2.2
     Downstream interface(s) information:
     Total number of downstreams: 1
          1: 100GE1/0/2
              Protocol: PIM-SM, UpTime: 00:00:44, Expires: never

(10.1.5.0, 225.1.1.1)     
     RP: 10.1.2.2
     Protocol: PIM-SM, Flag: ACT
     UpTime: 00:00:44
     Upstream interface: 100GE1/0/1, Refresh time: 00:00:44
         Upstream neighbor: 10.1.2.2
         RPF prime neighbor: 10.1.2.2
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
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.5.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
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
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/1
   c-rp 100GE1/0/1
  #
  ip rpf-route-static 10.1.5.0 24 10.1.4.2
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
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface 100GE1/0/3
   undo portswitch
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