Example for Configuring BGP over GRE over IPsec (Intra-Board)
=============================================================

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the following models support this configuration:

NE40E-M2K

NE40E-M2K-B

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372487__fig1), DeviceA is a CE, and DeviceB is a PE. The VSUs of both DeviceA and DeviceB reside in slot 1. Establish a GRE over IPsec tunnel between DeviceA and DeviceB. Packets are transmitted through the public MPLS LDP network before being encrypted and after being decrypted on DeviceB, and the DeviceB-side GRE tunnel is bound to an L3VPN. In an intra-board scenario, both GRE encapsulation and IPsec encryption need to be performed on a VSU.

**Figure 1** Configuring BGP over GRE over IPsec  
![](images/fig_dc_ne_ipsec_cfg_000301.png "Click to enlarge")  
#### Configuration Roadmap

The configuration roadmap for DeviceA is as follows:

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Create and configure a tunnel interface.
4. Configure a static route that steers traffic to a tunnel.
5. Configure a static route that steers encrypted packets to a physical link's outbound interface.
6. Configure BGP.
7. Configure ACL rules.
8. Configure an IKE proposal. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
9. Configure an IPsec proposal. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
10. Configure an IKE peer.
11. Configure an IPsec policy.
12. Configure an IPsec service-instance group.
13. Apply the IPsec policy.

The configuration roadmap for DeviceB is as follows:

1. Configure IS-IS.
2. Configure an MPLS session.
3. Configure IP addresses for interfaces.
4. Enable IPsec.
5. Create and configure a VPN instance.
6. Create and configure a tunnel interface.
7. Configure a static route that steers traffic to a tunnel.
8. Configure a static route that steers encrypted packets to a physical link's outbound interface.
9. Configure BGP.
10. Configure ACL rules.
11. Configure an IKE proposal.
12. Configure an IPsec proposal.
13. Configure an IKE peer.
14. Configure an IPsec policy.
15. Configure an IPsec service-instance group.
16. Apply the IPsec policy.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Security protocol, encapsulation mode, encryption and authentication algorithms that security protocols use
* Pre-shared key

#### Procedure

* Configure DeviceA.

1. Configure IP addresses for interfaces.
   
   * Configure an IP address for GE0/2/2.
     
     ```
     <DeviceA> system-view
     ```
     ```
     [~DeviceA] interface GigabitEthernet0/2/2
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/2] ip address 10.0.1.1 24
     ```
     ```
     [*DeviceA-GigabitEthernet0/2/2] quit
     ```
     ```
     [*DeviceA] commit
     ```
   * Configure an IP address for GE0/3/1.
     
     ```
     [~DeviceA] interface GigabitEthernet0/3/1
     ```
     ```
     [*DeviceA-GigabitEthernet0/3/1] ip address 10.116.1.1 24
     ```
     ```
     [*DeviceA-GigabitEthernet0/3/1] quit
     ```
     ```
     [*DeviceA] commit
     ```
2. Enable IPsec.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function.
   
   ```
   [~DeviceA] license
   [~DeviceA-license] active ipsec bandwidth-enhance 40 slot 1
   [*DeviceA-license] quit
   [*DeviceA] commit
   ```
3. Create and configure a tunnel interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a GRE over IPsec intra-board scenario, a tunnel interface name must be in the format of slot ID/card ID/interface ID.
   
   ```
   [~DeviceA] interface LoopBack1
   ```
   ```
   [*DeviceA-LoopBack1] ip address 10.60.60.60 32
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface Tunnel 0/0/1
   ```
   ```
   [*DeviceA-Tunnel0/0/1] ip address 10.200.1.1 24
   ```
   ```
   [*DeviceA-Tunnel0/0/1] tunnel-protocol gre
   ```
   ```
   [*DeviceA-Tunnel0/0/1] source LoopBack1
   ```
   ```
   [*DeviceA-Tunnel0/0/1] destination 10.200.200.200
   ```
   ```
   [*DeviceA-Tunnel0/0/1] quit
   ```
   ```
   [*DeviceA] commit
   ```
