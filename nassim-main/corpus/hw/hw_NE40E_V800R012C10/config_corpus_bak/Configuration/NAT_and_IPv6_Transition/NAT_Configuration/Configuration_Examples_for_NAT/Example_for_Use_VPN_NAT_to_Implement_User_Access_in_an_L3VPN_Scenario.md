Example for Use VPN NAT to Implement User Access in an L3VPN Scenario
=====================================================================

This section provides an example for configuring VPN NAT to allow VPN users on the same network segment to access one another in an L3VPN scenario and to allow the VPN users to access an internal server on the same network segment. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the L3VPN shown in [Figure 1](#EN-US_TASK_0172374663__fig_dc_ne_nat_cfg_015801), CE1 and CE2 belong to VPN-A. VPN-A connected to PE1 has IP addresses on the network segment 10.1.0.0/16, and VPN-A connected to PE2 has IP addresses on the network segment 10.2.0.0/16. VPN NAT is required for communication between VPN users connected to CE1 and CE2. VPN NAT also needs to be configured on the internal FTP server so that the VPN users connected to CE2 can access the internal FTP server connected to CE1.

**Figure 1** Networking for configuring VPN NAT![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/5, GE 0/2/2, GE 0/2/3, GE 0/2/4, and GE 0/2/5, respectively.


  
![](images/fig_dc_ne_nat_cfg_015801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure MPLS/BGP IP VPN so that CE1 can communicate with CE2.
2. Create a service-location group and a service-instance group.
3. Create a NAT instance and bind it to the service-instance group.
4. Configure address and port mapping for an internal server.
5. Configure a NAT traffic diversion policy.
6. Configure a NAT address pool and a NAT traffic conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Service-location group's index (1), service-instance group's name (group1), and service boards' slot IDs (1 and 3)
* NAT instance name (nat1) and index (1)
* NAT address pool name (address-group1), address pool number (1), and a range of IP addresses
* Internal server's private IP address (10.1.1.226) and public IP address (11.1.1.2)
* ACL number (3001), traffic classifier (c1), traffic behavior (b1), and traffic policy (p1)

#### Procedure

1. Configure an IGP on the MPLS backbone network to implement connectivity between the PEs and P.
   
   
   
   # Configure PE1.
   
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
   [~PE1] interface gigabitEthernet 0/2/3
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] ip address 172.16.2.2 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/3] quit
   ```
   ```
   [~PE1] interface LoopBack0
   ```
   ```
   [*PE1-LoopBack0] ip address 1.1.1.9 255.255.255.255
   ```
   ```
   [*PE1-LoopBack0] commit
   ```
   ```
   [~PE1-LoopBack0] quit
   ```
   ```
   [~PE1] ospf 1
   ```
   ```
   [*PE1-ospf-1] area 0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] network 1.1.1.9 0.0.0.0
   ```
   ```
   [*PE1-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE1-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE1-ospf-1] quit
   ```
   
   # Configure the P.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname P
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~P] interface gigabitEthernet 0/2/3
   ```
   ```
   [*P-GigabitEthernet0/2/3] undo shutdown
   ```
   ```
   [*P-GigabitEthernet0/2/3] ip address 172.16.2.1 255.255.255.0
   ```
   ```
   [*P-GigabitEthernet0/2/3] commit
   ```
   ```
   [~P-GigabitEthernet0/2/3] quit
   ```
   ```
   [~P] interface gigabitEthernet 0/2/2
   ```
   ```
   [*P-GigabitEthernet0/2/2] ip address 172.16.3.2 255.255.255.0
   ```
   ```
   [*P-GigabitEthernet0/2/2] commit
   ```
   ```
   [~P-GigabitEthernet0/2/2] quit
   ```
   ```
   [~P] interface LoopBack0
   ```
   ```
   [*P-LoopBack0] ip address 2.2.2.9 255.255.255.255
   ```
   ```
   [*P-LoopBack0] commit
   ```
   ```
   [~P-LoopBack0] quit
   ```
   ```
   [~P] ospf 1
   ```
   ```
   [~P-ospf-1] area 0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 172.16.2.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 2.2.2.9 0.0.0.0
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~P-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~P-ospf-1] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/2
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] ip address 172.16.3.1 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/2] quit
   ```
   ```
   [~PE2] interface LoopBack0
   ```
   ```
   [*PE2-LoopBack0] ip address 3.3.3.9 255.255.255.255
   ```
   ```
   [*PE2-LoopBack0] commit
   ```
   ```
   [~PE2-LoopBack0] quit
   ```
   ```
   [~PE2] ospf 1
   ```
   ```
   [*PE2-ospf-1] area 0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] network 3.3.3.9 0.0.0.0
   ```
   ```
   [*PE2-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~PE2-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~PE2-ospf-1] quit
   ```
