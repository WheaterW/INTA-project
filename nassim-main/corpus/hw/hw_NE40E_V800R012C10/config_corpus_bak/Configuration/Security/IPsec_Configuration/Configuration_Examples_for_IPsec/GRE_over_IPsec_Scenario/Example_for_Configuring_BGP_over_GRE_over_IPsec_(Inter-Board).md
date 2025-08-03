Example for Configuring BGP over GRE over IPsec (Inter-Board)
=============================================================

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported by a VSU or main control board.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372490__fig1), DeviceA is a CE, and DeviceB is a PE. The IPsec service boards of both DeviceA and DeviceB reside in slot 1. The GRE tunnel board of DeviceA resides in slot 1, and the GRE tunnel board of DeviceB resides in 1. Establish a GRE over IPsec tunnel between DeviceA and DeviceB. Packets are transmitted through the public MPLS LDP network before being encrypted and after being decrypted on DeviceB, and the DeviceB-side GRE tunnel is bound to an L3VPN. In an inter-board scenario, GRE encapsulation needs to be performed on a GRE tunnel and IPsec encryption needs to be performed on a VSU or main control board.

**Figure 1** Configuring BGP over GRE over IPsec  
![](images/fig_dc_ne_ipsec_cfg_000401.png "Click to enlarge")  
#### Configuration Roadmap

The configuration roadmap for DeviceA is as follows:

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Create a loopback interface and bind GRE to it.
4. Create and configure a tunnel interface.
5. Configure ACL rules.
6. Configure an IKE proposal. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
7. Configure an IPsec proposal. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
8. Configure an IKE peer.
9. Configure an IPsec policy.
10. Configure an IPsec service-instance group.
11. Create and configure an IPsec tunnel.
12. Configure a static route that steers traffic to a tunnel.
13. Configure a static route that steers GRE packets to an IPsec tunnel.
14. Configure a static route that steers encrypted packets to a physical link's outbound interface.
15. Configure BGP.

The configuration roadmap for DeviceB is as follows:

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Create a loopback interface and bind GRE to it.
4. Create and configure a VPN instance.
5. Create and configure a tunnel interface.
6. Configure ACL rules.
7. Configure an IKE proposal.
8. Configure an IPsec proposal.
9. Configure an IKE peer.
10. Configure an IPsec policy.
11. Configure an IPsec service-instance group.
12. Create and configure an IPsec tunnel.
13. Configure a static route that steers traffic to a tunnel.
14. Configure a static route that steers GRE packets to an IPsec tunnel.
15. Configure a static route that steers encrypted packets to a physical link's outbound interface.
16. Configure IS-IS.
17. Configure an MPLS session.
18. Configure BGP.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Security protocol, encapsulation mode, encryption and authentication algorithms that security protocols use
* Pre-shared key

#### Procedure

* Configure DeviceA.

1. Configure IP addresses for interfaces.
   
   * Configure an IP address for GE0/2/1.
     
     ```
     <DeviceA> system-view
     ```
     ```
     [~DeviceA] interface GigabitEthernet 0/2/1
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/1] ip address 10.0.0.1 24
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/1] quit
     ```
     ```
     [*DeviceA] commit
     ```
   * Configure an IP address for GE0/1/1.
     
     ```
     [~DeviceA] interface GigabitEthernet 0/1/1
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] ip address 10.1.0.1 24
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceA] commit
     ```
2. Enable IPsec.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function. After the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command is run, IPsec cannot be configured on the main control board.
   
   Only the following models support this configuration:
   
   NE40E-M2K
   
   NE40E-M2K-B
   
   ```
   [~DeviceA] license
   ```
   ```
   [~DeviceA-license] active ipsec bandwidth-enhance 40 slot 1
   ```
   ```
   [~DeviceA-license] quit
   ```
   ```
   [*DeviceA] commit
   ```
3. Create a loopback interface and bind GRE to it.
   
   ```
   [~DeviceA] interface LoopBack 1
   ```
   ```
   [*DeviceA-LoopBack1] ip address 10.60.60.60 32
   ```
   ```
   [*DeviceA-LoopBack1] binding tunnel gre
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] commit
   ```
