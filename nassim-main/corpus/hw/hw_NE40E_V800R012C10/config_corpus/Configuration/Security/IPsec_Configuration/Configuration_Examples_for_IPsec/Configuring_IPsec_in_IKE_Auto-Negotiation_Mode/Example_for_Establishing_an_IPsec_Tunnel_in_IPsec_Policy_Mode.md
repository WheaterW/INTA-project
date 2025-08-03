Example for Establishing an IPsec Tunnel in IPsec Policy Mode
=============================================================

To establish an IPsec tunnel in IKE mode, you need to configure the necessary parameter for the IKE negotiation, and then the IKE negotiation automatically creates and maintains the SA.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372456__fig1), resources are transmitted between network A and network B in gateway-to-gateway mode. Network A and network B connect to the Internet through DeviceA and DeviceB, respectively.

**Figure 1** Establishing an IPsec tunnel in IPsec policy mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_003201.png)

The networking is as follows:

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE0/1/1.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/1.
* Routes between DeviceA and DeviceB are reachable.

To improve communication security between PCA and PCB, configure an IPsec tunnel.


#### Configuration Notes

After configuring an IPsec tunnel, ensure that IP routes are reachable between the two ends of the tunnel.


#### Configuration Roadmap

This example describes how to configure an IPsec tunnel through IKE in gateway-to-gateway networking mode. The tunnel encapsulation mode is used.

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Create and configure tunnel interfaces.
4. Configure public network routes (typically static routes).
5. Configure ACLs to define the data flows to be protected.
6. Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
7. Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
8. Configure IKE peers.
9. Configure IPsec policies.
10. Configure IPsec service-instance groups.
11. Apply the IPsec policies to the tunnel interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* IP addresses of tunnel interfaces
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
        [~DeviceA-GigabitEthernet0/1/2] ip address 172.16.163.1 24
        [*DeviceA-GigabitEthernet0/1/2] quit
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
  3. Create and configure a tunnel interface.
     
     
     ```
     [~DeviceA] interface Tunnel 10
     [*DeviceA-Tunnel10] tunnel-protocol ipsec
     [*DeviceA-Tunnel10] ip address 192.168.1.1 32
     [*DeviceA-Tunnel10] quit
     [*DeviceA] commit
     ```
  4. Configure a static route to network B. The outbound interface and next hop IP address of the route are Tunnel10 and 192.168.1.2, respectively. Assume that the next hop address of DeviceA is 172.16.163.2/24.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a static route to steer IPsec traffic to an IPsec tunnel, you need to configure the IPsec tunnel interface as the outbound interface of the static route and specify the next hop address.
     
     ```
     [~DeviceA] ip route-static 10.1.2.0 255.255.255.0 Tunnel 10 192.168.1.2
     [*DeviceA] ip route-static 192.168.1.2 255.255.255.255 172.16.163.2
     [*DeviceA] commit
     ```
  5. Configure an advanced ACL numbered 3000 to allow PCA to access PCB.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule permit ip source 10.1.1.2 0.0.0.255 destination 10.1.2.2 0.0.0.255
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
     [*DeviceA-ike-peer-b] remote-address 192.168.1.2
     [*DeviceA-ike-peer-b] pre-shared-key abcde
     [*DeviceA-ike-peer-b] quit
     [*DeviceA] commit
     ```
  9. Configure DPD.
     
     
     ```
     [~DeviceA] ike dpd 100
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
  12. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceA] interface Tunnel 10
      ```
      ```
      [~DeviceA-Tunnel10] ipsec policy map1 service-instance-group group1
      ```
      ```
      [*DeviceA-Tunnel10] quit
      [*DeviceA] commit
      ```
* Configure DeviceB.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/1/1.
        
        ```
        <DeviceB> system-view
        [~DeviceB] interface gigabitethernet 0/1/1
        [~DeviceB-GigabitEthernet0/1/1] ip address 10.1.2.1 24
        [*DeviceB-GigabitEthernet0/1/1] quit
        [*DeviceB] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceB] interface gigabitethernet 0/1/2
        [~DeviceB-GigabitEthernet0/1/2] ip address 172.16.169.1 24
        [*DeviceB-GigabitEthernet0/1/2] quit
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
  3. Create and configure a tunnel interface.
     
     
     ```
     [~DeviceB] interface Tunnel 10
     [~DeviceB-Tunnel10] tunnel-protocol ipsec
     [*DeviceB-Tunnel10] ip address 192.168.1.2 32
     [*DeviceB-Tunnel10] quit
     [*DeviceB] commit
     ```
  4. Configure a static route destined for network A, with the outbound interface being Tunnel10 and the next hop address being 192.168.1.1. Assume that the next hop address of DeviceB is 172.16.169.2/24.
     
     
     ```
     [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 192.168.1.1
     [*DeviceB] ip route-static 192.168.1.1 255.255.255.255 172.16.169.2
     [*DeviceB] commit
     ```
  5. Configure an advanced ACL number 3000 to allow PCB to access PCA.
     
     
     ```
     [~DeviceB] acl 3000
     [*DeviceB-acl-adv-3000] rule permit ip source 10.1.2.2 0.0.0.0 destination 10.1.1.2 0.0.0.0
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
     [*DeviceB-ike-proposal-10] dh group14
     [*DeviceB-ike-proposal-10] quit
     [*DeviceB] commit
     ```
  8. Configure an IKE peer named **a**.
     
     
     ```
     [~DeviceB] ike peer a 
     [*DeviceB-ike-peer-a] ike-proposal 10 
     [*DeviceB-ike-peer-a] remote-address 192.168.1.1 
     [*DeviceB-ike-peer-a] pre-shared-key abcde 
     [*DeviceB-ike-peer-a] quit
     [*DeviceB] commit
     ```
  9. Configure DPD.
     
     
     ```
     [~DeviceB] ike dpd 100
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
  12. Apply the IPsec policy **map1** to the tunnel interface.
      
      
      ```
      [~DeviceB] interface Tunnel10
      [~DeviceB-Tunnel10] ipsec policy map1 service-instance-group group1
      [*DeviceB-Tunnel10] quit
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
  ike dpd 100
  #
  acl number 3000
    rule 5 permit ip source 10.1.1.2 0 destination 10.1.2.2 0
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer b
   pre-shared-key cipher %^%#CScZ$9Z&w+@:5+7>\{;7UI~3"Wcx/P#,,FT<6t!8%^%#
   ike-proposal 10
   remote-address 192.168.1.2
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
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   ip address 172.16.163.1 255.255.255.0
  #
  interface Tunnel10
   ip address 192.168.1.1 255.255.255.255
   tunnel-protocol ipsec
   ipsec policy map1 service-instance-group group1
  #
   ip route-static 10.1.2.0 255.255.255.0 Tunnel 10 192.168.1.2
   ip route-static 192.168.1.2 255.255.255.255 172.16.163.2
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
  ike dpd 100
  #
  acl number 3000
    rule 5 permit ip source 10.1.2.2 0 destination 10.1.1.2 0
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer a
   pre-shared-key cipher %^%#.EJ~F"jURXr&0--*9[2(uLl^I@0_]XBJe;=-0x,V%^%#
   ike-proposal 10
   remote-address 192.168.1.1
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
   ip address 10.1.2.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2 
   ip address 172.16.169.1 255.255.255.0
  #
  interface Tunnel10
   ip address 192.168.1.2 255.255.255.255
   tunnel-protocol ipsec
   ipsec policy map1 service-instance-group group1
  #
   ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 192.168.1.1
   ip route-static 192.168.1.1 255.255.255.255 172.16.169.2
  #
  return
  ```