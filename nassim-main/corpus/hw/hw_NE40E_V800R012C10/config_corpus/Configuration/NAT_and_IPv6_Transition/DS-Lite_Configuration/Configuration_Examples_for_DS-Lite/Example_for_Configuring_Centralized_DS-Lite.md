Example for Configuring Centralized DS-Lite
===========================================

This section provides an example for configuring centralized DS-Lite. Centralized DS-Lite allows private IPv4 users to pass through an IPv6 network to access a public IPv4 network.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374755__dc_ne_cfg_dslite_005701), a home user's PC with a private IPv4 address accesses an IPv6 MAN through an IPv4 and IPv6 dual-stack-capable and DS-Lite-capable CPE. The CPE and DS-Lite device establish a DS-Lite tunnel. The CPE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the DS-Lite device. The DS-Lite device decapsulates traffic, uses a Network Address Translation (NAT) technique to translate the private IPv4 address to a public IPv4 address, and forwards traffic to the IPv4 Internet. The DS-Lite device is equipped with DS-Lite boards in slots 1 and 2, respectively. The DS-Lite device's GE 0/2/1 is connected to an IPv6 MAN, and GE 0/2/2 is connected to the Internet. IPv4 home users need to access the IPv4 Internet through the IPv6 MAN. The carrier provides 11 public IPv4 addresses from 11.11.11.100 to 11.11.11.110.

The configuration requirements are as follows:

* The private IPv4 home users' PCs can access the IPv4 Internet through the IPv6 MAN.
* The private IPv4 addresses of home users can be mapped to multiple public IP addresses in many-to-many translation mode.