4. Create and configure a GRE tunnel.
   
   ```
   [~DeviceA] interface Tunnel 100
   ```
   ```
   [*DeviceA-Tunnel100] ip address 10.0.1.1 24
   ```
   ```
   [*DeviceA-Tunnel100] tunnel-protocol gre
   ```
   ```
   [*DeviceA-Tunnel100] source LoopBack 1
   ```
   ```
   [*DeviceA-Tunnel100] destination 10.108.108.108
   ```
   ```
   [*DeviceA-Tunnel100] quit
   ```
   ```
   [*DeviceA] commit
   ```
5. Configure an advanced ACL numbered 3001 to define the data flows to be protected.
   
   ```
   [~DeviceA] acl 3001
   ```
   ```
   [*DeviceA-acl4-advance-3001] rule permit gre source 10.60.60.60 0 destination 10.108.108.108 0
   ```
   ```
   [*DeviceA-acl4-advance-3001] quit
   ```
   ```
   [*DeviceA] commit
   ```
6. Configure an IKE proposal numbered 1.
   
   ```
   [~DeviceA] ike proposal 1
   ```
   ```
   [*DeviceA-ike-proposal-1] authentication-method pre-share
   ```
   ```
   [*DeviceA-ike-proposal-1] authentication-algorithm sha2-256
   ```
   ```
   [*DeviceA-ike-proposal-1] dh group14
   ```
   ```
   [*DeviceA-ike-proposal-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure an IPsec proposal named **pro1**.
   
   ```
   [~DeviceA] ipsec proposal pro1
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] encapsulation-mode tunnel
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] transform esp
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] esp authentication-algorithm sha2-256
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] esp encryption-algorithm aes 256
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] quit
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure an IKE peer named **peer1**.
   
   ```
   [~DeviceA] ike peer peer1
   ```
   ```
   [*DeviceA-ike-peer-peer1] pre-shared-key 1234567890
   ```
   ```
   [*DeviceA-ike-peer-peer1] ike-proposal 1
   ```
   ```
   [*DeviceA-ike-peer-peer1] remote-address 10.12.0.2 
   ```
   ```
   [*DeviceA-ike-peer-peer1] quit
   ```
   ```
   [*DeviceA] commit
   ```
9. Configure DPD.
   
   ```
   [~DeviceA] ike dpd interval 10 10
   [*DeviceA] commit
   ```
10. Configure an IPsec policy named **policy1** and numbered 1.
    
    ```
    [~DeviceA] ipsec policy policy1 1 isakmp
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] security acl 3001
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] proposal pro1
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] ike-peer peer1
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] quit
    ```
    ```
    [*DeviceA] commit
    ```
11. Configure an IPsec service-instance group.
    ```
    [~DeviceA] service-location 1
    [*DeviceA-service-location-1] location slot 1
    [*DeviceA-service-location-1] commit
    [~DeviceA-service-location-1] quit
    [~DeviceA] service-instance-group group1
    [*DeviceA-service-instance-group-group1] service-location 1
    [*DeviceA-service-instance-group-group1] commit
    [~DeviceA-service-instance-group-group1] quit
    ```
12. Create and configure an IPsec tunnel.
    
    ```
    [~DeviceA] interface Tunnel 1
    ```
    ```
    [*DeviceA-Tunnel1] ip address 10.12.0.1 24
    ```
    ```
    [*DeviceA-Tunnel1] tunnel-protocol ipsec
    ```
    ```
    [*DeviceA-Tunnel1] ipsec policy policy1 service-instance-group group1
    ```
    ```
    [*DeviceA-Tunnel1] quit
    ```
    ```
    [*DeviceA] commit
    ```
13. Configure a static route that steers traffic to a tunnel.
    
    ```
    [~DeviceA] ip route-static 10.0.1.2 255.255.255.255 Tunnel100
    ```
    ```
    [*DeviceA] commit
    ```
