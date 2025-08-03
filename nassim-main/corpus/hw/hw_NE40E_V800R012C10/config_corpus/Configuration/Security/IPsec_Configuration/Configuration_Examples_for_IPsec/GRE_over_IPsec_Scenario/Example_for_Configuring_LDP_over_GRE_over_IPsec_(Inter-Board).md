Example for Configuring LDP over GRE over IPsec (Inter-Board)
=============================================================

Example for Configuring LDP over GRE over IPsec (Inter-Board)

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported by a VSU or main control board.

On the network shown in [Figure 1](#EN-US_TASK_0172372493__fig4498125415555), establish a GRE over IPsec tunnel between the PEs or between a PE and a P on an MPLS network to protect data transmitted on the public network. In an inter-board scenario, GRE encapsulation needs to be performed on a GRE tunnel and IPsec encryption needs to be performed on a VSU or main control board.

**Figure 1** Networking diagram of LDP over GRE over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/0 and GE0/1/1, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_all_003601.png "Click to enlarge")

The networking is as follows:

* PE1's public network-side interface GE0/1/0 is connected to PE2, and PE1's private network-side interface GE0/1/1 is connected to CE1.
* PE2's public network-side interface GE0/1/0 is connected to PE1, and PE2's private network-side interface GE0/1/1 is connected to CE2.

A GRE over IPsec tunnel needs to be configured to implement secure communication between PE1 and PE2.


#### Configuration Roadmap

This section uses IPsec in IKE mode as an example to describe how to configure LDP over GRE over IPsec. The tunnel encapsulation mode is used.

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
   * Apply the IPsec policies to the tunnel interfaces.
   * Configure static routes to steer IPsec traffic.
5. Create and configure loopback interfaces, configure IS-IS, and enable IS-IS on GRE tunnel interfaces and loopback interfaces.
6. Establish an IBGP peer relationship between PE1 and PE2.
7. Enable MPLS and MPLS LDP.
8. Create a VPN instance so that PEs can communicate with each other.

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

