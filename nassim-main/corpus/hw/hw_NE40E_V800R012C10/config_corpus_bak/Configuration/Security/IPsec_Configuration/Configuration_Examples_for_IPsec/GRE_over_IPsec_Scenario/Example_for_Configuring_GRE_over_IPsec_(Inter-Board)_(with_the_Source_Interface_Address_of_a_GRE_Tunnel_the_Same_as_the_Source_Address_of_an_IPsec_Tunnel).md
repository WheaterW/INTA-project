Example for Configuring GRE over IPsec (Inter-Board) (with the Source Interface Address of a GRE Tunnel the Same as the Source Address of an IPsec Tunnel)
==========================================================================================================================================================

In GRE over IPsec networking, IP addresses are saved if the source interface address of a GRE tunnel is the same as the source address of an IPsec tunnel. In an inter-board scenario, GRE encapsulation needs to be performed on a GRE tunnel and IPsec encryption needs to be performed on a VSU or main control board. This configuration applies to common IP and L2VPN/L3VPN packets.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172372481__fig1) shows the network.

**Figure 1** Networking diagram of GRE over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](figure/en-us_image_0000001620017745.png "Click to enlarge")

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE0/1/1.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/1.
* Routes between DeviceA and DeviceB are reachable.

#### Configuration Notes

The GRE tunnel uses a loopback interface as the source interface, and the IPsec tunnel borrows the IP address of a physical interface. To ensure that the source interface address of the GRE tunnel is the same as the source address of the IPsec tunnel, bind the loopback interface to the corresponding VPN instance. This prevents an address conflict with a public network IP address.

The **binding tunnel ipsec** command configuration is automatically generated on the interface whose IP address is borrowed by the IPsec tunnel, and therefore the command does not need to be manually run.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported by a VSU or main control board.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a GRE tunnel between DeviceA and DeviceB to encapsulate multicast and broadcast packets through GRE.
2. Establish an IPsec tunnel between DeviceA and DeviceB to encrypt GRE-encapsulated packets through IPsec.
   * Configure ESP as the security protocol for an IPsec proposal. Specify the authentication algorithm SHA2-256 and the encryption algorithm AES-256 for ESP.
   * Configure an IKE proposal. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
3. Specify a loopback interface as the source interface of the GRE tunnel, and configure the IPsec tunnel to borrow the IP address of a physical interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Tunnel modes and IP addresses of tunnel interfaces; tunnel source and destination addresses
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposals
* Authentication algorithm to be used for the IKE proposals

#### Procedure