14. Configure a static route that steers GRE packets to an IPsec tunnel.
    
    ```
    [*DeviceA] ip route-static 10.108.108.108 32 Tunnel 1 10.12.0.2
    ```
    ```
    [*DeviceA] commit
    ```
15. Configure a static route that steers encrypted packets to a physical link's outbound interface.
    
    ```
    [*DeviceA] ip route-static 10.12.0.2 32 GigabitEthernet 0/2/1 10.0.0.2
    ```
    ```
    [*DeviceA] commit
    ```
16. Configure BGP.
    
    ```
    [~DeviceA] bgp 200
    ```
    ```
    [*DeviceA-bgp] peer 10.0.1.2 as-number 100 
    ```
    ```
    [*DeviceA-bgp] peer 10.0.1.2 ebgp-max-hop 255
    ```
    ```
    [*DeviceA-bgp] peer 10.0.1.2 connect-interface Tunnel 100
    ```
    ```
    [*DeviceA-bgp] ipv4-family unicast
    ```
    ```
    [*DeviceA-bgp-af-ipv4] network 10.1.0.0
    ```
    ```
    [*DeviceA-bgp-af-ipv4] quit
    ```
    ```
    [*DeviceA] commit
    ```

* Configure DeviceB.

1. Configure IP addresses for interfaces.
   
   ```
   [~DeviceB] interface GigabitEthernet0/1/3
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3] ip address 10.0.0.2 24
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceB] commit
   ```
2. Enable IPsec.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function. After the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command is run, IPsec cannot be configured on the main control board.
   
   Only the following models support this configuration:
   
   NE40E-M2K
   
   NE40E-M2K-B
   
   ```
   [~DeviceB] license
   ```
   ```
   [~DeviceB-license] active ipsec bandwidth-enhance 40 slot 1
   ```
   ```
   [*DeviceB-license] quit
   ```
   ```
   [*DeviceB] commit
   ```
3. Create a loopback interface and bind GRE to it.
   
   ```
   [~DeviceB] interface LoopBack 1
   ```
   ```
   [*DeviceB-LoopBack1] ip address 10.108.108.108 32
   ```
   ```
   [*DeviceB-LoopBack1] binding tunnel gre
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] commit
   ```
4. Configure a VPN instance.
   
   ```
   [~DeviceB] ip vpn-instance vpn1
   ```
   ```
   [*DeviceB-vpn-instance-vpn1] route-distinguisher 1:1
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DeviceB-vpn-instance-vpn1] quit
   ```
   ```
   [*DeviceB] commit
   ```
5. Configure a GRE tunnel.
   
   ```
   [~DeviceB] interface Tunnel 100
   ```
   ```
   [*DeviceB-Tunnel100] ip binding vpn-instance vpn1
   ```
   ```
   [*DeviceB-Tunnel100] ip address 10.0.1.2 24
   ```
   ```
   [*DeviceB-Tunnel100] tunnel-protocol gre
   ```
   ```
   [*DeviceB-Tunnel100] source LoopBack 1
   ```
   ```
   [*DeviceB-Tunnel100] destination 10.60.60.60
   ```
   ```
   [*DeviceB-Tunnel100] quit
   ```
   ```
   [*DeviceB] commit
   ```
6. Configure an advanced ACL numbered 3001 to define the data flows to be protected.
   
   ```
   [~DeviceB] acl 3001
   ```
   ```
   [*DeviceB-acl4-advance-3001] rule permit gre source 10.108.108.108 0 destination 10.60.60.60 0
   ```
   ```
   [*DeviceB-acl4-advance-3001] quit
   ```
   ```
   [*DeviceB] commit
   ```