4. Configure a static route that steers traffic to a tunnel.
   
   ```
   [~DeviceA] ip route-static 10.200.1.2 255.255.255.255 Tunnel0/0/1 10.200.200.200
   ```
   ```
   [*DeviceA] commit
   ```
5. Configure a static route that steers encrypted packets to a physical link's outbound interface.
   
   ```
   [*DeviceA] ip route-static 10.200.200.200 255.255.255.255 10.0.1.2
   ```
   ```
   [*DeviceA] commit
   ```
6. Configure BGP.
   
   ```
   [~DeviceA] bgp 200
   ```
   ```
   [*DeviceA-bgp] peer 10.200.1.2 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 10.200.1.2 ebgp-max-hop 255
   ```
   ```
   [*DeviceA-bgp] peer 10.200.1.2 connect-interface Tunnel0/0/1
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
7. Configure an advanced ACL numbered 3001 to define the data flows to be protected.
   
   ```
   [~DeviceA] acl 3001
   ```
   ```
   [*DeviceA-acl4-advance-3001] rule permit gre source 10.60.60.60 0 destination 10.200.200.200 0
   ```
   ```
   [*DeviceA-acl4-advance-3001] quit
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure an IKE proposal numbered 1.
   
   ```
   [~DeviceA] ike proposal 1
   ```
   ```
   [*DeviceA-ike-proposal-1] encryption-algorithm aes-cbc 256
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
9. Configure an IPsec proposal named **pro1**.
   
   ```
   [~DeviceA] ipsec proposal pro1
   ```
   ```
   [*DeviceA-ipsec-proposal-pro1] esp authentication-algorithm sha1
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
10. Configure an IKE peer named **peer1**.
    
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
    [*DeviceA-ike-peer-peer1] remote-address 10.200.200.200
    ```
    ```
    [*DeviceA-ike-peer-peer1] quit
    ```
    ```
    [*DeviceA] commit
    ```
11. Configure an IPsec policy named **policy1** and numbered 1.
    
    ```
    [~DeviceA] ipsec policy policy1 1 isakmp
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] security acl 3001
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] ike-peer peer1
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] proposal pro1
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] local-address 10.60.60.60
    ```
    ```
    [*DeviceA-ipsec-policy-isakmp-policy1-1] quit
    ```
    ```
    [*DeviceA] commit
    ```
12. Configure an IPsec service-instance group named **group1**.
    
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
13. Apply the IPsec policy named **policy1** on the tunnel interface.
    
    ```
    [~DeviceA] interface Tunnel 0/0/1
    ```
    ```
    [*DeviceA-Tunnel0/0/1] ipsec policy policy1 service-instance-group group1
    ```
    ```
    [*DeviceA-Tunnel0/0/1] quit
    ```
    ```
    [*DeviceA] commit
    ```

* Configure DeviceB.

1. Configure IS-IS.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] network-entity 00.0000.0000.0200.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
2. Configure an MPLS session.
   
   ```
   [~DeviceB] interface LoopBack0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 10.200.200.200 32 
   ```
   ```
   [*DeviceB-LoopBack0] isis enable 1
   ```
   ```
   [*DeviceB-LoopBack0] quit
   ```
   ```
   [*DeviceB] mpls lsr-id 10.200.200.200
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
   [*DeviceB] commit
   ```
3. Configure IP addresses for interfaces.
   
   * Configure an IP address for GE0/1/1.
     
     ```
     <DeviceB> system-view
     ```
     ```
     [~DeviceB] interface GigabitEthernet0/1/1
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] ip address 10.0.1.2 24
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceB] commit
     ```
   * Configure an IP address for GE0/2/2.
     
     ```
     [~DeviceB] interface GigabitEthernet0/2/2
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/2] ip address 10.201.1.1 24
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/2] isis enable 1
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/2] mpls
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/2] mpls ldp
     ```
     ```
     [*DeviceB-GigabitEthernet0/2/2] quit
     ```
     ```
     [*DeviceB] commit
     ```
4. Enable IPsec.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function.
   
   ```
   [~DeviceB] license
   [~DeviceB-license] active ipsec bandwidth-enhance 40 slot 1
   [*DeviceB-license] quit
   [*DeviceB] commit
   ```
5. Create and configure a VPN instance.
   
   ```
   [~DeviceB] ip vpn-instance vpn1
   ```
   ```
   [*DeviceB-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] route-distinguisher 1:1
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 export-extcommunity
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 import-extcommunity
   ```
   ```
   [*DeviceB-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DeviceB] commit
   ```
6. Create and configure a tunnel interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In a GRE over IPsec intra-board scenario, a tunnel interface name must be in the format of slot ID/card ID/interface ID.
   
   ```
   [~DeviceB] interface LoopBack1
   ```
   ```
   [*DeviceB-LoopBack1] ip address 10.200.200.200 32
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] interface Tunnel 0/0/1
   ```
   ```
   [*DeviceB-Tunnel0/0/1] ip binding vpn-instance vpn1
   ```
   ```
   [*DeviceB-Tunnel0/0/1] ip address 10.200.1.2 24
   ```
   ```
   [*DeviceB-Tunnel0/0/1] tunnel-protocol gre
   ```
   ```
   [*DeviceB-Tunnel0/0/1] source LoopBack1
   ```
   ```
   [*DeviceB-Tunnel0/0/1] destination 10.60.60.60
   ```
   ```
   [*DeviceB-Tunnel0/0/1] quit
   ```
   ```
   [*DeviceB] commit
   ```
7. Configure a static route that steers traffic to a tunnel.
   
   ```
   [~DeviceB] ip route-static vpn-instance vpn1 10.200.1.1 255.255.255.255 Tunnel0/0/1 10.60.60.60
   ```
   ```
   [*DeviceB] commit
   ```
8. Configure a static route that steers encrypted packets to a physical link's outbound interface.
   
   ```
   [*DeviceB] ip route-static 10.60.60.60 255.255.255.255 10.0.1.1
   ```
   ```
   [*DeviceB] commit
   ```
9. Configure BGP.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] peer 10.201.1.2 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 10.201.1.2 connect-interface LoopBack0
   ```
   ```
   [*DeviceB-bgp] ipv4-family vpnv4
   ```
   ```
   [*DeviceB-bgp-af-vpnv4] peer 10.201.1.2 enable
   ```
   ```
   [*DeviceB-bgp-af-vpnv4] quit
   ```
   ```
   [*DeviceB-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*DeviceB-bgp-vpn1] import-route direct
   ```
   ```
   [*DeviceB-bgp-vpn1] peer 10.200.1.1 as-number 200 
   ```
   ```
   [*DeviceB-bgp-vpn1] peer 10.200.1.1 ebgp-max-hop 255 
   ```
   ```
   [*DeviceB-bgp-vpn1] peer 10.200.1.1 connect-interface Tunnel0/0/1
   ```
   ```
   [*DeviceB-bgp-vpn1] quit
   ```
   ```
   [*DeviceB] commit
   ```