2. Configure basic MPLS functions, enable MPLS LDP, and establish LDP LSPs on the MPLS backbone network.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] lsp-trigger all
   ```
   ```
   [*PE1-mpls] commit
   ```
   ```
   [~PE1-mpls] quit
   ```
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] commit
   ```
   ```
   [~PE1-mpls-ldp] quit
   ```
   ```
   [~PE1] interface gigabitEthernet 0/2/3
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/3] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/3] quit
   ```
   
   # Configure the P.
   
   ```
   [~P] mpls lsr-id 2.2.2.9
   ```
   ```
   [*P] mpls
   ```
   ```
   [*P-mpls] lsp-trigger all
   ```
   ```
   [*P-mpls] commit
   ```
   ```
   [~P-mpls] quit
   ```
   ```
   [~P] mpls ldp
   ```
   ```
   [*P-mpls-ldp] commit
   ```
   ```
   [~P-mpls-ldp] quit
   ```
   ```
   [~P] interface gigabitEthernet 0/2/3
   ```
   ```
   [*P-GigabitEthernet0/2/3] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/3] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/3] commit
   ```
   ```
   [~P-GigabitEthernet0/2/3] quit
   ```
   ```
   [~P] interface gigabitEthernet 0/2/2
   ```
   ```
   [*P-GigabitEthernet0/2/2] mpls
   ```
   ```
   [*P-GigabitEthernet0/2/2] mpls ldp
   ```
   ```
   [*P-GigabitEthernet0/2/2] commit
   ```
   ```
   [~P-GigabitEthernet0/2/2] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 3.3.3.9
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] lsp-trigger all
   ```
   ```
   [*PE2-mpls] commit
   ```
   ```
   [~PE2-mpls] quit
   ```
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] commit
   ```
   ```
   [~PE2-mpls-ldp] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/2
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/2/2] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/2/2-mpls-ldp] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/2-mpls-ldp] quit
   ```
3. Configure VPN instances on PEs so that CEs can access PEs.
   
   
   
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
   [*PE1-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE1] interface gigabitEthernet 0/2/4
   ```
   ```
   [*PE1âGigabitEthernet0/2/4] undo shutdown
   ```
   ```
   [*PE1âGigabitEthernet0/2/4] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/4] ip address 172.16.1.2 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/2/4] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/4] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/5
   ```
   ```
   [*PE2âGigabitEthernet0/2/5] undo shutdown
   ```
   ```
   [*PE2âGigabitEthernet0/2/5] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/5] ip address 172.16.4.2 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/2/5] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/5] quit
   ```
4. Establish EBGP peer relationships between PEs and CEs and import VPN routes.
   
   
   
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
   [*CE1-bgp] commit
   ```
   ```
   [~CE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] bgp 300
   ```
   ```
   [*CE2-bgp] peer 172.16.4.2 as-number 100
   ```
   ```
   [*CE2-bgp] import-route direct
   ```
   ```
   [*CE2-bgp] commit
   ```
   ```
   [~CE2-bgp] quit
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
   [*PE1-bgp-vpna] import-route unr
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 172.16.4.1 as-number 300
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] import-route unr
   ```
   ```
   [*PE2-bgp-vpna] commit
   ```
   ```
   [~PE2-bgp-vpna] quit
   ```
5. Establish an MP-IBGP peer relationship between PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.9 connect-interface LoopBack0
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] policy vpn-target
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 3.3.3.9 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 connect-interface LoopBack0
   ```
   ```
   [*PE2-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE2-bgp-af-vpnv4] policy vpn-target
   ```
   ```
   [*PE2-bgp-af-vpnv4] peer 1.1.1.9 enable
   ```
   ```
   [*PE2-bgp-af-vpnv4] commit
   ```
   ```
   [~PE2-bgp-af-vpnv4] quit
   ```
   
   After completing the configuration, run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command on a PE to verify that the BGP peer relationship between PEs is in the **Established** state.
