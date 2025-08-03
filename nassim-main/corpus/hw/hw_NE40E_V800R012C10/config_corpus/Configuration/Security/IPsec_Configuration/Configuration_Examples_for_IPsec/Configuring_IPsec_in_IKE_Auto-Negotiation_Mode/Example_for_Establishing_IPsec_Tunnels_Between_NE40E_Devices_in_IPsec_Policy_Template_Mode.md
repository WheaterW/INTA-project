Example for Establishing IPsec Tunnels Between NE40E Devices in IPsec Policy Template Mode
==========================================================================================

Using the IPsec policy template mode, you can configure IPsec tunnels for multiple mobile devices and conveniently add or delete peer devices. An IPsec policy template needs to be configured on the NE40E to passively receive connection requests, and IPsec policies need to be configured on the peer devices to initiate such requests.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372462__fig1), networks A, B, and C are connected to the Internet through DeviceA, DeviceB, and DeviceC, respectively. There are reachable routes between DeviceA and DeviceB and between DeviceA and DeviceC.

**Figure 1** Establishing IPsec tunnels in IPsec policy template mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE0/1/1 and GE0/1/2, respectively.


  
![](images/fig_dc_vrp_ipsec_cfg_all_002801.png "Click to enlarge")

For security purposes, mutual access between networks A and B as well as between networks A and C is required, whereas networks B and C cannot communicate with each other.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Enable IPsec.
3. Configure ACLs to define the data flows to be protected.
4. Configure IPsec proposals. Specify ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
5. Configure IKE proposals. Specify SHA2-256 and pre-shared key authentication as the authentication algorithm and authentication method, respectively. In addition, set the DH group identifier used for key negotiation to group14.
6. Configure IKE peers.
7. Configure an IPsec policy template on DeviceA. In addition, configure IPsec policies on DeviceB and DeviceC.
8. Configure IPsec service-instance groups.
9. Create and configure tunnel interfaces. Then, apply the IPsec policies to the tunnel interfaces.
10. Configure public network routes (typically static routes).

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* IP addresses of tunnel interfaces
* IP address segment of each subnet
* Pre-shared key
* Security protocol, encryption algorithm, and authentication algorithm to be used for the IPsec proposals
* Authentication algorithm to be used for the IKE proposals

#### Procedure

1. Configure device names and interface IP addresses.
   
   
   
   For detailed configurations, see Configuration Files.
2. Enable IPsec.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring IPsec on the main control board, you do not need to enable IPsec. However, before configuring IPsec on the VSUP, run the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command in the system view and then perform the following steps to enable this function. After the [**vsm on-board-mode disable**](cmdqueryname=undo+vsm+on-board-mode+disable) command is run, IPsec cannot be configured on the main control board.
   
   Only the following models support this configuration:
   
   NE40E-M2K
   
   NE40E-M2K-B
   
   
   
   # Configure DeviceA.
   
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
   
   # Configure DeviceB.
   
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
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] license
   ```
   ```
   [~DeviceC-license] active ipsec bandwidth-enhance 40 slot 1
   ```
   ```
   [*DeviceC-license] quit
   ```
   ```
   [*DeviceC] commit
   ```
3. Define the data flows to be protected.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] acl 3000
   [*DeviceA-acl-adv-3000] rule permit ip 
   [*DeviceA-acl-adv-3000] quit
   [*DeviceA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In this example, the ACL rule permits all IP packets to pass through, so that you can conveniently add or delete peer devices. In addition, the ACL rule takes effect according to the generated route, avoiding risks.
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] acl 3000
   [*DeviceB-acl-adv-3000] rule 5 permit ip source 10.2.1.2 0.0.0.0 destination 10.1.1.2 0.0.0.0
   [*DeviceB-acl-adv-3000] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] acl 3000
   [*DeviceC-acl-adv-3000] rule 10 permit ip source 10.3.1.2 0.0.0.0 destination 10.1.1.2 0.0.0.0
   [*DeviceC-acl-adv-3000] quit
   [*DeviceC] commit
   ```