7. Configure an IKE proposal numbered 1.
   
   ```
   [~DeviceB] ike proposal 1
   ```
   ```
   [*DeviceB-ike-proposal-1] authentication-method pre-share
   ```
   ```
   [*DeviceB-ike-proposal-1] authentication-algorithm sha2-256
   ```
   ```
   [*DeviceB-ike-proposal-1] dh group14
   ```
   ```
   [*DeviceB-ike-proposal-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
8. Configure an IPsec proposal named **pro1**.
   
   ```
   [~DeviceB] ipsec proposal pro1
   ```
   ```
   [*DeviceB-ipsec-proposal-pro1] encapsulation-mode tunnel
   ```
   ```
   [*DeviceB-ipsec-proposal-pro1] transform esp
   ```
   ```
   [*DeviceB-ipsec-proposal-pro1] esp authentication-algorithm sha2-256
   ```
   ```
   [*DeviceB-ipsec-proposal-pro1] esp encryption-algorithm aes 256
   ```
   ```
   [*DeviceB-ipsec-proposal-pro1] quit
   ```
   ```
   [*DeviceB] commit
   ```
9. Configure an IKE peer named **peer1**.
   
   ```
   [~DeviceB] ike peer peer1
   ```
   ```
   [*DeviceB-ike-peer-peer1] pre-shared-key 1234567890
   ```
   ```
   [*DeviceB-ike-peer-peer1] ike-proposal 1
   ```
   ```
   [*DeviceB-ike-peer-peer1] remote-address 10.12.0.1
   ```
   ```
   [*DeviceB-ike-peer-peer1] quit
   ```
   ```
   [*DeviceB] commit
   ```
10. Configure DPD.
    
    ```
    [~DeviceB] ike dpd interval 10 10
    [*DeviceB] commit
    ```
11. Configure an IPsec policy named **policy1** and numbered 1.
    
    ```
    [~DeviceB] ipsec policy policy1 1 isakmp
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] security acl 3001
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] proposal pro1
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] ike-peer peer1
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] quit
    ```
    ```
    [*DeviceB] commit
    ```
12. Configure an IPsec service-instance group.
    ```
    [~DeviceB] service-location 1
    [*DeviceB-service-location-1] location slot 1
    [*DeviceB-service-location-1] commit
    [~DeviceB-service-location-1] quit
    [~DeviceB] service-instance-group group1
    [*DeviceB-service-instance-group-group1] service-location 1
    [*DeviceB-service-instance-group-group1] commit
    [~DeviceB-service-instance-group-group1] quit
    ```
13. Create and configure an IPsec tunnel.
    
    ```
    [~DeviceB] interface Tunnel 1
    ```
    ```
    [*DeviceB-Tunnel1] ip address 10.12.0.2 24
    ```
    ```
    [*DeviceB-Tunnel1] tunnel-protocol ipsec
    ```
    ```
    [*DeviceB-Tunnel1] ipsec policy policy1 service-instance-group group1
    ```
    ```
    [*DeviceB-Tunnel1] quit
    ```
    ```
    [*DeviceB] commit
    ```
14. Configure a static route that steers traffic to a tunnel.
    
    ```
    [~DeviceB] ip route-static vpn-instance vpn1 10.0.1.1 255.255.255.255 Tunnel100
    ```
    ```
    [*DeviceB] commit
    ```
15. Configure a static route that steers GRE packets to an IPsec tunnel.
    
    ```
    [*DeviceB] ip route-static 10.60.60.60 32 Tunnel 1 10.12.0.1
    ```
    ```
    [*DeviceB] commit
    ```
16. Configure a static route that steers encrypted packets to a physical link's outbound interface.
    
    ```
    [*DeviceB] ip route-static 10.12.0.1 32 GigabitEthernet 0/1/3 10.0.0.1
    ```
    ```
    [*DeviceB] commit
    ```
17. Configure IS-IS.
    
    ```
    [~DeviceB] isis 1
    ```
    ```
    [*DeviceB-isis-1] network-entity 00.0000.0000.0108.00
    ```
    ```
    [*DeviceB-isis-1] quit
    ```
    ```
    [*DeviceB] commit
    ```
18. Configure an MPLS session.
    
    ```
    [~DeviceB] interface LoopBack 0
    ```
    ```
    [*DeviceB-LoopBack0] ip address 10.108.108.108 32
    ```
    ```
    [*DeviceB-LoopBack0] isis enable 1
    ```
    ```
    [*DeviceB-LoopBack0] quit
    ```
    ```
    [*DeviceB] mpls lsr-id 10.108.108.108
    ```
    ```
    [*DeviceB] mpls
    ```
    ```
    [*DeviceB-mpls] quit
    ```
    ```
    [*DeviceB] mpls ldp
    ```
    ```
    [*DeviceB-mpls-ldp] quit
    ```
    ```
    [*DeviceB] interface GigabitEthernet0/1/2
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/2] ip address 10.2.0.1 24
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/2] isis enable 1
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/2] mpls
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/2] mpls ldp
    ```
    ```
    [*DeviceB-GigabitEthernet0/1/2] quit
    ```
    ```
    [*DeviceB] commit
    ```
19. Configure BGP.
    
    ```
    [~DeviceB] bgp 100
    ```
    ```
    [*DeviceB-bgp] peer 10.2.0.2 as-number 100
    ```
    ```
    [*DeviceB-bgp] peer 10.2.0.2 connect-interface LoopBack0
    ```
    ```
    [*DeviceB-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DeviceB-bgp-vpn1] peer 10.0.1.1 as-number 200
    ```
    ```
    [*DeviceB-bgp-vpn1] peer 10.0.1.1 ebgp-max-hop 255
    ```
    ```
    [*DeviceB-bgp-vpn1] peer 10.0.1.1 connect-interface Tunnel 100
    ```
    ```
    [*DeviceB-bgp-vpn1] quit
    ```
    ```
    [*DeviceB] commit
    ```

#### Configuration Files

* DeviceA configuration file

```
#
```
```
 sysname DeviceA
