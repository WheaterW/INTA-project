Example for Configuring Centralized DS-Lite over L3VPN
======================================================

This section provides an example for configuring centralized DS-Lite over L3VPN to allow users with private IPv4 addresses to traverse the IPv6 network to access the IPv4 public network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001420042601__dc_ne_cfg_dslite_005701), a home user using a private IPv4 address accesses a CPE through a VPN and accesses an IPv6 MAN through a PE. A DS-Lite tunnel is established between the PE and DS-Lite device. The PE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the DS-Lite device. The DS-Lite device decapsulates traffic, uses a NAT technique to translate the private IPv4 address to a public IPv4 address, and forwards traffic to the IPv4 Internet. The DS-Lite device is equipped with DS-Lite boards in slots 1 and 2, respectively. The DS-Lite device's GE 0/2/1 is connected to an IPv6 MAN, and GE 0/2/2 is connected to the Internet. IPv4 home users need to access the IPv4 Internet through the IPv6 MAN. The carrier provides 11 public IPv4 addresses from 11.11.11.100 to 11.11.11.110.

The configuration requirements are as follows:

* The private IPv4 home users' PCs can access the IPv4 Internet through the IPv6 MAN.
* The private IPv4 addresses of home users can be mapped to multiple public IP addresses in many-to-many translation mode.

