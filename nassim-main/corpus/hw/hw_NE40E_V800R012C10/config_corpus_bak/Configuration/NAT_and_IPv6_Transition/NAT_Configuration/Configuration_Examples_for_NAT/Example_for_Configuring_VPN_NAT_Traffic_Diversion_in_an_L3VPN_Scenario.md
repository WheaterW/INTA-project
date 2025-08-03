Example for Configuring VPN NAT Traffic Diversion in an L3VPN Scenario
======================================================================

This section provides an example for configuring VPN NAT traffic diversion in an L3VPN scenario so that users on different VPNs can access one another.

#### Networking Requirements

In an L3VPN scenario shown in [Figure 1](#EN-US_TASK_0172374666__fig_dc_ne_nat_cfg_015701), CE1 and CE3 belong to VPN-A, and CE2 and CE4 belong to VPN-B. Private network users PC1 and PC2 have the same IP address. PE2 is a NAT device. PC1 attempts to access PC3 through the NAT device. PC2 accesses PC4 without using the NAT device. A VPN traffic diversion policy is configured on the inbound interface of the egress PE to identify traffic of different VPNs.

**Figure 1** VPN NAT traffic diversion in an L3VPN scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 5 in this example represent GE 0/1/5, GE 0/2/2, GE 0/2/3, GE 0/2/4, and GE 0/2/5, respectively.


  
![](images/fig_dc_ne_nat_cfg_015701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure MPLS/BGP IP VPN so that CEs can communicate with each other and with PEs.
2. Create a service-location group and a service-instance group.
3. Create a NAT instance and bind it to the service-instance group.
4. Configure address and port mapping for a NAT internal server.
5. Configure a NAT traffic diversion policy.
6. Configure a NAT address pool and a NAT traffic conversion policy.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Service-location group index (1), service-instance group name (group1), and service board slot number (1)
* NAT instance name (nat1) and index (1)
* NAT address pool name (address-group1), address pool number (1), and public IP address range
* ACL number (3001), traffic classifier (c1), traffic behavior name (b1), and traffic policy name (p1)

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
   [*PE1-GigabitEthernet0/2/3] ip address 172.16.3.2 255.255.255.0
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
   [*PE1-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
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
   [*P-GigabitEthernet0/2/3] ip address 172.16.3.1 255.255.255.0
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
   [*P-GigabitEthernet0/2/2] ip address 172.16.4.2 255.255.255.0
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
   [*P-ospf-1-area-0.0.0.0] network 172.16.3.0 0.0.0.255
   ```
   ```
   [*P-ospf-1-area-0.0.0.0] network 172.16.4.0 0.0.0.255
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
   [*PE2-GigabitEthernet0/2/2] ip address 172.16.4.1 255.255.255.0
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
   [*PE2-ospf-1-area-0.0.0.0] network 172.16.4.0 0.0.0.255
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
   [*PE2-GigabitEthernet0/2/2] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/2] quit
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
   [~PE1] ip vpn-instance vpnb
   ```
   ```
   [*PE1-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] vpn-target 222:1 both
   ```
   ```
   [*PE1-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE1-vpn-instance-vpnb-af-ipv4] quit
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
   ```
   [~PE1] interface gigabitEthernet 0/2/5
   ```
   ```
   [*PE1âGigabitEthernet0/2/5] undo shutdown
   ```
   ```
   [*PE1âGigabitEthernet0/2/5] ip binding vpn-instance vpnb
   ```
   ```
   [*PE1-GigabitEthernet0/2/5] ip address 172.16.2.2 255.255.255.0
   ```
   ```
   [*PE1-GigabitEthernet0/2/5] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/5] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 300:1
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
   [~PE2] ip vpn-instance vpnb
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 400:1
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 222:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/4
   ```
   ```
   [*PE2âGigabitEthernet0/2/4] undo shutdown
   ```
   ```
   [*PE2âGigabitEthernet0/2/4] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/4] ip address 172.16.5.2 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/2/4] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/4] quit
   ```
   ```
   [~PE2] interface gigabitEthernet 0/2/5
   ```
   ```
   [*PE2âGigabitEthernet0/2/5] undo shutdown
   ```
   ```
   [*PE2âGigabitEthernet0/2/5] ip binding vpn-instance vpnb
   ```
   ```
   [*PE2-GigabitEthernet0/2/5] ip address 172.16.6.2 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/2/5] commit
   ```
   ```
   [~PE2-GigabitEthernet0/2/5] quit
   ```
4. Create EBGP peer relationships between PEs and CEs and import VPN routes.
   
   
   
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
   [*CE2-bgp] peer 172.16.2.2 as-number 100
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
   
   # Configure CE3.
   
   ```
   [~CE3] bgp 400
   ```
   ```
   [*CE3-bgp] peer 172.16.5.2 as-number 100
   ```
   ```
   [*CE3-bgp] import-route direct
   ```
   ```
   [*CE3-bgp] commit
   ```
   ```
   [~CE3-bgp] quit
   ```
   
   # Configure CE4.
   
   ```
   [~CE4] bgp 500
   ```
   ```
   [*CE4-bgp] peer 172.16.6.2 as-number 100
   ```
   ```
   [*CE4-bgp] import-route direct
   ```
   ```
   [*CE4-bgp] commit
   ```
   ```
   [~CE4-bgp] quit
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
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpnb
   ```
   ```
   [*PE1-bgp-vpnb] peer 172.16.2.1 as-number 200
   ```
   ```
   [*PE1-bgp-vpnb] import-route direct
   ```
   ```
   [*PE1-bgp-vpnb] commit
   ```
   ```
   [~PE1-bgp-vpnb] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp-vpna] peer 172.16.5.1 as-number 300
   ```
   ```
   [*PE2-bgp-vpna] import-route direct
   ```
   ```
   [*PE2-bgp-vpna] commit
   ```
   ```
   [~PE2-bgp-vpna] quit
   ```
   ```
   [*PE2-bgp] ipv4-family vpn-instance vpnb
   ```
   ```
   [*PE2-bgp-vpnb] peer 172.16.6.1 as-number 300
   ```
   ```
   [*PE2-bgp-vpnb] import-route direct
   ```
   ```
   [*PE2-bgp-vpnb] import-route unr
   ```
   ```
   [*PE2-bgp-vpnb] commit
   ```
   ```
   [~PE2-bgp-vpnb] quit
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
   
   After completing the configuration, run the [**display bgp peer**](cmdqueryname=display+bgp+peer) command on each PE. BGP peer relationships between PEs have been established and are in the [**Established**](cmdqueryname=Established) state.
6. On PE2, create a service-location group and a service-instance group and bind the service-location group to the NAT service board. Create a NAT instance and bind it to the service-instance group.
   
   
   ```
   <~PE2> system-view 
   ```
   ```
   [~PE2] service-location 1 
   ```
   ```
   [*PE2-service-location-1] location slot 3 
   ```
   ```
   [*PE2-service-location-1] commit 
   ```
   ```
   [~PE2-service-location-1] quit
   ```
   ```
   [~PE2] service-instance-group group1
   ```
   ```
   [*PE2-service-instance-group-group1] service-location 1
   ```
   ```
   [*PE2-service-instance-group-group1] commit 
   ```
   ```
   [~PE2-service-instance-group-group1] quit 
   ```
   ```
   [~PE2] nat instance nat1 id 1
   ```
   ```
   [*PE2-nat-instance-nat1] service-instance-group group1
   ```
   ```
   [*PE2-nat-instance-nat1] commit
   ```
   ```
   [~PE2-nat-instance-nat1] quit
   ```
7. Configure an ACL-based traffic classification rule and a traffic behavior on PE2.
   1. Configure a traffic classification rule.
      
      
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
   3. Configure a traffic behavior, which binds traffic to the NAT instance named **nat1**.
      
      
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
   4. Configure a traffic classification policy to associate the ACL rule with the traffic behavior.
      
      
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
8. On PE2, configure a NAT address pool and a NAT traffic conversion policy so that NAT is performed using addresses in the NAT address pool. This applies to all packets that are diverted by an interface board to a NAT service board.
   
   
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

#### Configuration Files

PE1 configuration file

```
#
 sysname PE1
#
ip vpn-instance vpna
 ipv4-family
  route-distinguisher 100:1
  apply-label per-instance 
  vpn-target 111:1 export-extcommunity
  vpn-target 111:1 import-extcommunity
 #
#
ip vpn-instance vpnb
 ipv4-family
  route-distinguisher 200:1
  apply-label per-instance 
  vpn-target 222:1 export-extcommunity
  vpn-target 222:1 import-extcommunity
 #
#
mpls lsr-id 1.1.1.9
mpls
 lsp-trigger all
#
mpls ldp
#
interface GigabitEthernet 0/2/4
 undo shutdown
 ip binding vpn-instance vpna
 ip address 172.16.1.2 255.255.255.0
#
interface GigabitEthernet 0/2/5
 undo shutdown
 ip binding vpn-instance vpnb
 ip address 172.16.2.2 255.255.255.0
#
interface GigabitEthernet 0/2/3
 undo shutdown
 ip address 172.16.3.2 255.255.255.0
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
 ipv4-family vpn-instance vpnb
  peer 172.16.2.1 as-number 200
  import-route direct
  import-route unr
 #
 ipv4-family vpnv4
  policy vpn-target
  peer 3.3.3.9 enable
#
ospf 1
  area 0.0.0.0
  network 172.16.3.0 0.0.0.255
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
 mpls
  lsp-trigger all
#
mpls ldp
#
interface GigabitEthernet 0/2/3
 ip address 172.16.3.1 255.255.255.0
 mpls
 mpls ldp
#
interface GigabitEthernet 0/2/2
 ip address 172.16.4.2 255.255.255.0
 mpls
 mpls ldp
#
interface LoopBack0
 ip address 2.2.2.9 255.255.255.255
#
ospf 1
 area 0.0.0.0
  network 172.16.3.0 0.0.0.255
  network 172.16.4.0 0.0.0.255
  network 2.2.2.9 0.0.0.0
#
return
```

PE2 configuration file

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
 ipv4-family
  route-distinguisher 300:1
  apply-label per-instance 
  vpn-target 111:1 export-extcommunity
  vpn-target 111:1 import-extcommunity
  traffic-policy p1 network inbound
 #
#
ip vpn-instance vpnb
 ipv4-family
  route-distinguisher 400:1
  apply-label per-instance 
  vpn-target 222:1 export-extcommunity
  vpn-target 222:1 import-extcommunity
 #
#
mpls lsr-id 3.3.3.9
mpls
 lsp-trigger all
#
mpls ldp
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 172.16.4.1 255.255.255.0
 mpls
 mpls ldp
#
interface GigabitEthernet 0/2/4
 undo shutdown
 ip binding vpn-instance vpna
 ip address 172.16.5.2 255.255.255.0
#
interface GigabitEthernet 0/2/5
 undo shutdown
 ip binding vpn-instance vpnb
 ip address 172.16.6.2 255.255.255.0
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
  peer 172.16.5.1 as-number 300
  import-route direct
  import-route unr
 #
 ipv4-family vpn-instance vpnb
  peer 172.16.6.1 as-number 300
  import-route direct
  import-route unr
#
ospf 1
 area 0.0.0.0
  network 172.16.4.0 0.0.0.255
  network 3.3.3.9 0.0.0.0
#
return
```

CE1 configuration file

```
#
 sysname CE1
#
interface GigabitEthernet 0/1/5
 undo shutdown
 ip address 172.16.1.1 255.255.255.0
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 10.1.1.3 255.255.255.0
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
 ip address 172.16.2.1 255.255.255.0
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
#
bgp 300
 peer 172.16.2.2 as-number 100
 import-route direct
#
return
```

CE3 configuration file

```
#
 sysname CE3
#
interface GigabitEthernet 0/1/5
 undo shutdown
 ip address 172.16.5.1 255.255.255.0
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 10.1.3.2 255.255.255.0
#
bgp 400
 peer 172.16.5.2 as-number 100
 import-route direct
#
return
```

CE4 configuration file

```
#
 sysname CE4
#
interface GigabitEthernet 0/1/5
 undo shutdown
 ip address 172.16.6.1 255.255.255.0
#
interface GigabitEthernet 0/2/2
 undo shutdown
 ip address 10.1.2.2 255.255.255.0
#
bgp 500
 peer 172.16.6.2 as-number 100
 import-route direct
#
return
```