**Figure 1** Networking diagram for a DS-Lite application![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_ds-lite_cfg_0060.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic license functions.
2. Configure a DS-Lite instance and bind it to a DS-Lite board.
3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
4. Configure a DS-Lite address pool with addresses ranging from 11.11.11.100 to 11.11.11.110.
5. Configure a traffic policy for the DS-Lite tunnel.
6. Bind the DS-Lite tunnel to the address pool.
7. Configure interfaces and a routing protocol.
8. Enable the device to advertise the local IP route to the IPv6 network and the address pool route to the IPv4 network.

#### Data Preparation

* DS-Lite instance name (ds-lite1)
* Slot IDs (1 and 2) of DS-Lite boards to which a DS-Lite instance is bound
* Local IP address (2001:DB8::1) and remote IP address (2001:DB8:2::1) of a DS-Lite tunnel
* DS-Lite address pool number (1) and address segment (11.11.11.100 to 11.11.11.110)
* ACL6 rule numbers used in DS-Lite traffic classification and used to be bound to a DS-Lite address pool

#### Procedure

1. Configure basic license functions.
   
   
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
2. Configure a DS-Lite instance and bind it to a DS-Lite board.
   
   
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
   [*DS-Lite] commit
   ```
3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
   
   
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
4. Configure a DS-Lite address pool with addresses ranging from 11.11.11.100 to 11.11.11.110.
   
   
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
5. Configure a traffic policy for the DS-Lite tunnel.
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
   3. Configure a traffic behavior and bind the traffic behavior to the DS-Lite instance named **ds-lite1**.
      
      
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
   4. Configure a DS-Lite traffic diversion policy and associate the IPv6 ACL-based traffic classification rule with the traffic behavior.
      
      
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
   5. Apply the policy to GE 0/2/1.
      
      
      ```
      [~DS-Lite] interface GigabitEthernet 0/2/1
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/1] traffic-policy p1 inbound
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/1] commit
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/1] quit
      ```
6. Bind the DS-Lite tunnel to the address pool.
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
7. Configure interfaces and a routing protocol.
   1. Configure IS-IS.
      
      
      ```
      [~DS-Lite] isis 100
      ```
      ```
      [*DS-Lite-isis-100] network-entity 10.1000.1000.1000.00
      ```
      ```
      [*DS-Lite-isis-100] commit
      ```
      ```
      [~DS-Lite-isis-100] quit
      ```
      ```
      [~DS-Lite] isis 1000
      ```
      ```
      [*DS-Lite-isis-1000] network-entity 10.1000.1000.1002.00
      ```
      ```
      [*DS-Lite-isis-1000] ipv6 enable
      ```
      ```
      [*DS-Lite-isis-1000] commit
      ```
      ```
      [~DS-Lite-isis-1000] quit
      ```
   2. Configure the DS-Lite device's interface connected to the IPv6 network.
      
      
      ```
      [~DS-Lite] interface GigabitEthernet0/2/1
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/1] ipv6 enable
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/1] ipv6 address 2001:DB8:1::2:1 64
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/1] isis ipv6 enable 1000
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/1] commit
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/1] quit
      ```
      ```
      [~DS-Lite] ipv6 route-static 2001:DB8:2:: 64 2001:DB8:1::2:2
      ```
      ```
      [*DS-Lite] commit
      ```
   3. Configure the DS-Lite device's interface connected to the IPv4 network.
      
      
      ```
      [~DS-Lite] interface GigabitEthernet0/2/2
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/2] ip address 192.168.10.1 24
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/2] isis enable 100
      ```
      ```
      [*DS-Lite-GigabitEthernet0/2/2] commit
      ```
      ```
      [~DS-Lite-GigabitEthernet0/2/2] quit
      ```
8. Enable the device to advertise the local IP route to the IPv6 network and the address pool route to the IPv4 network. Import the local IP route and address pool route to the IS-IS routing table. In this example, UNRs are used as the local IP route and address pool route.
   
   
   ```
   [~DS-Lite] isis 1000
   ```
   ```
   [~DS-Lite-isis-1000] ipv6 import-route unr
   ```
   ```
   [*DS-Lite-isis-1000] commit
   ```
   ```
   [~DS-Lite-isis-1000] quit
   ```
   ```
   [~DS-Lite] isis 100
   ```
   ```
   [~DS-Lite-isis-100] import-route unr
   ```
   ```
   [*DS-Lite-isis-100] commit
   ```
   ```
   [~DS-Lite-isis-100] quit
   ```
9. Verify the configuration.
   
   
   
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
    Interface    : InLoopBack0                         Flags        : D   
   ```
   
   # Display detailed information about users of CPU 0 on the service board in slot 1.
   
   ```
   [~DS-Lite] display nat user-information slot 1  verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ...             
   Slot: 1                                                                
   Total number:  1.                                                               
     ---------------------------------------------------------------------------   
     User Type                             :  DS-Lite                               
     CPE IP                                :  2001:DB8:2::1/128                        
     User ID                               :  -                                    
     VPN Instance                          :  -                                    
     Address Group                         :  group1                                    
     DS-Lite Instance                      :  ds-lite1                                  
     Public IP                             :  11.11.11.101                           
     Start Port                            :  1024                                 
     Port Range                            :  256                                  
     Port Total                            :  256                                  
     Extend Port Alloc Times               :  0                                    
     Extend Port Alloc Number              :  0                                    
     First/Second/Third Extend Port Start  :  0/0/0                                
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512                 
     Total/TCP/UDP/ICMP Session Current    :  0/0/0/0                              
     Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512                 
     Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0                              
     Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0                              
     Total/TCP/UDP/ICMP Port Current       :  0/0/0/0                              
     Nat ALG Enable                        :  NULL                                 
     Token/TB/TP                           :  0/0/0                                
     Port Forwarding Flag                  :  Non Port Forwarding                  
     Port Forwarding Ports                 :  0 0 0 0 0                            
     Aging Time(s)                         :  -                                    
     Left Time(s)                          :  -                                    
     Port Limit Discard Count              :  0                                    
     Session Limit Discard Count           :  0                                    
     Fib Miss Discard Count                :  0                                    
     -->Transmit Packets                   :  0                                    
     -->Transmit Bytes                     :  0                                    
     -->Drop Packets                       :  0                                    
     <--Transmit Packets                   :  0                                    
     <--Transmit Bytes                     :  0                                    
     <--Drop Packets                       :  0                                    
     ---------------------------------------------------------------------------  
   ```

#### Configuration Files

DS-Lite device configuration file

```
#                                                                               
 sysname DS-Lite  
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
 if-match ipv6 acl 3500  precedence 1
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
ipv6 route-static 2001:DB8:2:: 64 2001:DB8:1::2:2    
#    
return
```