**Figure 1** Networking diagram of DS-Lite over L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2, and interface 3 in this example represent GE0/2/1, GE0/2/2, and GE0/2/3, respectively.


  
![](figure/en-us_image_0000001420282709.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configuring an L3VPN service.
2. Configure basic license functions.
3. Configure a DS-Lite instance and bind it to a DS-Lite board.
4. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
5. Configure a DS-Lite address pool. The IP addresses in the address pool range from 11.11.11.100 to 11.11.11.110.
6. Configure a traffic policy for the DS-Lite tunnel.
7. Bind the DS-Lite tunnel to the address pool.
8. Configure interfaces and a routing protocol.
9. Enable the device to advertise the local IP route to the IPv6 network and the address pool route to the IPv4 network.

#### Data Preparation

* VPN instance name (vpna)
* DS-Lite instance name (ds-lite1)
* Slot IDs (1 and 2) of DS-Lite boards to which a DS-Lite instance is bound
* Local IP address (2001:DB8::1) and remote IP address (2001:DB8:2::1) of a DS-Lite tunnel
* DS-Lite address pool number (1) and address segment (11.11.11.100 to 11.11.11.110)
* ACL6 rule numbers used in DS-Lite traffic classification and used to be bound to a DS-Lite address pool

#### Procedure

1. Assign an IP address to each interface. For configuration details, see configuration files.
2. Configure an IGP on the IPv4 backbone network to implement interworking between PEs and DS-Lite devices. (For configuration details, see configuration files.)
3. Enable MPLS LDP on PEs and DS-Lite devices and interfaces.
   
   
   
   # Configure the PE.
   
   
   
   ```
   <PE> system-view
   ```
   ```
   [~PE] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE] mpls
   ```
   ```
   [*PE-mpls] quit
   ```
   ```
   [*PE] mpls ldp
   ```
   ```
   [*PE-mpls-ldp] quit
   ```
   ```
   [*PE] interface gigabitEthernet0/2/3
   ```
   ```
   [*PE-GigabitEthernet0/2/3] mpls
   ```
   ```
   [*PE-GigabitEthernet0/2/3] mpls ldp
   ```
   ```
   [*PE-GigabitEthernet0/2/3] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Configure DS-Lite.
   
   ```
   <DS-Lite> system-view
   ```
   ```
   [~DS-Lite] mpls lsr-id 2.2.2.2
   ```
   ```
   [*DS-Lite] mpls
   ```
   ```
   [*DS-Lite-mpls] quit
   ```
   ```
   [*DS-Lite] mpls ldp
   ```
   ```
   [*DS-Lite-mpls-ldp] quit
   ```
   ```
   [*DS-Lite] interface gigabitEthernet0/2/1
   ```
   ```
   [*DS-Lite-GigabitEthernet0/2/1] mpls
   ```
   ```
   [*DS-Lite-GigabitEthernet0/2/1] mpls ldp
   ```
   ```
   [*DS-Lite-GigabitEthernet0/2/1] quit
   ```
   ```
   [*DS-Lite] commit
   ```
4. Configure a VPN instance that supports the IPv6 address family on each PE and bind the PE interface connecting to the CPE to the VPN instance.
   
   
   
   # On the PE, configure an IPv6-address-family-capable VPN instance named **vpna**.
   
   
   
   ```
   [~PE] ip vpn-instance vpna
   ```
   ```
   [*PE-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv6] route-distinguisher 1000:1
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv6] vpn-target 1000: 1 export-extcommunity
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv6] vpn-target 1000: 1 import-extcommunity
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*PE-vpn-instance-vpna] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Bind the PE interface directly connected to the CPE to vpna.
   
   ```
   [~PE] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2 64
   ```
   ```
   [*PE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Configure a VPN instance named **vpna** that supports the IPv6 address family on the DS-Lite device.
   
   ```
   [~DS-Lite] ip vpn-instance vpna
   ```
   ```
   [*DS-Lite-vpn-instance-vpna] ipv6-family
   ```
   ```
   [*DS-Lite-vpn-instance-vpna-af-ipv6] route-distinguisher 1000:1
   ```
   ```
   [*DS-Lite-vpn-instance-vpna-af-ipv6] vpn-target 1000: 1 export-extcommunity
   ```
   ```
   [*DS-Lite-vpn-instance-vpna-af-ipv6] vpn-target 1000: 1 import-extcommunity
   ```
   ```
   [*DS-Lite-vpn-instance-vpna-af-ipv6] quit
   ```
   ```
   [*DS-Lite-vpn-instance-vpna] quit
   ```
   ```
   [*DS-Lite] commit
   ```
5. Establish VPNv6 peer relationships between PEs and DS-Lite devices.
   
   
   
   # Configure the PE.
   
   ```
   [~PE] bgp 65000
   ```
   ```
   [*PE-bgp] peer 3.3.3.3 as-number 65000
   ```
   ```
   [*PE-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE-bgp] peer 2001:db8:3::3 as-number 65000
   ```
   ```
   [*PE-bgp] peer 2001:db8:3::3 connect-interface loopback 1
   ```
   ```
   [*PE-bgp] ipv4-family unicast
   ```
   ```
   [*PE-bgp-af-ipv4] peer 3.3.3.3 enable
   ```
   ```
   [*PE-bgp-af-ipv4] peer 2001:db8:3::3 enable
   ```
   ```
   [*PE-bgp-af-ipv4] import-route direct
   ```
   ```
   [*PE-bgp-af-ipv4] quit
   ```
   ```
   [*PE-bgp] ipv6-family unicast
   ```
   ```
   [*PE-bgp-af-ipv6] import-route direct
   ```
   ```
   [*PE-bgp-af-ipv6] quit
   ```
   ```
   [*PE-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE-bgp-af-vpnv6] peer 3.3.3.3 enable
   ```
   ```
   [*PE-bgp-af-vpnv6] quit
   ```
   ```
   [*PE-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE-bgp-6-vpna] import-route direct
   ```
   ```
   [*PE-bgp] quit
   ```
   ```
   [*PE] commit
   ```
   
   # Configure the DS-Lite device.
   
   ```
   [~DS-Lite] bgp 65000
   ```
   ```
   [*DS-Lite-bgp] peer 1.1.1.1 as-number 65000
   ```
   ```
   [*DS-Lite-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*DS-Lite-bgp] peer 2001:db8:1::1 as-number 65000
   ```
   ```
   [*DS-Lite-bgp] peer 2001:db8:1::1 connect-interface loopback 1
   ```
   ```
   [*DS-Lite-bgp] ipv4-family
   ```
   ```
   [*DS-Lite-bgp-af-ipv4] peer 1.1.1.1 enable
   ```
   ```
   [*DS-Lite-bgp-af-ipv4] peer 2001:db8:1::1 enable
   ```
   ```
   [*DS-Lite-bgp-af-ipv4] import-route direct
   ```
   ```
   [*DS-Lite-bgp-af-ipv4] quit
   ```
   ```
   [*DS-Lite-bgp] ipv6-family unicast
   ```
   ```
   [*DS-Lite-bgp-af-ipv6] import-route direct
   ```
   ```
   [*DS-Lite-bgp-af-ipv6] quit
   ```
   ```
   [*DS-Lite-bgp] ipv6-family vpnv6
   ```
   ```
   [*DS-Lite-bgp-af-vpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*DS-Lite-bgp-af-vpnv6] quit
   ```
   ```
   [*DS-Lite-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*DS-Lite-bgp-6-vpna] import-route direct
   ```
   ```
   [*DS-Lite-bgp-6-vpna] import-route static
   ```
   ```
   [*DS-Lite-bgp] quit
   ```
   ```
   [*DS-Lite] commit
   ```
6. Configure basic license functions.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~DS-Lite] sysname DS-Lite
   ```
   ```
   [*DS-Lite] commit
   ```
   ```
   [~DS-Lite] vsm on-board-mode disable
   ```
   ```
   [*DS-Lite] commit
   ```
   ```
   [~DS-Lite] license
   ```
   ```
   [~DS-Lite-license] active ds-lite vsuf slot 1
   ```
   ```
   [*DS-Lite-license] active ds-lite vsuf slot 2
   ```
   ```
   [*DS-Lite-license] active nat session-table size 16 slot 1 
   ```
   ```
   [*DS-Lite-license] active nat session-table size 16 slot 2 
   ```
   ```
   [*DS-Lite-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*DS-Lite-license] active nat bandwidth-enhance 40 slot 2
   ```
   ```
   [*DS-Lite-license] commit
   ```
   ```
   [~DS-Lite-license] quit
   ```
