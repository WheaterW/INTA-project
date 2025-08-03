Example for Enabling the IGMP Function
======================================

Example for Enabling the IGMP Function

#### Networking Requirements

Multicast services need to be deployed on the PIM network shown in [Figure 1](#EN-US_TASK_0000001130624422__fig_dc_vrp_multicast_cfg_206801). Hosts (HostA, HostB, HostC, and HostD in the figure) on the network are required to receive VOD information in multicast mode. HostA and HostB are required to steadily receive popular programs from the multicast group 225.1.1.1.

**Figure 1** Network diagram of enabling the IGMP function![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001261567149.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device to ensure connectivity at the network layer.
2. Configure basic multicast functions on each device to implement multicast data forwarding on the network.
3. Enable IGMP on the interfaces connected to user hosts.
4. Add DeviceA's interface1 to the multicast group 225.1.1.1 statically.

#### Procedure

1. Configure IP addresses and a unicast routing protocol for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.110.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.110.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices, enable PIM-SM on all the involved interfaces, and configure RPs.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [~DeviceA] pim
   [*DeviceA-pim] c-bsr 100ge 1/0/2
   [*DeviceA-pim] c-rp 100ge 1/0/2
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable IGMP on the interfaces connected to user hosts.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] igmp enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
4. Add DeviceA's interface1 to the multicast group 225.1.1.1 statically.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] igmp static-group 225.1.1.1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display igmp interface** command to check IGMP information on interfaces. For example, the IGMP information on DeviceB's interface1 is as follows:

```
<DeviceB> display igmp interface
Interface information of VPN Instance: public net
 100GE1/0/1(10.110.2.1):
   IGMP is enabled   
   Current IGMP version is 2   
   IGMP state: up
   IGMP group policy: none
   IGMP limit: -
   Query interval for IGMP (negotiated): -
   Query interval for IGMP(configured): 60 s
   Other querier timeout for IGMP: 0 s
   Maximum query response time for IGMP: 10 s
   Querier for IGMP: 10.110.2.1 (this router)
   Total 1 IGMP Group reported
```

The command output shows that DeviceB is the querier. This is because the IP address of DeviceB's interface1, which is connected to the user network segment, is lower.

# Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on DeviceA to check whether interface1 is statically added to the multicast group 225.1.1.1. If the (\*, 225.1.1.1) entry exists, the downstream interface is interface1, and the protocol type is static, interface1 has been statically added to the multicast group 225.1.1.1. The command output is as follows:

```
<DeviceA> display pim routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 0 (S, G) entry
 (*, 225.1.1.1)
     RP: 192.168.4.1
     Protocol: pim-sm, Flag: WC
     UpTime: 00:12:17
     Upstream interface: 100GE1/0/2, Refresh time: 00:12:17
         Upstream neighbor: 192.168.1.2
         RPF prime neighbor: 192.168.1.2
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/1
             Protocol: static, UpTime: 00:12:17, Expires: -
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
   ip address 10.110.1.1 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 225.1.1.1
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 10.110.1.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/2
   c-rp 100GE1/0/2
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
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
    network 10.110.2.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/2
   c-rp 100GE1/0/2
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
  interface 100GE1/0/1
   undo portswitch
   ip address 10.110.2.2 255.255.255.0
   pim sm
   igmp enable
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
    network 10.110.2.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/2
   c-rp 100GE1/0/2
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
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2 
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/3 
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 192.168.4.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  pim
   c-bsr 100GE1/0/4
   c-rp 100GE1/0/4
  #
  return
  ```