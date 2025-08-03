Example for Configuring Rate Limiting for PPPoEv4 Access Users
==============================================================

This section provides an example for configuring rate limiting for PPPoEv4 access users.

#### Networking Requirements

Configure rate limiting for PPPoEv4 access users on the network, as shown in [Figure 1](#EN-US_TASK_0172374150__fig_dc_vrp_pppoe_cfg_001301), that has the following requirements:

* The users belong to the domain **isp1** and use PPPoEoVLAN to go online through GE 0/1/2.1 on the Router. The LAN switch marks the priorities of user packets with VLAN 1 and VLAN 2.
* RADIUS authentication and accounting are used.
* The IP address of the RADIUS server is 192.168.7.249. The authentication and accounting port numbers are 1645 and 1646, respectively. RADIUS+1.1 is used, with the key being **YsHsjx\_202206**.
* The IP address of the DNS server is 192.168.7.252.
* The network-side interface is GE 0/1/1.

**Figure 1** Configuring rate limiting for PPPoEv4 access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2.1, respectively.


  
![](../vrp/images/fig_dc_vrp_pppoe_cfg_001301.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a virtual template.
2. Configure AAA schemes.
3. Configure a RADIUS server group.
4. Configure an IPv4 address pool.
5. Configure a domain.
6. Configure a user VLAN on the sub-interface and bind the virtual template to it.
7. Configure a BAS interface.
8. Configure rate limiting for PPPoEv4 access users.
9. Configure OSPF.
10. Configure a loopback interface.

#### Data Preparation

* Virtual template number
* Authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* DNS server address
* Domain to which users belong
* BAS interface parameters

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
   [~HUAWEI-radius-rd1] radius-server type plus11
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
4. Configure an IPv4 address pool.
   
   
   ```
   [~HUAWEI] ip pool pool1 bas local
   ```
   ```
   [*HUAWEI-ip-pool-pool1] gateway 10.82.0.1 255.255.255.0
   ```
   ```
   [*HUAWEI-ip-pool-pool1] commit
   ```
   ```
   [~HUAWEI-ip-pool-pool1] section 0 10.82.0.2 10.82.0.200
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
5. Configure a domain named **isp1**.
   
   
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
   [*HUAWEI-aaa-domain-isp1] radius-server group rd1
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
6. Configure a user VLAN on the sub-interface and bind the virtual template to it.
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] user-vlan 1 2
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-vlan-1-2] quit
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] pppoe-server bind virtual-template 1
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1] commit
   ```
7. Configure a BAS interface.
   
   
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] access-type layer2-subscriber
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
   
   In this example, users go online with the domain name **isp1** carried in usernames. Therefore, the BAS interface does not need to have any authentication domain configured. If users go online with no domain name carried in the usernames, you must specify an authentication domain on the BAS interface.
8. Configure rate limiting for PPPoEv4 access users.
   
   
   ```
   [~HUAWEI] qos-profile p1
   ```
   ```
   [*HUAWEI-qos-profile-p1] car cir 1024 cbs 1024000 green pass red discard
   ```
   ```
   [*HUAWEI-qos-profile-p1] commit
   ```
   ```
   [~HUAWEI-qos-profile-p1] quit
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/2.1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] qos-profile none inbound identifier none 
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] qos-profile none outbound identifier none 
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/2.1-bas] commit 
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/2.1-bas] quit 
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In this example, an empty QoS profile needs to be configured on a BAS interface, and the RADIUS server needs to deliver the No. 17 RADIUS attribute to the QoS profile for PPPoE home users. You can run the **display access-user domain isp1 verbose** command to view detailed user information. The command output shows that the No. 17 RADIUS attribute has taken effect.
   * The QoS profile for common PPPoE users is delivered using No. 31 RADIUS attribute, and no QoS profile needs to be configured on a BAS interface.
9. Configure OSPF.
   
   
   ```
   [~HUAWEI] ospf 1
   ```
   ```
   [*HUAWEI-ospf-1] import-route unr
   ```
   ```
   [*HUAWEI-ospf-1] area 0.0.0.0
   ```
   ```
   [*HUAWEI-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*HUAWEI-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~HUAWEI-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~HUAWEI-ospf-1] quit
   ```
10. Configure a loopback interface.
    
    
    ```
    [~HUAWEI] interface loopback1
    ```
    ```
    [*HUAWEI-LoopBack1] ip address 10.1.2.2 255.255.255.255
    ```
    ```
    [*HUAWEI-LoopBack1] ospf enable 1 area 0.0.0.0
    ```
    ```
    [*HUAWEI-LoopBack1] commit
    ```
    ```
    [~HUAWEI-LoopBack1] quit
    ```
    ```
    [~HUAWEI] quit
    ```
11. Verify the configuration.
    
    
    
    # Check information about the address pool named **pool1**. The command output shows that the gateway address is 10.82.0.1, the addresses in the pool range from 10.82.0.2 to 10.82.0.200, and the DNS server address is 192.168.7.252.
    
    ```
    <HUAWEI> display ip pool name pool1
    ```
    ```
      Pool-Name      : pool1
      Pool-No        : 0  Pool-constant-index :- 
      Lease          : 3 Days 0 Hours 0 Minutes
      NetBios Type   : N-Node
      DNS-Suffix     : -
    
      DNS1         :192.168.7.252
      Position       : Local           Status           : Unlocked
      Gateway        : 10.82.0.1       Mask             : 255.255.0.0
      Vpn instance   : --
      Profile-Name   : -               Server-Name      : -
      Codes: CFLCT(conflicted)
      ------------------------------------------------------------------------------------
      ID           start             end          total   used  idle CFLCT disable reserved
      ------------------------------------------------------------------------------------
       0           10.82.0.2         10.82.0.200   199     0    98     0       0        0
      ------------------------------------------------------------------------------------ 
    ```
    
    # Check information about the domain named **isp1**. The command output shows that the address pool named **pool1** is bound to the domain **isp1**.
    
    ```
    <HUAWEI> display domain isp1
    ```
    ```
    ------------------------------------------------------------------------------
      Domain-name                     : isp1
      Domain-state                    : Active
      Authentication-scheme-name      : auth1
      Accounting-scheme-name          : acct1
      Authorization-scheme-name       :
      Primary-DNS-IP-address          : -
      Second-DNS-IP-address           : -
      Web-server-URL-parameter        : No
      Slave Web-IP-address            : -
      Slave Web-URL                   : -
      Slave Web-auth-server           : - 
      Slave Web-auth-state            : - 
      Portal-server-URL-parameter     : No
      Primary-NBNS-IP-address         : -
      Second-NBNS-IP-address          : -
      User-group-name                 : -
      Idle-data-attribute (time,flow) : 0, 60
      Install-BOD-Count               : 0
      Report-VSM-User-Count           : 0
      Value-added-service             : default
      User-access-limit               : 279552
      Online-number                   : 0
      Web-IP-address                  : -
      Web-URL                         : -
      Portal-server-IP                : -
      Portal-URL                      : -
      Portal-force-times              : 2
      PPPoE-user-URL                  : Disable
      IPUser-ReAuth-Time(second)      : 300
      mscg-name-portal-key            : -
      Portal-user-first-url-key       : -
      Ancp auto qos adapt             : Disable
      Service-type                    : STB
      RADIUS-server-template          : rd5
      Two-acct-template               : -
      HWTACACS-server-template        : -
      Bill Flow                       : Disable
      Tunnel-acct-2867                : Disabled
    
      Flow Statistic:
      Flow-Statistic-Up               : Yes
      Flow-Statistic-Down             : Yes
      Source-IP-route                 : Disable
      IP-warning-threshold            : -
      IPv6-warning-threshold          : - 
      Multicast Forwarding            : Yes
      Multicast Virtual               : No
      Max-multilist num               : 4
      Multicast-profile               : -
      Multicast-profile ipv6          : -
      IP-address-pool-name            : pool1
      Quota-out                     : Offline
      Service-type                    : -
      User-basic-service-ip-type      : -/-/-
      PPP-ipv6-address-protocol       : Ndra
      IPv6-information-protocol       : Stateless dhcpv6
      IPv6-PPP-assign-interfaceid     : Disable
      Trigger-packet-wait-delay       : 60s
      Peer-backup                     : enable    
      ------------------------------------------------------------------------------
    
    ```
    
    # Check detailed information about access users in the domain **isp1**.
    
    ```
    <HUAWEI> display access-user domain isp1 verbose
    ```
    ```
    ------------------------------------------------------------------------------
    Basic:                                                                                                                              
      User access index             : 8192                                                                                              
      State                         : Used                                                                                              
      User name                     : ceshi9                                                                                            
      Domain name                   : isp1                                                                                       
      User backup state             : No                                                                                                
      RUI user state                : -                                                                                                 
      User access interface         : GigabitEthernet0/1/2.1                                                                           
      User access PeVlan/CeVlan     : 2004/-                                                                                            
      User access slot              : 0                                                                                                 
      User MAC                      : 00e0-fc12-3456                                                                                    
      User IP address               : 10.82.0.166                                                                                   
      User IP netmask               : 255.255.255.255                                                                                   
      User gateway address          : 10.82.0.1                                                                                    
      User Primary-DNS              : 192.168.168.6                                                                                      
      User Secondary-DNS            : 192.168.168.7                                                                                      
      User Authen IP Type           : ipv4/-/-                                                                                          
      User Basic IP Type            : -/-/-                                                                                             
      User access type              : PPPoE                                                                                             
      User authentication type      : PPP authentication                                                                                
      Agent-Circuit-Id              : -                                                                                                 
      Agent-Remote-Id               : -                                                                                                 
      Access-line-id Information(pppoe+): -                                                                                             
      Access start time             : 2018-01-10 11:24:52                                                                               
      User-Group                    : -                                                                                                 
      Next-hop                      : -                                                                                                 
      Policy-route-IPV6-address     : -                                                                                                 
                                                                                                                                        
    AAA:                                                                                                                                
      RADIUS-server-template        : rd1                                                                                             
      Server-template of second acct: -                                                                                                 
      Current authen method         : RADIUS authentication                                                                             
      Authen result                 : Success                                                                                           
      Current author method         : Idle                                                                                              
      Author result                 : Success                                                                                           
      Action flag                   : Idle                                                                                              
      Authen state                  : Authed                                                                                            
      Author state                  : Idle                                                                                              
      Configured accounting method  : RADIUS accounting                                                                                     
      Quota-out                     : Offline                                                                                           
      Current accounting method     : RADIUS accounting                                                                                     
      Realtime-accounting-switch            : Close                                                                                     
      Realtime-accounting-interval(sec)     : -                                                                                         
      Realtime-accounting-send-update       : No                                                                                        
      Realtime-accounting-traffic-update    : No                                                                                        
      Accounting start time         : 2018-01-10 11:24:52                                                                               
      Online time (h:min:sec)       : 00:00:02                                                                                          
      Accounting state              : Ready                                                                                             
      MTU                           : 1280                                                                                              
      MRU                           : 1280                                                                                              
      Session time limit            : 86400 second(Radius)                                                                              
      Time remained(s)              : 86398(s)                                                                                          
      Idle-cut direction            : Both                                                                                              
      Idle-cut-data (time,rate,idle): 14400 sec, 60 kbyte/min, 0 min 0 sec(Radius)                                                      
      Ipv4 Realtime speed           : 104 kbyte/min                                                                                     
      Ipv4 Realtime speed inbound   : 104 kbyte/min                                                                                     
      Ipv4 Realtime speed outbound  : 0 kbyte/min                                                                                       
                                                                                                                                        
    Dot1X:                                                                                                                              
      User MSIDSN name              : -                                                                                                 
      EAP user                      : No                                                                                                
      MD5 end                       : No                                                                                                
                                                                                                                                        
    VPN&Policy-route:                                                                                                                   
      Vpn-Instance                  : -                                                                                                 
                                                                                                                                        
    Multicast Service:                                                                                                                  
      Multicast-profile             : -                                                                                                 
      Multicast-profile-ipv6        : -                                                                                                 
      Max Multicast List Number     : 4                                                                                                 
      IGMP enable                   : Yes                                                                                               
                                                                                                                                        
    ACL&QoS:                                                                                                                            
      Inbound Family-profile-name   : p1(Radius)
      Outbound Family-profile-name  : p1(Radius)
      Inbound family qos configuration     : User-CAR                                                                                
      Inbound cir                   : 1024(kbps)                                                                                        
      Inbound pir                   : 0(kbps)                                                                                           
      Inbound cbs                   : 1024000(bytes)                                                                                    
      Inbound pbs                   : 0(bytes)                                                                                          
      Outbound family qos configuration    : User-CAR                                                                                   
      Outbound cir                  : 1024(kbps)                                                                                        
      Outbound pir                  : 0(kbps)                                                                                           
      Outbound cbs                  : 1024000(bytes)                                                                                    
      Outbound pbs                  : 0(bytes)                                                                                          
      Inbound qos configuration     : User-CAR                                                                                          
      Inbound cir                   : 15729(kbps)(Radius)                                                                               
      Inbound pir                   : 0(kbps)                                                                                           
      Inbound cbs                   : 2941323(bytes)                                                                                    
      Inbound pbs                   : 0(bytes)                                                                                          
      Outbound qos configuration    : User-CAR                                                                                          
      Outbound cir                  : 15729(kbps)(Radius)                                                                               
      Outbound pir                  : 0(kbps)                                                                                           
      Outbound cbs                  : 2941323(bytes)                                                                                    
      Outbound pbs                  : 0(bytes)                                                                                          
      Link bandwidth auto adapt     : Disable                                                                                           
      UpPriority                    : Unchangeable                                                                                      
      DownPriority                  : Unchangeable                                                                                      
                                                                                                                                        
    Flow Statistic:                                                                                                                     
      If flow info contain l2-head  : Yes                                                                                               
      Flow-Statistic-Up             : Yes                                                                                               
      Flow-Statistic-Down           : Yes                                                                                               
      Up packets number(high,low)   : (0,17)                                                                                            
      Up bytes number(high,low)     : (0,2320)                                                                                          
      Down packets number(high,low) : (0,9)                                                                                             
      Down bytes number(high,low)   : (0,2909)                                                                                          
      IPV6 Up packets number(high,low)     : (0,0)                                                                                      
      IPV6 Up bytes number(high,low)       : (0,0)                                                                                      
      IPV6 Down packets number(high,low)   : (0,0)                                                                                      
      IPV6 Down bytes number(high,low)     : (0,0)                                                                                      
                                                                                                                                        
    Dslam information :                                                                                                                 
      Circuit ID                       :-                                                                                               
      Remote ID                        :-                                                                                               
      Actual datarate upstream         :0(Kbps)                                                                                         
      Actual datarate downstream       :0(Kbps)                                                                                         
      Min datarate upstream            :0(Kbps)                                                                                         
      Min datarate downstream          :0(Kbps)                                                                                         
      Attainable datarate upstream     :0(Kbps)                                                                                         
      Attainable datarate downstream   :0(Kbps)                                                                                         
      Max datarate upstream            :0(Kbps)                                                                                         
      Max datarate downstream          :0(Kbps)                                                                                         
      Min lowpower datarate upstream   :0(Kbps)                                                                                         
      Min lowpower datarate downstream :0(Kbps)                                                                                         
      Max delay upstream               :0(s)                                                                                            
      Max delay downstream             :0(s)                                                                                            
      Actual delay upstream            :0(s)                                                                                            
      Actual delay downstream          :0(s)                                                                                            
      Access loop encapsulation        :0x000000    
    
    ```

#### Configuration Files

```
#
sysname HUAWEI
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
 radius-server type plus11
#
interface Virtual-Template1
 ppp authentication-mode chap
#
interface GigabitEthernet0/1/2
#
interface GigabitEthernet0/1/2.1
 pppoe-server bind Virtual-Template 1
 user-vlan 1 2
 bas
  access-type layer2-subscriber
  qos-profile none inbound identifier none
  qos-profile none outbound identifier none
#
qos-profile none
#
qos-profile p1
car cir 1024 cbs 1024000 green pass red discard
#
interface GigabitEthernet0/1/1
 ip address 192.168.7.1 255.255.255.0
#
ospf 1
 import-route unr
 area 0.0.0.0
  network 10.1.2.0 0.0.0.255
#
interface LoopBack1
 ip address 10.1.2.2 255.255.255.255
 ospf enable 1 area 0.0.0.0
#
ip pool pool1 bas local
 gateway 10.82.0.1 255.255.255.0
 section 0 10.82.0.2 10.82.0.200
 dns-server 192.168.7.252
#
aaa
 #
 authentication-scheme auth1
 #
 accounting-scheme acct1
 #
 domain default0
 #
 domain default1
 #
 domain default_admin
 #
 domain isp1
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ip-pool pool1
#
return
```