7. Configure a DS-Lite instance and bind it to a DS-Lite board.
   
   
   ```
   [~DS-Lite] service-location 1
   ```
   ```
   [*DS-Lite-service-location-1] location slot 1  backup slot 2 
   ```
   ```
   [*DS-Lite-service-location-1] commit
   ```
   ```
   [~DS-Lite-service-location-1] quit
   ```
   ```
   [~DS-Lite] service-instance-group 1
   ```
   ```
   [*DS-Lite-instance-group-1] service-location 1
   ```
   ```
   [*DS-Lite-instance-group-1] commit
   ```
   ```
   [~DS-Lite-instance-group-1] quit
   ```
   ```
   [~DS-Lite] ds-lite instance ds-lite1 id 1
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] service-instance-group 1
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] quit
   ```
   ```
   [~DS-Lite-ds-lite-instance-ds-lite1] commit
   ```
8. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
   
   
   ```
   [~DS-Lite] ds-lite instance ds-lite1
   ```
   ```
   [~DS-Lite-ds-lite-instance-ds-lite1] local-ipv6 2001:DB8::1 prefix-length 128
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] remote-ipv6 2001:DB8:2::1 prefix-length 64
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] commit
   ```
   ```
   [~DS-Lite-ds-lite-instance-ds-lite1] quit
   ```
9. Configure a DS-Lite address pool. The IP addresses in the address pool range from 11.11.11.100 to 11.11.11.110.
   
   
   ```
   [~DS-Lite] ds-lite instance ds-lite1
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
   ```
   ```
   [*DS-Lite-ds-lite-instance-ds-lite1] commit
   ```
   ```
   [~DS-Lite-ds-lite-instance-ds-lite1] quit
   ```
10. Reconstruct the local IPv6 route of the DS-Lite instance and specify a public network device as the next hop.
    
    
    ```
    [~DS-Lite] ipv6 route-static vpn-instance vpna 2001:DB8::1 128 loopback
    ```
    ```
    [*DS-Lite] commit
    ```
11. Configure a traffic policy for the DS-Lite tunnel.
    1. Configure IPv6 ACL-based traffic classification rules.
       
       
       ```
       [~DS-Lite] acl ipv6 3500
       ```
       ```
       [*DS-Lite-acl6-basic-3500] rule permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128
       ```
       ```
       [*DS-Lite-acl6-basic-3500] commit
       ```
       ```
       [~DS-Lite-acl6-basic-3500] quit
       ```
    2. Configure a traffic classifier.
       
       
       ```
       [~DS-Lite] traffic classifier c1
       ```
       ```
       [*DS-Lite-classifier-c1] if-match ipv6 acl 3500
       ```
       ```
       [*DS-Lite-classifier-c1] commit
       ```
       ```
       [~DS-Lite-classifier-c1] quit
       ```
    3. Configure a traffic behavior and bind it to the DS-Lite instance named **ds-lite1**.
       
       
       ```
       [~DS-Lite] traffic behavior b1 
       ```
       ```
       [*DS-Lite-behavior-b1] ds-lite bind instance ds-lite1
       ```
       ```
       [*DS-Lite-behavior-b1] commit
       ```
       ```
       [~DS-Lite-behavior-b1] quit
       ```
    4. Configure a DS-Lite traffic policy and associate the rule with the behavior.
       
       
       ```
       [~DS-Lite] traffic policy p1
       ```
       ```
       [*DS-Lite-trafficpolicy-p1] classifier c1 behavior b1
       ```
       ```
       [*DS-Lite-trafficpolicy-p1] commit
       ```
       ```
       [~DS-Lite-trafficpolicy-p1] quit
       ```
    5. Bind the traffic diversion policy to the VPN instance.
       
       
       ```
       [~DS-Lite] ip vpn-instance vpna
       ```
       ```
       [~DS-Lite-vpn-instance-vpna] traffic-policy p1 network inbound
       ```
       ```
       [*DS-Lite-vpn-instance-vpna] commit
       ```
       ```
       [~DS-Lite-vpn-instance-vpna] quit
       ```
    6. Bind the VPN instance to GE0/2/1.
       
       
       ```
       [~DS-Lite] interface GigabitEthernet 0/2/1
       ```
       ```
       [~DS-Lite-GigabitEthernet0/2/1] ip binding vpn-instance vpna
       ```
       ```
       [*DS-Lite-GigabitEthernet0/2/1] commit
       ```
       ```
       [~DS-Lite-GigabitEthernet0/2/1] quit
       ```
