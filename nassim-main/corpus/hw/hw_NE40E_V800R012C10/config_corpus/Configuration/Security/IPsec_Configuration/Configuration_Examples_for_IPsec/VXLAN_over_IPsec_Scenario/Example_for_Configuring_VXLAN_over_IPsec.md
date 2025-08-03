Example for Configuring VXLAN over IPsec
========================================

Transmitting VXLAN packets in plaintext is insecure. To implement encrypted transmission and improve transmission security for VXLAN packets, you can configure IPsec to encapsulate the packets.

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001864833333__fig11431945113214) shows the network.

**Figure 1** Networking diagram of VXLAN over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_003601.png "Click to enlarge")  

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE0/1/2.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/2.
* Routes between DeviceA and DeviceB are reachable.

The network is required to implement the following functions:

* Transmits packets between VMs of the same type in different data centers through VXLAN tunnels.
* Encrypts the packets transmitted between PCA and PCB.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VXLAN IP address.
2. Configure VXLAN service access point information.
3. Configure a VXLAN tunnel.
4. Enable IPsec.
5. Configure ACL rules.
6. Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
7. Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
8. Configure IKE peers.
9. Configure IPsec policies.
10. Configure IPsec service-instance groups.
11. Create and configure an IPsec tunnel.
12. Configure a static route that steers traffic to a tunnel.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* VLAN IDs and VXLAN gateway addresses of VMs
* Tunnel mode, IP address, source address, and destination address of each tunnel interface
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposals
* Encryption algorithm and authentication algorithm to be used for the IKE proposals

#### Procedure