```
```
#
license
 active ipsec bandwidth-enhance 40 slot 1 //Perform this configuration for the VSUP.
```
```
#
service-location 1
 location slot 1
#
service-instance-group group1
 service-location 1
```
```
#
```
```
ike dpd interval 10 10
```
```
#
```
```
acl number 3001 
```
```
 rule 5 permit gre source 10.60.60.60 0 destination 10.108.108.108 0
```
```
#
```
```
ike proposal 1
```
```
 encryption-algorithm aes-cbc 256
```
```
 dh group14
```
```
 authentication-algorithm sha2-256
```
```
 integrity-algorithm hmac-sha2-256
```
```
#
```
```
ike peer peer1
```
```
 pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$
```
```
 ike-proposal 1
```
```
 remote-address 10.12.0.2
```
```
#
```
```
ipsec proposal pro1
```
```
 esp authentication-algorithm sha2-256
```
```
 esp encryption-algorithm aes 256
```
```
#
```
```
ipsec policy policy1 1 isakmp
```
```
 security acl 3001
```
```
 ike-peer peer1
```
```
 proposal pro1
```
```
#
```
```
interface GigabitEthernet0/2/1
```
```
 undo shutdown
```
```
 ip address 10.0.0.1 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/1/1
```
```
 undo shutdown
```
```
 ip address 10.1.0.1 255.255.255.0
```
```
#
```
```
interface LoopBack1
```
```
 ip address 10.60.60.60 255.255.255.255
```
```
 binding tunnel gre
```
```
#
```
```
interface Tunnel1
```
```
 ip address 10.12.0.1 255.255.255.0
```
```
 tunnel-protocol ipsec
```
```
 ipsec policy policy1 service-instance-group group1
```
```
#
```
```
interface Tunnel100
```
```
 ip address 10.0.1.1 255.255.255.0
```
```
 tunnel-protocol gre
```
```
 source LoopBack1
```
```
 destination 10.108.108.108
```
```
#
```
```
bgp 200
```
```
 peer 10.0.1.2 as-number 100
```
```
 peer 10.0.1.2 ebgp-max-hop 255
```
```
 peer 10.0.1.2 connect-interface Tunnel100
```
```
 #
```
```
 ipv4-family unicast
```
```
  undo synchronization
```
```
  network 10.1.0.0 255.255.255.0
```
```
  peer 10.0.1.2 enable
```
```
#
```
```
 ip route-static 10.0.1.2 255.255.255.255 Tunnel100
```
```
 ip route-static 10.12.0.2 255.255.255.255 GigabitEthernet0/2/1 10.0.0.2
