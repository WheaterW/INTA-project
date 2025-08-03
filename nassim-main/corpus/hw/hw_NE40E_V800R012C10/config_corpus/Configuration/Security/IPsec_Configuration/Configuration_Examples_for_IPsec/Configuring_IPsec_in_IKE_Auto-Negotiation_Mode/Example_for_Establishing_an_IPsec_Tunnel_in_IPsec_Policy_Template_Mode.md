Example for Establishing an IPsec Tunnel in IPsec Policy Template Mode
======================================================================

A major application of the NE40E is to establish an IPsec tunnel between it and a base station so that mobile devices camping on the base station can access an internal network. Using the IPsec policy template mode, you can configure IPsec tunnels for multiple base stations and conveniently add or delete base stations. An IPsec policy template needs to be configured on the NE40E to passively receive connection requests, and IPsec policies need to be configured on the base stations to initiate such requests.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372459__fig1), network A is connected to the Internet through DeviceA. Two base stations (NodeB1 and NodeB2) are also connected to the Internet. There are reachable routes between DeviceA and the two base stations.

**Figure 1** Establishing an IPsec tunnel in IPsec policy template mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_003301.png "Click to enlarge")

Mobile devices camping on the two base stations are required to securely access network A.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Create and configure a tunnel interface.
3. Enable IPsec.
4. Configure public-network routes (typically static routes).
5. Configure an ACL to define the data flows to be protected.
6. Configure an IPsec proposal. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
7. Configure an IKE proposal. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
8. Configure an IKE peer.
9. Configure an IPsec policy template.
10. Configure an IPsec service-instance group.
11. Apply the specified IPsec policy to the tunnel interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* IP address of the tunnel interface
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposal
* Authentication algorithm to be used for the IKE proposal

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
     [*DeviceA-Tunnel10] ip address 10.10.1.1 32
     [*DeviceA-Tunnel10] quit
     [*DeviceA] commit
     ```
  4. Configure a static route to the Internet. Assume that the next hop IP address of DeviceA is 172.16.163.2.
     
     
     ```
     [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 172.16.163.2
     ```
  5. Define the data flows to be protected.
     
     
     ```
     [~DeviceA] acl 3000
     [*DeviceA-acl-adv-3000] rule permit ip 
     [*DeviceA-acl-adv-3000] quit
     [*DeviceA] commit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In this example, the ACL rule permits all IP packets to pass through, so that you can conveniently add or delete peer base stations. In addition, the ACL rule takes effect according to the generated route, avoiding risks.
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
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     ESP is the default security protocol, and the tunnel mode is the default encapsulation mode. They do not need to be configured.
  7. Configure an IKE proposal numbered 10.
     
     
     ```
     [~DeviceA] ike proposal 10
     [*DeviceA-ike-proposal-10] authentication-method pre-share
     [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
     [*DeviceA-ike-proposal-10] dh group14
     [*DeviceA-ike-proposal-10] quit
     [*DeviceA] commit
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Pre-shared-key-based authentication is the default IKE authentication method and does not need to be configured.
  8. Configure an IKE peer named **b**.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The pre-shared key configured on the local device must be the same as that configured on the peer device.
     
     
     
     ```
     [~DeviceA] ike peer b
     [*DeviceA-ike-peer-b] ike-proposal 10
     [*DeviceA-ike-peer-b] pre-shared-key abcde
     [*DeviceA-ike-peer-b] quit
     [*DeviceA] commit
     ```
  9. Configure DPD.
     
     
     ```
     [~DeviceA] ike dpd 100
     [*DeviceA] commit
     ```
  10. Configure an IPsec policy template named **map\_temp** and numbered 1.
      
      
      ```
      [~DeviceA] ipsec policy-template map_temp 1
      [*DeviceA-ipsec-policy-templet-map_temp-1] security acl 3000
      [*DeviceA-ipsec-policy-templet-map_temp-1] proposal tran1
      [*DeviceA-ipsec-policy-templet-map_temp-1] ike-peer b
      [*DeviceA-ipsec-policy-templet-map_temp-1] quit
      [*DeviceA] commit
      ```
  11. Configure the IPsec policy **map1** to reference the IPsec policy template **map\_temp**.
      
      
      ```
      [~DeviceA] ipsec policy map1 10 isakmp template map_temp
      [*DeviceA] commit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The name of an IPsec policy template must be different from that of an IPsec policy.
  12. Configure an IPsec service-instance group.
      
      
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
  13. Apply the IPsec policy **map1** to the tunnel interface.
      
      
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
    rule 5 permit ip
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer b
   pre-shared-key cipher %^%#.EJ~F"jURXr&0--*9[2(uLl^I@0_]XBJe;=-0x,V%^%#
   ike-proposal 10
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy-template map_temp 1
   security acl 3000
   ike-peer b
   proposal tran1
  #
  ipsec policy map1 10 isakmp template map_temp
  #
  interface GigabitEthernet0/1/1
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   ip address 172.16.163.1 255.255.255.0
  #
  interface Tunnel10
   ip address 10.10.1.1 255.255.255.0
   tunnel-protocol ipsec
   ipsec policy map1 service-instance-group group1
  #
  ip route-static 0.0.0.0 0.0.0.0 172.16.163.2
  #
  return
  ```