Example for Enabling BGP Route Forwarding Between a CPE and a BRAS in a PPPoE Access Scenario
=============================================================================================

This section provides an example for enabling BGP route forwarding between a CPE and a BRAS. After obtaining an IP address from the BRAS through PPPoE dialup, the CPE uses the IP address to establish a BGP peer relationship with the BRAS, so that traffic between hosts attached to the CPE and the BRAS can be forwarded through BGP routes.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172374153__fig_dc_ne_pppox_cfg_0287), the user belongs to the domain **isp1** and accesses the network through GE 0/1/2.1 of the Router in PPPoE mode. RADIUS authentication and RADIUS accounting are configured on the BRAS. The CPE obtains an IPv4 address from the BRAS after passing the authentication. In this example, the obtained IP address 172.16.0.151 is delivered by the RADIUS server through the Framed-IP-Address attribute. By default, traffic cannot be forwarded through BGP routes after the CPE establishes a BGP peer relationship with the BRAS using the obtained IP address. In this case, enable BGP route forwarding on the BRAS to allow BGP-based traffic forwarding between the BRAS and hosts attached to the CPE or other IP addresses on the CPE.

**Figure 1** Enabling BGP route forwarding between a CPE and a BRAS in a PPPoE access scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2.1, respectively.


  
![](images/fig_dc_ne_pppox_cfg_0287.png "Click to enlarge")

#### Configuration Roadmap

1. Configure a virtual template.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure an IPv4 address pool.
5. Configure a domain.
6. Configure interfaces.
7. Enable BGP route forwarding between a CPE and a BRAS.
8. Establish a BGP peer relationship.
9. Check BGP peer information.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and server address
* DNS server address
* Domain to which users belong
* BAS interface parameters and network-side interface parameters
* Number of the AS in which the CPE is located

#### Procedure

1. Configure a virtual template.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface virtual-template 1
   ```
   ```
   [*HUAWEI-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*HUAWEI-Virtual-Template1] commit
   ```
   ```
   [~HUAWEI-Virtual-Template1] quit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-auth1] commit
   ```
   ```
   [~HUAWEI-aaa-authen-auth1] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~HUAWEI-aaa] accounting-scheme acct1
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*HUAWEI-aaa-accounting-acct1] commit
   ```
   ```
   [~HUAWEI-aaa-accounting-acct1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
3. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group rd1
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server authentication 192.168.7.249 1645
   ```
   ```
   [*HUAWEI-radius-rd1] radius-server accounting 192.168.7.249 1646
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] radius-server shared-key-cipher YsHsjx_202206 
   ```
   ```
   [*HUAWEI-radius-rd1] commit
   ```
   ```
   [~HUAWEI-radius-rd1] quit 
   ```
4. Configure an address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 172.16.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 172.16.0.2 172.16.0.200
   ```
   ```
   [~HUAWEI-ip-pool-pool1] dns-server 192.168.7.252
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] quit
   ```
