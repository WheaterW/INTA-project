Example for Configuring NAT Traffic Diversion in an SRv6 Scenario
=================================================================

This section provides an example for configuring NAT traffic diversion to implement mutual access between users in an SRv6 scenario.

#### Networking Requirements

In the SRv6 scenario shown in [Figure 1](#EN-US_TASK_0275817275__fig_dc_ne_nat_cfg_015701), CE1 and CE2 belong to VPN-A, and PE2 is a NAT device. PC1 needs to be able to communicate with PC2 after address translation on PE2, and NAT traffic diversion needs to be configured on the network-side inbound interface of the egress PE (PE2).

**Figure 1** Configuring NAT traffic diversion in an SRv6 scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](figure/en-us_image_0275817286.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure routing protocols to enable network connectivity.
2. Configure SRv6 to enable CEs to communicate with each other.
3. Create a service-location group and service-instance group.
4. Create a NAT instance and bind it to the service-instance group.
5. Configure a NAT traffic diversion policy.
6. Configure a NAT address pool and a NAT traffic conversion policy.

#### Data Preparation

* IPv4 addresses of interfaces on the CEs, IPv6 address of interfaces on the PEs and P device, IS-IS process ID and level, and VPN instance names on the PEs
* Index number of the service-location group: 1; name of the service-instance group: **group1**; slot ID of the service board: 1
* NAT instance name and index number: **nat1** and 1
* NAT address pool name: **address-group1**; address pool number: 1; IP address prefix
* ACL number: 3001; traffic classifier name: **c1**; traffic behavior name: **b1**; traffic policy name: **p1**

#### Procedure

1. # Assign IPv4 addresses to the interfaces on the CEs and PEs according to [Figure 1](#EN-US_TASK_0275817275__fig_dc_ne_nat_cfg_015701). For configuration details, see "Configuration Files" in this section.
2. Enable IPv6 forwarding and configure an IPv6 address for each interface. The following uses PE1 as an example. The configuration procedures on PE2 and P are the same.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] interface GigabitEthernet 0/2/2
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] ipv6 enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] ipv6 address 2001:db8:1::1 96
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] quit
   ```
   ```
   [*PE1] interface LoopBack 0
   ```
   ```
   [*PE1-LoopBack0] ipv6 enable
   ```
   ```
   [*PE1-LoopBack0] ipv6 address 2001:db8:10::1 64
   ```
   ```
   [*PE1-LoopBack0] quit
   ```
   ```
   [*PE1] commit
   ```
3. Configure IS-IS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] isis 1
   ```
   ```
   [*PE1-isis-1] is-level level-1
   ```
   ```
   [*PE1-isis-1] cost-style wide
   ```
   ```
   [*PE1-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*PE1-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/2/2
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] isis ipv6 enable 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/2] quit
   ```
   ```
   [*PE1] interface LoopBack 0
   ```
   ```
   [*PE1-LoopBack0] isis ipv6 enable 1
   ```
   ```
   [*PE1-LoopBack0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure the P device.
   
   ```
   [~P] isis 1 
   ```
   ```
   [*P-isis-1] is-level level-1
   ```
   ```
   [*P-isis-1] cost-style wide
   ```
   ```
   [*P-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*P-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*P-isis-1] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/2/1
   ```
   ```
   [*P-GigabitEthernet0/2/1] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/1] quit
   ```
   ```
   [*P] interface GigabitEthernet 0/2/2
   ```
   ```
   [*P-GigabitEthernet0/2/2] isis ipv6 enable 1
   ```
   ```
   [*P-GigabitEthernet0/2/2] quit
   ```
   ```
   [*P] interface LoopBack 0
   ```
   ```
   [*P-LoopBack0] isis ipv6 enable 1
   ```
   ```
   [*P-LoopBack0] quit
   ```
   ```
   [*P] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] isis 1
   ```
   ```
   [*PE2-isis-1] is-level level-1
   ```
   ```
   [*PE2-isis-1] cost-style wide
   ```
   ```
   [*PE2-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*PE2-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/2/2
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] isis ipv6 enable 1
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] quit
   ```
   ```
   [*PE2] interface LoopBack 0
   ```
   ```
   [*PE2-LoopBack0] isis ipv6 enable 1
   ```
   ```
   [*PE2-LoopBack0] quit
   ```
   ```
   [*PE2] commit
   ```
4. Configure a VPN instance on each PE, enable the IPv4 address family for the instance, and bind the interface that connects each PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface GigabitEthernet 0/2/1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] ip address 172.16.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface GigabitEthernet 0/2/1
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] ip address 172.16.5.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After completing the configuration, run the **display ip vpn-instance verbose** command on the PEs to check the VPN instance configuration. Each PE should be able to successfully ping its connected CE.
5. Establish an EBGP peer relationship between each PE and its connected CE.
   
   
   
   # Configure CE1.
   
   
   
   ```
   [~CE1] bgp 200
   ```
   ```
   [*CE1-bgp] peer 172.16.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] import-route direct
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] bgp 400
   ```
   ```
   [*CE2-bgp] peer 172.16.5.2 as-number 100
   ```
   ```
   [*CE2-bgp] import-route direct
   ```
   ```
   [*CE2-bgp] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 172.16.1.1 as-number 200
   ```
   ```
   [*PE1-bgp-vpna] import-route direct
   ```
   ```
   [*PE1-bgp-vpna] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 172.16.5.1 as-number 400
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] quit
   ```
   ```
   [*PE2-bgp] import-route unr
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on the PEs to check whether BGP peer relationships have been established between the PEs and CEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
6. Establish an MP-IBGP peer relationship between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] peer 2001:db8:30::1 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2001:db8:30::1 connect-interface LoopBack0
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:db8:30::1 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [~PE2-bgp] peer 2001:db8:10::1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 2001:db8:10::1 connect-interface LoopBack0
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:db8:10::1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-vpnv4] quit
   ```
   ```
   [~PE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the PEs to check whether a BGP peer relationship has been established between the PEs. If the **Established** state is displayed in the command output, the BGP peer relationships have been established successfully.
7. Establish SRv6 BE paths between the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] segment-routing ipv6
   ```
   ```
   [*PE1-segment-routing-ipv6] encapsulation source-address 2001:db8:10::1
   ```
   ```
   [*PE1-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:40:: 64 static 32
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] opcode ::20 end-dt4 vpn-instance vpna
   ```
   ```
   [*PE1-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE1-segment-routing-ipv6] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2001:db8:30::1 prefix-sid
   ```
   ```
   [*PE1-bgp-af-vpnv4] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 best-effort
   ```
   ```
   [*PE1-bgp-vpna] segment-routing ipv6 locator as1
   ```
   ```
   [*PE1-bgp-vpna] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] isis 1
   ```
   ```
   [*PE1-isis-1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE1-isis-1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] segment-routing ipv6
   ```
   ```
   [*PE2-segment-routing-ipv6] encapsulation source-address 2001:db8:30::1
   ```
   ```
   [*PE2-segment-routing-ipv6] locator as1 ipv6-prefix 2001:db8:50:: 64 static 32
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] opcode ::20 end-dt4 vpn-instance vpna
   ```
   ```
   [*PE2-segment-routing-ipv6-locator] quit
   ```
   ```
   [*PE2-segment-routing-ipv6] quit
   ```
   ```
   [*PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 2001:db8:10::1 prefix-sid
   ```
   ```
   [*PE2-bgp-af-vpnv4] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 best-effort
   ```
   ```
   [*PE2-bgp-vpna] segment-routing ipv6 locator as1
   ```
   ```
   [*PE2-bgp-vpna] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] isis 1
   ```
   ```
   [*PE2-isis-1] segment-routing ipv6 locator as1
   ```
   ```
   [*PE2-isis-1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Run the **display ip routing-table** **vpn-instance** command on the PEs to check that the VPN routing tables contain CE routes. CEs belonging to the same VPN should be able to successfully ping each other.
8. Create a service-location group and service-instance group on PE2, and bind the NAT service board to the service-location group. Create a NAT instance and bind it to the service-instance group.
   
   
   ```
   [~PE2] service-location 1 
   ```
   ```
   [*PE2-service-location-1] location slot 3 
   ```
   ```
   [*PE2-service-location-1] quit 
   ```
   ```
   [*PE2] service-instance-group group1
   ```
   ```
   [*PE2-service-instance-group-group1] service-location 1
   ```
   ```
   [*PE2-service-instance-group-group1] quit 
   ```
   ```
   [*PE2] nat instance nat1 id 1
   ```
   ```
   [*PE2-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*PE2-nat-instance-nat1] quit
   ```
   ```
   [*PE2] commit
   ```
9. Configure an ACL-based traffic policy and apply the traffic policy to the VPN instance on PE2.
   1. Configure an ACL and specify an ACL rule.
      
      
      ```
      [~PE2] acl 3001
      ```
      ```
      [*PE2-acl-adv-3001] rule 1 permit ip source 10.1.1.0 0.0.0.255
      ```
      ```
      [*PE2-acl-adv-3001] commit
      ```
      ```
      [~PE2-acl-adv-3001] quit
      ```
   2. Configure a traffic classifier and define an ACL-based matching rule.
      
      
      ```
      [~PE2] traffic classifier c1
      ```
      ```
      [*PE2-classifier-c1] if-match acl 3001
      ```
      ```
      [*PE2-classifier-c1] commit
      ```
      ```
      [~PE2-classifier-c1] quit
      ```
   3. Define a traffic behavior, in which the action is binding NAT instance **nat1**.
      
      
      ```
      [~PE2] traffic behavior b1
      ```
      ```
      [*PE2-behavior-b1] nat bind instance nat1
      ```
      ```
      [*PE2-behavior-b1] commit
      ```
      ```
      [~PE2-behavior-b1] quit
      ```
   4. Define a traffic policy to associate the configured traffic classifier with the traffic behavior.
      
      
      ```
      [~PE2] traffic policy p1
      ```
      ```
      [*PE2-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*PE2-trafficpolicy-p1] commit
      ```
      ```
      [~PE2-trafficpolicy-p1] quit
      ```
   5. Apply the traffic policy in the VPN instance view.
      
      
      ```
      [~PE2] ip vpn-instance vpna
      ```
      ```
      [*PE2-vpn-instance-vpna] traffic-policy p1 network inbound
      ```
      ```
      [*PE2-vpn-instance-vpna] commit
      ```
      ```
      [~PE2-vpn-instance-vpna] quit
      ```
10. Configure a NAT address pool and NAT conversion policy on PE2 so that all the packets diverted to the NAT service board from the interface board are directly translated using the addresses in the NAT address pool.
    
    
    ```
    [~PE2] nat instance nat1 id 1
    ```
    ```
    [*PE2-nat-instance-nat1] nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpna
    ```
    ```
    [*PE2-nat-instance-nat1] commit
    ```
    ```
    [~PE2-nat-instance-nat1] quit
    ```
    
    Run the **display nat session table** command on PE2 to check that the desired NAT session entry is displayed.
    
    ```
    <HUAWEI> display nat session table slot 1 
    This operation will take a few minutes. Press 'Ctrl+C' to break ... 
    Slot: 1  
    Current total sessions: 1.   
      udp: 10.1.1.2:1234[11.1.1.1:2234]--> 10.1.3.1:1024
    ```

#### Configuration Files

* PE1 configuration file
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #             
  segment-routing ipv6
   encapsulation source-address 2001:db8:10::1
   locator as1 ipv6-prefix 2001:db8:40:: 64 static 32
   opcode ::20 end-dt4 vpn-instance vpna
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #           
  #               
  interface GigabitEthernet0/2/1
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 172.16.1.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/2
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:1::1/96
   isis ipv6 enable 1
  #               
  interface LoopBack0
   ipv6 enable    
   ipv6 address 2001:db8:10::1/64
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 1.1.1.1
   peer 2001:db8:30::1 as-number 100
   peer 2001:db8:30::1 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:db8:30::1 enable
    peer 2001:db8:30::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 172.16.1.1 as-number 200
  #               
  return
  ```
* P configuration file
  ```
  #
  sysname P        
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #              
   ipv6 enable topology ipv6
   #
  #               
  interface GigabitEthernet0/2/1
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:1::2/96
   isis ipv6 enable 1 
  # 
  interface GigabitEthernet0/2/2
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:2::1/96
   isis ipv6 enable 1  
  #               
  interface LoopBack0
   ipv6 enable    
   ipv6 address 2001:db8:20::1/64
   isis ipv6 enable 1
  #               
  return 
  ```
* PE2 configuration file
  ```
  #
   sysname PE2
  #
  service-location 1
   location slot 3
  #
  service-instance-group group1
   service-location 1
  #
  nat instance nat1 id 1
   service-instance-group group1
   nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpna
  #
  acl 3001
   rule 1 permit ip source 10.1.1.0 0.0.0.255 
  #
  traffic classifier c1 operator or
   if-match acl 3001 precedence 1
  #
  traffic behavior b1
   nat bind instance nat1
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  ip vpn-instance vpna
  traffic-policy p1 network inbound
   ipv4-family
    route-distinguisher 100:1
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  segment-routing ipv6
   encapsulation source-address 2001:db8:30::1
   locator as1 ipv6-prefix 2001:db8:50:: 64 static 32
    opcode ::20 end-dt4 vpn-instance vpna
  #               
  isis 1          
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #              
   ipv6 enable topology ipv6
   segment-routing ipv6 locator as1
   #              
  #               
  interface GigabitEthernet0/2/1
   undo shutdown  
   ip binding vpn-instance vpna
   ip address 172.16.5.2 255.255.255.0
  #               
  interface GigabitEthernet0/2/2
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:db8:2::2/96
   isis ipv6 enable 1
  #               
  interface LoopBack0
   ipv6 enable    
   ipv6 address 2001:db8:30::1/64
   isis ipv6 enable 1
  #               
  bgp 100         
   router-id 2.2.2.2
   peer 2001:db8:10::1 as-number 100
   peer 2001:db8:10::1 connect-interface LoopBack0
   #              
   ipv4-family unicast
    undo synchronization
   #              
   ipv6-family unicast
    undo synchronization
   #              
   ipv4-family vpnv4
    policy vpn-target
    peer 2001:db8:10::1 enable
    peer 2001:db8:10::1 prefix-sid
   #              
   ipv4-family vpn-instance vpna
    import-route direct
    segment-routing ipv6 locator as1
    segment-routing ipv6 best-effort
    peer 172.16.5.1 as-number 400
  #               
  return
  ```
* CE1 configuration file
  ```
  #
   sysname CE1
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
  bgp 200
   peer 172.16.1.2 as-number 100
   import-route direct
  #
  return
  ```
* CE2 configuration file
  ```
  #
   sysname CE2
  #
  interface GigabitEthernet0/2/1
   undo shutdown
   ip address 172.16.5.1 255.255.255.0
  #
  bgp 400
   peer 172.16.5.2 as-number 100
   import-route direct
  #
  return
  ```