* Configure DeviceA.
  1. Configure IP addresses for interfaces.
     
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sysname DeviceA
     ```
     ```
     [*HUAWEI] commit
     ```
     ```
     [~DeviceA] interface loopback 1
     ```
     ```
     [*DeviceA-LoopBack1] ip address 1.1.1.1 32
     ```
     ```
     [*DeviceA-LoopBack1] quit
     ```
     ```
     [*DeviceA] interface gigabitethernet 0/1/1
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] ip address 192.168.1.1 16
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceA] commit
     ```
  2. Configure a service access point.
     
     
     ```
     [~DeviceA] bridge-domain 10
     ```
     ```
     [*DeviceA-bd10] quit
     ```
     ```
     [*DeviceA] interface gigabitethernet0/1/2.1 mode l2
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2.1] rewrite pop single
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2.1] bridge-domain 10
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/2.1] quit
     ```
     ```
     [*DeviceA] commit
     ```
  3. Configure a VXLAN tunnel.
     
     
     ```
     [~DeviceA] bridge-domain 10
     ```
     ```
     [~DeviceA-bd10] vxlan vni 1
     ```
     ```
     [*DeviceA-bd10] quit
     ```
     ```
     [~DeviceA] interface loopback 2
     ```
     ```
     [*DeviceA-LoopBack2] ip address 3.3.3.3 32
     ```
     ```
     [*DeviceA-LoopBack2] quit
     ```
     ```
     [*DeviceA] interface nve 1
     ```
     ```
     [*DeviceA-Nve1] source 3.3.3.3
     ```
     ```
     [*DeviceA-Nve1] vni 1 head-end peer-list 4.4.4.4
     ```
     ```
     [*DeviceA-Nve1] quit
     ```
     ```
     [*DeviceA] commit
     ```
  4. Enable IPsec.
     
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
  5. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule 5 permit ip source 3.3.3.3 0 destination 4.4.4.4 0
     [*DeviceA-acl-adv-3000] quit
     [*DeviceA] commit
     ```
  6. Configure an IPsec proposal named **tran1**.
     
     
     ```
     [~DeviceA] ipsec proposal tran1
     [*DeviceA-ipsec-proposal-tran1] encapsulation-mode tunnel
     [*DeviceA-ipsec-proposal-tran1] transform esp
     [*DeviceA-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
     [*DeviceA-ipsec-proposal-tran1] esp encryption-algorithm aes 256
     [*DeviceA-ipsec-proposal-tran1] quit
     [*DeviceA] commit
     ```
  7. Configure an IKE proposal numbered 10.
     
     
     ```
     [~DeviceA] ike proposal 10
     [*DeviceA-ike-proposal-10] authentication-method pre-share
     [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
     [*DeviceA-ike-proposal-10] integrity-algorithm hmac-sha2-256
     [*DeviceA-ike-proposal-10] dh group14
     [*DeviceA-ike-proposal-10] quit
     [*DeviceA] commit
     ```
  8. Configure an IKE peer named **b**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceA] ike peer b
     [*DeviceA-ike-peer-b] ike-proposal 10
     [*DeviceA-ike-peer-b] remote-address 2.2.2.2
     [*DeviceA-ike-peer-b] pre-shared-key abcde
     [*DeviceA-ike-peer-b] quit
     [*DeviceA] commit
     ```
  9. Configure an IPsec policy named **map1** and numbered 10.
     
     
     ```
     [~DeviceA] ipsec policy map1 10 isakmp
     [*DeviceA-ipsec-policy-isakmp-map1-10] security acl 3000
     [*DeviceA-ipsec-policy-isakmp-map1-10] proposal tran1
     [*DeviceA-ipsec-policy-isakmp-map1-10] ike-peer b
     [~DeviceA-ipsec-policy-isakmp-map1-10] local-address 1.1.1.1
     [*DeviceA-ipsec-policy-isakmp-map1-10] quit
     [*DeviceA] commit
     ```
  10. Configure an IPsec service-instance group.
      
      
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
  11. Create and configure an IPsec tunnel.
      
      
      ```
      [~DeviceA] interface Tunnel 1
      [*DeviceA-Tunnel1] ip address unnumbered interface loopback1
      [*DeviceA-Tunnel1] tunnel-protocol ipsec
      [*DeviceA-Tunnel1] ipsec policy map1 service-instance-group group1
      [*DeviceA-Tunnel1] quit
      [*DeviceA] commit
      ```
  12. Configure a static route that steers traffic to a tunnel.
      
      
      ```
      [~DeviceA] ip route-static 2.2.2.2 255.255.255.255 GigabitEthernet0/1/1 192.168.2.1
      [*DeviceA] ip route-static 4.4.4.4 255.255.255.255 Tunnel1 2.2.2.2
      [*DeviceA] commit
      ```
* Configure DeviceB.
  1. Configure IP addresses for interfaces.
     
     
     ```
     <HUAWEI> system-view
     ```
     ```
     [~HUAWEI] sysname DeviceB
     ```
     ```
     [*HUAWEI] commit
     ```
     ```
     [~DeviceB] interface loopback 1
     ```
     ```
     [*DeviceB-LoopBack1] ip address 2.2.2.2 32
     ```
     ```
     [*DeviceB-LoopBack1] quit
     ```
     ```
     [*DeviceB] interface gigabitethernet 0/1/1
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/1] ip address 192.168.2.1 16
     ```
     ```
     [*DeviceA-GigabitEthernet0/1/1] quit
     ```
     ```
     [*DeviceB] commit
     ```
  2. Configure a service access point.
     
     
     ```
     [~DeviceB] bridge-domain 10
     ```
     ```
     [*DeviceB-bd10] quit
     ```
     ```
     [*DeviceB] interface gigabitethernet0/1/2.1 mode l2
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2.1] rewrite pop single
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2.1] bridge-domain 10
     ```
     ```
     [*DeviceB-GigabitEthernet0/1/2.1] quit
     ```
     ```
     [*DeviceB] commit
     ```
  3. Configure a VXLAN tunnel.
     
     
     ```
     [~DeviceB] bridge-domain 10
     ```
     ```
     [~DeviceB-bd10] vxlan vni 1
     ```
     ```
     [*DeviceB-bd10] quit
     ```
     ```
     [~DeviceB] interface loopback 2
     ```
     ```
     [*DeviceB-LoopBack2] ip address 4.4.4.4 32
     ```
     ```
     [*DeviceB-LoopBack2] quit
     ```
     ```
     [*DeviceB] interface nve 1
     ```
     ```
     [*DeviceB-Nve1] source 4.4.4.4
     ```
     ```
     [*DeviceB-Nve1] vni 1 head-end peer-list 3.3.3.3
     ```
     ```
     [*DeviceB-Nve1] quit
     ```
     ```
     [*DeviceB] commit
     ```
  4. Enable IPsec.
     
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
  5. Configure an advanced ACL numbered 3000 to define the data flows to be protected.
     
     
     ```
     [~DeviceB] acl 3000
     [*DeviceB-acl-adv-3000] rule 5 permit ip
     [*DeviceB-acl-adv-3000] quit
     [*DeviceB] commit
     ```
  6. Configure an IPsec proposal named **tran1**.
     
     
     ```
     [~DeviceB] ipsec proposal tran1
     [*DeviceB-ipsec-proposal-tran1] encapsulation-mode tunnel
     [*DeviceB-ipsec-proposal-tran1] transform esp
     [*DeviceB-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
     [*DeviceB-ipsec-proposal-tran1] esp encryption-algorithm aes 256
     [*DeviceB-ipsec-proposal-tran1] quit
     [*DeviceB] commit
     ```
  7. Configure an IKE proposal numbered 10.
     
     
     ```
     [~DeviceB] ike proposal 10
     [*DeviceB-ike-proposal-10] authentication-method pre-share
     [*DeviceB-ike-proposal-10] authentication-algorithm sha2-256
     [*DeviceB-ike-proposal-10] integrity-algorithm hmac-sha2-256
     [*DeviceB-ike-proposal-10] dh group14
     [*DeviceB-ike-proposal-10] quit
     [*DeviceB] commit
     ```
  8. Configure an IKE peer named **1**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceB] ike peer 1
     [*DeviceB-ike-peer-1] ike-proposal 10
     [*DeviceB-ike-peer-1] remote-address 1.1.1.1
     [*DeviceB-ike-peer-1] pre-shared-key abcde
     [*DeviceB-ike-peer-1] quit
     [*DeviceB] commit
     ```
  9. Configure an IPsec policy template named **temp1** and numbered 1.
     
     
     ```
     [~DeviceB] ipsec policy-template temp1 1
     [*DeviceB-ipsec-policy-templet-temp1-1] security acl 3000
     [*DeviceB-ipsec-policy-templet-temp1-1] proposal tran1
     [*DeviceB-ipsec-policy-templet-temp1-1] ike-peer 1
     [*DeviceB-ipsec-policy-templet-temp1-1] local-address 2.2.2.2
     [*DeviceB-ipsec-policy-templet-temp1-1] quit
     [*DeviceB] commit
     ```
  10. Create an IPsec policy using an IPsec policy template.
      
      
      ```
      [~DeviceB] ipsec policy 1 1 isakmp template temp1
      [*DeviceB] commit
      ```
  11. Configure an IPsec service-instance group.
      
      
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
  12. Create and configure an IPsec tunnel.
      
      
      ```
      [~DeviceB] interface Tunnel 1
      [*DeviceB-Tunnel1] ip address unnumbered interface loopback1
      [*DeviceB-Tunnel1] tunnel-protocol ipsec
      [*DeviceB-Tunnel1] ipsec policy 1 service-instance-group group1
      [*DeviceB-Tunnel1] quit
      [*DeviceB] commit
      ```
  13. Configure a static route that steers traffic to a tunnel.
      
      
      ```
      [~DeviceB] ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 192.168.1.1
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
  bridge-domain 10
   vxlan vni 1
  #
  acl number 3000
    rule 5 permit ip source 3.3.3.3 0 destination 4.4.4.4 0
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
   remote-address 2.2.2.2
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer b
   proposal tran1
   local-address 1.1.1.1
  #
  interface GigabitEthernet0/1/1 
   undo shutdown
   ip address 192.168.1.1 255.255.0.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface loopback1
   ip address 1.1.1.1 255.255.255.255
  #
  interface loopback2
   ip address 3.3.3.3 255.255.255.255
  #
  interface Nve1
   source 3.3.3.3
   vni 1 head-end peer-list 4.4.4.4
  #
  interface Tunnel1
   ip address unnumbered interface loopback1
   tunnel-protocol ipsec
   ipsec policy map1 service-instance-group group1
  #
  ip route-static 2.2.2.2 255.255.255.255 GigabitEthernet0/1/1 192.168.2.1
  ip route-static 4.4.4.4 255.255.255.255 Tunnel1 2.2.2.2
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
  bridge-domain 10
   vxlan vni 1
  #
  acl number 3000
    rule 5 permit ip
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
   remote-address 1.1.1.1
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy-template temp1 1
  #
   security acl 3000
   ike-peer 1
   proposal tran1
   local-address 2.2.2.2
  #
  ipsec policy 1 1 isakmp template temp1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.2.1 255.255.0.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface loopback1
   ip address 2.2.2.2 255.255.255.255
  #              
  interface loopback2
   ip address 4.4.4.4 255.255.255.255
  #
  interface Nve1
   source 4.4.4.4
   vni 1 head-end peer-list 3.3.3.3
  #
  interface Tunnel1
   ip address unnumbered interface loopback1
   tunnel-protocol ipsec 
   ipsec policy 1 service-instance-group group1
  #
   ip route-static 1.1.1.1 255.255.255.255 GigabitEthernet0/1/1 192.168.1.1
  #
  return
  ```