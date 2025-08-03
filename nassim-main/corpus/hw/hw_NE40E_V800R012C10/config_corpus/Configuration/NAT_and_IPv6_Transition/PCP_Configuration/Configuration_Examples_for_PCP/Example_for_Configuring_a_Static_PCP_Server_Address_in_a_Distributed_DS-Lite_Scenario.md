Example for Configuring a Static PCP Server Address in a Distributed DS-Lite Scenario
=====================================================================================

This section provides an example for configuring a static PCP server address in a distributed DS-Lite scenario.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172374865__fig_dc_ne_cfg_pcp_0002), a private network IPv4 user traverses an IPv6 network and accesses the IPv4 Internet after a CGN device performs DS-Lite for the user. The CGN device is required to have a static IPv4 PCP server address (10.1.1.1) configured so that private network user can establish a PCP connection.

**Figure 1** PCP server with a static IP address in a distributed DS-Lite scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/2/1 and GE 0/2/2, respectively.


  
![](images/fig_dc_ne_cfg_pcp_0002.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic license functions.
2. Configure a DS-Lite instance and bind it to a DS-Lite board.
3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
4. Configure a DS-Lite address pool with addresses ranging from 11.11.11.100 to 11.11.11.110.
5. Configure a static PCP server in the DS-Lite instance.
6. Configure DS-Lite user information and RADIUS authentication on the BRAS.
7. Configure a traffic diversion policy for the DS-Lite tunnel.
8. Bind the DS-Lite tunnel to the address pool.
9. Configure interfaces and a routing protocol.
10. Enable the DS-Lite device to advertise the local IP route to the IPv6 network and the address pool route to the IPv4 network.


#### Data Preparation

To complete the configuration, you need the following data:

* Name of a DS-Lite instance
* Slot IDs of DS-Lite boards to which a DS-Lite instance is bound
* Local IP address and remote IP address for a DS-Lite tunnel
* DS-Lite address pool number and start and end IP addresses
* Name of a user group bound to a DS-Lite instance
* IPv6 ACL rule number used in DS-Lite traffic classification
* IPv6 ACL rule number used to be bound to a DS-Lite address pool
* Static PCP server address
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The static PCP server address must differ from a physical interface address, loopback interface address, or an address in the address pool of the DS-Lite instance.

#### Procedure

1. Configure basic license functions.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] vsm on-board-mode disable
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] license
   ```
   ```
   [~BRAS-license] active ds-lite vsuf slot 1
   ```
   ```
   [*BRAS-license] active nat session-table size 16 slot 1 
   ```
   ```
   [*BRAS_NAT-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS-license] active pcp vsuf slot 1
   ```
   ```
   [*BRAS-license] commit
   ```
   ```
   [~BRAS-license] quit
   ```
2. Configure a DS-Lite instance and bind it to a DS-Lite board.
   
   
   ```
   [~BRAS] service-location 1
   ```
   ```
   [*BRAS-service-location-1] location slot 1 backup slot 2 
   ```
   ```
   [*BRAS-service-location-1] commit
   ```
   ```
   [~BRAS-service-location-1] quit
   ```
   ```
   [~BRAS] service-instance-group 1
   ```
   ```
   [*BRAS-instance-group-1] service-location 1
   ```
   ```
   [*BRAS-instance-group-1] commit
   ```
   ```
   [~BRAS-instance-group-1] quit
   ```
   ```
   [~BRAS] ds-lite instance ds-lite1 id 1
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] service-instance-group 1
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] commit
   ```
   ```
   [~BRAS-ds-lite-instance-ds-lite1] quit
   ```
3. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
   
   
   ```
   [~BRAS] ds-lite instance ds-lite1
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] local-ipv6 2001:DB8::1 prefix-length 128
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] remote-ipv6 2001:DB8:2::2 prefix-length 96
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] commit
   ```
   ```
   [~BRAS-ds-lite-instance-ds-lite1] quit
   ```
4. Configure a DS-Lite address pool with addresses ranging from 11.11.11.100 to 11.11.11.110.
   
   
   ```
   [~BRAS] ds-lite instance ds-lite1
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
   ```
5. Configure a static PCP server in the DS-Lite instance.
   
   
   ```
   [*BRAS-ds-lite-instance-ds-lite1] pcp server ipv4 10.1.1.1 255.255.255.255
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite1] commit
   ```
   ```
   [~BRAS-ds-lite-instance-ds-lite1] quit
   ```
6. Configure DS-Lite user information.
   1. Configure the BRAS service to enable users to go online. For detailed configurations, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - User Access*.
      
      ![](../../../../public_sys-resources/notice_3.0-en-us.png) In the IPv6 address pool view of a BRAS, the DNS server address and AFTR name must be specified. The AFTR name identifies a DS-Lite server. The following conditions must be met so that the DS-Lite tunnel between the DS-Lite device and CPE can be established:
      * When the BRAS uses the ND mode to assign an IP address to a WAN interface on the CPE, the AFTR name and DNS information must be configured in the PD address pool. Otherwise, the DS-Lite tunnel between the DS-Lite device and CPE cannot be established.
      * After the AFTR name is configured on the BRAS, the mapping between the AFTR name and the local IP address of the DS-Lite instance must be configured on the DNS server. The DS-Lite device advertises its local IP address to the CPE.
   2. Configure a user group.
      
      
      ```
      [~BRAS] user-group group1
      ```
      ```
      [*BRAS] commit
      ```
   3. Specify the domain of users.
      
      
      ```
      [~BRAS] aaa
      ```
      ```
      [*BRAS-aaa] domain isp1 
      ```
      ```
      [*BRAS-aaa-domain-isp1] user-group group1 bind ds-lite instance ds-lite1
      ```
      ```
      [*BRAS-aaa-domain-isp1] quit
      ```
      ```
      [*BRAS-aaa] commit
      ```
      ```
      [~BRAS-aaa] quit
      ```
7. Configure a traffic diversion policy for the DS-Lite tunnel.
   1. Configure IPv6 ACL-based traffic classification rules.
      
      
      ```
      [~BRAS] acl ipv6 6001
      ```
      ```
      [*BRAS-acl6-ucl-6001] rule 1 permit ipv6 source user-group group1 destination ipv6-address 2001:DB8::1 128
      ```
      ```
      [*BRAS-acl6-ucl-6001] commit
      ```
      ```
      [~BRAS-acl6-ucl-6001] quit
      ```
   2. Configure a traffic classifier.
      
      
      ```
      [~BRAS] traffic classifier c1
      ```
      ```
      [*BRAS-classifier-c1] if-match ipv6 acl 6001
      ```
      ```
      [*BRAS-classifier-c1] commit
      ```
      ```
      [~BRAS-classifier-c1] quit
      ```
   3. Configure a traffic behavior and bind the traffic behavior to the DS-Lite instance named **ds-lite1**.
      
      
      ```
      [~BRAS] traffic behavior b1 
      ```
      ```
      [*BRAS-behavior-b1] ds-lite bind instance ds-lite1
      ```
      ```
      [*BRAS-behavior-b1] commit
      ```
      ```
      [~BRAS-behavior-b1] quit
      ```
   4. Configure a DS-Lite traffic diversion policy and associate the IPv6 ACL-based traffic classification rule with the traffic behavior.
      
      
      ```
      [~BRAS] traffic policy p1
      ```
      ```
      [*BRAS-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*BRAS-trafficpolicy-p1] commit
      ```
      ```
      [~BRAS-trafficpolicy-p1] quit
      ```
   5. Apply the DS-Lite traffic diversion policy in the system view.
      
      
      ```
      [~BRAS] traffic-policy p1 inbound
      ```
      ```
      [*BRAS] commit
      ```
8. Bind the DS-Lite tunnel to the address pool.
   1. Configure IPv6 ACL and use the address pool named **group1** to translate the source addresses in the range of 2001:DB8:2::2/96 in tunnel packets.
      
      
      ```
      [~BRAS] acl ipv6 3000
      ```
      ```
      [*BRAS-acl6-adv-3000] rule permit ipv6 source 2001:DB8:2::2 96
      ```
      ```
      [*BRAS-acl6-adv-3000] commit
      ```
      ```
      [~BRAS-acl6-adv-3000] quit
      ```
   2. Associate the ACL rule with the DS-Lite address pool. In the DS-Lite instance named **ds-lite1**, bind the IPv6 ACL numbered 3000 to the address pool named **group1**.
      
      
      ```
      [~BRAS] ds-lite instance ds-lite1
      ```
      ```
      [*BRAS-ds-lite-instance-ds-lite1] ds-lite outbound 3000 address-group group1
      ```
      ```
      [*BRAS-ds-lite-instance-ds-lite1] commit
      ```
      ```
      [~BRAS-ds-lite-instance-ds-lite1] quit
      ```
9. Configure interfaces and a routing protocol.
   1. Configure IS-IS.
      
      
      ```
      [~BRAS] isis 100
      ```
      ```
      [*BRAS-isis-100] network-entity 10.1000.1000.1000.00
      ```
      ```
      [*BRAS-isis-100] commit
      ```
      ```
      [~BRAS-isis-100] quit
      ```
      ```
      [~BRAS] isis 1000
      ```
      ```
      [*BRAS-isis-1000] network-entity 10.1000.1000.1002.00
      ```
      ```
      [*BRAS-isis-1000] ipv6 enable
      ```
      ```
      [*BRAS-isis-1000] commit
      ```
      ```
      [~BRAS-isis-1000] quit
      ```
   2. Configure the DS-Lite device's interface connected to the IPv6 network.
      
      
      ```
      [~BRAS] interface GigabitEthernet0/2/1
      ```
      ```
      [*BRAS-GigabitEthernet0/2/1] ipv6 enable
      ```
      ```
      [*BRAS-GigabitEthernet0/2/1] isis ipv6 enable 1000
      ```
      ```
      [*BRAS-GigabitEthernet0/2/1] commit
      ```
      ```
      [~BRAS-GigabitEthernet0/2/1] quit
      ```
   3. Configure the DS-Lite device's interface connected to the IPv4 network.
      
      
      ```
      [~BRAS] interface GigabitEthernet0/2/2
      ```
      ```
      [~BRAS-GigabitEthernet0/2/2] ip address 1.1.1.1 24
      ```
      ```
      [*BRAS-GigabitEthernet0/2/2] isis enable 100
      ```
      ```
      [*BRAS-GigabitEthernet0/2/2] commit
      ```
      ```
      [~BRAS-GigabitEthernet0/2/2] quit
      ```
10. Enable the DS-Lite device to advertise the local IP route to the IPv6 network and the address pool route to the IPv4 network. Import the local IP route and address pool route to the IS-IS routing table. In this example, UNRs are used as the local IP route and address pool route.
    
    
    ```
    [~BRAS] isis 1000
    ```
    ```
    [~BRAS-isis-1000] ipv6 import-route unr
    ```
    ```
    [*BRAS-isis-1000] commit
    ```
    ```
    [~BRAS-isis-1000] quit
    ```
    ```
    [~BRAS] isis 100
    ```
    ```
    [~BRAS-isis-100] import-route unr
    ```
    ```
    [*BRAS-isis-100] commit
    ```
    ```
    [~BRAS-isis-100] quit
    ```
11. After completing the preceding configurations, run the following command. The command output shows that the DS-Lite device has established IS-IS neighbor relationships with other devices, and the neighbor relationship status is **up**. In addition, the CPE is routable to the local IP address and the addresses in the address pool.
    
    
    ```
    [~BRAS] display ipv6 routing-table 2001:DB8::1
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

