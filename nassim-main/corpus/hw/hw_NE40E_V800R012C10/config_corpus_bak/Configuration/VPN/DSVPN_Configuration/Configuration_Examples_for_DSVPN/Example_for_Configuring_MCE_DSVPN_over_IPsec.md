Example for Configuring MCE DSVPN over IPsec
============================================

Example_for_Configuring_MCE_DSVPN_over_IPsec

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.

In an enterprise, the HQ hub connects to branch spokes over the public network, and Spoke 1 and Spoke 2 also connect over the public network. Branch spokes connect to the public network through dynamic addresses. Data transmitted between the HQ and branches and between branches needs to be protected through encryption. The HQ hub and branch spokes are located in different areas, and the subnet environments of the HQ and branches change frequently. The enterprise wants to realize VPN communication and service isolation between branches and encrypt data exchanged between the HQ and branches and between branches. To meet this requirement, deploy dynamic routing (OSPF) based on the enterprise network planning and configure MCE DSVPN over IPsec to realize direct communication between Spoke 1 and Spoke 2, data encryption, and service isolation. [Figure 1](#EN-US_TASK_0000001115219894__fig_dc_cfg_dsvpn_001901) shows the related networking.

**Figure 1** Networking diagram for configuring MCE DSVPN over IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](figure/en-us_image_0000001161779665.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Because branches access the public network through dynamic IP addresses, branches are unaware of the public IP address of each other. Therefore, configure DSVPN to connect branches.
2. Because a large number of branches exist, configure DSVPN in shortcut mode.
3. Because the subnet environments of the HQ and branches frequently change, deploy OSPF based on enterprise network planning for communication between the HQ and branches to simplify maintenance.
4. Because data transmitted between organizations needs to be encrypted, configure DSVPN over IPsec. The authentication algorithms used in the IKE proposal, AH, and ESP are all SHA2-256.
5. Because MCE needs to be deployed for the subnet between the HQ and users to isolate services, plan the binding of different mGRE tunnel interfaces to different VPNs.
6. Because the HQ and branches each have only one physical link to the public network, you need to configure mGRE tunnels with the same source.


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
   [*Hub] ip vpn-instance vpna
   [*Hub-vpn-instance-vpna] ipv4-family
   [*Hub-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   [*Hub-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both 
   [*Hub-vpn-instance-vpna-af-ipv4] quit
   [*Hub-vpn-instance-vpna] quit
   [*Hub] ip vpn-instance vpnb
   [*Hub-vpn-instance-vpnb] ipv4-family
   [*Hub-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2
   [*Hub-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both 
   [*Hub-vpn-instance-vpnb-af-ipv4] quit
   [*Hub-vpn-instance-vpnb] quit
   [*Hub] interface tunnel 0
   [*Hub-Tunnel0] ip binding vpn-instance vpna
   [*Hub-Tunnel0] ip address 172.16.1.1 255.255.255.0
   [*Hub-Tunnel0] quit
   [*Hub] interface tunnel 1
   [*Hub-Tunnel1] ip binding vpn-instance vpnb
   [*Hub-Tunnel1] ip address 172.16.1.1 255.255.255.0
   [*Hub-Tunnel1] quit
   [*Hub] interface loopback 0
   [*Hub-LoopBack0] ip binding vpn-instance vpna
   [*Hub-LoopBack0] ip address 192.168.0.1 255.255.255.255
   [*Hub-LoopBack0] quit
   [*Hub] interface loopback 1
   [*Hub-LoopBack1] ip binding vpn-instance vpnb
   [*Hub-LoopBack1] ip address 192.168.0.1 255.255.255.255
   [*Hub-LoopBack1] quit
   [*Hub] commit
   ```
   
   Assign an IP address to each interface on Spoke 1 and Spoke 2 according to [Figure 1](#EN-US_TASK_0000001115219894__fig_dc_cfg_dsvpn_001901). The configurations of the spokes are similar to the configuration of the hub.
2. Configure public network routes between devices.
   
   
   
   Configure OSPF on each device to ensure that public network routes are available.
   
   # Configure OSPF on Hub.
   
   ```
   [~Hub] ospf 1 router-id 10.1.1.10
   [*Hub-ospf-1] area 0.0.0.1
   [*Hub-ospf-1-areHub-0.0.0.1] network 10.1.1.0 0.0.0.255
   [*Hub-ospf-1-areHub-0.0.0.1] quit
   [*Hub-ospf-1] quit
   [*Hub] commit
   ```
   
   # Configure OSPF on Spoke 1.
   
   ```
   [~Spoke1] ospf 1 router-id 10.1.2.10
   [*Spoke1-ospf-1] area 0.0.0.1
   [*Spoke1-ospf-1-areHub-0.0.0.1] network 10.1.2.0 0.0.0.255
   [*Spoke1-ospf-1-areHub-0.0.0.1] quit
   [*Spoke1-ospf-1] quit
   [*Spoke1] commit
   ```
   
   # Configure OSPF on Spoke 2.
   
   ```
   [~Spoke2] ospf 1 router-id 10.1.3.10
   [*Spoke2-ospf-1] area 0.0.0.1
   [*Spoke2-ospf-1-areHub-0.0.0.1] network 10.1.3.0 0.0.0.255
   [*Spoke2-ospf-1-areHub-0.0.0.1] quit
   [*Spoke2-ospf-1] quit
   [*Spoke2] commit
   ```
3. Configure basic OSPF functions.
   
   
   
   # Configure Hub.
   
   ```
   [~Hub] ospf 2 router-id 172.16.1.1 vpn-instance vpna
   [*Hub-ospf-2] vpn-instance-capability simple
   Warning: This operation may cause a routing loop. Continue? [Y/N]:Y
   [*Hub-ospf-2] area 0.0.0.0
   [*Hub-ospf-2-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub-ospf-2-areHub-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub-ospf-2-areHub-0.0.0.0] quit
   [*Hub-ospf-2] quit
   [*Hub] commit
   [~Hub] ospf 3 router-id 172.16.1.1 vpn-instance vpnb
   [*Hub-ospf-3] area 0.0.0.0
   [*Hub-ospf-3-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub-ospf-3-areHub-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub-ospf-3-areHub-0.0.0.0] quit
   [*Hub-ospf-3] quit
   [*Hub] commit
   ```
   
   # Configure Spoke 1.
   
   ```
   [~Spoke1] ospf 2 router-id 172.16.1.2 vpn-instance vpna
   [*Spoke1-ospf-2] vpn-instance-capability simple
   Warning: This operation may cause a routing loop. Continue? [Y/N]:Y
   [*Spoke1-ospf-2] area 0.0.0.0
   [*Spoke1-ospf-2-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke1-ospf-2-areHub-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*Spoke1-ospf-2-areHub-0.0.0.0] quit
   [*Spoke1-ospf-2] quit
   [*Spoke1] commit
   [~Spoke1] ospf 3 router-id 172.16.1.2 vpn-instance vpnb
   [*Spoke1-ospf-3] area 0.0.0.0
   [*Spoke1-ospf-3-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke1-ospf-3-areHub-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*Spoke1-ospf-3-areHub-0.0.0.0] quit
   [*Spoke1-ospf-3] quit
   [*Spoke1] commit
   ```
   
   # Configure Spoke 2.
   
   ```
   [~Spoke2] ospf 2 router-id 172.16.1.3 vpn-instance vpna
   [*Spoke2-ospf-2] vpn-instance-capability simple
   Warning: This operation may cause a routing loop. Continue? [Y/N]:Y
   [*Spoke2-ospf-2] area 0.0.0.0
   [*Spoke2-ospf-2-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke2-ospf-2-areHub-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*Spoke2-ospf-2-areHub-0.0.0.0] quit
   [*Spoke2-ospf-2] quit
   [~Spoke2] ospf 3 router-id 172.16.1.3 vpn-instance vpnb
   [*Spoke2-ospf-3] area 0.0.0.0
   [*Spoke2-ospf-3-areHub-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke2-ospf-3-areHub-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*Spoke2-ospf-3-areHub-0.0.0.0] quit
   [*Spoke2-ospf-3] quit
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
   
   
   
   Configure the IKE peer required for IKE negotiation on Hub and spokes.
   
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
   
   
   
   Create an IPsec proposal on Hub and spokes.
   
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
   
   
   
   Configure an IPsec profile on Hub and spokes.
   
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
   
   
   
   Configure an IPsec service instance group on Hub and spokes.
   
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
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Generally, one IPsec profile can be applied only to one interface. In a scenario where multiple mGRE tunnels of a DSVPN share the same source, if the same IPsec profile needs to be applied to multiple tunnel interfaces for IPsec tunnel sharing, specify the **share** parameter when running this command. The **share** parameter can be used only in this scenario. In addition, mGRE tunnels with the same source must be configured with different keys.
    
    
    # Configure tunnel interfaces and OSPF attributes and apply the IPsec profile on Hub.
    ```
    [~Hub] interface tunnel 0
    [*Hub-Tunnel0] tunnel-protocol gre p2mp
    [*Hub-Tunnel0] nhrp enable
    [*Hub-Tunnel0] source 10.1.1.10
    [*Hub-Tunnel0] gre key cipher 123
    [*Hub-Tunnel0] nhrp entry multicast dynamic
    [*Hub-Tunnel0] ospf network-type p2mp
    [*Hub-Tunnel0] nhrp redirect
    [*Hub-Tunnel0] ipsec policy 1 service-instance-group group1 share  
    [*Hub-Tunnel0] quit
    [*Hub] commit
    [~Hub] interface tunnel 1
    [*Hub-Tunnel1] tunnel-protocol gre p2mp
    [*Hub-Tunnel1] nhrp enable
    [*Hub-Tunnel1] source 10.1.1.10
    [*Hub-Tunnel1] gre key cipher 456
    [*Hub-Tunnel1] nhrp entry multicast dynamic
    [*Hub-Tunnel1] ospf network-type p2mp
    [*Hub-Tunnel1] nhrp redirect
    [*Hub-Tunnel1] ipsec policy 1 service-instance-group group1 share  
    [*Hub-Tunnel1] quit
    [*Hub] commit
    ```
    
    # Configure tunnel interfaces, OSPF route attributes, and Hub's static NHRP peer entry, and apply the IPsec profile on Spoke 1.
    ```
    [~Spoke1] interface tunnel 0
    [*Spoke1-Tunnel0] tunnel-protocol gre p2mp
    [*Spoke1-Tunnel0] nhrp enable
    [*Spoke1-Tunnel0] source 10.1.2.10
    [*Spoke1-Tunnel0] gre key cipher 123
    [*Spoke1-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke1-Tunnel0] ospf network-type p2mp
    [*Spoke1-Tunnel0] nhrp shortcut
    [*Spoke1-Tunnel0] ipsec policy 1 service-instance-group group1 share
    [*Spoke1-Tunnel0] quit
    [*Spoke1] commit
    [~Spoke1] interface tunnel 1
    [*Spoke1-Tunnel1] tunnel-protocol gre p2mp
    [*Spoke1-Tunnel1] nhrp enable
    [*Spoke1-Tunnel1] source 10.1.2.10
    [*Spoke1-Tunnel1] gre key cipher 456
    [*Spoke1-Tunnel1] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke1-Tunnel1] ospf network-type p2mp
    [*Spoke1-Tunnel1] nhrp shortcut
    [*Spoke1-Tunnel1] ipsec policy 1 service-instance-group group1 share
    [*Spoke1-Tunnel1] quit
    [*Spoke1] commit
    ```
    
    # Configure tunnel interfaces, OSPF route attributes, and Hub's static NHRP peer entry, and apply the IPsec profile on Spoke 2.
    ```
    [~Spoke2] interface tunnel 0
    [*Spoke2-Tunnel0] tunnel-protocol gre p2mp
    [*Spoke2-Tunnel0] nhrp enable
    [*Spoke2-Tunnel0] source 10.1.3.10
    [*Spoke2-Tunnel0] gre key cipher 123
    [*Spoke2-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke2-Tunnel0] ospf network-type p2mp
    [*Spoke2-Tunnel0] nhrp shortcut
    [*Spoke2-Tunnel0] ipsec policy 1 service-instance-group group1 share
    [*Spoke2-Tunnel0] quit
    [*Spoke2] commit
    [~Spoke2] interface tunnel 1
    [*Spoke2-Tunnel1] tunnel-protocol gre p2mp
    [*Spoke2-Tunnel1] nhrp enable
    [*Spoke2-Tunnel1] source 10.1.3.10
    [*Spoke2-Tunnel1] gre key cipher 456
    [*Spoke2-Tunnel1] nhrp entry 172.16.1.1 10.1.1.10 register
    [*Spoke2-Tunnel1] ospf network-type p2mp
    [*Spoke2-Tunnel1] nhrp shortcut
    [*Spoke2-Tunnel1] ipsec policy 1 service-instance-group group1 share
    [*Spoke2-Tunnel1] quit
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
    Tunnel interface: Tunnel0 (VPN instance: vpna) 
    Created time    : 00:10:58 
    Expire time     : -- 
    ------------------------------------------------------------------------------- 
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
    ------------------------------------------------------------------------------- 
    172.16.1.1      32    10.1.1.10      172.16.1.1       hub          up 
    ------------------------------------------------------------------------------- 
    Tunnel interface: Tunnel1 (VPN instance: vpnb) 
    Created time    : 00:10:59 
    Expire time     : -- 
    -------------------------- 
    Number of nhrp peers: 2 
    ```
    
    # Run the **display nhrp peer all** command on Spoke 2. The command output is as follows.
    ```
    [~Spoke2] display nhrp peer all
    ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.1      32    10.1.1.10      172.16.1.1       hub          up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel0 (VPN instance: vpna) 
     Created time    : 00:07:55 
     Expire time     : -- 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.1      32    10.1.1.10      172.16.1.1       hub          up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel1 (VPN instance: vpnb) 
     Created time    : 00:07:56 
     Expire time     : -- 
     -------------------------- 
     Number of nhrp peers: 2 
    ```
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    After the configuration is complete, the **display nhrp peer all** command output shows only the static NHRP peer entries mapped to Hub on Spoke 1 and Spoke 2.
    
    On Hub, verify registration information about Spoke 1 and Spoke 2.
    
    # Run the **display nhrp peer all** command on Hub. The command output is as follows.
    ```
    [~Hub] display nhrp peer all
    ------------------------------------------------------------------------------- 
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
    ------------------------------------------------------------------------------- 
    172.16.1.2      32    10.1.2.10      172.16.1.2      registered   up|unique 
    ------------------------------------------------------------------------------- 
    Tunnel interface: Tunnel0 (VPN instance: vpna) 
    Created time    : 00:02:02 
    Expire time     : 01:57:58 
    ------------------------------------------------------------------------------- 
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
    ------------------------------------------------------------------------------- 
    172.16.1.3      32    10.1.3.10      172.16.1.3      registered   up|unique 
    ------------------------------------------------------------------------------- 
    Tunnel interface: Tunnel0 (VPN instance: vpna) 
    Created time    : 00:01:53 
    Expire time     : 01:58:07 
    ------------------------------------------------------------------------------- 
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
    ------------------------------------------------------------------------------- 
    172.16.1.2      32    10.1.2.10      172.16.1.2      registered   up|unique 
    ------------------------------------------------------------------------------- 
    Tunnel interface: Tunnel1 (VPN instance: vpnb) 
    Created time    : 00:02:03 
    Expire time     : 01:57:57 
    ------------------------------------------------------------------------------- 
    Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag 
    ------------------------------------------------------------------------------- 
    172.16.1.3      32    10.1.3.10      172.16.1.3      registered   up|unique 
    ------------------------------------------------------------------------------- 
    Tunnel interface: Tunnel1 (VPN instance: vpnb) 
    Created time    : 00:01:54 
    Expire time     : 01:58:06 
    -------------------------- 
    Number of nhrp peers: 4 
    ```
12. Run the **ping** command and check the configuration result.
    
    
    
    Ping the subnet address 192.168.2.1 of Spoke 2 from the two VPN instances on Spoke 1. Then, verify the dynamic NHRP peer entries of Spoke 1 and Spoke 2.
    
    # Run the **ping -vpn-instance-vpna -a 192.168.1.1 192.168.2.1** and **ping -vpn-instance-vpnb -a 192.168.1.1 192.168.2.1** commands on Spoke 1. The command output is as follows.
    
    ```
    [~Spoke1] ping -vpn-instance-vpna -a 192.168.1.1 192.168.2.1
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
    
    [~Spoke1] ping -vpn-instance-vpnb -a 192.168.1.1 192.168.2.1 
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
    
    # Run the **display nhrp peer all** command on Spoke 1. The command output on Spoke 1 is used as an example.
    
    ```
    [~Spoke1] display nhrp peer all
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.1      32    10.1.1.10      172.16.1.1      hub              up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel0 (VPN instance: vpna) 
     Created time    : 00:46:35 
     Expire time     : -- 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     192.168.2.1     32    10.1.3.10      172.16.1.3      remote-network  up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel0 (VPN instance: vpna) 
     Created time    : 00:00:28 
     Expire time     : 01:59:32 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.3      32    10.1.3.10      172.16.1.3      remote          up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel0 (VPN instance: vpna) 
     Created time    : 00:00:28 
     Expire time     : 01:59:32 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.2      32    10.1.2.10      172.16.1.2      local           up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel0 (VPN instance: vpna) 
     Created time    : 00:00:28 
     Expire time     : 01:59:32 
    [~Spoke1] display nhrp peer all
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.1      32    10.1.1.10      172.16.1.1      hub              up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel1 (VPN instance: vpnb) 
     Created time    : 00:46:36 
     Expire time     : -- 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     192.168.2.1     32    10.1.3.10      172.16.1.3      remote-network  up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel1 (VPN instance: vpnb) 
     Created time    : 00:00:22 
     Expire time     : 01:59:38 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.3      32    10.1.3.10      172.16.1.3      remote          up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel1 (VPN instance: vpnb) 
     Created time    : 00:00:22 
     Expire time     : 01:59:38 
     ------------------------------------------------------------------------------- 
     Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type            Flag 
     ------------------------------------------------------------------------------- 
     172.16.1.2      32    10.1.2.10      172.16.1.2      local           up 
     ------------------------------------------------------------------------------- 
     Tunnel interface: Tunnel1 (VPN instance: vpnb) 
     Created time    : 00:00:22 
     Expire time     : 01:59:38 
     -------------------------- 
     Number of nhrp peers: 8 
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
  ip vpn-instance vpna 
    ipv4-family 
     route-distinguisher 100:1 
     apply-label per-instance
     vpn-target 111:1 export-extcommunity 
     vpn-target 111:1 import-extcommunity 
  # 
  ip vpn-instance vpnb 
   ipv4-family 
    route-distinguisher 100:2 
    apply-label per-instance
    vpn-target 222:2 export-extcommunity 
    vpn-target 222:2 import-extcommunity 
  # 
  interface GigabitEthernet0/1/0
   ip address 10.1.1.10 255.255.255.0
  # 
  interface LoopBack0
   ip binding vpn-instance vpna
   ip address 192.168.0.1 255.255.255.255
  # 
  interface LoopBack1 
   ip binding vpn-instance vpnb 
   ip address 192.168.0.1 255.255.255.255 
  #
  interface Tunnel0
   ip binding vpn-instance vpna
   ip address 172.16.1.1 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.1.10
   gre key cipher %^%#GF3A:qC<_7"nw=Hb'vv~S8l,.!(GB%)&%]3NBmc*%^%#
   nhrp enable
   nhrp redirect
   nhrp entry multicast dynamic
   ipsec policy 1 service-instance-group group1 share
   ospf network-type p2mp
  # 
  interface Tunnel1 
   ip binding vpn-instance vpnb 
   ip address 172.16.1.1 255.255.255.0 
   tunnel-protocol gre p2mp 
   source 10.1.1.10 
   gre key cipher %^%#8-'W16TBd:UJ-rHbf&{P^Syv#i\Q!U`ukG>uDul%%^%#
   nhrp enable 
   nhrp redirect 
   nhrp entry multicast dynamic 
   ipsec policy 1 service-instance-group group1 share 
   ospf network-type p2mp 
  #
  ospf 1 router-id 10.1.1.10
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
  #
  ospf 2 router-id 172.16.1.1 vpn-instance vpna 
   vpn-instance-capability simple 
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.0.0 0.0.0.255
  # 
  ospf 3 router-id 172.16.1.1 vpn-instance vpnb 
   vpn-instance-capability simple 
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.0.0 0.0.0.255
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
  ip vpn-instance vpna 
   ipv4-family 
    route-distinguisher 200:1 
    apply-label per-instance 
    vpn-target 111:1 export-extcommunity 
    vpn-target 111:1 import-extcommunity 
  #
  ip vpn-instance vpnb 
   ipv4-family 
    route-distinguisher 200:2 
    apply-label per-instance 
    vpn-target 222:2 export-extcommunity 
    vpn-target 222:2 import-extcommunity 
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.2.10 255.255.255.0
  # 
  interface LoopBack0
   ip binding vpn-instance vpna
   ip address 192.168.1.1 255.255.255.255
  # 
  interface LoopBack1
   ip binding vpn-instance vpnb
   ip address 192.168.1.1 255.255.255.255
  # 
  interface Tunnel0
   ip binding vpn-instance vpna
   ip address 172.16.1.2 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.2.10
   gre key cipher %^%#GF3A:qC<_7"nw=Hb'vv~S8l,.!(GB%)&%]3NBmc*%^%# 
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1 share
   ospf network-type p2mp
  # 
  interface Tunnel1
   ip binding vpn-instance vpnb
   ip address 172.16.1.2 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.2.10
   gre key cipher %^%#8-'W16TBd:UJ-rHbf&{P^Syv#i\Q!U`ukG>uDul%%^%# 
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1 share
   ospf network-type p2mp
  #
  ospf 1 router-id 10.1.2.10
   area 0.0.0.1
    network 10.1.2.0 0.0.0.255
  #
  ospf 2 router-id 172.16.1.2 vpn-instance vpna
   vpn-instance-capability simple 
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #  
  ospf 3 router-id 172.16.1.2 vpn-instance vpnb
   vpn-instance-capability simple 
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
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
  ipsec policy 1
   ike-peer spoke2
   proposal pro1
  # 
  ip vpn-instance vpna 
   ipv4-family 
    route-distinguisher 300:1 
    apply-label per-instance
    vpn-target 111:1 export-extcommunity 
    vpn-target 111:1 import-extcommunity 
  #
  ip vpn-instance vpnb
   ipv4-family 
    route-distinguisher 300:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity 
    vpn-target 222:2 import-extcommunity 
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.3.10 255.255.255.0
  # 
  interface LoopBack0
   ip binding vpn-instance vpna
   ip address 192.168.2.1 255.255.255.255
  # 
  interface LoopBack1
   ip binding vpn-instance vpnb
   ip address 192.168.2.1 255.255.255.255
  #
  interface Tunnel0
   ip binding vpn-instance vpna
   ip address 172.16.1.3 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.3.10
   gre key cipher %^%#GF3A:qC<_7"nw=Hb'vv~S8l,.!(GB%)&%]3NBmc*%^%# 
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1 share
   ospf network-type p2mp
  # 
  interface Tunnel1
   ip binding vpn-instance vpnb
   ip address 172.16.1.3 255.255.255.0
   tunnel-protocol gre p2mp
   source 10.1.3.10
   gre key cipher %^%#8-'W16TBd:UJ-rHbf&{P^Syv#i\Q!U`ukG>uDul%%^%#  
   nhrp enable
   nhrp shortcut
   nhrp entry 172.16.1.1 10.1.1.10 register
   ipsec policy 1 service-instance-group group1 share
   ospf network-type p2mp
  #
  ospf 1 router-id 10.1.3.10 
   area 0.0.0.1 
    network 10.1.3.0 0.0.0.255 
  # 
  ospf 2 router-id 172.16.1.3 vpn-instance vpna
   vpn-instance-capability simple
   area 0.0.0.0 
    network 172.16.1.0 0.0.0.255 
    network 192.168.2.0 0.0.0.255 
  # 
  ospf 3 router-id 172.16.1.3 vpn-instance vpnb 
   vpn-instance-capability simple
   area 0.0.0.0 
    network 172.16.1.0 0.0.0.255 
    network 192.168.2.0 0.0.0.255 
  # 
  return 
  ```