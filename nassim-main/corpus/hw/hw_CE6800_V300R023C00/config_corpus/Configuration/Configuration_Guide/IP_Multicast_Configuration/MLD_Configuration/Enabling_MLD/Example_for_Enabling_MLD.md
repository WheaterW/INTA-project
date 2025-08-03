Example for Enabling MLD
========================

Example for Enabling MLD

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001589496153__fig_dc_vrp_multicast_cfg_206801), IPv6 multicast services are deployed. An IGP has been deployed on the network, and IPv6 unicast is running properly. Hosts on the network are required to receive VOD information in IPv6 multicast mode. HostA and HostB are required to steadily receive popular programs from the IPv6 multicast group FF13::101.

**Figure 1** Network diagram of enabling MLD![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001538257250.png)

| Device | Interface | IPv6 Address |
| --- | --- | --- |
| DeviceA | 100GE1/0/1 | 2001:db8:5::1/64 |
| 100GE1/0/2 | 2001:db8:1::1/64 |
| DeviceB | 100GE1/0/1 | 2001:db8:6::1/64 |
| 100GE1/0/2 | 2001:db8:2::1/64 |
| DeviceC | 100GE1/0/1 | 2001:db8:7::1/64 |
| 100GE1/0/2 | 2001:db8:3::1/64 |
| DeviceD | 100GE1/0/1 | 2001:db8:1::2/64 |
| 100GE1/0/2 | 2001:db8:2::2/64 |
| 100GE1/0/3 | 2001:db8:3::2/64 |
| 100GE1/0/4 | 2001:db8:4::1/64 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses and a unicast routing protocol for interfaces on each device to ensure connectivity at the network layer.
2. Configure basic IPv6 multicast functions on each device to implement multicast data forwarding on the network.
3. Enable MLD on the interfaces connected to user hosts.
4. Add DeviceA's 100GE1/0/1 to the IPv6 multicast group FF13::101 statically.

#### Procedure

1. Configure IPv6 addresses and a unicast routing protocol for interfaces on each device.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:5::1 64
   [*DeviceA-100GE1/0/1] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all the devices, enable IPv6 PIM-SM on all the involved interfaces, and configure RPs.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] pim ipv6
   [*DeviceA-pim6] c-bsr 2001:db8:1::1
   [*DeviceA-pim6] c-rp 2001:db8:1::1
   [*DeviceA-pim6] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] mld enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
4. Add interface1 of DeviceA to the multicast group FF13::101 statically.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] mld static-group ff13::101
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display mld interface** command to check MLD information on interfaces. For example, MLD information on 100GE1/0/1 of DeviceB is as follows:

```
<DeviceB> display mld interface
Interface information of VPN Instance: public net
 100GE1/0/1(2001:db8:6::1):
   MLD is enabled   
   Current MLD version is 2   
   MLD state: up
   MLD group policy: none
   MLD limit: -
   Query interval for MLD (negotiated): -
   Query interval for MLD(configured): 60 s
   Other querier timeout for MLD: 0 s
   Maximum query response time for MLD: 10 s
   Querier for MLD: 2001:db8:6::1 (this router)
   Total 1 MLD Group reported
```

The command output shows that DeviceB is the querier, as the IPv6 address of DeviceB's 100GE1/0/1 connected to the user network segment is smaller.

# Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command on DeviceA to check whether 100GE1/0/1 is statically added to the multicast group FF13::101. If a (\*, FF13::101) entry exists, the downstream interface is 100GE1/0/1, and the protocol type is static, 100GE1/0/1 has statically joined the multicast group FF13::101. The following information is displayed:

```
<DeviceA> display pim ipv6 routing-table
VPN-Instance: public net
 Total 1 (*, G) entry; 0 (S, G) entry
 (*, FF13::101)
     RP: 2001:db8:4::1
     Protocol: pim-sm, Flag: WC
     UpTime: 00:12:17
     Upstream interface: 100GE1/0/2, Refresh time: 00:12:17
         Upstream neighbor: 2001:db8:1::2
         RPF prime neighbor: 2001:db8:1::2
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
  multicast ipv6 routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   pim ipv6 sm
   mld enable
   mld static-group ff13::101
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:1::1
   c-rp 2001:db8:1::1
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
   ipv6 address 2001:db8:6::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:2::1
   c-rp 2001:db8:2::1
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
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:7::1/64
   pim ipv6 sm
   mld enable
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:3::1
   c-rp 2001:db8:3::1
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
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3 
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   pim ipv6 sm
   ospfv3 1 area 0.0.0.0
  #
  ospfv3 1
   router-id 4.4.4.4
   area 0.0.0.0
  #
  pim ipv6
   c-bsr 2001:db8:4::1
   c-rp 2001:db8:4::1
  #
  return
  ```