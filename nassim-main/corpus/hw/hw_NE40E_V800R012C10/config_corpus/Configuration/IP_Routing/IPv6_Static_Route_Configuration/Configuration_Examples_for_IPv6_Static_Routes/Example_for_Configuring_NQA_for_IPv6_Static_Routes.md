Example for Configuring NQA for IPv6 Static Routes
==================================================

NQA for IPv6 static routes can quickly detect network faults and control the advertisement of static routes.

#### Networking Requirements

On a simple network or when the Router cannot use a dynamic routing protocol to generate routes, you can configure static routes. Unlike dynamic routing protocols, static routes do not have a detection mechanism. If a link fails, a network administrator must manually delete the corresponding static route from the IPv6 routing table, which delays link switchovers and causes a lengthy service interruption.

Bidirectional Forwarding Detection (BFD) for static routes is adaptable to link changes but requires that both ends of a link support BFD. If either end of a link does not support BFD, configure NQA for IPv6 static routes. If an NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv6 routing table. Then traffic is switched to a backup route to prevent lengthy service interruptions.

In [Figure 1](#EN-US_TASK_0172365502__fig_dc_vrp_static-route_disjoin_cfg_004201), backup links are deployed on the IP metropolitan area network (MAN).

* Static routes are configured on Device B and Device C. Device B is the master device, while Device C is the backup device.
* In most cases, traffic is transmitted over the primary link (Device B -> Switch A).
* If the primary link fails, traffic switches to the backup link (Device C -> Switch A).

**Figure 1** NQA for IPv6 static routes  
![](images/fig_dc_vrp_static-route_disjoin_cfg_004201.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 2001:db8:1::1/64 |
| GE 0/2/3 | 2001:db8:2::1/64 |
| DeviceB | GE 0/1/0 | 2001:db8:1::2/64 |
| GE 0/1/1 | 2001:db8:3::1/64 |
| DeviceC | GE 0/1/0 | 2001:db8:6::1/64 |
| GE 0/2/3 | 2001:db8:2::2/64 |
| SwitchA | VLANIF 10 | 2001:db8:3::2/64 |
| VLANIF 20 | 2001:db8:6::2/64 |
| VLANIF 30 | 2001:db8:7::1/64 |


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this networking, Switch A provides access services for users. In actual networking, optical line terminals (OLTs), digital subscriber line access multiplexers (DSLAMs), multiservice access nodes (MSANs), or x digital subscriber lines (xDSLs) can be used for user access. The configurations on Device A, Device B, and Device C are the same.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an Internet Control Message Protocol (ICMP) NQA test instance to monitor the status of the primary link.
   
   Create an ICMP NQA test instance on the NQA client Device B to test whether the primary link is running properly.
2. Configure static routes and associate the static route along the primary link with the ICMP NQA test instance.
   
   Configure static routes on Device B and Device C, and associate the static route configured on Device B with the ICMP NQA test instance. If the ICMP NQA test instance detects a link fault, it instructs the routing management module to delete the associated static route from the IPv6 routing table.
3. Configure a dynamic routing protocol.
   
   Configure a dynamic routing protocol on Device A, Device B, and Device C so that they can learn routes from one another.
4. Configure the dynamic routing protocol to import static routes and set a higher cost for the static route along the backup link than for the one along the primary link.
   
   Configure the dynamic routing protocol on Device B and Device C to import static routes, and set a higher cost for the static route imported by Device C than for the one imported by Device B. This configuration allows Device A to preferentially select the link (Device B -> Switch A).

#### Data Preparation

To complete the configuration, you need the following data:

* Interface IPv6 addresses
* NQA item values (for details, see [Table 1](#EN-US_TASK_0172365502__table_02))
  
  **Table 1** NQA item values
  | Item | Value |
  | --- | --- |
  | Administrator name | admin |
  | Name of the test instance | test |
  | Test type | ICMP |
  | Destination address | 2001:db8:3::2 |
  | Interval at which the NQA test automatically runs | 3 seconds |
* OSPFv3 backbone area (Area 0) of Device A, Device B, and Device C, and their router IDs (1.1.1.1, 2.2.2.2, and 3.3.3.3)

#### Procedure

1. Configure interface IPv6 addresses. For configuration details, see [Configuration Files](#EN-US_TASK_0172365502__title_01) in this section.
2. Create an NQA test instance on Device B to test the link between Device B and Switch A.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa test-instance admin test
   ```
   ```
   [*DeviceB-nqa-admin-test] test-type icmp
   ```
   ```
   [*DeviceB-nqa-admin-test] destination-address ipv6 2001:db8:3::2
   ```
   ```
   [*DeviceB-nqa-admin-test] frequency 9
   ```
   ```
   [*DeviceB-nqa-admin-test] interval seconds 3
   ```
   ```
   [*DeviceB-nqa-admin-test] start now
   ```
   ```
   [*DeviceB-nqa-admin-test] commit
   ```
   ```
   [~DeviceB-nqa-admin-test] quit
   ```
3. Configure IPv6 static routes.
   
   
   
   # Configure an IPv6 static route on Device B and associate it with the NQA test instance.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:7:: 64 GigabitEthernet 0/1/1 2001:db8:3::2 track nqa admin test
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure an IPv6 static route on Device C.
   
   ```
   [*DeviceC] ipv6 route-static 2001:db8:7:: 64 GigabitEthernet 0/1/0 2001:db8:6::2
   ```
   ```
   [*DeviceC] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The next hop address of the IPv6 static route configured on the local end must be the link-local address of the peer end, which can be obtained using the [**display ipv6 interface**](cmdqueryname=display+ipv6+interface) [ *interface-type* *interface-number* ] command on the peer end.
4. Configure a dynamic routing protocol on Device A, Device B, and Device C.
   
   
   
   # Configure OSPFv3 on Device A.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/2/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/3] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/3] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/3] quit
   ```
   
   # Configure OSPFv3 on Device B.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure OSPFv3 on Device C.
   
   ```
   [~DeviceC] interface GigabitEthernet 0/2/3
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/3] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/3] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/3] quit
   ```
5. Configure OSPFv3 on Device B and Device C to import static routes.
   
   
   
   # Configure OSPFv3 on Device B to import a static route and set the cost to 10 for the static route.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] import-route static cost 10
   ```
   ```
   [*DeviceB-ospfv3-1] commit
   ```
   ```
   [~DeviceB-ospfv3-1] quit
   ```
   
   # Configure OSPFv3 on Device C to import a static route and set the cost to 20 for the static route.
   
   ```
   [*DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] import-route static cost 20
   ```
   ```
   [*DeviceC-ospfv3-1] commit
   ```
   ```
   [~DeviceC-ospfv3-1] quit
   ```
6. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display current-configuration | include nqa** command on Device B in the system view. The command output shows that the IPv6 static route has been associated with the NQA test instance. Run the **display nqa results** command. The command output shows that an NQA test instance has been created.
   
   # Display configurations of NQA for IPv6 static routes.
   
   ```
   [~DeviceB] display current-configuration | include nqa
   ```
   ```
   ipv6 route-static 2001:db8:7:: 64 GigabitEthernet0/1/1 2001:db8:3::2 track nqa admin test
   nqa test-instance admin test
   
   ```
   
   # Display NQA test results.
   
   ```
   [~DeviceB] display nqa results test-instance admin test
   ```
   ```
    NQA entry(admin, test) : testflag is active ,testtype is icmp
     1 . Test 359 result     The test is finished
      Send operation times: 3                Receive response times: 3
      Completion:success                   RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:0
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Stats errors number:0
      Destination ip address:2001:db8:3::2
      Min/Max/Average Completion Time: 1/3/2
      Sum/Square-Sum  Completion Time: 7/19
      Last Good Probe Time: 2012-11-14 12:15:22.3
      Lost packet ratio: 0 %
   ```
   
   The command output shows "Lost packet ratio 0 %," indicating that the link is running properly.
   
   # Display the routing table on Device B.
   
   ```
   [~DeviceB] display ipv6 routing-table 2001:db8:7::
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : 2001:db8:3::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                    Flags        : D
   ```
   
   The command output shows that the static route exists in the routing table.
   
   # Display the routing table on Device A.
   
   ```
   [~DeviceA] display ipv6 routing-table 2001:db8:7::
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : FE80::2200:10FF:FE03:0                  Preference   : 150
   Cost         : 10                                      Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                  Flags        : D
   ```
   
   The command output shows that a route to 2001:db8:7::1/128 exists in the routing table. The outbound interface of the route is GE 0/1/0 and the cost is 10. Traffic is preferentially transmitted along the link Device B -> Switch A.
   
   # Shut down GE 0/1/1 on Device B to simulate a link fault.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
   
   # Display NQA test results.
   
   ```
   [~DeviceB] display nqa results test-instance admin test
   ```
   ```
    NQA entry(admin, test) : testflag is active ,testtype is icmp
     1 . Test 1156 result    The test is finished
      Send operation times: 3                Receive response times: 0
      Completion:failed                    RTD OverThresholds number:0
      Attempts number:1                      Drop operation number:0
      Disconnect operation number:0          Operation timeout number:3
      System busy operation number:0         Connection fail number:0
      Operation sequence errors number:0     RTT Stats errors number:0
      Destination ip address:2001:db8:3::2
      Min/Max/Average Completion Time: 0/0/0
      Sum/Square-Sum  Completion Time: 0/0
      Last Good Probe Time: 0000-00-00 00:00:00.0
      Lost packet ratio: 100 %
   ```
   
   The command output shows "Completion:failed" and "Lost packet ratio is 100 %," indicating that the link is faulty.
   
   # Display the routing table on Device B.
   
   ```
   [~DeviceB] display ipv6 routing-table 2001:db8:7::
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : FE80::3A00:10FF:FE03:0                  Preference   : 150
   Cost         : 20                                      Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   ```
   
   The command output shows that the static route has been deleted and that the route has become an OSPFv3 route learned from Device A.
   
   # Display the routing table on Device A.
   
   ```
   [~DeviceA] display ipv6 routing-table 2001:db8:7::
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:7::                            PrefixLength : 64
   NextHop      : FE80::3A00:10FF:FE03:107                Preference   : 150
   Cost         : 20                                      Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/3                 Flags        : D
   ```
   
   The static route has been associated with the NQA test instance on Device B. If NQA detects a link fault, it rapidly notifies Device B that the associated static route is unavailable. Device A cannot learn the route to 2001:db8:7::/64 from Device B. However, Device A can learn the route to 2001:db8:7::/64 from Device C. The route's outbound interface is GE 0/2/3, and the cost is 20. Traffic switches to the link Device C -> Switch A.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   import-route static cost 10
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
  #
  ipv6 route-static 2001:db8:7:: 64 GigabitEthernet0/1/1 2001:db8:3::2 track nqa admin test
  #
  nqa test-instance admin test
   test-type icmp
   destination-address ipv6 2001:db8:3::2
   interval seconds 3
   frequency 9
   start now
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
   import-route static cost 20
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  ipv6 route-static 2001:db8:7:: 64 GigabitEthernet0/1/0 2001:db8:6::2
  #
  return
  ```