* Configure DeviceA.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/1/1.
        
        ```
        <DeviceA> system-view
        [~DeviceA] interface GigabitEthernet 0/1/1
        [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 24
        [*DeviceA-GigabitEthernet0/1/1] quit
        [*DeviceA] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceA] interface GigabitEthernet 0/1/2
        [~DeviceA-GigabitEthernet0/1/2] ip address 172.16.3.1 24
        [*DeviceA-GigabitEthernet0/1/2] quit
        [*DeviceA] commit
        ```
     3. Configure an IP address for Loopback1 and bind Loopback1 to the corresponding VPN instance.
        
        ```
        [~DeviceA] ip vpn-instance vpna
        [~DeviceA-vpn-instance-vpna] ipv4-family
        [*DeviceA-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
        [*DeviceA-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
        [*DeviceA-vpn-instance-vpna-af-ipv4] quit
        [*DeviceA-vpn-instance-vpna] quit
        [*DeviceA] interface loopback1
        [*DeviceA-Loopback1] ip binding vpn-instance vpna
        [*DeviceA-Loopback1] ip address 172.16.3.1 255.255.255.255 
        [*DeviceA-Loopback1] quit
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
     [*DeviceA-license] quit
     ```
     ```
     [*DeviceA] commit
     ```
  3. Configure an IPsec service-instance group.
     
     
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
  4. Create and configure a tunnel interface.
     
     
     ```
     [~DeviceA] interface loopback1
     [*DeviceA-Loopback1] binding tunnel gre
     [*DeviceA-Loopback1] quit
     [~DeviceA] interface Tunnel 2
     [*DeviceA-Tunnel2] tunnel-protocol gre
     [*DeviceA-Tunnel2] ip address 172.21.1.1 24
     [*DeviceA-Tunnel2] source loopback1
     [*DeviceA-Tunnel2] destination vpn-instance vpna 172.16.9.1
     [*DeviceA-Tunnel2] quit
     [*DeviceA] commit
     [~DeviceA] interface Tunnel 1
     [*DeviceA-Tunnel1] tunnel-protocol ipsec
     [*DeviceA-Tunnel1] ip address unnumbered interface GigabitEthernet0/1/2
     [*DeviceA-Tunnel1] quit
     [*DeviceA] commit
     ```
  5. Configure a static route to network B. Assume that the next hop address of DeviceA is 172.16.3.2/24.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a static route to steer IPsec traffic to an IPsec tunnel, you need to configure the IPsec tunnel interface as the outbound interface of the static route and specify the next hop address.
     
     ```
     [~DeviceA] ip route-static 10.1.2.2 255.255.255.255 Tunnel 2
     [*DeviceA] ip route-static vpn-instance vpna 172.16.9.1 255.255.255.255 Tunnel 1 172.16.9.1
     [*DeviceA] ip route-static 172.16.9.1 255.255.255.255 172.16.3.2
     [*DeviceA] commit
     ```
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule permit gre vpn-instance vpna source 172.16.3.1 0.0.0.0 destination 172.16.9.1 0.0.0.0
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
     [*DeviceA-ike-peer-b] remote-address 172.16.9.1 
     [*DeviceA-ike-peer-b] pre-shared-key abcde 
     [*DeviceA-ike-peer-b] sa binding vpn-instance vpna 
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
  11. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceA] interface Tunnel 1
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
        [~DeviceB-GigabitEthernet0/1/1] ip address 10.1.2.1 24
        [*DeviceB-GigabitEthernet0/1/1] quit
        [*DeviceB] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceB] interface GigabitEthernet 0/1/2
        [~DeviceB-GigabitEthernet0/1/2] ip address 172.16.9.1 24
        [*DeviceB-GigabitEthernet0/1/2] quit
        [*DeviceB] commit
        ```
     3. Configure an IP address for Loopback1 and bind Loopback1 to the corresponding VPN instance.
        
        ```
        [~DeviceB] ip vpn-instance vpna
        [~DeviceB-vpn-instance-vpna] ipv4-family
        [*DeviceB-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
        [*DeviceB-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
        [*DeviceB-vpn-instance-vpna-af-ipv4] quit
        [*DeviceB-vpn-instance-vpna] quit
        [*DeviceB] interface loopback1
        [*DeviceB-Loopback1] ip binding vpn-instance vpna
        [*DeviceB-Loopback1] ip address 172.16.9.1 255.255.255.255 
        [*DeviceB-Loopback1] quit
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
  3. Configure an IPsec service-instance group.
     
     
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
  4. Create and configure a tunnel interface.
     
     
     ```
     [~DeviceB] interface loopback1
     [*DeviceB-Loopback1] binding tunnel gre
     [*DeviceB-Loopback1] quit
     [~DeviceB] interface Tunnel 2
     [*DeviceB-Tunnel2] tunnel-protocol gre
     [*DeviceB-Tunnel2] ip address 172.21.1.2 24
     [*DeviceB-Tunnel2] source loopback1
     [*DeviceB-Tunnel2] destination vpn-instance vpna 172.16.3.1
     [*DeviceB-Tunnel2] quit
     [*DeviceB] commit
     [~DeviceB] interface Tunnel 1
     [*DeviceB-Tunnel1] tunnel-protocol ipsec
     [*DeviceB-Tunnel1] ip address unnumbered interface GigabitEthernet0/1/2
     [*DeviceB-Tunnel1] quit
     [*DeviceB] commit
     ```
  5. Configure a static route to network A. Assume that the next hop address of DeviceB is 172.16.9.2/24.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a static route to steer IPsec traffic to an IPsec tunnel, you need to configure the IPsec tunnel interface as the outbound interface of the static route and specify the next hop address.
     
     ```
     [~DeviceB] ip route-static 10.1.1.2 255.255.255.255 Tunnel 2
     [*DeviceB] ip route-static vpn-instance vpna 172.16.3.1 255.255.255.255 Tunnel 1 172.16.3.1
     [*DeviceB] ip route-static 172.16.3.1 255.255.255.255 172.16.9.2
     [*DeviceB] commit
     ```
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceB] acl 3000
     [*DeviceB-acl-adv-3000] rule permit gre vpn-instance vpna source 172.16.9.1 0.0.0.0 destination 172.16.3.1 0.0.0.0
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
  9. Configure an IKE peer named **a**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceB] ike peer a 
     [*DeviceB-ike-peer-a] ike-proposal 10 
     [*DeviceB-ike-peer-a] remote-address 172.16.3.1 
     [*DeviceB-ike-peer-a] pre-shared-key abcde 
     [*DeviceB-ike-peer-a] sa binding vpn-instance vpna 
     [*DeviceB-ike-peer-a] quit
     [*DeviceB] commit
     ```
  10. Configure an IPsec policy named **map1** and numbered 10.
      
      
      ```
      [~DeviceB] ipsec policy map1 10 isakmp 
      [*DeviceB-ipsec-policy-isakmp-map1-10] security acl 3000 
      [*DeviceB-ipsec-policy-isakmp-map1-10] proposal tran1 
      [*DeviceB-ipsec-policy-isakmp-map1-10] ike-peer a 
      [*DeviceB-ipsec-policy-isakmp-map1-10] quit
      [*DeviceB] commit
      ```
  11. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceB] interface Tunnel1 
      [*DeviceB-Tunnel1] ipsec policy map1 service-instance-group group1
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
  acl number 3000
    rule 5 permit gre vpn-instance vpna source 172.16.3.1 0 destination 172.16.9.1 0
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
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
   remote-address 172.16.9.1
   sa binding vpn-instance vpna
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
  interface GigabitEthernet0/1/1 
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.3.1 255.255.255.0 
   binding tunnel ipsec
  #
  interface loopback1
   ip binding vpn-instance vpna
   ip address 172.16.3.1 255.255.255.255 
   binding tunnel gre
  #
  interface Tunnel1
   ip address unnumbered interface GigabitEthernet0/1/2
   tunnel-protocol ipsec
   ipsec policy policy1 service-instance-group group1
  #
  interface Tunnel2
   ip address 172.21.1.1 255.255.255.0
   tunnel-protocol gre
   source loopback1
   destination vpn-instance vpna 172.16.9.1
  #
   ip route-static 10.1.2.2 255.255.255.255 Tunnel 2 172.16.9.1
   ip route-static vpn-instance vpna 172.16.9.1 255.255.255.255 Tunnel 1 172.16.9.1
   ip route-static 172.16.9.1 255.255.255.255 172.16.3.2
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
  acl number 3000
    rule 5 permit gre vpn-instance vpna source 172.16.9.1 0 destination 172.16.3.1 0
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer a
   pre-shared-key %$%$THBGMJK2659z"C(T{J"-,.2n%$%$
   ike-proposal 10
   remote-address 172.16.3.1
   sa binding vpn-instance vpna
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer a
   proposal tran1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.9.1 255.255.255.0
   binding tunnel ipsec
  #
  interface loopback1
   ip binding vpn-instance vpna
   ip address 172.16.9.1 255.255.255.255 
   binding tunnel gre
  #
  interface Tunnel1
   ip address unnumbered interface GigabitEthernet0/1/2
   tunnel-protocol ipsec
   ipsec policy policy1 service-instance-group group1
  #
  interface Tunnel2
   ip address 172.21.1.2 255.255.255.0
   tunnel-protocol gre
   source loopback1
   destination vpn-instance vpna 172.16.3.1
  #
   ip route-static 10.1.1.2 255.255.255.255 Tunnel 2 172.16.3.1
   ip route-static vpn-instance vpna 172.16.3.1 255.255.255.255 Tunnel 1 172.16.3.1
   ip route-static 172.16.3.1 255.255.255.255 172.16.9.2
  #
  return
  ```