10. Configure an advanced ACL numbered 3001 to define the data flows to be protected.
    
    ```
    [~DeviceB] acl 3001
    ```
    ```
    [*DeviceB-acl4-advance-3001] rule permit ip vpn-instance vpn1 source 10.200.200.200 0 destination 10.60.60.60 0
    ```
    ```
    [*DeviceB-acl4-advance-3001] quit
    ```
    ```
    [*DeviceB] commit
    ```
11. Configure an IKE proposal numbered 1.
    
    ```
    [~DeviceB] ike proposal 1
    ```
    ```
    [*DeviceB-ike-proposal-1] encryption-algorithm aes-cbc 256
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
12. Configure an IPsec proposal named **pro1**.
    
    ```
    [~DeviceB] ipsec proposal pro1
    ```
    ```
    [*DeviceB-ipsec-proposal-pro1] esp authentication-algorithm sha1
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
13. Configure an IKE peer named **peer1**.
    
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
    [*DeviceB-ike-peer-peer1] remote-address 10.60.60.60
    ```
    ```
    [*DeviceB-ike-peer-peer1] sa binding vpn-instance vpn1
    ```
    ```
    [*DeviceB-ike-peer-peer1] quit
    ```
    ```
    [*DeviceB] commit
    ```
14. Configure an IPsec policy named **policy1** and numbered 1.
    
    ```
    [~DeviceB] ipsec policy policy1 1 isakmp
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] security acl 3001
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] ike-peer peer1
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] proposal pro1
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] local-address 10.200.200.200
    ```
    ```
    [*DeviceB-ipsec-policy-isakmp-policy1-1] quit
    ```
    ```
    [*DeviceB] commit
    ```
15. Configure an IPsec service-instance group named **group1**.
    
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
16. Apply the IPsec policy named **policy1** on the tunnel interface.
    
    ```
    [~DeviceB] interface Tunnel 0/0/1
    ```
    ```
    [*DeviceB-Tunnel0/0/1] ipsec policy policy1 service-instance-group group1
    ```
    ```
    [*DeviceB-Tunnel0/0/1] quit
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
acl number 3001 
```
```
 rule permit gre source 10.60.60.60 0 destination 10.200.200.200 0 
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
 remote-address 10.200.200.200