```
```
 ip route-static 10.108.108.108 255.255.255.255 Tunnel1 10.12.0.2
```
```
#
```
```
return
```

* DeviceB configuration file

```
#
```
```
 sysname DeviceB
```
```
#
license
 active ipsec bandwidth-enhance 40 slot 1 //Perform this configuration for the VSUP.
```
```
#
service-location 1
 location slot 1
#
service-instance-group group1
 service-location 1
```
```
#
```
```
ike dpd interval 10 10
```
```
#
```
```
ip vpn-instance vpn1
```
```
 ipv4-family
```
```
  route-distinguisher 1:1
```
```
  apply-label per-instance
```
```
  vpn-target 1:1 export-extcommunity
```
```
  vpn-target 1:1 import-extcommunity
```
```
#
```
```
mpls lsr-id 10.108.108.108
```
```
#
```
```
mpls
```
```
#
```
```
mpls ldp
```
```
 #
 ipv4-family
```
```
#
```
```
acl number 3001
```
```
 rule 5 permit gre source 10.108.108.108 0 destination 10.60.60.60 0
```
```
#
```
```
ike proposal 1
```
```
 encryption-algorithm aes-cbc 256
```
```
 dh group14
```
```
 authentication-algorithm sha2-256
```
```
 integrity-algorithm hmac-sha2-256
```
```
#
```
```
ike peer peer1
```
```
 pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$
```
```
 ike-proposal 1
```
```
 remote-address 10.12.0.1
```
```
#
```
```
ipsec proposal pro1
```
```
 esp authentication-algorithm sha2-256
```
```
 esp encryption-algorithm aes 256
```
```
#
```
```
ipsec policy policy1 1 isakmp
```
```
 security acl 3001
```
```
 ike-peer peer1
```
```
 proposal pro1
```
```
#
```
```
isis 1
```
```
 network-entity 00.0000.0000.0108.00
```
```
#
```
```
interface GigabitEthernet0/1/3
```
```
 undo shutdown
```
```
 ip address 10.0.0.2 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
 undo shutdown
```
```
 ip address 10.2.0.1 255.255.255.0
```
```
 isis enable 1
```
```
 mpls
```
```
 mpls ldp
```
```
#
```
```
interface LoopBack0
```
```
 ip address 10.108.108.108 255.255.255.255
```
```
 isis enable 1
```
```
#
```
```
interface LoopBack1
```
```
 ip address 10.108.108.108 255.255.255.255
```
```
 binding tunnel gre
```
```
#
```
```
interface Tunnel1
```
```
 ip address 10.12.0.2 255.255.255.0
```
```
 tunnel-protocol ipsec
```
```
 ipsec policy policy1 service-instance-group group1
```
```
#
```
```
interface Tunnel100
```
```
 ip binding vpn-instance vpn1
```
```
 ip address 10.0.1.2 255.255.255.0
```
```
 tunnel-protocol gre
```
```
 source LoopBack1
```
```
 destination 10.60.60.60
```
```
#
```
```
bgp 100
```
```
 peer 10.2.0.2 as-number 100
```
```
 peer 10.2.0.2 connect-interface LoopBack0
```
```
#
```
```
 ipv4-family unicast
```
```
  undo synchronization
```
```
  peer 10.2.0.2 enable
```
```
#
```
```
 ipv4-family vpnv4
```
```
  policy vpn-target
```
```
  peer 10.2.0.2 enable
```
```
#
```
```
 ipv4-family vpn-instance vpn1
```
```
  import-route direct
```
```
  peer 10.0.1.1 as-number 200 
```
```
  peer 10.0.1.1 ebgp-max-hop 255 
```
```
  peer 10.0.1.1 connect-interface Tunnel100
```
```
#
```
```
 ip route-static 10.12.0.1 255.255.255.255 GigabitEthernet0/1/3 10.0.0.1
```
```
 ip route-static 10.60.60.60 255.255.255.255 Tunnel1 10.12.0.1
```
```
 ip route-static vpn-instance vpn1 10.0.1.1 255.255.255.255 Tunnel100
```
```
#
```
```
return
```