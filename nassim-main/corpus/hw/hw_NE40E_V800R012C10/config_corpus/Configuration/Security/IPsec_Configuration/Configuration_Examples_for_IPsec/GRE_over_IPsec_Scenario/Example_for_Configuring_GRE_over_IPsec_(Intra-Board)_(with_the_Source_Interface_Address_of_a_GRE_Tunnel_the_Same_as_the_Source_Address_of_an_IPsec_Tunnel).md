Example for Configuring GRE over IPsec (Intra-Board) (with the Source Interface Address of a GRE Tunnel the Same as the Source Address of an IPsec Tunnel)
==========================================================================================================================================================

In GRE over IPsec networking, IP addresses are saved if the source interface address of a GRE tunnel is the same as the source address of an IPsec tunnel. In an intra-board scenario, both GRE encapsulation and IPsec encryption need to be performed on a VSU. This configuration applies to common IP packets.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172372478__fig1) shows the network.

**Figure 1** Networking diagram of GRE over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_004201.png "Click to enlarge")  

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE0/1/1.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/1.
* Routes between DeviceA and DeviceB are reachable.

The network is required to implement the following functions:

* Transmits multicast and broadcast packets, which are not supported by IPsec, between PCA and PCB.
* Encrypts the packets transmitted between PCA and PCB.
* Allows the source interface address of a GRE tunnel to be the same as the source IP address of an IPsec tunnel so as to conserve IP addresses.


#### Configuration Notes

In a GRE over IPsec intra-board scenario, a tunnel interface name must be in the format of slot ID/card ID/interface ID.

The **binding tunnel ipsec** command configuration is automatically generated on the interface whose IP address is borrowed by the IPsec tunnel, and therefore the command does not need to be manually run. In addition, RIP or OSPF cannot be configured on the interface whose IP address is borrowed by the IPsec tunnel. Otherwise, the multicast and broadcast functions used by these protocols are affected.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the following models support this configuration:

NE40E-M2K

NE40E-M2K-B


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the VSU supports this configuration.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a GRE tunnel between DeviceA and DeviceB to encapsulate multicast and broadcast packets through GRE.
2. Establish an IPsec tunnel between DeviceA and DeviceB to encrypt GRE-encapsulated packets through IPsec.
   * Configure ESP as the security protocol for an IPsec proposal. Specify the authentication algorithm SHA2-256 and the encryption algorithm AES-256 for ESP.
   * Configure an IKE proposal. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.

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
  2. Enable IPsec.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function.
     
     
     
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
     [DeviceA] interface Tunnel 0/0/1
     [*DeviceA-Tunnel0/0/1] tunnel-protocol gre
     [*DeviceA-Tunnel0/0/1] ip address unnumbered interface GigabitEthernet0/1/2
     [*DeviceA-Tunnel0/0/1] source 172.16.3.1
     [*DeviceA-Tunnel0/0/1] destination 172.16.9.1
     [*DeviceA-Tunnel0/0/1] quit
     [*DeviceA] commit
     ```
  5. Configure a static route to network B. Assume that the next hop address of DeviceA is 172.16.3.2/24.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a static route to steer IPsec traffic to an IPsec tunnel, you need to configure the IPsec tunnel interface as the outbound interface of the static route and specify the next hop address.
     
     ```
     [~DeviceA] ip route-static 10.1.2.2 255.255.255.255 Tunnel0/0/1 172.16.9.1
     [*DeviceA] ip route-static 172.16.9.1 255.255.255.255 172.16.3.2
     [*DeviceA] commit
     ```
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule permit gre source 172.16.3.1 0.0.0.0 destination 172.16.9.1 0.0.0.0
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
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If GRE encapsulation is configured on a VSU service board, configure the local address in the IPsec policy view.
      
      ```
      [~DeviceA-ipsec-policy-isakmp-map1-10] local-address 172.16.3.1
      ```
  11. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceA] interface Tunnel0/0/1 
      [*DeviceA-Tunnel0/0/1] ipsec policy map1 service-instance-group group1
      [*DeviceA-Tunnel0/0/1] quit
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
  2. Enable IPsec.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function.
     
     
     
     ```
     [~DeviceB] license
     [~DeviceB-license] active ipsec bandwidth-enhance 40 slot 1
     [*DeviceB-license] quit
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
     [DeviceB] interface Tunnel 0/0/1
     [*DeviceB-Tunnel0/0/1] tunnel-protocol gre
     [*DeviceB-Tunnel0/0/1] ip address unnumbered interface GigabitEthernet0/1/2
     [*DeviceB-Tunnel0/0/1] source 172.16.9.1
     [*DeviceB-Tunnel0/0/1] destination 172.16.3.1
     [*DeviceB-Tunnel0/0/1] quit
     [*DeviceB] commit
     ```
  5. Configure a static route to network A. Assume that the next hop address of DeviceB is 172.16.9.2/24.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a static route to steer IPsec traffic to an IPsec tunnel, you need to configure the IPsec tunnel interface as the outbound interface of the static route and specify the next hop address.
     
     ```
     [~DeviceB] ip route-static 10.1.1.2 255.255.255.255 Tunnel0/0/1 172.16.3.1
     [*DeviceB] ip route-static 172.16.3.1 255.255.255.255 172.16.9.2
     [*DeviceB] commit
     ```
  6. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceB] acl 3000
     [*DeviceB-acl-adv-3000] rule permit gre source 172.16.9.1 0.0.0.0 destination 172.16.3.1 0.0.0.0
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
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If GRE encapsulation is configured on a VSU service board, configure the local address in the IPsec policy view.
      
      ```
      [~DeviceB-ipsec-policy-isakmp-map1-10] local-address 172.16.9.1
      ```
  11. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceB] interface Tunnel0/0/1 
      [*DeviceB-Tunnel0/0/1] ipsec policy map1 service-instance-group group1
      [*DeviceB-Tunnel0/0/1] quit
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
    rule 5 permit gre source 172.16.3.1 0 destination 172.16.9.1 0
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
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer b
   proposal tran1
   local-address 172.16.3.1
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
  interface Tunnel0/0/1 
   ip address unnumbered interface GigabitEthernet0/1/2
   tunnel-protocol gre
   source 172.16.3.1
   destination 172.16.9.1
   ipsec policy map1 service-instance-group group1
  #
   ip route-static 10.1.2.2 255.255.255.255 Tunnel0/0/1 172.16.9.1
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
    rule 5 permit gre source 172.16.9.1 0 destination 172.16.3.1 0
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
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer a
   proposal tran1
   local-address 172.16.9.1
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
  interface Tunnel0/0/1
   ip address unnumbered interface GigabitEthernet0/1/2
   tunnel-protocol gre
   source 172.16.9.1
   destination 172.16.3.1
   ipsec policy map1 service-instance-group group1
  #
   ip route-static 10.1.1.2 255.255.255.255 Tunnel0/0/1 172.16.3.1
   ip route-static 172.16.3.1 255.255.255.255 172.16.9.2
  #
  return
  ```