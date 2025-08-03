Example for Configuring PPPoEv6 User Access in a 6PE Scenario
=============================================================

This section provides an example for configuring PPPoEv6 user access in a 6PE scenario. The BRAS uses RADIUS authentication and accounting to implement user access.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0204843995__fig16472113232919), an IPv4/MPLS network is deployed between two discontinuous IPv6 networks. 6PE can be deployed to allow the two IPv6 networks to communicate with each other. In 6PE mode, IPv4 and IPv6 dual stacks are implemented on the PEs of an ISP. The labels allocated by MP-BGP are used to identify IPv6 routes, and the LSPs established between the PEs are used to implement IPv6 interworking. An IPv6 user terminal connects to PE1 over CE1. After the IPv6 user initiates a PPPoE connection request, PE1 implements RADIUS authentication and accounting. After the IPv6 user passes the authentication, user packets need to traverse the IPv4/MPLS backbone network to reach the destination IPv6 network. PE1 that functions as a 6PE device converts IPv6 packets into the MPLS packets that can be transmitted on the IPv4 backbone network. The MPLS packets are then forwarded to PE2 that also functions as a 6PE device through LSPs. After receiving the MPLS packets, PE2 removes MPLS labels from the packets, checks the IPv6 routing table, and forwards the packets based on the destination address contained in the restored IPv6 packet header. In this manner, CE1 and CE2 can communicate with each other over an IPv4 network.

