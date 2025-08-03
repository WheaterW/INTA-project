Example for Configuring DSVPN over IPsec
========================================

Example_for_Configuring_DSVPN_over_IPsec

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.

In an enterprise, the HQ hub connects to branch spokes over the public network, and Spoke 1 and Spoke 2 also connect over the public network. Branch spokes connect to the public network through dynamic addresses. Data transmitted between the HQ and branches and between branches needs to be protected through encryption. The HQ hub and branch spokes are located in different areas, and the subnet environments of the HQ and branches change frequently. The enterprise wants to use a VPN for communication between branches and encrypt data exchanged between the HQ and branches and between branches. To meet this requirement, deploy dynamic routing (OSPF) based on the enterprise network planning and configure DSVPN over IPsec to realize direct communication between Spoke 1 and Spoke 2 and data encryption. [Figure 1](#EN-US_TASK_0172369169__fig_dc_cfg_dsvpn_001901) shows the related networking.

**Figure 1** Networking diagram for configuring DSVPN over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_cfg_dsvpn_001501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Because branches access the public network through dynamic IP addresses, branches are unaware of each other's public IP address. Therefore, configure DSVPN to interconnect branches.
2. Because a large number of branches exist, configure DSVPN in shortcut mode.
3. Because the subnet environments of the HQ and branches frequently change, deploy OSPF based on enterprise network planning for communication between the HQ and branches to simplify maintenance.
4. Because data transmitted between organizations needs to be encrypted, configure DSVPN over IPsec. The authentication algorithms used in the IKE proposal, AH, and ESP are all SHA2-256.


#### Procedure

1. Configure interface IP addresses.
   
   
   
   Configure interface IP addresses on each device.
   
   # Configure interface IP addresses on Hub.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Hub
   [*HUAWEI] commit
   [~Hub] interface GigabitEthernet 0/1/0
   [*Hub-GigabitEthernet0/1/0] ip address 10.1.1.10 255.255.255.0
   [*Hub-GigabitEthernet0/1/0] quit
   [*Hub] interface tunnel 0
   [*Hub-Tunnel0] ip address 172.16.1.1 255.255.255.0
   [*Hub-Tunnel0] quit
   [*Hub] interface loopback 0
   [*Hub-LoopBack0] ip address 192.168.0.1 255.255.255.255
   [*Hub-LoopBack0] quit
   [*Hub] commit
   ```
   
   Assign an IP address to each interface of Spoke 1 and Spoke 2 according to [Figure 1](#EN-US_TASK_0172369169__fig_dc_cfg_dsvpn_001901). The configurations of the spokes are similar to the configuration of the hub.
2. Configure public network routes between devices to implement connectivity.
   
   
   
   Configure OSPF on each device to ensure that the public network routes are available.
   
   # Configure OSPF on Hub.
   
   ```
   [~Hub] ospf 2 router-id 10.1.1.10
   [*Hub-ospf-2] area 0.0.0.1
   [*Hub-ospf-2-areHub-0.0.0.1] network 10.1.1.0 0.0.0.255
   [*Hub-ospf-2-areHub-0.0.0.1] quit
   [*Hub-ospf-2] quit
   [*Hub] commit
   ```
   
   # Configure OSPF on Spoke 1.
   
   ```
   [~Spoke1] ospf 2 router-id 10.1.2.10
   [*Spoke1-ospf-2] area 0.0.0.1
   [*Spoke1-ospf-2-areHub-0.0.0.1] network 10.1.2.0 0.0.0.255
   [*Spoke1-ospf-2-areHub-0.0.0.1] quit
   [*Spoke1-ospf-2] quit
   [*Spoke1] commit
   ```
   
   # Configure OSPF on Spoke 2.
   
   ```
   [~Spoke2] ospf 2 router-id 10.1.3.10
   [*Spoke2-ospf-2] area 0.0.0.1
   [*Spoke2-ospf-2-areHub-0.0.0.1] network 10.1.3.0 0.0.0.255
   [*Spoke2-ospf-2-areHub-0.0.0.1] quit
   [*Spoke2-ospf-2] quit
   [*Spoke2] commit
   ```
3. Configure basic OSPF functions.
   
   
   
   # Configure Hub.
   
   ```
   [~Hub] ospf 1 router-id 172.16.1.1
   [*Hub-ospf-1] area 0.0.0.0
   [*Hub-ospf-1-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub-ospf-1-areHub-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub-ospf-1-areHub-0.0.0.0] quit
   [*Hub-ospf-1] quit
   [*Hub] commit
   ```
   
   # Configure Spoke 1.
   
   ```
   [~Spoke1] ospf 1 router-id 172.16.1.2
   [*Spoke1-ospf-1] area 0.0.0.0
   [*Spoke1-ospf-1-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke1-ospf-1-areHub-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*Spoke1-ospf-1-areHub-0.0.0.0] quit
   [*Spoke1-ospf-1] quit
   [*Spoke1] commit
   ```
   
   # Configure Spoke 2.
   
   ```
   [~Spoke2] ospf 1 router-id 172.16.1.3
   [*Spoke2-ospf-1] area 0.0.0.0
   [*Spoke2-ospf-1-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke2-ospf-1-areHub-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*Spoke2-ospf-1-areHub-0.0.0.0] quit
   [*Spoke2-ospf-1] quit
   [*Spoke2] commit
   ```
4. Enable NHRP globally.
   
   
   
   # Configure Hub.
   
   ```
   [~Hub] nhrp enable
   ```
   
   The configurations of the spokes are similar to the configuration of the hub. For detailed configurations, see Configuration Files.
5. Configure an IKE proposal.
   
   
   
   Configure an IKE proposal on Hub and spokes and select the same authentication mode.
   
   # Configure Hub.
   
   ```
   [~Hub] ike proposal 1
   [*Hub-ike-proposal-1] encryption-algorithm aes-cbc 256
   [*Hub-ike-proposal-1] dh group14
   [*Hub-ike-proposal-1] authentication-algorithm sha2-256
   [*Hub-ike-proposal-1] quit
   [*Hub] commit
   ```
   
   The configurations of Spoke 1 and Spoke 2 are similar to the configuration of Hub. For configuration details, see Configuration Files in this section.
6. Configure an IKE peer.
   
   
   
   Configure the IKE peer required for IKE negotiation on the hub and spokes.
   
   # Configure Hub.
   
   ```
   [~Hub] ike peer hub
   [*Hub-ike-peer-hub] ike-proposal 1
   [*Hub-ike-peer-hub] pre-shared-key gfdsa@1234
   [*Hub-ike-peer-hub] quit
   [*Hub] commit
   ```
   
   The configurations of Spoke 1 and Spoke 2 are similar to the configuration of Hub. For configuration details, see Configuration Files in this section.
7. Create an IPsec proposal.
   
   
   
   Create an IPsec proposal on the hub and spokes.
   
   # Configure Hub.
   
   ```
   [~Hub] ipsec proposal pro1
   [*Hub-ipsec-proposal-pro1] transform ah-esp
   [*Hub-ipsec-proposal-pro1] ah authentication-algorithm sha2-256
   [*Hub-ipsec-proposal-pro1] esp authentication-algorithm sha2-256
   [*Hub-ipsec-proposal-pro1] esp encryption-algorithm aes 192
   [*Hub-ipsec-proposal-pro1] quit
   [*Hub] commit
   ```
   
   The configurations of Spoke 1 and Spoke 2 are similar to the configuration of Hub. For configuration details, see Configuration Files in this section.
8. Configure an IPsec profile.
   
   
   
   Configure an IPsec profile on the hub and spokes.
   
   # Configure Hub.
   
   ```
   [~Hub] ipsec policy 1 profile
   [*Hub-ipsec-policy-profile-1] ike-peer hub
   [*Hub-ipsec-policy-profile-1] proposal pro1
   [*Hub-ipsec-policy-profile-1] quit
   [*Hub] commit
   ```
   
   The configurations of Spoke 1 and Spoke 2 are similar to the configuration of Hub. For configuration details, see Configuration Files in this section.
9. Configure an IPsec service instance group.
   
   
   
   Configure an IPsec service instance group on the Hub and Spokes.
   
   # Configure Hub.
   
   ```
   [~Hub] service-location 1
   [*Hub-service-location-1] location slot 1
   [*Hub-service-location-1] commit
   [~Hub-service-location-1] quit
   [~Hub] service-instance-group group1
   [*Hub-service-instance-group-group1] service-location 1
   [*Hub-service-instance-group-group1] commit
   [~Hub-service-instance-group-group1] quit
   ```
   
   The configurations of Spoke 1 and Spoke 2 are similar to the configuration of Hub. For configuration details, see Configuration Files in this section.
10. Configure tunnel interfaces.
    
    # Configure a tunnel interface and OSPF attributes and apply the IPsec profile on Hub.
    ```
    [~Hub] interface tunnel 0
    [*Hub-Tunnel0] tunnel-protocol gre p2mp
    [*Hub-Tunnel0] nhrp enable
    [*Hub-Tunnel0] source 10.1.1.10
    [*Hub-Tunnel0] nhrp entry multicast dynamic
    [*Hub-Tunnel0] ospf network-type p2mp
    [*Hub-Tunnel0] nhrp redirect
    [*Hub-Tunnel0] ipsec policy 1 service-instance-group group1  
    [*Hub-Tunnel0] quit
    [*Hub] commit
    ```
    
    # Configure tunnel interfaces, OSPF route attributes, and Hub's static NHRP peer entry, and apply the IPsec profile on Spoke 1.
    ```
    [~Spoke1] interface tunnel 0
    [*Spoke1-Tunnel0] tunnel-protocol gre p2mp
    [*Spoke1-Tunnel0] nhrp enable
    [*Spoke1-Tunnel0] source 10.1.2.10
    [*Spoke1-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke1-Tunnel0] ospf network-type p2mp
    [*Spoke1-Tunnel0] nhrp shortcut
    [*Spoke1-Tunnel0] ipsec policy 1 service-instance-group group1
    [*Spoke1-Tunnel0] quit
    [*Spoke1] commit
    ```
    
    # Configure tunnel interfaces, OSPF route attributes, and Hub's static NHRP peer entry, and apply the IPsec profile on Spoke 2.
    ```
    [~Spoke2] interface tunnel 0
    [*Spoke2-Tunnel0] tunnel-protocol gre p2mp
    [*Spoke2-Tunnel0] nhrp enable
    [*Spoke2-Tunnel0] source 10.1.3.10
    [*Spoke2-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke2-Tunnel0] ospf network-type p2mp
    [*Spoke2-Tunnel0] nhrp shortcut
    [*Spoke2-Tunnel0] ipsec policy 1 service-instance-group group1
    [*Spoke2-Tunnel0] quit
    [*Spoke2] commit
    ```
11. Verify the DSVPN configuration.
    
    
    
    After completing the configuration, verify the NHRP peer entry on spokes.
    
    # Run the **display nhrp peer all** command on Spoke 1. The command output is as follows.
    ```
    [~Spoke1] display nhrp peer all
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
    -------------------------------------------------------------------------------
    172.16.1.1      32    10.1.1.10      172.16.1.1       hub          up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_) 
    Created time    : 00:10:58
    Expire time     : --
    
    Number of nhrp peers: 1
    
    ```
    
    # Run the **display nhrp peer all** command on Spoke 2. The command output is as follows.
    ```
    [~Spoke2] display nhrp peer all
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
    -------------------------------------------------------------------------------
    172.16.1.1      32    10.1.1.10      172.16.1.1       hub          up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:07:55
    Expire time     : --
    
    Number of nhrp peers: 1
    
    ```
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The **display nhrp peer all** command output shows that the static NHRP peer entry mapped only to Hub is displayed on Spoke 1 and Spoke 2.
    
    On Hub, verify registration information about Spoke 1 and Spoke 2.
    
    # Run the **display nhrp peer all** command on Hub. The command output is as follows.
    ```
    [~Hub] display nhrp peer all
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
    -------------------------------------------------------------------------------
    172.16.1.2      32    10.1.2.10      172.16.1.2      registered   up|unique
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:02:02
    Expire time     : 01:57:58
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
    -------------------------------------------------------------------------------
    172.16.1.3      32    10.1.3.10      172.16.1.3      registered   up|unique
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:01:53
    Expire time     : 01:59:35
    
    Number of nhrp peers: 2
    
    ```
12. Run the **ping** command and check the configuration result.
    
    
    
    On Spoke 1, ping the subnet address 192.168.2.1 of Spoke 2. Then, verify the dynamic NHRP peer entries of Spoke 1 and Spoke 2.
    
    # Run the **ping -a 192.168.1.1 192.168.2.1** command on Spoke 1. The ping is successful.
    
    ```
    [~Spoke1] ping -a 192.168.1.1 192.168.2.1
      PING 192.168.2.1: 56  data bytes, press CTRL_C to break
        Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=254 time=3 ms
        Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=255 time=2 ms
        Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=255 time=2 ms
        Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=255 time=2 ms
        Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=255 time=2 ms
    
      --- 192.168.2.1 ping statistics ---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max = 2/2/3 ms
    
    ```
    
    # Run the **display nhrp peer all** command on each spoke. The command output on Spoke 1 is used as an example. If the following information is displayed, the NHRP peer entry information is correct.
    
    ```
    [~Spoke1] display nhrp peer all
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag
    -------------------------------------------------------------------------------
    172.16.1.1      32    10.1.1.10      172.16.1.1      hub              up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:46:35
    Expire time     : --
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag
    -------------------------------------------------------------------------------
    192.168.2.1     32    10.1.3.10      172.16.1.3      remote-network  up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:00:28
    Expire time     : 01:59:32
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag
    -------------------------------------------------------------------------------
    172.16.1.3      32    10.1.3.10      172.16.1.3      remote          up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:00:28
    Expire time     : 01:59:32
    -------------------------------------------------------------------------------
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag
    -------------------------------------------------------------------------------
    172.16.1.2      32    10.1.2.10      172.16.1.2      local           up
    -------------------------------------------------------------------------------
    Tunnel interface: Tunnel0 (VPN instance: _public_)
    Created time    : 00:00:28
    Expire time     : 01:59:32
    
    Number of nhrp peers: 4
    
    ```

#### Configuration Files

* Hub configuration file
  
  ```
  #
  sysname Hub
  # 
  ike dpd 100
  #
  ike proposal 1
   encryption-algorithm aes-cbc 256                                                   
   dh group14                                                                      
   authentication-algorithm sha2-256                                       
   authentication-method pre-share                                                
   integrity-algorithm hmac-sha2-256                                              
  # 
  ike peer hub
   pre-shared-key cipher %^%#6n%Y;[:>0T\w~V2nMW//EnxY@k;[q0/x~`.gjZ>#%^%#
   ike-proposal 1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  ipsec proposal pro1
   transform ah-esp
   ah authentication-algorithm sha2-256
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 192
  # 
  ipsec policy 1 profile
   ike-peer hub
   proposal pro1
  # 
  nhrp enable
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.10 255.255.255.0
  # 
  interface LoopBack0
   ip address 192.168.0.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.1 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.1.10
   ospf network-type p2mp
   nhrp enable
   nhrp redirect
   nhrp entry multicast dynamic
   ipsec policy 1 service-instance-group group1
  # 
  ospf 1 router-id 172.16.1.1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.0.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.1.10
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
  # 
  return
  
  ```
* Spoke 1 configuration file
  
  ```
  #
  sysname Spoke1
  # 
  nhrp enable
  #
  ike dpd 100
  #
  ike proposal 1
   encryption-algorithm aes-cbc 256                                                   
   dh group14                                                                      
   authentication-algorithm sha2-256                                       
   authentication-method pre-share                                                
   integrity-algorithm hmac-sha2-256                                              
  # 
  ike peer spoke1
   pre-shared-key cipher %^%#6n%Y;[:>0T\w~V2nMW//EnxY@k;[q0/x~`.gjZ>#%^%#
   ike-proposal 1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  ipsec proposal pro1
   transform ah-esp
   ah authentication-algorithm sha2-256
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 192
  # 
  ipsec policy 1 profile
   ike-peer spoke1
   proposal pro1
  # 
  interface GigabitEthernet0/1/0
   ip address 10.1.2.10 255.255.255.0
  # 
  interface LoopBack0
   ip address 192.168.1.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.2 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.2.10
   ospf network-type p2mp
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1
  # 
  ospf 1 router-id 172.16.1.2
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.2.10
   area 0.0.0.1
    network 10.1.2.0 0.0.0.255
  # 
  return
  
  ```
* Spoke 2 configuration file
  
  ```
  #
  sysname Spoke2
  # 
  nhrp enable
  #
  ike dpd 100
  #
  ike proposal 1
   encryption-algorithm aes-cbc 256                                                   
   dh group14                                                                      
   authentication-algorithm sha2-256                                       
   authentication-method pre-share                                                
   integrity-algorithm hmac-sha2-256                                              
  # 
  ike peer spoke2
   pre-shared-key gfdsa@1234
   ike-proposal 1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  ipsec proposal pro1
   transform ah-esp
   ah authentication-algorithm sha2-256
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 192
  # 
  ipsec policy 1 profile
   ike-peer spoke2
   proposal pro1
  # 
  interface GigabitEthernet0/1/0
   ip address 10.1.3.10 255.255.255.0
  # 
  interface LoopBack0
   ip address 192.168.2.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.3 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.3.10
   ospf network-type p2mp
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1
  # 
  ospf 1 router-id 172.16.1.3
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.3.10
   area 0.0.0.1
    network 10.1.3.0 0.0.0.255
  # 
  return
  
  ```