6. Create a service-location group and a service-instance group and bind a NAT service board to the service-location group. Create a NAT instance and bind it to the service-instance group.
   
   
   ```
   <~PE1> system-view 
   ```
   ```
   [~PE1] service-location 1 
   ```
   ```
   [*PE1-service-location-1] location slot 3
   ```
   ```
   [*PE1-service-location-1] commit 
   ```
   ```
   [~PE1-service-location-1] quit
   ```
   ```
   [~PE1] service-instance-group group1
   ```
   ```
   [*PE1-service-instance-group-group1] service-location 1
   ```
   ```
   [*PE1-service-instance-group-group1] commit 
   ```
   ```
   [~PE1-service-instance-group-group1] quit 
   ```
   ```
   [~PE1] nat instance nat1
   ```
   ```
   [*PE1-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*PE1-nat-instance-nat1] commit
   ```
   ```
   [~PE1-nat-instance-nat1] quit
   ```
7. Configure an internal server on PE1.
   
   
   ```
   [~PE1] nat instance nat1
   ```
   ```
   [*PE1-nat-instance-nat1] nat server protocol tcp global 11.1.1.2 ftp vpn-instance vpna inside 10.1.1.226 ftp vpn-instance vpna
   ```
   ```
   [*PE1-nat-instance-nat1] commit
   ```
   ```
   [~PE1-nat-instance-nat1] quit
   ```
8. Configure ACL-based traffic classification rules and a traffic behavior on PE1.
   1. Configure traffic classification rules.
      
      
      * Rule 1: Configure a NAT traffic diversion policy for diverting user traffic with the network segment address of 10.1.0.0/16 to the server board for NAT processing.
      * Rule 2: Configure a NAT traffic translation policy so that addresses in the NAT address pool can be assigned to user traffic during the NAT processing.
      ```
      [~PE1] acl 3001
      ```
      ```
      [*PE1-acl-adv-3001] rule 1 permit ip source 10.1.0.0 0.0.255.255
      ```
      ```
      [*PE1-acl-adv-3001] rule 2 permit ip vpn-instance vpna source 10.1.0.0 0.0.255.255
      ```
      ```
      [*PE1-acl-adv-3001] commit
      ```
      ```
      [~PE1-acl-adv-3001] quit
      ```
   2. Configure a traffic classifier and define an ACL-based matching rule.
      
      
      ```
      [~PE1] traffic classifier c1
      ```
      ```
      [*PE1-classifier-c1] if-match acl 3001
      ```
      ```
      [*PE1-classifier-c1] commit
      ```
      ```
      [~PE1-classifier-c1] quit
      ```
   3. Configure a traffic behavior, which binds traffic to the NAT instance named **nat1**.
      
      
      ```
      [~PE1] traffic behavior b1
      ```
      ```
      [*PE1-behavior-b1] nat bind instance nat1
      ```
      ```
      [*PE1-behavior-b1] commit
      ```
      ```
      [~PE1-behavior-b1] quit
      ```
   4. Configure a traffic classification policy and associate the ACL rule with the traffic behavior.
      
      
      ```
      [~PE1] traffic policy p1
      ```
      ```
      [*PE1-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*PE1-trafficpolicy-p1] commit
      ```
      ```
      [~PE1-trafficpolicy-p1] quit
      ```
   5. Apply the ACL-based traffic policy in the interface view.
      
      
      ```
      [~PE1] interface gigabitEthernet 0/2/4
      ```
      ```
      [*PE1-GigabitEthernet0/2/4] traffic-policy p1 inbound
      ```
9. On PE1, configure a NAT address pool and a NAT traffic conversion policy so that interface boards divert matching packets to the NAT service boards to use addresses in the address pool to perform NAT.
   
   
   ```
   [~PE1] nat instance nat1
   ```
   ```
   [*PE1-nat-instance-nat1] nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpna
   ```
   ```
   [*PE1-nat-instance-nat1] commit
   ```
   ```
   [~PE1-nat-instance-nat1] quit
   ```