#### Configuration File

DS-Lite device configuration file

```
#                                                                               
sysname BRAS  
#
vsm on-board-mode disable
#
license
 active ds-lite vsuf slot 1
 active pcp vsuf slot 1
 active nat session-table size 16 slot 1 
 active nat bandwidth-enhance 40 slot 1
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server type plus11
 radius-server traffic-unit kbyte
#
interface Virtual-Template1
 ppp authentication-mode auto
#
interface GigabitEthernet0/2/1                                                  
 undo shutdown                                                                  
 ipv6 enable                                                                    
 isis ipv6 enable 1000 
# 
interface GigabitEthernet0/2/2                                                  
 undo shutdown                                                                                                                                      
 ip address 1.1.1.1 255.255.255.0 
 isis enable 100    
# 
ipv6 prefix pre1 local
 prefix 2001:DB8:2::/96
#
ipv6 pool pool1 bas local
prefix pre1
dns-server 2001:DB8::1:2      //Configure the IPv6 DNS server address. In a DS-Lite scenario, setting this parameter in the local address pool is recommended. When a BRAS assigns an IP address in ND mode to a WAN interface on the CPE, the AFTR named and DNS information must be configured in the PD address pool. 
aftr-name www.huawei.com         //Configure the AFTR name. The AFTR is DS-Lite server. After the AFTR name is configured on the DS-Lite server, the configuration must be advertised to the CPE. Otherwise, the DS-Lite tunnel between the CPE and DS-Lite server cannot be established. The notification sent by the DNS server contains the mapping between the AFTR name and the local IP address configured in the DS-Lite instance.
#
service-location 1
 location slot 1 backup slot 2 
#
service-instance-group 1
 service-location 1
#                                                                                                                                                                                                                                           
ds-lite instance ds-lite1 id 1
 service-instance-group 1
 ds-lite address-group group1 group-id 1 11.11.11.100 11.11.11.110
 ds-lite outbound 3000 address-group group1
 local-ipv6 2001:DB8::1 prefix-length 128
 remote-ipv6 2001:DB8:2::2 prefix-length 96
 pcp server ipv4 10.1.1.1 255.255.255.255
#                                                                                                                                                           
acl ipv6 6001
 rule 1 permit ipv6 source user-group group1 destination ipv6-address 2001:DB8::1 128
#
acl ipv6 3000
 rule permit ipv6 source 2001:DB8:2::2 96
#                                                                                                                                                             
traffic classifier c1 operator or                                                                                                           
 if-match ipv6 acl 6001 precedence 1                                                                                                        
#                                                                               
traffic behavior b1
 ds-lite bind instance ds-lite1                                                             
#                                                                                                                                                   
traffic policy p1                                                               
 share-mode                                                                                                                                  
 classifier c1 behavior b1 precedence 1                                     
#                                                                               
traffic-policy p1 inbound
#
isis 100  
 network-entity 10.1000.1000.1000.00                                                                     
 import-route unr                                                                                                                                                                                        
#                                                                               
isis 1000                                                                       
 network-entity 10.1000.1000.1002.00                                            
 #                                                                              
 ipv6 enable topology ipv6                                                  
 ipv6 import-route unr                                                          
 #
#
user-group group1
#
aaa
 authentication-scheme auth1
  authentication-mode radius
#
 accounting-scheme acct1
  accounting-mode radius
#
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ipv6-pool pool1
  user-group group1 bind ds-lite instance ds-lite1
#                                                                                                                                                            
return
```