**Figure 1** Configuring PPPoEv6 user access in a 6PE scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 4 in this example represent GE 0/1/0, GE 0/2/0, loopback 0, and loopback 1, respectively.


  
![](figure/en-us_image_0207896343.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure user access on PE1.
2. Configure OSPF on PE1 and PE2 so that they can learn the IP address of the loopback interface from each other.
3. Enable MPLS and MPLS LDP on the backbone network and establish an LDP LSP between PE1 and PE2.
4. Establish a 6PE peer relationship between PE1 and PE2.
5. Configure BGP4+ between PE1 and CE1 and between PE2 and CE2 to exchange IPv6 routes.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of the AS where each device resides
* Router ID of each device
* Virtual template number
* RADIUS authentication and accounting schemes and their names
* RADIUS server group name and RADIUS server addresses
* Start ID and end ID of a VLAN range created on a BAS interface
* Local prefix pool name
* Assignable IPv6 prefixes and prefix lengths
* Local address pool name
* Domain name

#### Configuration Procedure

1. Configure user access on PE1.
   1. Configure a virtual template.
      ```
      <HUAWEI> system-view
      [~HUAWEI] sysname PE1
      [*HUAWEI] commit
      [~PE1] interface virtual-template 1
      [*PE1-Virtual-Template1] ppp authentication-mode chap
      [*PE1-Virtual-Template1] quit
      [*PE1] commit
      ```
   2. Configure authentication and accounting schemes.
      ```
      [~PE1] aaa
      [~PE1-aaa] authentication-scheme auth1
      [*PE1-aaa-authen-auth1] authentication-mode radius
      [*PE1-aaa-authen-auth1] quit
      [*PE1-aaa] accounting-scheme auth1
      [*PE1-aaa-accounting-auth1] accounting-mode radius
      [*PE1-aaa-accounting-auth1] quit
      [*PE1-aaa] commit
      [~PE1-aaa] quit
      ```
   3. Configure a RADIUS server group.
      ```
      [~PE1] radius-server group rd1
      [*PE1-radius-rd1] radius-server authentication 192.168.7.249 1645
      [*PE1-radius-rd1] radius-server accounting 192.168.7.249 1646
      [*PE1-radius-rd1] commit
      [~PE1-radius-rd1] radius-server type standard
      [~PE1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
      [*PE1-radius-rd1] commit
      [~PE1-radius-rd1] quit
      ```
   4. Configure a local IPv6 prefix pool.
      ```
      [~PE1] ipv6 prefix pre1 local 
      [*PE1-ipv6-prefix-pre1] prefix 2001:db8:1::1/64
      [*PE1-ipv6-prefix-pre1] commit
      [~PE1-ipv6-prefix-pre1] quit
      ```
   5. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local IPv6 address pool.
      ```
      [~PE1] ipv6 pool pool1 bas local 
      [*PE1-ipv6-pool-pool1] prefix pre1
      [*PE1-ipv6-pool-pool1] dns-server 2001:db8:4::1 
      [*PE1-ipv6-pool-pool1] commit
      [~PE1-ipv6-pool-pool1] quit 
      ```
   6. Configure a domain named **isp1**.
      ```
      [~PE1] aaa
      [~PE1-aaa] domain isp1
      [*PE1-aaa-domain-isp1] authentication-scheme auth1
      [*PE1-aaa-domain-isp1] accounting-scheme acct1
      [*PE1-aaa-domain-isp1] radius-server group rd1
      [*PE1-aaa-domain-isp1] ipv6-pool pool1
      [*PE1-aaa-domain-isp1] commit
      [~PE1-aaa-domain-isp1] quit
      [~PE1-aaa] quit
      ```
   7. Configure interfaces.
      
      # Bind the virtual template to GE 0/1/0.1.
      
      ```
      [~PE1] interface gigabitethernet 0/1/0.1
      [*PE1-GigabitEthernet0/1/0.1] commit
      [~PE1-GigabitEthernet0/1/0.1] pppoe-server bind virtual-template 1
      ```
      
      # Configure a BAS interface.
      
      ```
      [~PE1-GigabitEthernet0/1/0.1] user-vlan 1 100
      [~PE1-GigabitEthernet0/1/0.1-vlan-1-100] quit
      [~PE1-GigabitEthernet0/1/0.1] bas
      [~PE1-GigabitEthernet0/1/0.1-bas] access-type layer2-subscriber default-domain authentication isp1
      [*PE1-GigabitEthernet0/1/0.1-bas] authentication-method-ipv6 ppp
      [*PE1-GigabitEthernet0/1/0.1-bas] commit
      [~PE1-GigabitEthernet0/1/0.1-bas] quit
      ```
      
      # Enable IPv6 on the interface.
      
      ```
      [*PE1-GigabitEthernet0/1/0.1] ipv6 enable
      [*PE1-GigabitEthernet0/1/0.1] ipv6 address auto link-local
      [*PE1-GigabitEthernet0/1/0.1] quit
      [*PE1] commit
      ```
      
      # Configure an upstream interface.
      
      ```
      [~PE1] interface gigabitEthernet 0/2/0
      [*PE1-GigabitEthernet0/2/0] ipv6 enable
      [*PE1-GigabitEthernet0/2/0] ipv6 address auto link-local
      [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:db8:3::1/64 eui-64
      [*PE1] commit
      ```
2. Configure OSPF between PE1 and PE2 so that PE1 and PE2 can learn the routes to each other's loopback interfaces. For configuration details, see Configuration Files.
3. Enable MPLS and MPLS LDP on the backbone network and establish an LDP LSP between PE1 and PE2.
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 2.2.2.2 
   [*PE1] mpls
   [*PE1-mpls] quit
   [*PE1] mpls ldp
   [*PE1-mpls-ldp] quit
   [*PE1] interface gigabitethernet 0/2/0
   [*PE1-GigabitEthernet0/2/0] mpls
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   [*PE1-GigabitEthernet0/2/0] quit
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.3 
   [*PE2] mpls 
   [*PE2] quit 
   [*PE2] mpls ldp 
   [*PE2-mpls-ldp] quit 
   [*PE2] interface gigabitethernet 0/2/0
   [*PE2-GigabitEthernet0/2/0] mpls 
   [*PE2-GigabitEthernet0/2/0] mpls ldp 
   [*PE2-GigabitEthernet0/2/0] quit 
   [*PE2] commit
   ```
   
   After the configuration is complete, run the **display mpls ldp session** command on PE1. The command output shows that an LDP session has been established between PE1 and PE2.
   
   ```
   [~PE1] display mpls ldp session
     LDP Session(s) in Public Network  Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)  
     An asterisk (*) before a session means the session is being deleted.   
   --------------------------------------------------------------------------  
   PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------  
   3.3.3.3:0         Operational DU   Passive  000:00:35     143/199 
   -------------------------------------------------------------------------- 
   TOTAL: 1 Session(s) Found.
   ```
4. Establish a 6PE peer relationship between PE1 and PE2.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 200 
   [*PE1-bgp] peer 3.3.3.3 as-number 200 
   [*PE1-bgp] peer 3.3.3.3 connect-interface LoopBack0 
   [*PE1-bgp] ipv6-family unicast 
   [*PE1-bgp-af-ipv6] import-route direct 
   [*PE1-bgp-af-ipv6] peer 3.3.3.3 enable 
   [*PE1-bgp-af-ipv6] peer 3.3.3.3 label-route-capability 
   [*PE1-bgp-af-ipv6] quit 
   [*PE1-bgp] quit 
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200 
   [*PE2-bgp] peer 2.2.2.2 as-number 200 
   [*PE2-bgp] peer 2.2.2.2 connect-interface LoopBack0 
   [*PE2-bgp] ipv6-family unicast 
   [*PE2-bgp-af-ipv6] import-route direct 
   [*PE2-bgp-af-ipv6] peer 2.2.2.2 enable 
   [*PE2-bgp-af-ipv6] peer 2.2.2.2 label-route-capability 
   [*PE2-bgp-af-ipv6] commit 
   [*PE2-bgp-af-ipv6] quit 
   [*PE2-bgp] quit 
   [*PE2] commit
   ```
   
   # After the configuration is complete, run the **display bgp ipv6 peer** command on PE1. The command output shows that a BGP peer relationship has been established between PE1 and PE2.
   
   ```
   [~PE1] display bgp ipv6 peer
     BGP local router ID : 2.2.2.2  
     Local AS number : 200  Total number of peers : 2                 Peers in established state : 2 
     Peer            V          AS  MsgRcvd     MsgSent  OutQ  Up/Down      State     PrefRcv
     3.3.3.3         4         200     1248     1342      0 18:06:28    Established      1
   ```