#### Configuration Files

PE1 configuration file

```
#
 sysname PE1
#
service-location 1
 location slot 3
#
service-instance-group group1
 service-location 1
#
nat instance nat1
 service-instance-group group1
 nat address-group address-group1 group-id 1 11.1.1.1 11.1.1.5 vpn-instance vpna
 nat server protocol tcp global 11.1.1.2 ftp vpn-instance vpna inside 10.1.1.226 ftp vpn-instance vpna
#
acl 3001
 rule 1 permit ip source 10.1.0.0 0.0.255.255 
 rule 2 permit ip vpn-instance vpna source 10.1.0.0 0.0.255.255 
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
 ipv4-family
  route-distinguisher 100:1
  apply-label per-instance 
  vpn-target 111:1 export-extcommunity
  vpn-target 111:1 import-extcommunity
#
mpls lsr-id 1.1.1.9
#
mpls
 lsp-trigger all
#
mpls ldp
 #
 ipv4-family
#
interface GigabitEthernet 0/2/4
 undo shutdown
 ip binding vpn-instance vpna
 ip address 172.16.1.2 255.255.255.0
 traffic-policy p1 inbound
#
interface GigabitEthernet 0/2/3
 undo shutdown
 ip address 172.16.2.2 255.255.255.0
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 1.1.1.9 255.255.255.255
#
bgp 100
 peer 3.3.3.9 as-number 100
 peer 3.3.3.9 connect-interface LoopBack0
 #
 ipv4-family vpn-instance vpna
  peer 172.16.1.1 as-number 200
  import-route direct
  import-route unr
 #
 ipv4-family vpnv4
  policy vpn-target
  peer 3.3.3.9 enable
#
ospf 1
 import-route static
 area 0.0.0.0
  network 172.16.2.0 0.0.0.255
  network 1.1.1.9 0.0.0.0
#
 return
```

P configuration file

```
#
 sysname P
#
mpls lsr-id 2.2.2.9
#
mpls
 lsp-trigger all
#
mpls ldp
 #
 ipv4-family
#
interface GigabitEthernet 0/2/3
 ip address 172.16.2.1 255.255.255.0
 mpls
 mpls ldp
#
interface GigabitEthernet 0/2/2
 ip address 172.16.3.2 255.255.255.0
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 2.2.2.9 255.255.255.255
#
ospf 1
 area 0.0.0.0
  network 172.16.2.0 0.0.0.255
  network 172.16.3.0 0.0.0.255
  network 2.2.2.9 0.0.0.0
#
return
```

PE2 configuration file

```
#
 sysname PE2
#
ip vpn-instance vpna
 ipv4-family
 route-distinguisher 200:1
 apply-label per-instance 
 vpn-target 111:1 export-extcommunity
 vpn-target 111:1 import-extcommunity
#
mpls lsr-id 3.3.3.9
#
mpls
 lsp-trigger all
#
mpls ldp
 #
 ipv4-family
#
interface GigabitEthernet 0/2/5
 undo shutdown
 ip binding vpn-instance vpna
 ip address 172.16.4.2 255.255.255.0
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 172.16.3.1 255.255.255.0
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 3.3.3.9 255.255.255.255
#
bgp 100
 peer 1.1.1.9 as-number 100
 peer 1.1.1.9 connect-interface LoopBack0
 ipv4-family vpnv4
  policy vpn-target
  peer 1.1.1.9 enable
 #
 ipv4-family vpn-instance vpna
  peer 172.16.4.1 as-number 300
  import-route direct
  import-route unr
#
ospf 1
 area 0.0.0.0
  network 172.16.3.0 0.0.0.255
  network 3.3.3.9 0.0.0.0
#
return
```

CE1 configuration file

```
#
 sysname CE1
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 172.16.1.1 255.255.255.0
#
bgp 200
 peer 172.16.1.2 as-number 100
 import-route direct
#
return
```

CE2 configuration file

```
#
 sysname CE2
#
interface GigabitEthernet 0/1/5
 undo shutdown
 ip address 172.16.4.1 255.255.255.0
#
bgp 300
 peer 172.16.4.2 as-number 100
 import-route direct
#
return
```