5. Configure a user access domain named **isp1**.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] domain isp1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] authentication-scheme auth1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] accounting-scheme acct1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] radius-server group rd1
   ```
   ```
   [*HUAWEI-aaa-domain-isp1] commit
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [~HUAWEI-aaa-domain-isp1] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
6. Configure interfaces.
   1. Bind a sub-interface to the virtual template.
      
      
      ```
      [~HUAWEI] interface gigabitethernet 0/1/2.1
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] statistic enable
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1] commit
      ```
   2. Configure a BAS interface.
      
      
      ```
      [*HUAWEI-Virtual-Ethernet0/1/2.1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] bas
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber default-domain authentication isp1 
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] authentication-method ppp
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/2.1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In this example, the user goes online using a username carrying the domain name **isp1**. Therefore, you do not need to bind the BAS interface to an authentication domain. If the user goes online using a username without a domain name, you must bind the BAS interface to an authentication domain.
   3. Configure a network-side interface on the BRAS.
      
      
      ```
      [~HUAWEI] interface gigabitethernet 0/1/1
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] ip address 192.168.7.1 255.255.255.0
      ```
      ```
      [*HUAWEI-GigabitEthernet0/1/1] commit
      ```
      ```
      [~HUAWEI-GigabitEthernet0/1/1] quit
      ```
   4. Configure loopback interface 100 as the source interface for sending BGP packets.
      
      
      ```
      [~HUAWEI] interface LoopBack100
      ```
      ```
      [~HUAWEI-LoopBack100] ip address 10.1.1.1 255.255.255.0
      ```
      ```
      [*HUAWEI-LoopBack100] commit
      ```
      ```
      [~HUAWEI-LoopBack100] quit
      ```
7. Enable BGP route forwarding between the CPE and the BRAS.
   
   
   ```
   [~HUAWEI] aaa
   ```
   ```
   [~HUAWEI-aaa] bgp over pppoe enable 
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
8. Establish a BGP peer relationship.
   
   
   ```
   [~HUAWEI] bgp 100
   ```
   ```
   [*HUAWEI-bgp] peer 172.16.0.151 as-number 100 
   ```
   ```
   [*HUAWEI-bgp] peer 172.16.0.151 connect-interface LoopBack100 
   ```
   ```
   [*HUAWEI-bgp] ipv4-family unicast
   ```
   ```
   [*HUAWEI-bgp-af-ipv4] peer 172.16.0.151 enable
   ```
   ```
   [*HUAWEI-bgp-af-ipv4] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the IP address delivered by the RADIUS server to the CPE is used to establish a BGP peer relationship. You can also use an IP address delivered by a non-RADIUS server to establish a BGP peer relationship. However, if the IP address of the user changes, you must use the new IP address of the user to set up a BGP peer relationship.
9. Check the BGP peer information.
   
   
   ```
   <HUAWEI> display bgp peer
   BGP local router ID : 10.1.1.1
   Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1       
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State      Pr
     172.16.0.151    4         100     6844     6858     0 0099h36m       Established 0
   ```

#### Configuration Files

```
#
sysname HUAWEI                                                         
#                                                                               
radius-server group rd1                                                         
 radius-server shared-key-cipher %^%#Q'!i-TMV5&@=QE}g/QK2ouBHee8WB|s|mB%^%
 radius-server authentication 192.168.7.249 1645 weight 0                       
 radius-server accounting 192.168.7.249 1646 weight 0                           
#                                                                               
ip pool pool1 bas local                                                         
 gateway 172.16.0.1 255.255.255.0                                                
 section 0 172.16.0.2 172.16.0.200                                                
 dns-server 192.168.7.252                                                       
#                                                                               
aaa                                                                             
 bgp over pppoe enable                                                          
 #                                                                              
 authentication-scheme auth1                                                    
 accounting-scheme acct1                                                        
 #                                                                              
 domain isp1                                                                    
  authentication-scheme auth1                                                   
  accounting-scheme acct1                                                       
  radius-server group rd1                                                       
  ip-pool pool1                                                                 
#                                                                               
interface Virtual-Template1                                                     
 ppp authentication-mode chap                                                   
#
interface GigabitEthernet0/1/2.1                                                
 statistic enable                                                               
 pppoe-server bind Virtual-Template 1                                           
 bas                                                                            
 access-type layer2-subscriber default-domain authentication isp1
              
#
interface GigabitEthernet0/1/1
 ip address 192.168.7.1 255.255.255.0
#                                                                               
interface LoopBack100                                                           
 ip address 10.1.1.1 255.255.255.0                                              
#                                                                               
bgp 100                                                                         
 peer 172.16.0.151 as-number 100                                               
 peer 172.16.0.151 connect-interface LoopBack100                               
 #                                                                              
 ipv4-family unicast                                                            
  undo synchronization                                                          
  peer 172.16.0.151 enable                                                      
#                                                                               
return                                       
```