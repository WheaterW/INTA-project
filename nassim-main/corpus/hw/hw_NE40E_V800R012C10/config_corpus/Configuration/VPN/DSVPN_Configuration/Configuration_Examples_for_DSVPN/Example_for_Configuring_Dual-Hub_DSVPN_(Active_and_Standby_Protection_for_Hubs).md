Example for Configuring Dual-Hub DSVPN (Active/Standby Protection for Hubs)
===========================================================================

Example for Configuring Dual-Hub DSVPN (Active/Standby Protection for Hubs)

#### Networking Requirements

In an enterprise, HQ hubs (Hub 1 and Hub 2) connect to branch spokes (Spoke 1 and Spoke 2) over the public network, and branch spokes use dynamic addresses to access the public network. HQ hubs (Hub 1 and Hub 2) and branch spokes (Spoke 1 and Spoke 2) are located in different areas, and the subnet environments of the HQ and branches change frequently. The enterprise wants to use a VPN for communication between branches, with Hub 1 as the active hub and Hub 2 the standby hub. Hub 2 forwards protocol packets when Hub 1 is faulty and continues to serve as the standby hub after Hub 1 recovers. To meet this requirement, deploy dynamic routing (OSPF) based on enterprise network planning and configure dual-hub DSVPN to improve the reliability of the DSVPN and enable Spoke 1 and Spoke 2 to directly communicate. [Figure 1](#EN-US_TASK_0172369166__fig_dc_cfg_dsvpn_001801) shows the related networking.

**Figure 1** Configuring dual-hub DSVPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](images/fig_dc_cfg_dsvpn_001801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Because branches access the public network through dynamic IP addresses, branches are unaware of each other's public IP address. Therefore, configure DSVPN to interconnect branches.
2. Because a large number of branches exist, configure DSVPN in shortcut mode.
3. Because the subnet environments of the HQ and branches frequently change, deploy OSPF based on enterprise network planning for communication between the HQ and branches to simplify maintenance.
4. To use Hub 2 for backup, configure dual-hub DSVPN.


#### Procedure

1. Configure interface IP addresses.
   
   
   
   Configure interface IP addresses on each device.
   
   # Configure interface IP addresses on Hub 1.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Hub1
   [*HUAWEI] commit
   [~Hub1] interface GigabitEthernet 0/1/0
   [*Hub1-GigabitEthernet0/1/0] ip address 10.1.1.10 255.255.255.0
   [*Hub1-GigabitEthernet0/1/0] binding tunnel gre
   [*Hub1-GigabitEthernet0/1/0] quit
   [*Hub1] interface tunnel 0
   [*Hub1-Tunnel0] ip address 172.16.1.1 255.255.255.0
   [*Hub1-Tunnel0] quit
   [*Hub1] interface loopback 0
   [*Hub1-LoopBack0] ip address 192.168.0.1 255.255.255.255
   [*Hub1-LoopBack0] quit
   [*Hub1] commit
   ```
   
   Assign an IP address to each interface of Spoke 1, Spoke 2, and Hub 2 according to [Figure 1](#EN-US_TASK_0172369166__fig_dc_cfg_dsvpn_001801). The configurations of the spokes are similar to the configuration of Hub 1.
2. Configure public network routes between devices to implement connectivity.
   
   
   
   Configure OSPF on each device to ensure that the public network routes are available.
   
   # Configure OSPF on Hub 1.
   
   ```
   [~Hub1] ospf 2 router-id 10.1.1.10
   [*Hub1-ospf-2] area 0.0.0.1
   [*Hub1-ospf-2-area-0.0.0.1] network 10.1.1.0 0.0.0.255
   [*Hub1-ospf-2-area-0.0.0.1] quit
   [*Hub1-ospf-2] quit
   [*Hub1] commit
   ```
   
   # Configure OSPF on Hub 2.
   
   ```
   [~Hub2] ospf 2 router-id 10.1.254.10
   [*Hub2-ospf-2] area 0.0.0.1
   [*Hub2-ospf-2-area-0.0.0.1] network 10.1.254.0 0.0.0.255
   [*Hub2-ospf-2-area-0.0.0.1] quit
   [*Hub2-ospf-2] quit
   [*Hub2] commit
   ```
   
   # Configure OSPF on Spoke 1.
   
   ```
   [~Spoke1] ospf 2 router-id 10.1.2.10
   [*Spoke1-ospf-2] area 0.0.0.1
   [*Spoke1-ospf-2-area-0.0.0.1] network 10.1.2.0 0.0.0.255
   [*Spoke1-ospf-2-area-0.0.0.1] quit
   [*Spoke1-ospf-2] quit
   [*Spoke1] commit
   ```
   
   # Configure OSPF on Spoke 2.
   
   ```
   [~Spoke2] ospf 2 router-id 10.1.3.10
   [*Spoke2-ospf-2] area 0.0.0.1
   [*Spoke2-ospf-2-area-0.0.0.1] network 10.1.3.0 0.0.0.255
   [*Spoke2-ospf-2-area-0.0.0.1] quit
   [*Spoke2-ospf-2] quit
   [*Spoke2] commit
   ```
3. Configure basic OSPF functions.
   
   
   
   # Configure Hub 1.
   
   ```
   [~Hub1] acl number 2000
   [*Hub1-acl4-basic-2000] rule 5 permit source 192.168.0.0 0.0.0.255
   [*Hub1-acl4-basic-2000] quit
   [*Hub1] route-policy 1 permit node 1
   [*Hub1-route-policy] if-match acl 2000
   [*Hub1-route-policy] quit
   [*Hub1] acl number 2001
   [*Hub1-acl4-basic-2001] rule 5 permit source 192.168.1.0 0.0.0.255
   [*Hub1-acl4-basic-2001] rule 10 permit source 192.168.2.0 0.0.0.255
   [*Hub1-acl4-basic-2001] quit
   [*Hub1] route-policy 2 permit node 2
   [*Hub1-route-policy] if-match acl 2001
   [*Hub1-route-policy] quit
   [*Hub1] ospf 1 router-id 172.16.1.1
   [*Hub1-ospf-1] import-route ospf 3 route-policy 1
   [*Hub1-ospf-1] area 0.0.0.0
   [*Hub1-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub1-ospf-1-area-0.0.0.0] quit
   [*Hub1-ospf-1] quit
   [*Hub1] ospf 3 router-id 192.168.0.1
   [*Hub1-ospf-3] import-route ospf 1 route-policy 2
   [*Hub1-ospf-3] area 0.0.0.0
   [*Hub1-ospf-3-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub1-ospf-3-area-0.0.0.0] quit
   [*Hub1-ospf-3] quit
   [*Hub1] commit
   ```
   
   # Configure Hub 2.
   
   ```
   [~Hub2] acl number 2000
   [*Hub2-acl4-basic-2000] rule 5 permit source 192.168.0.0 0.0.0.255
   [*Hub2-acl4-basic-2000] quit
   [*Hub2] route-policy 1 permit node 1
   [*Hub2-route-policy] if-match acl 2000
   [*Hub2-route-policy] quit
   [*Hub2] acl number 2001
   [*Hub2-acl4-basic-2001] rule 5 permit source 192.168.1.0 0.0.0.255
   [*Hub2-acl4-basic-2001] rule 10 permit source 192.168.2.0 0.0.0.255
   [*Hub2-acl4-basic-2001] quit
   [*Hub2] route-policy 2 permit node 2
   [*Hub2-route-policy] if-match acl 2001
   [*Hub2-route-policy] quit
   [*Hub2] ospf 1 router-id 172.16.1.254
   [*Hub2-ospf-1] import-route ospf 3 route-policy 1
   [*Hub2-ospf-1] area 0.0.0.0
   [*Hub2-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub2-ospf-1-area-0.0.0.0] quit
   [*Hub2-ospf-1] quit
   [*Hub2] ospf 3 router-id 192.168.0.2
   [*Hub2-ospf-3] import-route ospf 1 route-policy 2
   [*Hub2-ospf-3] area 0.0.0.0
   [*Hub2-ospf-3-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub2-ospf-3-area-0.0.0.0] quit
   [*Hub2-ospf-3] quit
   [*Hub2] commit
   ```
   
   # Configure Spoke 1.
   
   ```
   [~Spoke1] ospf 1 router-id 172.16.1.2
   [*Spoke1-ospf-1] area 0.0.0.0
   [*Spoke1-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke1-ospf-1-area-0.0.0.0] network 192.168.1.0 0.0.0.255
   [*Spoke1-ospf-1-area-0.0.0.0] quit
   [*Spoke1-ospf-1] quit
   [*Spoke1] commit
   ```
   
   # Configure Spoke 2.
   
   ```
   [~Spoke2] ospf 1 router-id 172.16.1.3
   [*Spoke2-ospf-1] area 0.0.0.0
   [*Spoke2-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Spoke2-ospf-1-area-0.0.0.0] network 192.168.2.0 0.0.0.255
   [*Spoke2-ospf-1-area-0.0.0.0] quit
   [*Spoke2-ospf-1] quit
   [*Spoke2] commit
   ```
4. Enable NHRP globally.
   
   
   
   # Configure Hub 1.
   
   ```
   [~Hub1] nhrp enable
   ```
   
   The configurations of Spoke 1, Spoke 2, and Hub 2 are similar to the configuration of Hub 1.
5. Configure tunnel interfaces.
   
   
   
   Set the OSPF network type to P2MP on the hubs and spokes. Enable the NHRP redirection function on Hub 1 and Hub 2. Configure NHRP peer entries mapped to Hub 1 and Hub 2 respectively and enable the NHRP shortcut function on Spoke 1 and Spoke 2.
   
   # Configure a tunnel interface and OSPF route attributes and enable the NHRP redirection function on Hub 1.
   ```
   [~Hub1] interface tunnel 0
   [*Hub1-Tunnel0] tunnel-protocol gre p2mp
   [*Hub-Tunnel0] nhrp enable
   [*Hub1-Tunnel0] source gigabitethernet 0/1/0
   [*Hub1-Tunnel0] nhrp entry multicast dynamic
   [*Hub1-Tunnel0] ospf network-type p2mp
   [*Hub1-Tunnel0] nhrp redirect
   [*Hub1-Tunnel0] quit
   [*Hub1] commit
   ```
   
   # Configure a tunnel interface and OSPF route attributes and enable the NHRP redirection function on Hub 2.
   ```
   [~Hub2] interface tunnel 0
   [*Hub2-Tunnel0] tunnel-protocol gre p2mp
   [*Hub2-Tunnel0] nhrp enable
   [*Hub2-Tunnel0] source gigabitethernet 0/1/0
   [*Hub2-Tunnel0] nhrp entry multicast dynamic
   [*Hub2-Tunnel0] ospf network-type p2mp
   [*Hub2-Tunnel0] nhrp redirect
   [*Hub2-Tunnel0] quit
   [*Hub2] commit
   ```
   
   # Configure a tunnel interface, OSPF route attributes, and static NHRP peer entries (mapped to Hub 1 and Hub 2), and enable the NHRP shortcut function on Spoke 1.
   ```
   [~Spoke1] interface tunnel 0
   [*Spoke1-Tunnel0] tunnel-protocol gre p2mp
   [*Spoke1-Tunnel0] nhrp enable
   [*Spoke1-Tunnel0] source gigabitethernet 0/1/0
   [*Spoke1-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
   [*Spoke1-Tunnel0] nhrp entry 172.16.1.254 10.1.254.10 register
   [*Spoke1-Tunnel0] ospf network-type p2mp
   [*Spoke1-Tunnel0] nhrp shortcut
   [*Spoke1-Tunnel0] nhrp registration interval 300
   [*Spoke1-Tunnel0] quit
   [*Spoke1] commit
   [~Spoke1] ospf 1
   [*Spoke1-ospf-1] nexthop 172.16.1.1 weight 1
   [*Spoke1] commit
   ```
   
   # Configure a tunnel interface, OSPF route attributes, and static NHRP peer entries (mapped to Hub 1 and Hub 2), and enable the NHRP shortcut function on Spoke 2.
   ```
   [~Spoke2] interface tunnel 0
   [*Spoke2-Tunnel0] tunnel-protocol gre p2mp
   [*Spoke2-Tunnel0] nhrp enable
   [*Spoke2-Tunnel0] source gigabitethernet 0/1/0
   [*Spoke2-Tunnel0] nhrp entry 172.16.1.1 10.1.1.10 register
   [*Spoke2-Tunnel0] nhrp entry 172.16.1.254 10.1.254.10 register
   [*Spoke2-Tunnel0] ospf network-type p2mp
   [*Spoke2-Tunnel0] nhrp shortcut
   [*Spoke2-Tunnel0] nhrp registration interval 300
   [*Spoke2-Tunnel0] quit
   [*Spoke2] commit
   [~Spoke2] ospf 1
   [*Spoke2-ospf-1] nexthop 172.16.1.1 weight 1
   [*Spoke2] commit
   ```
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To enable spokes to preferentially select Hub 1 as a next hop, configure different OSPF cost values for Hub 1 and Hub 2.
   * When Hub 1 recovers, it restarts to forward OSPF protocol packets when receiving NHRP Registration Request packets from spokes. The spokes learn routes to Hub 1 after the routes they have already learned are aged out. Set the interval for sending NHRP Registration Request packets to a proper value to ensure that the spokes can quick detect Hub 1 recovery. The interval is set to 1800 seconds by default.
6. Verify the DSVPN configuration.
   
   
   
   After completing the configuration, check NHRP peer information on the spokes and hubs. The following command output on Spoke 1 is used as an example.
   
   # Run the **display nhrp peer all** command on Spoke 1. The command output is as follows.
   
   ```
   [~Spoke1] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.1.1.10      172.16.1.1      hub           up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 05:35:50
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.254    32    10.1.254.10    172.16.1.254    hub          up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 04:32:49
   Expire time     : --
   
   Number of nhrp peers: 2
   
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **display nhrp peer all** command output shows that the static NHRP peer entry mapped only to Hub is displayed on Spoke 1 and Spoke 2.
7. Run the **ping** command and check the configuration result.
   
   
   
   On Spoke 1, ping the subnet address 192.168.2.1 of Spoke 2. Then, verify the dynamic NHRP peer entries of Spoke 1 and Spoke 2.
   
   # Run the **ping -a 192.168.1.1 192.168.2.1** command on Spoke 1. The command output is as follows.
   
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
   
   # Run the **display nhrp peer all** command on each spoke. The following uses the command output on Spoke 1 as an example.
   
   ```
   [~Spoke1] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.1.1.10      172.16.1.1      hub          up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 05:42:50
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.254    32    10.1.254.10    172.16.1.254    hub          up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 04:39:49
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type           Flag
   -------------------------------------------------------------------------------
   192.168.2.1     32    10.1.3.10      172.16.1.3      remote-network up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:19
   Expire time     : 01:59:41
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.3      32    10.1.3.10      172.16.1.3      remote       up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:19
   Expire time     : 01:59:41
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   192.168.1.1     32    10.1.2.10      172.16.1.2      local        up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:19
   Expire time     : 01:59:41
   
   Number of nhrp peers: 5
   ```
8. Simulate a Hub 1 failure by shutting down GE 0/1/0 connected to the public network on Hub 1.
   
   
   
   # Shut down GE 0/1/0 on Hub 1.
   
   ```
   [~Hub1] interface GigabitEthernet 0/1/0
   [~Hub1-GigabitEthernet0/1/0] shutdown
   [~Hub1-GigabitEthernet0/1/0] quit
   ```
9. Run the **ping** command again and check the configuration result.
   
   
   
   On Spoke 1, ping the subnet address 192.168.2.1 of Spoke 2. Then, verify the dynamic NHRP peer entries of Spoke 1 and Spoke 2.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   Before running the **ping** command, ensure that no default route to Hub 1 exists on the local device.
   
   # Run the **ping -a 192.168.1.1 192.168.2.1** command on Spoke 1. The command output is as follows.
   
   ```
   [~Spoke1] ping -a 192.168.1.1 192.168.2.1
     PING 192.168.2.1: 56  data bytes, press CTRL_C to break
       Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=254 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=255 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=255 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=255 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=255 time=2 ms
   
     --- 192.168.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 2/2/2 ms
   ```
   
   # Run the **display nhrp peer all** command on each spoke. The following uses the command output on Spoke 1 as an example.
   
   ```
   [~Spoke1] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.1.1.10      172.16.1.1      hub          down
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 05:46:29
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.254    32    10.1.254.10    172.16.1.254    hub          up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 04:43:28
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type           Flag
   -------------------------------------------------------------------------------
   192.168.2.1     32    10.1.3.10      172.16.1.3      remote-network up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:22
   Expire time     : 01:59:38
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.3      32    10.1.3.10      172.16.1.3      remote       up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:22
   Expire time     : 01:59:38
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   192.168.1.1     32    10.1.2.10      172.16.1.2      local        up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:22
   Expire time     : 01:59:38
   
   Number of nhrp peers: 5
   ```

#### Configuration Files

* Hub 1 configuration file
  
  ```
  #
  sysname Hub1
  #
  acl number 2000
   rule 5 permit source 192.168.0.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.1.0 0.0.0.255
   rule 10 permit source 192.168.2.0 0.0.0.255
  #
  route-policy 1 permit node 1
   if-match acl 2000
  #
  route-policy 2 permit node 2
   if-match acl 2001
  # 
  nhrp enable
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.1.10 255.255.255.0
   binding tunnel gre
  #
  interface LoopBack0
   ip address 192.168.0.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.1 255.255.255.0
   tunnel-protocol gre p2mp
   source GigabitEthernet0/1/0
   ospf network-type p2mp
   nhrp enable
   nhrp redirect
   nhrp entry multicast dynamic
  #
  ospf 1 router-id 172.16.1.1
   import-route ospf 3 route-policy 1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.1.10
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
  #
  ospf 3 router-id 192.168.0.1
   import-route ospf 1 route-policy 2
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
  # 
  return
  ```
* Hub 2 configuration file
  
  ```
  #
  sysname Hub2
  #
  acl number 2000
   rule 5 permit source 192.168.0.0 0.0.0.255
  #
  acl number 2001
   rule 5 permit source 192.168.1.0 0.0.0.255
   rule 10 permit source 192.168.2.0 0.0.0.255
  #
  route-policy 1 permit node 1
   if-match acl 2000
  #
  route-policy 2 permit node 2
   if-match acl 2001
  # 
  nhrp enable
  #
  interface GigabitEthernet0/1/0
   ip address 10.1.254.10 255.255.255.0
   binding tunnel gre
  #
  interface LoopBack0
   ip address 192.168.0.2 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.254 255.255.255.0
   tunnel-protocol gre p2mp
   source GigabitEthernet0/1/0
   ospf network-type p2mp
   nhrp enable
   nhrp redirect
   nhrp entry multicast dynamic
  #
  ospf 1 router-id 172.16.1.254
   import-route ospf 3 route-policy 1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.254.10
   area 0.0.0.1
    network 10.1.254.0 0.0.0.255
  #
  ospf 3 router-id 192.168.0.2
   import-route ospf 1 route-policy 2
    area 0.0.0.0
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
  interface GigabitEthernet0/1/0
   ip address 10.1.2.10 255.255.255.0
   binding tunnel gre
  #
  interface LoopBack0
   ip address 192.168.1.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.2 255.255.255.0
   tunnel-protocol gre p2mp
   source GigabitEthernet0/1/0
   ospf network-type p2mp
   nhrp enable
   nhrp shortcut
   nhrp registration interval 300
   nhrp entry 172.16.1.254 10.1.254.10 register
   nhrp entry 172.16.1.1 10.1.1.10 register
  # 
  ospf 1 router-id 172.16.1.2
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
    nexthop 172.16.1.1 weight 1
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
  interface GigabitEthernet0/1/0
   ip address 10.1.3.10 255.255.255.0
   binding tunnel gre
  #
  interface LoopBack0
   ip address 192.168.2.1 255.255.255.255
  # 
  interface Tunnel0
   ip address 172.16.1.3 255.255.255.0
   tunnel-protocol gre p2mp
   source GigabitEthernet0/1/0
   ospf network-type p2mp
   nhrp enable
   nhrp shortcut
   nhrp registration interval 300
   nhrp entry 172.16.1.254 10.1.254.10 register
   nhrp entry 172.16.1.1 10.1.1.10 register
  # 
  ospf 1 router-id 172.16.1.3
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
    nexthop 172.16.1.1 weight 1
  # 
  ospf 2 router-id 10.1.3.10
   area 0.0.0.1
    network 10.1.3.0 0.0.0.255
  # 
  return
  ```