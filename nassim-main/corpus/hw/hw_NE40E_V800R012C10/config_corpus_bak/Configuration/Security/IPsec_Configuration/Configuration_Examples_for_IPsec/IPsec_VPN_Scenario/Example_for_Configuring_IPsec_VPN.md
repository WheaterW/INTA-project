Example for Configuring IPsec VPN
=================================

This section provides an example for configuring IPsec VPN. This technology enables an IPsec tunnel to be established among two or more VPNs over a public network. By utilizing encryption and authentication algorithms, it ensures the security of VPN connections.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001818336822__fig1):

* PCA belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE0/1/2.
* PCB belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/2.
* Routes between DeviceA and DeviceB are reachable.

Establish an IPsec tunnel between PCA and PCB to encrypt the data transmitted between them.

**Figure 1** IPsec VPN networking diagram![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001818177046.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure VPN instances and bind interfaces to them.
3. Create and configure tunnel interfaces.
4. Configure a static route.
5. Enable IPsec.
6. Configure ACL rules.
7. Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
8. Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
9. Configure IKE peers.
10. Configure IPsec policies.
11. Configure an IPsec service-instance group.
12. Apply the IPsec policies to the tunnel interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Names, RDs, and RTs of VPN instances
* IP addresses of tunnel interfaces
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposals
* Encryption algorithm and authentication algorithm to be used for the IKE proposals

#### Procedure

* Configure DeviceA.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/1/1.
        
        ```
        <DeviceA> system-view
        [~DeviceA] interface GigabitEthernet 0/1/1
        [~DeviceA-GigabitEthernet0/1/1] ip address 192.168.1.1 24
        [*DeviceA-GigabitEthernet0/1/1] quit
        [*DeviceA] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceA] interface GigabitEthernet 0/1/2
        [~DeviceA-GigabitEthernet0/1/2] ip address 10.1.1.1 24
        [*DeviceA-GigabitEthernet0/1/2] quit
        [*DeviceA] commit
        ```
  2. Configure a VPN instance and bind an interface to it.
     
     
     ```
     [~DeviceA] ip vpn-instance vpnA
     ```
     ```
     [*DeviceA-vpn-instance-vpnA] ipv4-family
     ```
     ```
     [*DeviceA-vpn-instance-vpnA-af-ipv4] route-distinguisher 100:1
     ```
     ```
     [*DeviceA-vpn-instance-vpnA-af-ipv4] vpn-target 111:1 both
     ```
     ```
     [*DeviceA-vpn-instance-vpnA-af-ipv4] commit
     ```
     ```
     [~DeviceA-vpn-instance-vpnA-af-ipv4] quit
     ```
     ```
     [*DeviceA] interface gigabitethernet 0/1/2
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] undo shutdown
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] ip binding vpn-instance vpnA
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] ip address 10.1.1.1 24
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceA-GigabitEthernet0/1/2] quit
     ```
  3. Create a tunnel interface.
     
     
     ```
     [~DeviceA] interface Tunnel1
     [*DeviceA-Tunnel1] tunnel-protocol ipsec
     [*DeviceA-Tunnel1] ip address 172.16.1.1 32
     [*DeviceA-Tunnel1] quit
     ```
  4. Configure a static route used to steer traffic to a tunnel. Set the destination address to 10.1.2.0/24 and the next hop address of the outbound interface to 172.16.2.1.
     
     
     ```
     [*DeviceA] ip route-static vpn-instance vpnA 10.1.2.0 255.255.255.0 Tunnel1 172.16.2.1
     [*DeviceA] ip route-static 172.16.2.1 255.255.255.255 192.168.1.2
     [*DeviceA] commit
     ```
  5. Enable IPsec.
     
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
     [*DeviceA-license] quit
     ```
     ```
     [*DeviceA] commit
     ```
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule 5 permit ip vpn-instance vpnA source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
     [*DeviceA-acl-adv-3000] quit
     [*DeviceA] commit
     ```
  7. Configure an IPsec proposal named **tran1**.
     
     
     ```
     [~DeviceA] ipsec proposal tran1
     [*DeviceA-ipsec-proposal-tran1] encapsulation-mode tunnel
     [*DeviceA-ipsec-proposal-tran1] transform esp
     [*DeviceA-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
     [*DeviceA-ipsec-proposal-tran1] esp encryption-algorithm aes 256
     [*DeviceA-ipsec-proposal-tran1] quit
     [*DeviceA] commit
     ```
  8. Configure an IKE proposal numbered 10.
     
     
     ```
     [~DeviceA] ike proposal 10
     [*DeviceA-ike-proposal-10] authentication-method pre-share
     [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
     [*DeviceA-ike-proposal-10] integrity-algorithm hmac-sha2-256
     [*DeviceA-ike-proposal-10] dh group14
     [*DeviceA-ike-proposal-10] quit
     [*DeviceA] commit
     ```
  9. Configure an IKE peer named **b**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceA] ike peer b
     [*DeviceA-ike-peer-b] ike-proposal 10
     [*DeviceA-ike-peer-b] remote-address 172.16.2.1
     [*DeviceA-ike-peer-b] pre-shared-key abcde
     [*DeviceA-ike-peer-b] sa binding vpn-instance vpnA
     [*DeviceA-ike-peer-b] quit
     [*DeviceA] commit
     ```
  10. Configure an IPsec policy named **map1** and numbered 10.
      
      
      ```
      [~DeviceA] ipsec policy map1 10 isakmp
      [*DeviceA-ipsec-policy-isakmp-map1-10] security acl 3000
      [*DeviceA-ipsec-policy-isakmp-map1-10] proposal tran1
      [*DeviceA-ipsec-policy-isakmp-map1-10] ike-peer b
      [*DeviceA-ipsec-policy-isakmp-map1-10] quit
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
  12. Apply the security policy to the tunnel interface.
      
      
      ```
      [~DeviceA] interface Tunnel1
      [*DeviceA-Tunnel1] ipsec policy map1 service-instance-group group1
      [*DeviceA-Tunnel1] quit
      [*DeviceA] commit
      ```
