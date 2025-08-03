Example for Configuring IPv6 over GRE over IPsec (Inter-Board)
==============================================================

IPsec supports the transmission of only IPv4 unicast packets. To enable the transmission of packets that are not supported by IPsec, such as L2VPN/L3VPN IPv4 packets, IPv6 unicast packets, IPv4 multicast packets, and IPv4 broadcast packets, configure IPv6 over GRE over IPsec. In an inter-board scenario, GRE encapsulation needs to be performed on a GRE tunnel and IPsec encryption needs to be performed on a VSU or main control board.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported by a VSU or main control board.

[Figure 1](#EN-US_TASK_0172372484__fig1) shows the network.

**Figure 1** Configuring IPv6 over GRE over IPsec  
![](images/fig_dc_ne_ipsec_cfg_000201.png "Click to enlarge")

* DeviceA is connected to network A through GE0/3/1.
* DeviceB is connected to network B through GE0/1/2.
* The IPv4 address and IPv6 address of DeviceA are 10.1.2.1 and 2001:db8:1::1, respectively. On DeviceA, the IPsec service board resides in slot 1, and the tunnel service board resides in slot 1.
* The IPv4 address and IPv6 address of DeviceB are 10.1.3.1 and 2001:db8:2::1, respectively. On DeviceB, the IPsec service board resides in slot 1, and the tunnel service board resides in slot 1.
* Routes between DeviceA and DeviceB are reachable.

Configure IPv6 over GRE over IPsec to enable the network to transmit the following types of packets between PCA and PCB in encrypted mode: L2VPN/L3VPN IPv4 packets, IPv4 unicast packets, IPv6 unicast packets, IPv4 multicast packets, and IPv4 broadcast packets.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Create a loopback interface and bind GRE to it.
4. Create and configure a GRE tunnel.
5. Configure ACL rules.
6. Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
7. Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
8. Configure IKE peers.
9. Configure IPsec policies.
10. Configure an IPsec service-instance group.
11. Create and configure an IPsec tunnel.
12. Configure static routes to destination networks.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* Tunnel modes and IP addresses of tunnel interfaces; tunnel source and destination addresses
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encapsulation mode, encryption algorithm, and authentication algorithm to be used for an IPsec proposal
* Encryption algorithm and authentication algorithm to be used for an IKE proposal

#### Procedure

* Configure DeviceA.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/3/2.10.
        
        ```
        <DeviceA> system-view
        [~DeviceA] interface GigabitEthernet 0/3/2.10
        [*DeviceA-GigabitEthernet0/3/2.10] vlan-type dot1q 200
        [*DeviceA-GigabitEthernet0/3/2.10] ip address 10.1.1.6 24
        [*DeviceA-GigabitEthernet0/3/2.10] quit
        [*DeviceA] commit
        ```
     2. Configure an IP address for GE0/3/1.
        
        ```
        [~DeviceA] interface GigabitEthernet 0/3/1
        [~DeviceA-GigabitEthernet0/3/1] ip address 10.1.2.1 24
        [*DeviceA-GigabitEthernet0/3/1] ipv6 enable
        [*DeviceA-GigabitEthernet0/3/1] ipv6 address 2001:db8:1::1/64
        [*DeviceA-GigabitEthernet0/3/1] ipv6 neighbor 2001:db8:1::2 11-11-11
        [*DeviceA-GigabitEthernet0/3/1] quit
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
  3. Create a loopback interface and bind GRE to it.
     
     
     ```
     [~DeviceA] interface loopback 111
     [*DeviceA-Loopback111] ip address 1.1.1.6 32
     [*DeviceA-Loopback111] binding tunnel gre
     [*DeviceA-Loopback111] quit
     [*DeviceA] commit
     ```
  4. Configure a GRE tunnel.
     
     
     ```
     [~DeviceA] interface tunnel 200
     [*DeviceA-tunnel200] tunnel-protocol gre
     [*DeviceA-tunnel200] ip address 10.1.4.1 24
     [*DeviceA-tunnel200] source loopback 111
     [*DeviceA-tunnel200] destination 1.1.1.7
     [*DeviceA-tunnel200] ipv6 enable
     [*DeviceA-tunnel200] ipv6 address 2001:db8:3::1/64
     [*DeviceA-tunnel200] quit
     [*DeviceA] commit
     ```
  5. Configure an advanced ACL numbered 3018 to define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3018
     [*DeviceA-acl4-advance-3018] rule permit gre source 1.1.1.6 0 destination 1.1.1.7 0
     [*DeviceA-acl4-advance-3018] quit
     [*DeviceA] commit
     ```
  6. Configure an IPsec proposal named **pro1**.
     
     
     ```
     [~DeviceA] ipsec proposal pro1 
     [*DeviceA-ipsec-proposal-pro1] encapsulation-mode tunnel
     [*DeviceA-ipsec-proposal-pro1] transform esp
     [*DeviceA-ipsec-proposal-pro1] esp authentication-algorithm sha2-256
     [*DeviceA-ipsec-proposal-pro1] esp encryption-algorithm aes 256
     [*DeviceA-ipsec-proposal-pro1] quit
     [*DeviceA] commit
     ```
  7. Configure an IKE proposal numbered 1.
     
     
     ```
     [~DeviceA] ike proposal 1
     [*DeviceA-ike-proposal-1] authentication-method pre-share
     [*DeviceA-ike-proposal-1] authentication-algorithm sha2-256
     [*DeviceA-ike-proposal-1] dh group14
     [*DeviceA-ike-proposal-1] quit
     [*DeviceA] commit
     ```
  8. Configure an IKE peer named **peer1**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceA] ike peer peer1
     [*DeviceA-ike-peer-peer1] ike-proposal 1
     [*DeviceA-ike-peer-peer1] remote-address 10.1.5.2
     [*DeviceA-ike-peer-peer1] pre-shared-key 1234567890
     [*DeviceA-ike-peer-peer1] quit
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
      [*DeviceA-ipsec-policy-isakmp-policy1-1] security acl 3018
      [*DeviceA-ipsec-policy-isakmp-policy1-1] proposal pro1
      [*DeviceA-ipsec-policy-isakmp-policy1-1] ike-peer peer1
      [*DeviceA-ipsec-policy-isakmp-policy1-1] quit
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
      [~DeviceA] interface Tunnel 1600
      [*DeviceA-Tunnel1600] ip address 10.1.5.1 24
      [*DeviceA-Tunnel1600] tunnel-protocol ipsec
      [*DeviceA-Tunnel1600] ipsec policy policy1 service-instance-group group1
      [*DeviceA-Tunnel1600] quit
      [*DeviceA] commit
      ```
  13. Configure a static route to network B.
      
      
      ```
      [~DeviceA] ip route-static 1.1.1.7 255.255.255.255 Tunnel1600  10.1.5.2
      [*DeviceA] ip route-static 10.1.5.2 255.255.255.255 GigabitEthernet0/3/2.10 10.1.1.7
      [*DeviceA] ip route-static 10.1.3.1 255.255.255.0 Tunnel200  1.1.1.7
      [*DeviceA] ipv6 route-static 2001:db8:2::2 64 Tunnel200
      [*DeviceA] commit
      ```
* Configure DeviceB.
  1. Configure IP addresses for interfaces.
     
     
     1. Configure an IP address for GE0/1/1.10.
        
        ```
        <DeviceB> system-view
        [~DeviceB] interface GigabitEthernet0/1/1.10
        [*DeviceB-GigabitEthernet0/1/1.10] vlan-type dot1q 200
        [*DeviceB-GigabitEthernet0/1/1.10] ip address 10.1.1.7 24
        [*DeviceB-GigabitEthernet0/1/1.10] quit
        [*DeviceB] commit
        ```
     2. Configure an IP address for GE0/1/2.
        
        ```
        [~DeviceB] interface GigabitEthernet 0/1/2
        [*DeviceB-GigabitEthernet0/1/2] ip address 10.1.3.1 24
        [*DeviceB-GigabitEthernet0/1/2] ipv6 enable
        [*DeviceB-GigabitEthernet0/1/2] ipv6 address 2001:db8:2::1/64
        [*DeviceB-GigabitEthernet0/1/2] ipv6 neighbor 2001:db8:2::2 22-22-22
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
  3. Create a loopback interface and bind GRE to it.
     
     
     ```
     [~DeviceB] interface loopback 111
     [*DeviceB-Loopback111] ip address 1.1.1.7 255.255.255.255
     [*DeviceB-Loopback111] binding tunnel gre
     [*DeviceB-Loopback111] quit
     [*DeviceB] commit
     ```
  4. Configure a GRE tunnel.
     
     
     ```
     [~DeviceB] interface tunnel 200
     [*DeviceB-tunnel200] tunnel-protocol gre
     [*DeviceB-tunnel200] ip address 10.1.4.2 255.255.255.0
     [*DeviceB-tunnel200] ipv6 enable
     [*DeviceB-tunnel200] ipv6 address 2001:db8:3::2/64
     [*DeviceB-tunnel200] source LoopBack 111
     [*DeviceB-tunnel200] destination 1.1.1.6
     [*DeviceB-tunnel200] quit
     [*DeviceB] commit
     ```
  5. Configure an advanced ACL numbered 3018 to define the data flows to be protected.
     
     
     ```
     [~DeviceB] acl 3018
     [*DeviceB-acl4-advance-3018] rule permit gre source 1.1.1.7 0 destination 1.1.1.6 0
     [*DeviceB-acl4-advance-3018] quit
     [*DeviceB] commit
     ```
  6. Configure an IPsec proposal named **pro1**.
     
     
     ```
     [~DeviceB] ipsec proposal pro1
     [*DeviceB-ipsec-proposal-pro1] encapsulation-mode tunnel
     [*DeviceB-ipsec-proposal-pro1] transform esp
     [*DeviceB-ipsec-proposal-pro1] esp authentication-algorithm sha2-256
     [*DeviceB-ipsec-proposal-pro1] esp encryption-algorithm aes 256
     [*DeviceB-ipsec-proposal-pro1] quit
     [*DeviceB] commit
     ```
  7. Configure an IKE proposal numbered 1.
     
     
     ```
     [~DeviceB] ike proposal 1 
     [*DeviceB-ike-proposal-1] authentication-method pre-share 
     [*DeviceB-ike-proposal-1] authentication-algorithm sha2-256
     [*DeviceB-ike-proposal-1] dh group14
     [*DeviceB-ike-proposal-1] quit
     [*DeviceB] commit
     ```
  8. Configure an IKE peer named **peer1**.
     
     
     ```
     [~DeviceB] ike peer peer1 
     [*DeviceB-ike-peer-peer1] ike-proposal 1
     [*DeviceB-ike-peer-peer1] remote-address 10.1.5.1 
     [*DeviceB-ike-peer-peer1] pre-shared-key 1234567890 
     [*DeviceB-ike-peer-peer1] quit
     [*DeviceB] commit
     ```
  9. Configure DPD.
     
     
     ```
     [~DeviceB] ike dpd interval 10 10
     [*DeviceB] commit
     ```
  10. Configure an IPsec policy named **policy1** and numbered 1.
      
      
      ```
      [~DeviceB] ipsec policy policy1 1 isakmp
      [*DeviceB-ipsec-policy-isakmp-policy1-1] security acl 3018
      [*DeviceB-ipsec-policy-isakmp-policy1-1] proposal pro1
      [*DeviceB-ipsec-policy-isakmp-policy1-1] ike-peer peer1
      [*DeviceB-ipsec-policy-isakmp-policy1-1] quit
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
  12. Create a tunnel interface and configure IPsec for the tunnel interface.
      
      
      ```
      [~DeviceB] interface Tunnel 1600
      [*DeviceB-Tunnel1600] ip address 10.1.5.2 24
      [*DeviceB-Tunnel1600] tunnel-protocol ipsec
      [*DeviceB-Tunnel1600] ipsec policy policy1 service-instance-group group1
      [*DeviceB-Tunnel1600] quit
      [*DeviceB] commit
      ```
  13. Configure a static route to network A.
      
      
      ```
      [~DeviceB] ip route-static 10.1.2.1 255.255.255.0 Tunnel200  1.1.1.6
      [*DeviceB] ip route-static 10.1.5.1 255.255.255.255 GigabitEthernet0/1/1.10 10.1.1.6
      [*DeviceB] ip route-static 1.1.1.6 255.255.255.255 Tunnel1600 10.1.5.1
      [*DeviceB] ipv6 route-static 2001:db8:1::2 64 Tunnel200
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
  ike dpd interval 10 10
  #
  acl number 3018
   rule 5 permit gre source 1.1.1.6 0 destination 1.1.1.7 0
  #
  ike proposal 1
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer peer1
   pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$
   ike-proposal 1
   remote-address 10.1.5.2
  #
  ipsec proposal pro1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy policy1 1 isakmp
   security acl 3018
   ike-peer peer1
   proposal pro1
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ipv6 enable
   ip address 10.1.2.1 255.255.255.0
   ipv6 address 2001:db8:1::1/64
   ipv6 neighbor 2001:db8:1::2 00e0-fc12-3456
   undo dcn
  #
  interface GigabitEthernet0/3/2.10
   vlan-type dot1q 200
   ip address 10.1.1.6 255.255.255.0
  #
  interface LoopBack111
   ip address 1.1.1.6 255.255.255.255
   binding tunnel gre
  #
  interface Tunnel1600
   ip address 10.1.5.1 255.255.255.0
   tunnel-protocol ipsec
   ipsec policy policy1 service-instance-group group1
  #
  interface Tunnel200
   ipv6 enable
   ip address 10.1.4.1 255.255.255.0
   ipv6 address 2001:db8:3::1/64
   tunnel-protocol gre
   source LoopBack111
   destination 1.1.1.7
  #
  ip route-static 10.1.3.0 255.255.255.0 Tunnel200 1.1.1.7
  ip route-static 10.1.5.2 255.255.255.255 GigabitEthernet0/3/2.10 10.1.1.7
  ip route-static 1.1.1.7 255.255.255.255 Tunnel1600 10.1.5.2
  #
  ipv6 route-static 2001:db8:2::2 64 Tunnel200
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
  ike dpd interval 10 10
  #
  acl number 3018
   rule 5 permit gre source 1.1.1.7 0 destination 1.1.1.6 0
  #
  ike proposal 1
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer peer1
   pre-shared-key %$%$0\WT%.iDi6%K-f)_^mQ6,.2n%$%$
   ike-proposal 1
   remote-address 10.1.5.1
  #
  ipsec proposal pro1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy policy1 1 isakmp
   security acl 3018
   ike-peer peer1
   proposal pro1
  #
  interface GigabitEthernet0/1/1.10
   vlan-type dot1q 200
   ip address 10.1.1.7 255.255.255.0
  #
  interface LoopBack111
   ip address 1.1.1.7 255.255.255.255
   binding tunnel gre
  #
  interface Tunnel1600
   ip address 10.1.5.2 255.255.255.0
   tunnel-protocol ipsec
   ipsec policy policy1 service-instance-group group1
  #
  interface Tunnel200
   ipv6 enable
   ip address 10.1.4.2 255.255.255.0
   ipv6 address 2001:db8:3::2/64
   tunnel-protocol gre
   source LoopBack111
   destination 1.1.1.6
  #
  ip route-static 10.1.2.0 255.255.255.0 Tunnel200 1.1.1.6
  ip route-static 10.1.5.1 255.255.255.255 GigabitEthernet0/1/1.10 10.1.1.6
  ip route-static 1.1.1.6 255.255.255.255 Tunnel1600 10.1.5.1
  #
  ipv6 route-static 2001:db8:1::2 64 Tunnel200
  #
  return
  ```