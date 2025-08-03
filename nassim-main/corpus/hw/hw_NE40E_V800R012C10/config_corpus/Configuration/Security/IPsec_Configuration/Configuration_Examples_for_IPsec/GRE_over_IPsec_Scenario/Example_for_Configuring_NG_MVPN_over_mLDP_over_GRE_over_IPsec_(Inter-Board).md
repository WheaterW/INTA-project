Example for Configuring NG MVPN over mLDP over GRE over IPsec (Inter-Board)
===========================================================================

Example for Configuring NG MVPN over mLDP over GRE over IPsec (Inter-Board)

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported by a VSU or main control board.


On the intra-AS NG MVPN (over mLDP P2MP tunnels) shown in [Figure 1](#EN-US_TASK_0000001352681245__fig4757182915104), GRE over IPsec tunnels are established between PEs or between PEs and Ps to provide IPsec protection for data transmitted on the public network. In an inter-board scenario, GRE encapsulation needs to be performed on a GRE tunnel and IPsec encryption needs to be performed on a VSU or main control board.**Figure 1** Configuring NG MVPN over mLDP over GRE over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/1/1, and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001301186512.png)

The networking is as follows:

* On PE1, public network-side interfaces GE0/1/0 and GE0/1/2 respectively connect to PE2 and PE3, and VPN-side interface GE0/1/1 connects to CE1's GE0/1/1.
* On PE2, public network-side interface GE0/1/0 connects to PE1, and VPN-side interface GE0/1/1 connects to CE2's GE0/1/1.
* On PE3, public network-side interface GE0/1/0 connects to PE1, and VPN-side interface GE0/1/1 connects to CE3's GE0/1/1.

To improve communication security between PE1 and PE2 and between PE1 and PE3, configure GRE over IPsec tunnels between them.




#### Configuration Roadmap

This section provides an example for configuring NG MVPN-triggered mLDP over GRE over IPsec in IKE mode. The tunnel encapsulation mode is used.

1. Configure IP addresses for interfaces.
2. Create loopback interfaces and bind GRE to them.
3. Create tunnel interfaces and configure GRE for these interfaces.
4. Configure IPsec. Specifically:
   * Enable IPsec.
   * Configure ACLs to define the data flows to be protected.
   * (Recommended) Configure DPD.
   * Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
   * Configure IKE peers.
   * Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
   * Configure IPsec policies.
   * Configure an IPsec service-instance group.
   * Create and configure a tunnel interface.
   * Apply the IPsec policy to the tunnel interface.
   * Configure static routes to steer IPsec traffic.
5. Create a loopback interface, configure IS-IS, and enable IS-IS on the loopback interface and GRE tunnel interface.
6. Establish an IBGP peer relationship between PE1 and PE2.
7. Enable MPLS, MPLS LDP, and mLDP.
8. Configure the NG MVPN over mLDP service. Specifically:
   * Configure a BGP/MPLS IP VPN and ensure that the unicast VPN is running properly.
   * Enable all PEs to establish BGP MVPN peer relationships and configure BGP to transmit A-D and C-multicast routes.
   * Configure PE1 to use mLDP for I-PMSI tunnel establishment so that mLDP P2MP tunnels can be established.
   * Configure PIM on PE interfaces bound to VPN instances and on CE interfaces connected to PEs so that VPN multicast routing entries are generated for multicast traffic forwarding.
   * Configure IGMP on the multicast device's interface that connects to the user network segment to manage multicast group members on that network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* IPsec-related data, mainly including:
  + DPD data
  + ACL number
  + IP address segment of each subnet
  + Pre-shared key
  + Authentication algorithm to be used for the IKE proposal
  + Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposal
  + IP addresses of tunnel interfaces
* L3VPN data, including the IS-IS system ID, MPLS LSR ID, VPN instance name, RD, and VPN target

#### Procedure

* Configure PE1, PE2, and PE3.
  
  
  
  | Item | PE1 | PE2 | PE3 |
  | --- | --- | --- | --- |
  | 1. Configure IP addresses for interfaces. | ``` interface GigabitEthernet0/1/0  undo shutdown  ip address 192.168.5.1 255.255.255.0 # interface GigabitEthernet0/1/2  undo shutdown  ip address 192.168.6.1 255.255.255.0 # interface LoopBack0  ip address 1.1.1.1 255.255.255.255 # interface LoopBack1  ip address 10.1.1.1 255.255.255.255 # ``` | ``` interface GigabitEthernet0/1/0  undo shutdown  ip address 192.168.5.2 255.255.255.0 # interface LoopBack0  ip address 2.2.2.2 255.255.255.255 #  interface LoopBack1  ip address 10.2.1.1 255.255.255.255 # ``` | ``` interface GigabitEthernet0/1/2  undo shutdown  ip address 192.168.6.2 255.255.255.0 # interface LoopBack0  ip address 3.3.3.3 255.255.255.255 # interface LoopBack1  ip address 10.3.1.1 255.255.255.255 # ``` |
  | 2. Configure a GRE tunnel interface. | ``` interface LoopBack1  binding tunnel gre # interface Tunnel12  ip address 11.1.1.1 255.255.255.0  tunnel-protocol gre  source 10.1.1.1  destination 10.2.1.1 # interface Tunnel14  ip address 22.1.1.2 255.255.255.0  tunnel-protocol gre  source 10.1.1.1  destination 10.3.1.1 # ``` | ``` interface LoopBack1  binding tunnel gre # interface Tunnel21  ip address 11.1.1.2 255.255.255.0  tunnel-protocol gre  source 10.2.1.1  destination 10.1.1.1 # ``` | ``` interface LoopBack1  binding tunnel gre # interface Tunnel41  ip address 22.1.1.1 255.255.255.0  tunnel-protocol gre  source 10.3.1.1  destination 10.1.1.1 # ``` |
  | 4. Enable DPD. | ``` ike dpd interval 10 10 //Deploying DPD is recommended. ``` | ``` ike dpd interval 10 10 //Deploying DPD is recommended. ``` | ``` ike dpd interval 10 10 //Deploying DPD is recommended. ``` |
  | 5. Configure an ACL to define the data flows to be protected. | ``` acl number 3000  rule 5 permit gre source 10.1.1.1 0 destination 10.3.1.1 0 # acl number 3001  rule 5 permit gre source 10.1.1.1 0 destination 10.2.1.1 0 # ``` | ``` acl number 3001  rule 5 permit gre source 10.2.1.1 0 destination 10.1.1.1 0 # ``` | ``` acl number 3000  rule 5 permit gre source 10.3.1.1 0 destination 10.1.1.1 0 # ``` |
  | 6. Configure an IKE proposal and an IKE peer. | ``` ike proposal 1  encryption-algorithm aes-cbc 256  dh group14  authentication-algorithm sha2-256  integrity-algorithm hmac-sha2-256 # ike peer pe1  pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1  remote-address 33.1.2.1 # ike peer pe2   pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1  remote-address 10.6.2.2 # ``` | ``` ike proposal 1  encryption-algorithm aes-cbc 256  dh group14  authentication-algorithm sha2-256  integrity-algorithm hmac-sha2-256 # ike peer pe2  pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1   remote-address 10.6.2.1 # ``` | ``` ike proposal 1  encryption-algorithm aes-cbc 256  dh group14  authentication-algorithm sha2-256  integrity-algorithm hmac-sha2-256 # ike peer pe1  pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1   remote-address 10.5.2.2 # ``` |
  | 7. Configure a service-instance group. | ``` # service-location 1  location slot 1 # service-instance-group group1  service-location 1 ``` | ``` # service-location 1  location slot 1 # service-instance-group group1  service-location 1 ``` | ``` # service-location 1  location slot 1 # service-instance-group group1  service-location 1 ``` |
  | 8. Configure an IPsec tunnel. | ``` ipsec proposal zh //Configure an IPsec proposal.  esp authentication-algorithm sha2-256  esp encryption-algorithm aes 256 # ipsec policy axpo2 10 isakmp //Configure an IPsec policy.  security acl 3001  ike-peer pe2   proposal zh # ipsec policy axpo 10 isakmp  security acl 3000  ike-peer pe1  proposal zh # interface Tunnel121 //Configure an IPsec tunnel.  ip address 10.6.2.1 255.255.255.0  tunnel-protocol ipsec  ipsec policy axpo2 service-instance-group 1 interface Tunnel141  ip address 10.5.2.2 255.255.255.0  tunnel-protocol ipsec  ipsec policy axpo service-instance-group 1 # ``` | ``` ipsec proposal zh //Configure an IPsec proposal.  esp authentication-algorithm sha2-256   esp encryption-algorithm aes 256  #  ipsec policy axpo2 10 isakmp //Configure an IPsec policy.  security acl 3001  ike-peer pe2  proposal zh # interface Tunnel211 //Configure an IPsec tunnel.  ip address 10.6.2.2 255.255.255.0  tunnel-protocol ipsec  ipsec policy axpo2 service-instance-group 1 # ``` | ``` ipsec proposal zh //Configure an IPsec proposal.  esp authentication-algorithm sha2-256   esp encryption-algorithm aes 256  #  ipsec policy axpo 10 isakmp  security acl 3000  ike-peer pe1  proposal zh # interface Tunnel411  ip address 10.5.2.1 255.255.255.0  tunnel-protocol ipsec  ipsec policy axpo service-instance-group 1 # ``` |
  | 9. Configure traffic diversion routes. | ``` ip route-static 10.2.1.1 255.255.255.255 Tunnel121 10.6.2.2 //Divert traffic to the IPsec tunnel for encryption. ip route-static 10.6.2.2 255.255.255.255 GigabitEthernet0/1/0 192.168.5.2 //Divert the IPsec-encrypted traffic to the actual physical outbound interface. ip route-static 10.3.1.1 255.255.255.255 Tunnel141 10.5.2.1 //Divert traffic to the IPsec tunnel for encryption. ip route-static 10.5.2.1 255.255.255.255 GigabitEthernet0/1/2 192.168.6.2 //Divert IPsec-encrypted traffic to the actual physical outbound interface. ``` | ``` ip route-static 10.1.1.1 255.255.255.255 Tunnel211 10.6.2.1 //Divert traffic to the IPsec tunnel for encryption. ip route-static 10.6.2.1 255.255.255.255 GigabitEthernet0/1/0 192.168.5.1 //Divert IPsec-encrypted traffic to the actual physical outbound interface.  ``` | ``` ip route-static 10.1.1.1 255.255.255.255 Tunnel411 10.5.2.2 //Divert traffic to the IPsec tunnel for encryption. ip route-static 10.5.2.2 255.255.255.255 GigabitEthernet0/1/2 192.168.6.1 //Divert IPsec-encrypted traffic to the actual physical outbound interface. ``` |
  | 10. Configure IS-IS. | ``` isis 1  is-level level-2  cost-style wide  network-entity 01.0000.0000.0003.00 # interface LoopBack0  isis enable 1 # interface Tunnel12  isis enable 1 # ``` | ``` isis 1  is-level level-2  cost-style wide  network-entity 01.0000.0000.0005.00 #  interface LoopBack0  isis enable 1 # interface Tunnel21  isis enable 1 # ``` | ``` isis 1  is-level level-2  cost-style wide  network-entity 01.0000.0000.0004.00 #  interface LoopBack0  isis enable 1 # interface Tunnel41  isis enable 1 # ``` |
  | 11. Configure mLDP. | ``` mpls lsr-id 1.1.1.1 # mpls # mpls ldp  mldp p2mp  #  ipv4-family # interface Tunnel12  mpls  mpls ldp # ``` | ``` mpls lsr-id 2.2.2.2 # mpls # mpls ldp  mldp p2mp  #  ipv4-family # interface Tunnel21  mpls  mpls ldp # ``` | ``` mpls lsr-id 3.3.3.3 # mpls # mpls ldp  mldp p2mp  #  ipv4-family # interface Tunnel41  mpls  mpls ldp # ``` |
  | 12. Configure VPN. | ``` ip vpn-instance mldp  ipv4-family   route-distinguisher 100:100   apply-label per-instance   vpn-target 100:100 export-extcommunity   vpn-target 100:100 import-extcommunity # ``` | ``` ip vpn-instance ipsec_vpn  ipv4-family   route-distinguisher 100:100   vpn-target 200:200 export-extcommunity   vpn-target 200:200 import-extcommunity # ``` | ``` ip vpn-instance mldp  ipv4-family   route-distinguisher 100:100   apply-label per-instance   vpn-target 100:100 export-extcommunity   vpn-target 100:100 import-extcommunity # ``` |
  | 13. Configure BGP. | ``` bgp 100  private-4-byte-as enable  peer 2.2.2.2 as-number 100  peer 2.2.2.2 connect-interface LoopBack0  peer 3.3.3.3 as-number 100  peer 3.3.3.3 connect-interface LoopBack0  #  ipv4-family unicast   undo synchronization   peer 2.2.2.2 enable   peer 3.3.3.3 enable  #  ipv4-family mvpn   policy vpn-target   peer 2.2.2.2 enable   peer 3.3.3.3 enable  #  ipv4-family vpnv4   policy vpn-target   peer 2.2.2.2 enable   peer 3.3.3.3 enable  #  ipv4-family vpn-instance mldp   import-route direct # ``` | ``` bgp 100  private-4-byte-as enable  peer 1.1.1.1 as-number 100  peer 1.1.1.1 connect-interface LoopBack0  #  ipv4-family unicast   undo synchronization   peer 1.1.1.1 enable  #  ipv4-family mvpn   policy vpn-target   peer 1.1.1.1 enable  #  ipv4-family vpnv4   policy vpn-target   peer 1.1.1.1 enable  #  ipv4-family vpn-instance mldp   import-route direct # ``` | ``` bgp 100  private-4-byte-as enable  peer 1.1.1.1 as-number 100  peer 1.1.1.1 connect-interface LoopBack0  #  ipv4-family unicast   undo synchronization   peer 1.1.1.1 enable  #  ipv4-family mvpn   policy vpn-target   peer 1.1.1.1 enable  #  ipv4-family vpnv4   policy vpn-target   peer 1.1.1.1 enable  #  ipv4-family vpn-instance mldp   import-route direct # ``` |
  | 14. Configure MVPN. | ``` ip vpn-instance mldp  ipv4-family   multicast routing-enable   mvpn    sender-enable    rpt-spt mode    ipmsi-tunnel     mldp # ``` | ``` ip vpn-instance mldp  ipv4-family   multicast routing-enable   mvpn    c-multicast signaling bgp    rpt-spt mode # ``` | ``` ip vpn-instance mldp  ipv4-family   multicast routing-enable   mvpn    c-multicast signaling bgp    rpt-spt mode # ``` |
  | 15. Configure PIM. | ``` interface GigabitEthernet0/1/1  undo shutdown  ip binding vpn-instance mldp  ip address 192.168.10.1 255.255.255.0  pim sm  dcn # ``` | ``` interface GigabitEthernet0/1/1  undo shutdown  ip binding vpn-instance mldp  ip address 192.168.12.1 255.255.255.0  pim sm  dcn # ``` | ``` interface GigabitEthernet0/1/1  undo shutdown  ip binding vpn-instance mldp  ip address 192.168.14.1 255.255.255.0  pim sm  dcn # ``` |
  | 16. Configure a static RP. | ``` pim vpn-instance mldp  static-rp 192.168.10.1 # ``` | ``` pim vpn-instance mldp  static-rp 192.168.10.1 # ``` | ``` pim vpn-instance mldp  static-rp 192.168.10.1 # ``` |
  | 17. Configure VPN OSPF. | ``` ospf 2 vpn-instance VPNA import-route bgp area 0.0.0.0 network 192.168.10.0 0.0.0.255 # ``` | ``` ospf 2 vpn-instance VPNA import-route bgp area 0.0.0.0 network 192.168.12.0 0.0.0.255 # ``` | ``` ospf 2 vpn-instance VPNA import-route bgp area 0.0.0.0 network 192.168.14.0 0.0.0.255 # ``` |
* Configure CE1, CE2, and CE3.
  
  
  
  | Item | CE1 | CE2 | CE3 |
  | --- | --- | --- | --- |
  | 1. Configure IP addresses for interfaces. | ``` interface GigabitEthernet0/1/1  undo shutdown  ip address 192.168.10.2 255.255.255.0  pim sm  igmp enable  dcn # interface LoopBack1  ip address 4.4.4.4 255.255.255.255 # interface GigabitEthernet0/1/2  undo shutdown  ip address 192.168.1.2 255.255.255.0  pim sm # ``` | ``` interface GigabitEthernet0/1/1  undo shutdown  ip address 192.168.12.2 255.255.255.0  pim sm  igmp enable  dcn # interface LoopBack1  ip address 5.5.5.5 255.255.255.255 # interface GigabitEthernet0/1/2  undo shutdown  ip address 192.168.2.2 255.255.255.0  pim sm # ``` | ``` interface GigabitEthernet0/1/1  undo shutdown  ip address 192.168.14.2 255.255.255.0  pim sm  igmp enable  dcn # interface LoopBack1  ip address 6.6.6.6 255.255.255.255 # interface GigabitEthernet0/1/2  undo shutdown  ip address 192.168.3.2 255.255.255.0  pim sm # ``` |
  | 2. Configure a static RP. | ``` pim  static-rp 4.4.4.4 # ``` | ``` pim  static-rp 4.4.4.4 # ``` | ``` pim  static-rp 4.4.4.4 # ``` |
  | 3. Configure OSPF for communication with PEs. | ``` ospf 2  area 0.0.0.0  network 4.4.4.4 0.0.0.0  network 192.168.10.0 0.0.0.255  network 192.168.1.0 0.0.0.255 # ``` | ``` ospf 2  area 0.0.0.0  network 5.5.5.5 0.0.0.0  network 192.168.12.0 0.0.0.255  network 192.168.2.0 0.0.0.255 # ``` | ``` ospf 2  area 0.0.0.0  network 6.6.6.6 0.0.0.0  network 192.168.14.0 0.0.0.255  network 192.168.3.0 0.0.0.255 # ``` |