12. Bind the DS-Lite tunnel to the address pool.
    1. Configure the IPv6 ACL-based traffic classification rule and use the address pool named **group1** to translate the source addresses in the range of 2001:DB8:2::1/64 in tunnel packets.
       
       
       ```
       [~DS-Lite] acl ipv6 3000
       ```
       ```
       [*DS-Lite-acl6-adv-3000] rule permit ipv6 source 2001:DB8:2::1 64
       ```
       ```
       [*DS-Lite-acl6-adv-3000] commit
       ```
       ```
       [~DS-Lite-acl6-adv-3000] quit
       ```
    2. Associate the ACL rule with the DS-Lite address pool. In the DS-Lite instance named **ds-lite1**, bind the IPv6 ACL numbered 3000 to the address pool named **group1**.
       
       
       ```
       [~DS-Lite] ds-lite instance ds-lite1
       ```
       ```
       [~DS-Lite-ds-lite-instance-ds-lite1] ds-lite outbound 3000 address-group group1
       ```
       ```
       [*DS-Lite-ds-lite-instance-ds-lite1] commit
       ```
       ```
       [~DS-Lite-ds-lite-instance-ds-lite1] quit
       ```
13. Verify the configuration.
    
    
    
    # After the configuration is complete, the DS-Lite device can establish connections with other devices. The CPE has a local IP address and a route to the address pool.
    
    ```
    [~DS-Lite] display ipv6 routing-table 2001:DB8::1
    ```
    ```
    Routing Table : Public
    Summary Count : 1
     Destination  : 2001:DB8::1                         PrefixLength : 128
     NextHop      : FE80::218:82FF:FE84:CCF             Preference   : 15
     Cost         : 10                                  Protocol     : Unr
     RelayNextHop : ::                                  TunnelID     : 0x0
     Interface    : InLoopBack1                         Flags        : D   
    ```

#### Configuration Files

Configuration file of the PE.

```
#                                                                               
 sysname PE
#
isis 1
 is-level level-2
 network-entity 10.0000.0000.0001.00
 traffic-eng level-2
 #
 ipv6 enable topology ipv6
 #
#
interface LoopBack1
 ipv6 enable
 ip address 1.1.1.1 255.255.255.255
 ipv6 address 2001:DB8:1::1/128
 isis enable 1
 isis ipv6 enable 1
#
mpls lsr-id 1.1.1.1
#
mpls
#
mpls ldp
 #
 ipv4-family
#
interface GigabitEthernet0/2/3
 undo shutdown
 ipv6 enable
 ip address 10.1.1.1 255.255.255.0
 ipv6 address 2001:DB8:10::1/64
 isis enable 1
 isis ipv6 enable 1
 mpls
 mpls ldp
 undo dcn
#
ip vpn-instance vpna
 ipv4-family
  route-distinguisher 1000:1
  apply-label per-instance
  vpn-target 1000:1 export-extcommunity
  vpn-target 1000:1 import-extcommunity
 ipv6-family
  route-distinguisher 1000:1
  apply-label per-instance
  vpn-target 1000:1 export-extcommunity
  vpn-target 1000:1 import-extcommunity
#
interface gigabitethernet 0/1/0
ip binding vpn-instance vpna
ipv6 enable
ipv6 address 2001:db8:1::2 64
#
bgp 65000
 router-id 1.1.1.1
 private-4-byte-as enable
 peer 3.3.3.3 as-number 65000
 peer 3.3.3.3 connect-interface LoopBack1
 peer 2001:DB8:3::3 as-number 65000
 peer 2001:DB8:3::3 connect-interface LoopBack1
 #
 ipv4-family unicast
  undo synchronization
  import-route direct
  peer 3.3.3.3 enable
  peer 2001:DB8:3::3 enable
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
 #
 ipv6-family vpnv6
  policy vpn-target
  peer 3.3.3.3 enable
 #
 ipv6-family vpn-instance vpna
  import-route direct
#
```