5. Configure BGP4+ between PE1 and CE1 and between PE2 and CE2 to exchange IPv6 routes.
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 100 
   [*CE1-bgp] router-id 5.5.5.5 
   [*CE1-bgp] peer 2001:db8:1::2 as-number 200 
   [*CE1-bgp] ipv6-family unicast 
   [*CE1-bgp-af-ipv6] peer 2001:db8:1::2 enable 
   [*CE1-bgp-af-ipv6] network 2001:db8:5::5 128 
   [*CE1-bgp-af-ipv6] commit 
   [~CE1-bgp-af-ipv6] quit 
   [~CE1-bgp] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 200 
   [*PE1-bgp] peer 2001:db8:1::1 as-number 100 
   [*PE1-bgp] ipv6-family unicast 
   [*PE1-bgp-af-ipv6] peer 2001:db8:1::1 enable 
   [*PE1-bgp-af-ipv6] commit 
   [*PE1-bgp-af-ipv6] quit 
   [*PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   [*PE2-bgp] peer 2001:db8:2::1 as-number 300
   [*PE2-bgp] ipv6-family unicast
   [*PE2-bgp-af-ipv6] peer 2001:db8:2::1 enable
   [*PE2-bgp-af-ipv6] commit
   [~PE2-bgp-af-ipv6] quit
   [~PE2-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] bgp 300
   [*CE2-bgp] router-id 6.6.6.6
   [*CE2-bgp] peer 2001:db8:2::2 as-number 200
   [*CE2-bgp] ipv6-family unicast
   [*CE2-bgp-af-ipv6] peer 2001:db8:2::2 enable
   [*CE2-bgp-af-ipv6] network 2001:db8:6::6 128
   [*CE2-bgp-af-ipv6] commit
   [~CE2-bgp-af-ipv6] quit
   [~CE2-bgp] quit
   ```
   
   After the configuration is complete, run the **display bgp ipv6 peer** command on PE1. The command output shows that a BGP peer relationship has been established between PE1 and CE1.
   
   ```
   [~PE1] display bgp ipv6 peer
     BGP local router ID : 2.2.2.2 
     Local AS number : 100 
     Total number of peers : 2         Peers in established state : 2    
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State      PrefRcv   
     3.3.3.3         4         200       59       60     0 00:35:46   Established        1   
     2001:db8:1::1   4         100       40       45     0 00:06:16   Established        1
   ```
6. Verify the configuration.
   
   # After completing the configurations, run the **display ipv6 prefix pre1** command to view information about the prefix pool named **pre1**. The command output shows that **pre1** is a local prefix pool and the prefix address is **2001:db8::/64**.
   
   ```
   <~PE1> display ipv6 prefix pre1  
   -------------------------------------------------------------  
   Prefix Name        : pre1  
   Prefix Index       : 4 
   Prefix constant index: -  
   Prefix Type        : LOCAL  
   Prefix Address     : 2001:db8::  
   Prefix Length      : 64 
   Reserved Type      : NONE    V
   valid Lifetime      : 3 Days 0 Hours 0 Minutes  
   Preferred Lifetime : 2 Days 0 Hours 0 Minutes  
   IfLocked           : Unlocked 
   Vpn instance       : -        
   Conflict address   : - 
   Free Prefix Count  : 262144  
   Used Prefix Count  : 0  
   Reserved Prefix Count: 0   
   ```
   
   # Run the **display ipv6 pool pool1** command to view information about the address pool named **pool1**. The command output shows that **pool1** is a local address pool on the user side and the local prefix pool **pre1** is bound to the address pool **pool1**.
   
   ```
   <~PE1> display ipv6 pool pool1  
   ----------------------------------------------------------------------  
   Pool name          : pool1  
   Pool No            : 4    
   Pool-constant-index :-   
   Pool type          : BAS LOCAL  
   Preference         : 0  
   Renew time         : 50  
   Rebind time        : 80  
   Status              : UNLOCKED  
   Refresh interval   : 0 Days 0 Hours 0 Minutes  
   Used by domain     : 1  
   Dhcpv6 Unicast     : disable  
   Dhcpv6 rapid-commit: disable  
   Dns list             : -  
   Dns server master  : 2001:db8:4::1  
   Dns server slave   : - 
   AFTR name          : -   
   ----------------------------------------------------------------------  
   Prefix-Name                      Prefix-Type  
   ----------------------------------------------------------------------  
   pre1                               LOCAL 
   ---------------------------------------------------------------------- 
   ```
   
   # Run the **display domain isp1** command to view information about the domain named **isp1**. The command output shows that the IPv6 address pool named **pool1** is bound to this domain.
   
   ```
   <~PE1> display domain isp1 
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
   Idle-data-attribute (time,flow) : 0, 60   I
   nstall-BOD-Count                : 0   
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
   RADIUS-server-template          : rd1   
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
   IPv6-Pool-name                  : pool1   
   Quota-out                       : Offline   
   Service-type                    : -   
   User-basic-service-ip-type      : -/-/-   
   PPP-ipv6-address-protocol       : Ndra   
   IPv6-information-protocol       : Stateless dhcpv6   
   IPv6-PPP-assign-interfaceid     : Disable   
   Trigger-packet-wait-delay       : 60s   
   Peer-backup                     : enable      
   ------------------------------------------------------------------------------ 
   ```

#### Configuration Files

# CE1 configuration file

```
#
sysname CE1
#
interface gigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:1::1/64
#
interface LoopBack1
 ipv6 enable
 ipv6 address 2001:db8:5::5/128
#
bgp 100
 router-id 5.5.5.5
 peer 2001:db8:1::2 as-number 200
 #
 ipv4-family unicast
  undo synchronization 
 #
 ipv6-family unicast
  undo synchronization 
  network 2001:db8:5::5 128
  peer 2001:db8:1::2 enable
#
return
```

# PE1 configuration file

```
#
sysname PE1
#
radius-server group rd1
 radius-server authentication 2001:db8:4::2 1645 weight 0
 radius-server accounting 2001:db8:4::2 1646 weight 0
 radius-server shared-key-cipher %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
#
interface Virtual-Template1
 ppp authentication-mode chap
#
ipv6 prefix pre1 local
prefix 2001:db8:1::1/64
#
ip pool pool1 bas local
prefix pre1
dns-server 2001:db8:4::1
#
aaa
 authentication-scheme auth1
 authentication-mode radius
 accounting-scheme acct1
 accounting-mode radius
#
domain  isp1
 authentication-scheme auth1
 accounting-scheme acct1
 ipv6-pool pool1
 radius-server group rd1
#
interface gigabitethernet 0/1/0.1
 pppoe-server bind Virtual-Template 1
 ipv6 enable
 ipv6 address auto link-local
 bas
 access-type layer2-subscriber default-domain authentication isp1
#
interface gigabitEthernet 0/2/0
 ipv6 enable
 ipv6 address 2001:db8:3::1/64 eui-64
 ipv6 address auto link-local
#
return
#
sysname PE1
#
mpls lsr-id 2.2.2.2
#
mpls
#
mpls ldp
#
interface gigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:1::2/64
#
interface GigabitEthernet0/2/0
 undo shutdown
 ip address 10.0.0.1 255.255.255.252
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 2.2.2.2 255.255.255.255
#
bgp 200
 peer 3.3.3.3 as-number 200
 peer 3.3.3.3 connect-interface LoopBack0
 peer 2001:db8:1::1 as-number 100
#
 ipv4-family unicast
  undo synchronization 
  peer 3.3.3.3 enable
 #
 ipv6-family unicast
  undo synchronization 
  import-route direct
  peer 3.3.3.3 enable
  peer 3.3.3.3 label-route-capability
  peer 2001:db8:1::1 enable
#
ospf 1
 area 0.0.0.0
  network 2.2.2.2 0.0.0.0
  network 10.0.0.0 0.0.0.3
#
return
```

# PE2 configuration file

```
#
sysname PE2
#
mpls lsr-id 3.3.3.3
#
mpls
#
mpls ldp
#
interface gigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:2::2/64
#
interface gigabitEthernet0/2/0
 undo shutdown
 ip address 10.0.0.2 255.255.255.252
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 3.3.3.3 255.255.255.255
#
bgp 200
 peer 2.2.2.2 as-number 200
 peer 2.2.2.2 connect-interface LoopBack0
 peer 2001:db8:2::1 as-number 300
#
 ipv4-family unicast
  undo synchronization 
  peer 2.2.2.2 enable
 #
 ipv6-family unicast
  undo synchronization 
  import-route direct
  peer 2.2.2.2 enable
  peer 2.2.2.2 label-route-capability
  peer 2001:db8:2::1 enable
#
ospf 1
 area 0.0.0.0
  network 3.3.3.3 0.0.0.0
  network 10.0.0.0 0.0.0.3
#
return
```

# CE2 configuration file

```
#
sysname CE2
#
interface gigabitEthernet0/1/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:2::1/64
#
interface LoopBack1
 ipv6 enable
 ipv6 address 2001:db8:6::6/128
#
bgp 300
 router-id 6.6.6.6
 peer 2001:db8:2::2 as-number 200
 #
 ipv4-family unicast
  undo synchronization 
 #
 ipv6-family unicast
  undo synchronization 
  network 2001:db8:6::6 128
  peer 2001:db8:2::2 enable
#
return
```