* Configure PE1 and PE2.
  
  
  
  | Item | PE1 | PE2 |
  | --- | --- | --- |
  | 1. Configure IP addresses for interfaces. | ``` interface GigabitEthernet0/1/0  undo shutdown  ip address 192.168.5.1 255.255.255.0 # interface LoopBack1  ip address 1.1.1.1 255.255.255.255 # interface LoopBack2  ip address 3.3.3.3 255.255.255.255 ``` | ``` interface GigabitEthernet0/1/0  undo shutdown  ip address 192.168.5.2 255.255.255.0 # interface LoopBack1  ip address 2.2.2.2 255.255.255.255 #  interface LoopBack2  ip address 4.4.4.4 255.255.255.255 ``` |
  | 2. Configure a GRE tunnel interface. | ``` interface LoopBack1  binding tunnel gre # interface Tunnel 802 ip address 172.16.5.1 255.255.255.0 // This address is meaningless and is used to make the interface Up.  tunnel-protocol gre  source LoopBack1  destination 2.2.2.2 ``` | ``` interface LoopBack1  binding tunnel gre # interface Tunnel 502 ip address 172.16.5.2 255.255.255.0 // This address is meaningless and is used to make the interface Up.  tunnel-protocol gre  source LoopBack1  destination 1.1.1.1 ``` |
  | 3. Enable IPsec. | NOTE:  Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function. After the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command is run, IPsec cannot be configured on the main control board.  Only the following models support this configuration:  NE40E-M2K  NE40E-M2K-B  ``` license ``` ```  active ipsec bandwidth-enhance 40 slot 1 ``` | NOTE:  Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function. After the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command is run, IPsec cannot be configured on the main control board.  Only the following models support this configuration:  NE40E-M2K  NE40E-M2K-B  ``` license ``` ```  active ipsec bandwidth-enhance 40 slot 1 ``` |
  | 4. Enable DPD. | ``` ike dpd interval 10 10 //Deploying DPD is recommended. ``` | ``` ike dpd interval 10 10 //Deploying DPD is recommended. ``` |
  | 5. Configure an ACL to define the data flows to be protected. | ``` acl number 3100  rule 5 permit gre source 1.1.1.1 0 destination 2.2.2.2 0 ``` | ``` acl number 3100  rule 5 permit gre source 2.2.2.2 0 destination 1.1.1.1 0 ``` |
  | 6. Configure an IKE proposal and an IKE peer. | ``` ike proposal 1  encryption-algorithm aes-cbc 256  dh group14  authentication-algorithm sha2-256  integrity-algorithm hmac-sha2-256 # ike peer pe  pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1  remote-address 172.17.5.2 ``` | ``` ike proposal 1  encryption-algorithm aes-cbc 256  dh group14  authentication-algorithm sha2-256  integrity-algorithm hmac-sha2-256 # ike peer pe  pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$ //Set the pre-shared key to 1234567890 (displayed in ciphertext).  ike-proposal 1  remote-address 172.17.5.1 ``` |
  | 7. Configure a service-instance group. | ``` # service-location 1  location slot 1 # service-instance-group group1  service-location 1 ``` | ``` # service-location 1  location slot 1 # service-instance-group group1  service-location 1 ``` |
  | 8. Configure an IPsec tunnel. | ``` ipsec proposal zh //Configure an IPsec proposal.  esp authentication-algorithm sha2-256  esp encryption-algorithm aes 256 # ipsec policy zh 10 isakmp //Configure an IPsec policy.  security acl 3100  ike-peer pe   proposal zh # interface Tunnel 5   //Configure an IPsec tunnel.  ip address 172.17.5.1 255.255.255.0  tunnel-protocol ipsec  ipsec policy zh service-instance-group 1 ``` | ``` ipsec proposal zh //Configure an IPsec proposal.  esp authentication-algorithm sha2-256  esp encryption-algorithm aes 256 # ipsec policy zh 10 isakmp //Configure an IPsec policy.  security acl 3100  ike-peer pe   proposal zh # interface Tunnel 5   //Configure an IPsec tunnel.  ip address 172.17.5.2 255.255.255.0  tunnel-protocol ipsec  ipsec policy zh service-instance-group 1 ``` |
  | 9. Configure traffic steering routes. | ```  ip route-static 2.2.2.2 255.255.255.255 Tunnel5 172.17.5.2  //Steer traffic to the IPsec tunnel for encryption.  ip route-static 172.17.5.2 255.255.255.255 GigabitEthernet0/1/0 192.168.5.2   //Steer IPsec-encrypted traffic to the actual physical outbound interface. ``` | ``` ip route-static 1.1.1.1 255.255.255.255 Tunnel5 172.17.5.1   //Steer traffic to the IPsec tunnel for encryption. ip route-static 172.17.5.1 255.255.255.255 GigabitEthernet 0/1/0 192.168.5.1 //Steer IPsec-encrypted traffic to the actual physical outbound interface. ``` |
  | 10. Configure IS-IS. | ``` isis 1  is-level level-2  network-entity 01.0000.0000.0003.00 # interface LoopBack2  isis enable 1 # interface Tunnel802  isis enable 1 ``` | ``` isis 1  is-level level-2  network-entity 01.0000.0000.0005.00 #  interface LoopBack2  isis enable 1 # interface Tunnel502  isis enable 1 ``` |
  | 11. Configure VPN instances. | ``` ip vpn-instance ipsec_vpn  ipv4-family   route-distinguisher 100:100   vpn-target 200:200 export-extcommunity   vpn-target 200:200 import-extcommunity # interface GigabitEthernet0/1/1  undo shutdown  ip binding vpn-instance ipsec_vpn  ip address 10.1.1.1 255.255.255.0 ``` | ``` ip vpn-instance ipsec_vpn  ipv4-family   route-distinguisher 100:100   vpn-target 200:200 export-extcommunity   vpn-target 200:200 import-extcommunity # interface GigabitEthernet0/1/1  undo shutdown  ip binding vpn-instance ipsec_vpn  ip address 10.2.1.1 255.255.255.0 ``` |
  | 12. Configure BGP. | ``` bgp 100  peer 4.4.4.4 as-number 100  peer 4.4.4.4 connect-interface LoopBack2 #  ipv4-family unicast   undo synchronization   peer 4.4.4.4 enable #  ipv4-family vpnv4   policy vpn-target   peer 4.4.4.4 enable #  ipv4-family vpn-instance ipsec_vpn   import-route direct ``` | ``` bgp 100  peer 3.3.3.3 as-number 100  peer 3.3.3.3 connect-interface LoopBack2 #  ipv4-family unicast   undo synchronization   peer 3.3.3.3 enable #  ipv4-family vpnv4    policy vpn-target    peer 3.3.3.3 enable #  ipv4-family vpn-instance ipsec_vpn   import-route direct ``` |
  | 13. Configure MPLS tunnels. | ``` mpls lsr-id 3.3.3.3 # mpls # mpls ldp  #  ipv4-family # interface Tunnel802 //Enable MPLS LDP on the GRE tunnel interface.  mpls  mpls ldp ``` | ``` mpls lsr-id 4.4.4.4 # mpls # mpls ldp  #  ipv4-family # interface Tunnel502 //Enable MPLS LDP on the GRE tunnel interface.  mpls  mpls ldp ``` |