DS-Lite device configuration file

```
#                                                                               
 sysname DS-Lite  
#
isis 1
 is-level level-2
 network-entity 10.0000.0000.0002.00
 traffic-eng level-2
 #
 ipv6 enable topology ipv6
 #
#
interface LoopBack1
 ipv6 enable
 ip address 3.3.3.3 255.255.255.255
 ipv6 address 2001:DB8:3::3/128
 isis enable 1
 isis ipv6 enable 1
#
mpls lsr-id 3.3.3.3
#
mpls
#
mpls ldp
 #
 ipv4-family
#
interface GigabitEthernet0/2/1
 undo shutdown
 ipv6 enable
 ip address 10.1.1.2 255.255.255.0
 ipv6 address 2001:DB8:10::2/64
 isis enable 1
 isis ipv6 enable 1
 mpls
 mpls ldp
 undo dcn
#
ip vpn-instance vpna
 ipv4-family
  route-distinguisher 1000:1
  apply-label per-instance
  vpn-target 1000:1 export-extcommunity
  vpn-target 1000:1 import-extcommunity
 ipv6-family
  route-distinguisher 1000:1
  apply-label per-instance
  vpn-target 1000:1 export-extcommunity
  vpn-target 1000:1 import-extcommunity
#
bgp 65000
 router-id 3.3.3.3
 private-4-byte-as enable
 peer 1.1.1.1 as-number 65000
 peer 2001:DB8:1::1 as-number 65000
 #
 ipv4-family unicast
  undo synchronization
  import-route direct
  peer 1.1.1.1 enable
  peer 2001:DB8:1::1 enable
 #
 ipv6-family unicast
  undo synchronization
  import-route direct
  peer 2001:DB8:1::1 enable
 #
 ipv6-family vpnv6
  policy vpn-target
  peer 1.1.1.1 enable
 #
 ipv6-family vpn-instance vpna
  import-route direct
  import-route static
#
vsm on-board-mode disable
#
license
 active ds-lite vsuf slot 1
 active ds-lite vsuf slot 2
 active nat session-table size 16 slot 1 
 active nat session-table size 16 slot 2 
 active nat bandwidth-enhance 40 slot 1
 active nat bandwidth-enhance 40 slot 2
#
service-location 1
 location slot 1  backup slot 2 
#
service-instance-group 1
 service-location 1
#     
ds-lite instance ds-lite1 id 1
 service-instance-group 1
 ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
 ds-lite outbound 3000 address-group group1
 local-ipv6 2001:DB8::1  prefix-length 128
 remote-ipv6 2001:DB8:2::1  prefix-length 64
#   
acl ipv6 number 3500                                                            
 rule 5 permit ipv6 source 2001:DB8:2::1 64 destination 2001:DB8::1 128  
#                                                                               
acl ipv6 number 3000                                                            
 rule 0 permit ipv6 source 2001:DB8:2::1/64                                           
#         
traffic classifier c1 operator or  
 if-match ipv6 acl 3500 precedence 1
#                                                                               
traffic behavior b1
 ds-lite bind instance ds-lite1                                                             
#    
traffic policy p1                                                               
 share-mode  
 classifier c1 behavior b1 precedence 1
#                                                                               
isis 100  
 network-entity 10.1000.1000.1000.00                                                                     
 import-route unr   
#                                                                               
isis 1000                                                                       
 network-entity 10.0000.0000.0002.000                                            
 #                                                                              
 ipv6 enable topology ipv6                                                  
 ipv6 import-route unr                                                          
 #                                                                              
#                                                                                
interface GigabitEthernet0/2/1                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                                                             
 ipv6 address 2001:DB8:1::2:1/64 
 traffic-policy p1 inbound
 isis ipv6 enable 1000 
# 
interface GigabitEthernet0/2/2                                                  
 undo shutdown    
 ip address 192.168.10.2 255.255.255.0 
 isis enable 100    
#    
return
```