* Configure DeviceB.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/1/1.
        
        ```
        <DeviceB> system-view
        [~DeviceB] interface GigabitEthernet 0/1/1
        [~DeviceB-GigabitEthernet0/1/1] ip address 192.168.1.2 24
        [*DeviceB-GigabitEthernet0/1/1] quit
        [*DeviceB] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceB] interface GigabitEthernet 0/1/2
        [~DeviceB-GigabitEthernet0/1/2] ip address 10.1.2.1 24
        [*DeviceB-GigabitEthernet0/1/2] quit
        [*DeviceB] commit
        ```
  2. Configure a VPN instance and bind an interface to it.
     
     
     ```
     [~DeviceB] ip vpn-instance vpnB
     ```
     ```
     [*DeviceB-vpn-instance-vpnB] ipv4-family
     ```
     ```
     [*DeviceB-vpn-instance-vpnB-af-ipv4] route-distinguisher 100:1
     ```
     ```
     [*DeviceB-vpn-instance-vpnB-af-ipv4] vpn-target 111:1 both
     ```
     ```
     [*DeviceB-vpn-instance-vpnB-af-ipv4] commit
     ```
     ```
     [~DeviceB-vpn-instance-vpnB-af-ipv4] quit
     ```
     ```
     [*DeviceB] interface gigabitethernet 0/1/2
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] undo shutdown
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] ip binding vpn-instance vpnB
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] ip address 10.1.2.1 24
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2] commit
     ```
     ```
     [~DeviceB-GigabitEthernet0/1/2] quit
     ```
  3. Create a tunnel interface.
     
     
     ```
     [~DeviceB] interface Tunnel1
     [*DeviceB-Tunnel1] tunnel-protocol ipsec
     [*DeviceB-Tunnel1] ip address 172.16.2.1 32
     [*DeviceB-Tunnel1] quit
     ```
  4. Configure a static route used to steer traffic to a tunnel. Set the destination address to 10.1.1.0/24 and the next hop address of the outbound interface to 172.16.1.1.
     
     
     ```
     [*DeviceB] ip route-static vpn-instance vpnB 10.1.1.0 255.255.255.0 Tunnel1 172.16.1.1
     [*DeviceB] ip route-static 172.16.1.1 255.255.255.255 192.168.1.1 
     [*DeviceB] commit
     ```
  5. Enable IPsec.
     
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
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceB] acl 3000
     [*DeviceB-acl-adv-3000] rule 5 permit ip vpn-instance vpnB source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255
     [*DeviceB-acl-adv-3000] quit
     [*DeviceB] commit
     ```
  7. Configure an IPsec proposal named **tran1**.
     
     
     ```
     [~DeviceB] ipsec proposal tran1
     [*DeviceB-ipsec-proposal-tran1] encapsulation-mode tunnel
     [*DeviceB-ipsec-proposal-tran1] transform esp
     [*DeviceB-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
     [*DeviceB-ipsec-proposal-tran1] esp encryption-algorithm aes 256
     [*DeviceB-ipsec-proposal-tran1] quit
     [*DeviceB] commit
     ```
  8. Configure an IKE proposal numbered 10.
     
     
     ```
     [~DeviceB] ike proposal 10
     [*DeviceB-ike-proposal-10] authentication-method pre-share
     [*DeviceB-ike-proposal-10] authentication-algorithm sha2-256
     [*DeviceB-ike-proposal-10] integrity-algorithm hmac-sha2-256
     [*DeviceB-ike-proposal-10] dh group14
     [*DeviceB-ike-proposal-10] quit
     [*DeviceB] commit
     ```
  9. Configure an IKE peer named **1**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceB] ike peer 1
     [*DeviceB-ike-peer-1] ike-proposal 10
     [*DeviceB-ike-peer-1] remote-address 172.16.1.1
     [*DeviceB-ike-peer-1] pre-shared-key abcde
     [*DeviceB-ike-peer-1] sa binding vpn-instance vpnB
     [*DeviceB-ike-peer-1] quit
     [*DeviceB] commit
     ```
  10. Configure an IPsec policy template named **temp1** and numbered 1.
      
      
      ```
      [~DeviceB] ipsec policy-template temp1 1
      [*DeviceB-ipsec-policy-templet-temp1-1] security acl 3000
      [*DeviceB-ipsec-policy-templet-temp1-1] proposal tran1
      [*DeviceB-ipsec-policy-templet-temp1-1] ike-peer 1
      [*DeviceB-ipsec-policy-templet-temp1-1] quit
      [*DeviceB] commit
      ```
  11. Create a security policy using a security template.
      
      
      ```
      [~DeviceB] ipsec policy 1 1 isakmp template temp1
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
  13. Apply the security policy to the tunnel interface.
      
      
      ```
      [~DeviceB] interface Tunnel1
      [*DeviceB-Tunnel1] ipsec policy 1 service-instance-group group1
      [*DeviceB-Tunnel1] quit
      [*DeviceB] commit
      ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
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
  interface GigabitEthernet0/1/1 
   ip address 192.168.1.1 24
  #
  ip vpn-instance vpnA
   ipv4-family
    route-distinguisher 100:1
    vpn-target 111:1 both
  #
  interface gigabitethernet 0/1/2
   undo shutdown
   ip binding vpn-instance vpnA
   ip address 10.1.1.1 24
  #
  ip route-static vpn-instance vpnA 10.1.2.0 255.255.255.0 Tunnel1 172.16.2.1
  ip route-static 172.16.2.1 255.255.255.255 192.168.1.2
  #
  acl number 3000
    rule 5 permit ip vpn-instance vpnA source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer b
   pre-shared-key %$%$THBGMJK2659z"C(T{J"-,.2n%$%$
   ike-proposal 10
   remote-address 172.16.2.1
   sa binding vpn-instance vpnA
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer b
   proposal tran1
  #
  interface Tunnel1
   tunnel-protocol ipsec
   ip address 172.16.1.1 32
   ipsec policy map1 service-instance-group group1
  #
  return
  ```
* DeviceB configuration file
  ```
  #
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
  interface GigabitEthernet0/1/1 
   ip address 192.168.1.2 24
  #
  ip vpn-instance vpnB
   ipv4-family
    route-distinguisher 100:1
    vpn-target 111:1 both
  #
  interface gigabitethernet 0/1/2
   undo shutdown
   ip binding vpn-instance vpnB
   ip address 10.1.2.1 24
  #
  ip route-static vpn-instance vpnB 10.1.1.0 255.255.255.0 Tunnel1 172.16.1.1
  ip route-static 172.16.1.1 255.255.255.255 192.168.1.1
  #
  acl number 3000
    rule 5 permit ip vpn-instance vpnB source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256 
   integrity-algorithm hmac-sha2-256
  #
  ike peer 1
   pre-shared-key %$%$THBGMJK2659z"C(T{J"-,.2n%$%$
   ike-proposal 10
   remote-address 172.16.1.1
   sa binding vpn-instance vpnB
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy-template temp1 1
   security acl 3000
   ike-peer 1
   proposal tran1
  #
  ipsec policy 1 1 isakmp template temp1
  #
  interface Tunnel1
   tunnel-protocol ipsec
   ip address 172.16.2.1 32
   ipsec policy 1 service-instance-group group1
  #
  return
  ```