```
```
#
```
```
ipsec proposal pro1
```
```
 esp authentication-algorithm sha1
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
 local-address 10.60.60.60
```
```
#
```
```
interface GigabitEthernet0/2/2
```
```
 undo shutdown
```
```
 ip address 10.0.1.1 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/3/1
```
```
 undo shutdown
```
```
 ip address 10.116.1.1 255.255.255.0
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
 binding tunnel ipsec
```
```
#
```
```
interface Tunnel0/0/1
```
```
 ip address 10.200.1.1 255.255.255.0
```
```
 tunnel-protocol gre
```
```
 source LoopBack1
```
```
 destination 10.200.200.200
```
```
 ipsec policy policy1 service-instance-group group1
```
```
#
```
```
bgp 200
```
```
 peer 10.200.1.2 as-number 100
```
```
 peer 10.200.1.2 ebgp-max-hop 255
```
```
 peer 10.200.1.2 connect-interface Tunnel0/0/1
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
  import-route direct
```
```
  peer 10.200.1.2 enable
```
```
#
```
```
ip route-static 10.200.1.2 255.255.255.255 Tunnel0/0/1 10.200.200.200
```
```
ip route-static 10.200.200.200 255.255.255.255 10.0.1.2
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
mpls lsr-id 10.200.200.200
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
 rule permit ip vpn-instance vpn1 source 10.200.200.200 0 destination 10.60.60.60 0
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
 remote-address 10.60.60.60
```
```
 sa binding vpn-instance vpn1
```
```
#
```
```
ipsec proposal pro1
```
```
 esp authentication-algorithm sha1
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
 local-address 10.200.200.200
```
```
#
```
```
isis 1
```
```
 network-entity 00.0000.0000.0200.00
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
 ip address 10.0.1.2 255.255.255.0
```
```
#
```
```
interface GigabitEthernet0/2/2
```
```
 undo shutdown
```
```
 ip address 10.201.1.1 255.255.255.0
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
 ip address 10.200.200.200 255.255.255.255
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
 ip address 10.200.200.200 255.255.255.255
```
```
 binding tunnel ipsec
```
```
#
```
```
interface Tunnel0/0/1
```
```
 ip binding vpn-instance vpn1
```
```
 ip address 10.200.1.2 255.255.255.0 
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
 ipsec policy policy1 service-instance-group group1
```
```
#
```
```
bgp 100
```
```
 peer 10.201.1.2 as-number 100
```
```
 peer 10.201.1.2 connect-interface LoopBack0
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
  peer 10.201.1.2 enable
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
  peer 10.201.1.2 enable
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
  peer 10.200.1.1 as-number 200
```
```
  peer 10.200.1.1 ebgp-max-hop 255
```
```
  peer 10.200.1.1 connect-interface Tunnel0/0/1
```
```
#
```
```
ip route-static 10.60.60.60 255.255.255.255 10.0.1.1
```
```
ip route-static vpn-instance vpn1 10.200.1.1 255.255.255.255 Tunnel0/0/1 10.60.60.60
```
```
#
```
```
return
```