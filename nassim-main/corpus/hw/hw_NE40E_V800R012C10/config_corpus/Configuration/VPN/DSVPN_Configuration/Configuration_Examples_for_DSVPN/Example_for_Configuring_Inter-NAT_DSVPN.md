Example for Configuring Inter-NAT DSVPN
=======================================

Example for Configuring Inter-NAT DSVPN

#### Networking Requirements

An enterprise has an HQ (Hub) and multiple branches (represented by Spoke 1 and Spoke 2 in this example). Spoke 1 and Spoke 2 connect to Hub over the public network after address translation by the NAT device. The translated addresses of Spoke 1 and Spoke 2 are unknown. The HQ hub and branch spokes are located in different areas, and the subnet environments of the HQ and branches change frequently. The enterprise wants to use a VPN for communication between branch spokes. To meet this requirement, deploy dynamic routing (OSPF) based on enterprise network planning and configure inter-NAT DSVPN to realize direct communication between Spoke 1 and Spoke 2. [Figure 1](#EN-US_TASK_0172369163__fig_dc_cfg_dsvpn_001701) shows the related networking.

**Figure 1** Configuring inter-NAT DSVPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GE0/1/0.


  
![](images/fig_dc_cfg_dsvpn_001701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Because branches access the public network after NAT processing, branches are unaware of each other's public IP address after NAT processing. In this situation, configure inter-NAT DSVPN to interconnect branches.
2. Because a large number of branches exist, configure DSVPN in shortcut mode.
3. Because the subnet environments of the HQ and branches frequently change, deploy OSPF based on enterprise network planning for communication between the HQ and branches to simplify maintenance.


#### Procedure

1. Configure interface IP addresses.
   
   
   
   Configure interface IP addresses on each device.
   
   # Configure interface IP addresses on Hub.
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Hub
   [*HUAWEI] commit
   [~Hub] interface GigabitEthernet 0/1/0
   [*Hub-GigabitEthernet0/1/0] ip address 10.10.1.10 255.255.255.0
   [*Hub-GigabitEthernet0/1/0] binding tunnel gre
   [*Hub-GigabitEthernet0/1/0] quit
   [*Hub] interface tunnel 0
   [*Hub-Tunnel0] ip address 172.16.1.1 255.255.255.0
   [*Hub-Tunnel0] quit
   [*Hub] interface loopback 0
   [*Hub-LoopBack0] ip address 192.168.0.1 255.255.255.255
   [*Hub-LoopBack0] quit
   [*Hub] commit
   ```
   
   Configure IP addresses for interfaces on Spoke 1, Spoke 2, NAT1, and NAT2 according to [Figure 1](#EN-US_TASK_0172369163__fig_dc_cfg_dsvpn_001701). The configurations of the spokes and NAT devices are the similar to the configuration of the hub.
2. Configure public network routes between devices to implement connectivity.
   
   
   
   Configure OSPF on each device to ensure that the public network routes are available.
   
   # Configure OSPF on Hub.
   
   ```
   [~Hub] ospf 2 router-id 10.10.1.10
   [*Hub-ospf-2] area 0.0.0.1
   [*Hub-ospf-2-area-0.0.0.1] network 10.10.1.0 0.0.0.255
   [*Hub-ospf-2-area-0.0.0.1] quit
   [*Hub-ospf-2] quit
   [*Hub] commit
   ```
   
   # Configure OSPF on Spoke 1.
   
   ```
   [~Spoke1] ospf 2 router-id 10.1.1.1
   [*Spoke1-ospf-2] area 0.0.0.1
   [*Spoke1-ospf-2-area-0.0.0.1] network 10.1.1.0 0.0.0.255
   [*Spoke1-ospf-2-area-0.0.0.1] quit
   [*Spoke1-ospf-2] quit
   [*Spoke1] commit
   ```
   
   # Configure OSPF on Spoke 2.
   
   ```
   [~Spoke2] ospf 2 router-id 10.2.2.2
   [*Spoke2-ospf-2] area 0.0.0.1
   [*Spoke2-ospf-2-area-0.0.0.1] network 10.2.2.0 0.0.0.255
   [*Spoke2-ospf-2-area-0.0.0.1] quit
   [*Spoke2-ospf-2] quit
   [*Spoke2] commit
   ```
3. Configure basic OSPF functions.
   
   
   
   # Configure Hub.
   
   ```
   [~Hub] ospf 1 router-id 172.16.1.1
   [*Hub-ospf-1] area 0.0.0.0
   [*Hub-ospf-1-area-0.0.0.0] network 172.16.1.0 0.0.0.255
   [*Hub-ospf-1-area-0.0.0.0] network 192.168.0.0 0.0.0.255
   [*Hub-ospf-1-area-0.0.0.0] quit
   [*Hub-ospf-1] quit
   [*Hub] commit
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
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on a spoke subnet is given as an example. Perform the same configuration on other spoke subnets. If a spoke subnet is changed, you only need to configure the dynamic routing policy on the local device.
4. Enable NHRP globally.
   
   
   
   # Configure Hub.
   
   ```
   [~Hub] nhrp enable
   ```
   
   The configurations of the spokes are similar to the configuration of the hub. For detailed configurations, see Configuration Files.
5. Configure tunnel interfaces.
   
   
   
   Set the OSPF network type to P2MP on the hub and spokes. Enable the NHRP redirection function on Hub. Configure static NHRP peer entries (mapped to Hub) and enable the NHRP shortcut function on Spoke 1 and Spoke 2.
   
   # Configure a tunnel interface and OSPF route attributes and enable the NHRP redirection function on Hub.
   ```
   [~Hub] interface tunnel 0
   [*Hub-Tunnel0] tunnel-protocol gre p2mp
   [*Hub-Tunnel0] nhrp enable
   [*Hub-Tunnel0] source gigabitethernet 0/1/0
   [*Hub-Tunnel0] nhrp entry multicast dynamic
   [*Hub-Tunnel0] ospf network-type p2mp
   [*Hub-Tunnel0] nhrp redirect
   [*Hub-Tunnel0] quit
   [*Hub] commit
   ```
   
   # Configure a tunnel interface, OSPF route attributes, and a static NHRP peer entry (mapped to Hub), and enable the NHRP shortcut function on Spoke 1.
   ```
   [~Spoke1] interface tunnel 0
   [*Spoke1-Tunnel0] tunnel-protocol gre p2mp
   [*Spoke1-Tunnel0] nhrp enable
   [*Spoke1-Tunnel0] source gigabitethernet 0/1/0
   [*Spoke1-Tunnel0] nhrp entry 172.16.1.1 10.10.1.10 register
   [*Spoke1-Tunnel0] ospf network-type p2mp
   [*Spoke1-Tunnel0] nhrp shortcut
   [*Spoke1-Tunnel0] quit
   [*Spoke1] commit
   ```
   
   # Configure a tunnel interface, OSPF route attributes, and a static NHRP peer entry (mapped to Hub), and enable the NHRP shortcut function on Spoke 2.
   ```
   [~Spoke2] interface tunnel 0
   [*Spoke2-Tunnel0] tunnel-protocol gre p2mp
   [*Spoke1-Tunnel0] nhrp enable
   [*Spoke2-Tunnel0] source gigabitethernet 0/1/0
   [*Spoke2-Tunnel0] nhrp entry 172.16.1.1 10.10.1.10 register
   [*Spoke2-Tunnel0] ospf network-type p2mp
   [*Spoke2-Tunnel0] nhrp shortcut
   [*Spoke2-Tunnel0] quit
   [*Spoke2] commit
   ```
6. Verify the DSVPN configuration.
   
   
   
   After the configuration is complete, verify NHRP peer information on spokes.
   
   # Run the **display nhrp peer all** command on Spoke 1. The command output is as follows.
   ```
   [~Spoke1] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.10.1.10      172.16.1.1       hub          up
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
   172.16.1.1      32    10.10.1.10      172.16.1.1       hub          up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:07:55
   Expire time     : --
   
   Number of nhrp peers: 1
   
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
   172.16.1.2      32    10.10.2.10      172.16.1.2      registered   up|unique
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:02:02
   Expire time     : 01:57:58
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.3      32    10.10.3.10      172.16.1.3      registered   up|unique
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:01:53
   Expire time     : 01:59:35
   
   Number of nhrp peers: 2
   
   ```
7. Run the **ping** command and check the configuration result.
   
   
   
   On Spoke 1, ping the subnet address 192.168.2.1 of Spoke 2. Then, verify the dynamic NHRP peer entries of Spoke 1 and Spoke 2.
   
   # Run the **ping -a 192.168.1.1 192.168.2.1** command on Spoke 1. The command output is as follows.
   
   ```
   [~Spoke1] ping -a 192.168.1.1 192.168.2.1
     PING 192.168.2.1: 56  data bytes, press CTRL_C to break
       Reply from 192.168.2.1: bytes=56 Sequence=1 ttl=254 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=2 ttl=255 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=3 ttl=255 time=1 ms
       Reply from 192.168.2.1: bytes=56 Sequence=4 ttl=255 time=2 ms
       Reply from 192.168.2.1: bytes=56 Sequence=5 ttl=255 time=1 ms
   
     --- 192.168.2.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/1/2 ms
                                                                                                        
   
   ```
   
   # Run the **display nhrp peer all** command on Spoke 1. The command output is as follows.
   
   ```
   [~Spoke1] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.10.1.10      172.16.1.1      hub           up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:39:32
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type           Flag
   -------------------------------------------------------------------------------
   192.168.2.1     32    10.10.3.10      172.16.1.3      remote-network up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Before NAT NBMA-addr: 10.2.2.2
   Created time    : 00:00:13
   Expire time     : 01:59:47
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.3      32    10.10.3.10      172.16.1.3      remote       up
   
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Before NAT NBMA-addr: 10.2.2.2
   Created time    : 00:00:13
   Expire time     : 01:59:47
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   192.168.1.1     32    10.1.1.1        172.16.1.2      local        up
   
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:13
   Expire time     : 01:59:47
   
   Number of nhrp peers: 4
   
   ```
   
   # Run the **display nhrp peer all** command on Spoke 2. The command output is as follows.
   
   ```
   [~Spoke2] display nhrp peer all
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.1      32    10.10.1.10      172.16.1.1      hub           up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:41:08
   Expire time     : --
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type           Flag
   -------------------------------------------------------------------------------
   192.168.1.1     32    10.10.2.10      172.16.1.2      remote-network up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Before NAT NBMA-addr: 10.1.1.1
   Created time    : 00:00:52
   Expire time     : 01:59:08
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   172.16.1.2      32    10.10.2.10      172.16.1.2      remote       up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Before NAT NBMA-addr: 10.1.1.1
   Created time    : 00:00:52
   Expire time     : 01:59:08
   -------------------------------------------------------------------------------
   Protocol-addr   Mask  NBMA-addr       NextHop-addr    Type         Flag
   -------------------------------------------------------------------------------
   192.168.2.1     32    10.2.2.2        172.16.1.3      local        up
   -------------------------------------------------------------------------------
   Tunnel interface: Tunnel0 (VPN instance: _public_)
   Created time    : 00:00:52
   Expire time     : 01:59:08
   
   Number of nhrp peers: 4
   
   ```

#### Configuration Files

* Hub configuration file
  
  ```
  #
  sysname Hub
  # 
  nhrp enable
  #
  interface GigabitEthernet0/1/0
   ip address 10.10.1.10 255.255.255.0
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
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.0.0 0.0.0.255
  # 
  ospf 2 router-id 10.10.1.10
   area 0.0.0.1
    network 10.10.1.0 0.0.0.255
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
   nhrp entry 172.16.1.1 10.10.1.10 register
  # 
  ospf 1 router-id 172.16.1.2
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  # 
  ospf 2 router-id 10.1.1.1
   area 0.0.0.1
    network 10.1.1.0 0.0.0.255
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
   nhrp entry 172.16.1.1 10.10.1.10 register
  # 
  ospf 1 router-id 172.16.1.3
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  # 
  ospf 2 router-id 10.2.2.2
   area 0.0.0.1
    network 10.2.2.0 0.0.0.255
  # 
  return
  
  ```