4. Configure IPsec proposals.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ipsec proposal tran1
   [*DeviceA-ipsec-proposal-tran1] encapsulation-mode tunnel
   [*DeviceA-ipsec-proposal-tran1] transform esp
   [*DeviceA-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
   [*DeviceA-ipsec-proposal-tran1] esp encryption-algorithm aes 256
   [*DeviceA-ipsec-proposal-tran1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ipsec proposal tran1
   [*DeviceB-ipsec-proposal-tran1] encapsulation-mode tunnel
   [*DeviceB-ipsec-proposal-tran1] transform esp
   [*DeviceB-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
   [*DeviceB-ipsec-proposal-tran1] esp encryption-algorithm aes 256
   [*DeviceB-ipsec-proposal-tran1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ipsec proposal tran1
   [*DeviceC-ipsec-proposal-tran1] encapsulation-mode tunnel
   [*DeviceC-ipsec-proposal-tran1] transform esp
   [*DeviceC-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
   [*DeviceC-ipsec-proposal-tran1] esp encryption-algorithm aes 256
   [*DeviceC-ipsec-proposal-tran1] quit
   [*DeviceC] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   ESP is the default security protocol, and the tunnel mode is the default encapsulation mode. They do not need to be configured.
5. Configure IKE proposals.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ike proposal 10
   [*DeviceA-ike-proposal-10] authentication-method pre-share
   [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
   [*DeviceA-ike-proposal-10] dh group14
   [*DeviceA-ike-proposal-10] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ike proposal 10
   [*DeviceB-ike-proposal-10] authentication-method pre-share
   [*DeviceB-ike-proposal-10] authentication-algorithm sha2-256
   [*DeviceB-ike-proposal-10] dh group14
   [*DeviceB-ike-proposal-10] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ike proposal 10
   [*DeviceC-ike-proposal-10] authentication-method pre-share
   [*DeviceC-ike-proposal-10] authentication-algorithm sha2-256
   [*DeviceC-ike-proposal-10] dh group14
   [*DeviceC-ike-proposal-10] quit
   [*DeviceC] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Pre-shared-key-based authentication is the default IKE authentication method and does not need to be configured.
6. Configure IKE peers.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The pre-shared key configured on the local device must be the same as that configured on the peer device.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ike peer p1
   [*DeviceA-ike-peer-p1] ike-proposal 10
   [*DeviceA-ike-peer-p1] pre-shared-key abcde
   [*DeviceA-ike-peer-p1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ike peer a
   [*DeviceB-ike-peer-a] ike-proposal 10
   [*DeviceB-ike-peer-a] remote-address 192.168.1.1
   [*DeviceB-ike-peer-a] pre-shared-key abcde
   [*DeviceB-ike-peer-a] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ike peer a
   [*DeviceC-ike-peer-a] ike-proposal 10
   [*DeviceC-ike-peer-a] remote-address 192.168.1.1
   [*DeviceC-ike-peer-a] pre-shared-key abcde
   [*DeviceC-ike-peer-a] quit
   [*DeviceC] commit
   ```
7. Configure DPD.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ike dpd interval 10 10
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ike dpd interval 10 10
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ike dpd interval 10 10
   [*DeviceC] commit
   ```
8. Configure an IPsec policy template and IPsec policies.
   
   
   
   # Configure an IPsec policy template on DeviceA and enable IPsec policies to reference the template.
   
   ```
   [~DeviceA] ipsec policy-template map_temp 1
   [*DeviceA-ipsec-policy-templet-map_temp-1] security acl 3000
   [*DeviceA-ipsec-policy-templet-map_temp-1] proposal tran1
   [*DeviceA-ipsec-policy-templet-map_temp-1] ike-peer p1
   [*DeviceA-ipsec-policy-templet-map_temp-1] quit
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] ipsec policy map1 10 isakmp template map_temp
   [*DeviceA] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The name of an IPsec policy template must be different from that of an IPsec policy.
   
   # Configure an IPsec policy on DeviceB.
   
   ```
   [~DeviceB] ipsec policy map1 10 isakmp
   [*DeviceB-ipsec-policy-isakmp-map1-10] security acl 3000
   [*DeviceB-ipsec-policy-isakmp-map1-10] proposal tran1
   [*DeviceB-ipsec-policy-isakmp-map1-10] ike-peer a
   [*DeviceB-ipsec-policy-isakmp-map1-10] quit
   [*DeviceB] commit
   ```
   
   # Configure an IPsec policy on DeviceC.
   
   ```
   [~DeviceC] ipsec policy map1 10 isakmp
   [*DeviceC-ipsec-policy-isakmp-map1-10] security acl 3000
   [*DeviceC-ipsec-policy-isakmp-map1-10] proposal tran1
   [*DeviceC-ipsec-policy-isakmp-map1-10] ike-peer a
   [*DeviceC-ipsec-policy-isakmp-map1-10] quit
   [*DeviceC] commit
   ```
9. Configure IPsec service-instance groups.
   
   
   
   # Configure DeviceA.
   
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
   
   # Configure DeviceB.
   
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
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] service-location 1
   ```
   ```
   [*DeviceC-service-location-1] location slot 1
   ```
   ```
   [*DeviceC-service-location-1] commit
   ```
   ```
   [~DeviceC-service-location-1] quit
   ```
   ```
   [~DeviceC] service-instance-group group1
   ```
   ```
   [*DeviceC-service-instance-group-group1] service-location 1
   ```
   ```
   [*DeviceC-service-instance-group-group1] commit
   ```
   ```
   [~DeviceC-service-instance-group-group1] quit
   ```
10. Create and configure tunnel interfaces.
    
    
    
    # Configure DeviceA.
    
    ```
    [~DeviceA] interface Tunnel 10
    ```
    ```
    [*DeviceA-Tunnel10] tunnel-protocol ipsec
    ```
    ```
    [*DeviceA-Tunnel10] ip address 192.168.1.1 32
    ```
    ```
    [~DeviceA-Tunnel10] ipsec policy map1 service-instance-group group1
    ```
    ```
    [*DeviceA-Tunnel10] quit
    [*DeviceA] commit
    ```
    
    # Configure DeviceB.
    
    ```
    [~DeviceB] interface Tunnel 10
    ```
    ```
    [*DeviceB-Tunnel10] tunnel-protocol ipsec
    ```
    ```
    [*DeviceB-Tunnel10] ip address 192.168.2.1 32
    ```
    ```
    [~DeviceB-Tunnel10] ipsec policy map1 service-instance-group group1
    ```
    ```
    [*DeviceB-Tunnel10] quit
    [*DeviceB] commit
    ```
    
    # Configure DeviceC.
    
    ```
    [~DeviceC] interface Tunnel 10
    ```
    ```
    [*DeviceC-Tunnel10] tunnel-protocol ipsec
    ```
    ```
    [*DeviceC-Tunnel10] ip address 192.168.3.1 32
    ```
    ```
    [~DeviceC-Tunnel10] ipsec policy map1 service-instance-group group1
    ```
    ```
    [*DeviceC-Tunnel10] quit
    [*DeviceC] commit
    ```
11. Configure static routes.
    
    
    
    Static routes are used to steer data traffic to IPsec tunnels.
    
    # Configure DeviceA. Assume that the next hop IP address of DeviceA is 172.16.163.2.
    
    ```
    [~DeviceA] ip route-static 0.0.0.0 0.0.0.0 172.16.163.2
    ```
    ```
    [*DeviceA] commit
    ```
    
    # Configure DeviceB. Assume that the next hop IP address of DeviceB is 172.16.169.2.
    
    ```
    [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 192.168.1.1
    ```
    ```
    [*DeviceB] ip route-static 192.168.1.1 255.255.255.255 172.16.169.2
    ```
    ```
    [*DeviceB] commit
    ```
    
    # Configure DeviceC. Assume that the next hop IP address of DeviceC is 172.16.170.2.
    
    ```
    [~DeviceC] ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 192.168.1.1
    ```
    ```
    [*DeviceC] ip route-static 192.168.1.1 255.255.255.255 172.16.170.2
    ```
    ```
    [*DeviceC] commit
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
  acl number 3000
    rule 5 permit ip
  #
  ike proposal 10
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256
   integrity-algorithm hmac-sha2-256
  #
  ike peer p1
   pre-shared-key cipher %^%#.EJ~F"jURXr&0--*9[2(uLl^I@0_]XBJe;=-0x,V%^%#
   ike-proposal 10
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy-template map_temp 1
   security acl 3000
   ike-peer p1
   proposal tran1
  #
  ipsec policy map1 10 isakmp template map_temp
  #
  interface GigabitEthernet0/1/1 
   undo shutdown
   ip address 10.1.1.1 255.255.255.0 
  #
  interface GigabitEthernet0/1/2  
   undo shutdown
   ip address 172.16.163.1 255.255.255.0
  #
  interface Tunnel 10
   ip address 192.168.1.1 255.255.255.0
   tunnel-protocol ipsec
  ```
  ```
   ipsec policy map1 service-instance-group group1
  ```
  ```
  #
  ip route-static 0.0.0.0 0.0.0.0 172.16.163.2
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
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2 
   undo shutdown
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
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
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
  acl number 3000
    rule 10 permit ip source 10.1.3.2 0 destination 10.1.1.2 0
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
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 172.16.170.1 255.255.255.0
  #
  interface Tunnel10
   ip address 192.168.1.3 255.255.255.255
   tunnel-protocol ipsec
   ipsec policy map1 service-instance-group group1
  #
   ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 192.168.1.1
   ip route-static 192.168.1.1 255.255.255.255 172.16.170.2
  #
  return
  ```