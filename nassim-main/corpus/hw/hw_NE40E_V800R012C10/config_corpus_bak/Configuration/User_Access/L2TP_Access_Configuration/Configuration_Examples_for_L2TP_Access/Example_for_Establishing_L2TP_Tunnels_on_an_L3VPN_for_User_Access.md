Example for Establishing L2TP Tunnels on an L3VPN for User Access
=================================================================

This section provides an example for establishing L2TP tunnels on an L3VPN. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374297__fig_dc_ne_l2tp_cfg_01441401), DeviceA and DeviceB function as PEs on the MPLS backbone network. At the same time, DeviceA functions as a LAC, and DeviceB functions as an LNS. L2TP tunnels are established between the two devices on the VPN. Loopback0 belongs to VRF1, and Loopback1 belongs to VRF2.

**Figure 1** Establishing L2TP tunnels on an L3VPN for user access![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/2/0.100 and GE0/3/0, respectively.


  
![](images/fig_dc_ne_l2tp_cfg_01441401.png "Click to enlarge")  

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GigabitEthernet0/3/0 | 172.16.1.1/24 |
| DeviceA | LoopBack0 | 10.1.1.3/24 |
| DeviceA | LoopBack1 | 10.2.1.3/24 |
| DeviceA | LoopBack2 | 1.1.1.9/32 |
| DeviceA | lsr-id | 1.1.1.9 |
| DeviceB | GigabitEthernet0/3/0 | 172.16.1.2/24 |
| DeviceB | LoopBack0 | 10.3.1.3/24 |
| DeviceB | LoopBack1 | 10.4.1.3/24 |
| DeviceB | LoopBack2 | 2.2.2.9/32 |
| DeviceB | lsr-id | 2.2.2.9 |




#### Configuration Roadmap

1. Set up an MPLS VPN on the backbone network.
2. Bind the interfaces of the L2TP tunnel to the VPN instance.
3. Configure a dial-up connection on the user side.
4. Configure the LAC.
5. Configure the LNS.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR ID of each PE (IP address of Loopback2)
* Usernames and passwords of PC1 and PC2
* Tunnel passwords and LNS-side local and remote names
* VPN instances
* Numbers of two VTs and two L2TP groups
* IDs, address ranges, and address masks of remote address pools

#### Procedure

1. Perform configuration on the user side.
   
   
   
   Create a dial-up connection, with the access number of DeviceA specified to receive addresses assigned by the LNS.
   
   For PC1, enter the username **user1@isp1** and password (which have been registered on the LNS) in the dial-up terminal window that is displayed.
   
   For PC2, enter the username (user1@isp2) and password, which have been registered at the LNS, in the displayed dial-up terminal window.
2. Configure DeviceA that functions as the LAC.
   
   
   
   # Configure VT1.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceA
   ```
   ```
   [*DeviceA] interface virtual-template 1
   ```
   ```
   [*DeviceA-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceA-Virtual-Template1] commit
   ```
   ```
   [~DeviceA-Virtual-Template1] quit
   ```
   
   # Bind VT1 to GE0/2/0.100.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0.100
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100] pppoe-server bind virtual-template 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] user-vlan 1 100
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100-vlan-1-100] quit
   ```
   
   # Configure a BAS interface.
   
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] bas
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] authentication-method ppp
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0.100-bas] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100-bas] quit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0.100] quit
   ```
   
   # Create VPN instances.
   
   ```
   [~DeviceA] ip vpn-instance vrf1
   ```
   ```
   [*DeviceA-vpn-instance-vrf1] route-distinguisher 100:1
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] apply-label per-instance
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] vpn-target 100:1 both
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] commit
   ```
   ```
   [~DeviceA-vpn-instance-vrf1-af-ipv4] quit
   ```
   ```
   [~DeviceA-vpn-instance-vrf1] quit
   ```
   ```
   [~DeviceA] ip vpn-instance vrf2
   ```
   ```
   [*DeviceA-vpn-instance-vrf2] route-distinguisher 100:2
   ```
   ```
   [*DeviceA-vpn-instance-vrf2-af-ipv4] apply-label per-instance
   ```
   ```
   [*DeviceA-vpn-instance-vrf2-af-ipv4] vpn-target 100:2 both
   ```
   ```
   [*DeviceA-vpn-instance-vrf2-af-ipv4] commit
   ```
   ```
   [~DeviceA-vpn-instance-vrf2-af-ipv4] quit
   ```
   ```
   [~DeviceA-vpn-instance] quit
   ```
   
   # Create loopback interfaces.
   
   ```
   [~DeviceA] interface loopback0
   ```
   ```
   [*DeviceA-LoopBack0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA-LoopBack0] ip address 10.1.1.3 255.255.255.0
   ```
   ```
   [*DeviceA-LoopBack0] commit
   ```
   ```
   [~DeviceA-LoopBack0] quit
   ```
   ```
   [~DeviceA] interface loopback1
   ```
   ```
   [*DeviceA-LoopBack1] ip binding vpn-instance vrf2
   ```
   ```
   [*DeviceA-LoopBack1] ip address 10.2.1.3 255.255.255.0
   ```
   ```
   [*DeviceA-LoopBack1] commit
   ```
   ```
   [~DeviceA-LoopBack1] quit
   ```
   
   # Configure an L2TP group and specify related attributes.
   
   ```
   [~DeviceA] l2tp enable
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] l2tp-group lac1
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel name lac1
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA-l2tp-lac1] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel source loopback0
   ```
   ```
   [*DeviceA-l2tp-lac1] commit
   ```
   ```
   [~DeviceA-l2tp-lac1] start l2tp ip 10.3.1.3
   ```
   ```
   [~DeviceA-l2tp-lac1] quit
   ```
   ```
   [~DeviceA] l2tp-group lac2
   ```
   ```
   [*DeviceA-l2tp-lac2] tunnel name lac2
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [*DeviceA-l2tp-lac2] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-lac2] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceA-l2tp-lac2] tunnel source loopback1
   ```
   ```
   [*DeviceA-l2tp-lac2] commit
   ```
   ```
   [~DeviceA-l2tp-lac2] start l2tp ip 10.4.1.3
   ```
   ```
   [~DeviceA-l2tp-lac2] quit
   ```
   
   # Configure a RADIUS server group on LAC1.
   
   ```
   [~DeviceA] radius-server group radius1
   ```
   ```
   [*DeviceA-radius-radius1] radius-server authentication 10.0.0.249 1812
   ```
   ```
   [*DeviceA-radius-radius1] radius-server accounting 10.0.0.249 1813
   ```
   ```
   [*DeviceA-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceA-radius-radius1] commit
   ```
   ```
   [~DeviceA-radius-radius1] quit
   ```
   
   # Configure a user access domain on LAC1.
   
   ```
   [~DeviceA] aaa
   ```
   ```
   [*DeviceA-aaa] domain isp1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] radius-server group radius1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] authentication-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] accounting-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] commit
   ```
   ```
   [*DeviceA-aaa-domain-isp1] idle-cut 60 500
   ```
   ```
   [~DeviceA-aaa-domain-isp1] l2tp-group lac1
   ```
   ```
   [~DeviceA-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceA-aaa] domain isp2
   ```
   ```
   [*DeviceA-aaa-domain-isp2] radius-server group radius1
   ```
   ```
   [*DeviceA-aaa-domain-isp2] authentication-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp2] accounting-scheme default1
   ```
   ```
   [*DeviceA-aaa-domain-isp2] commit
   ```
   ```
   [*DeviceA-aaa-domain-isp2] idle-cut 60 500
   ```
   ```
   [~DeviceA-aaa-domain-isp2] l2tp-group lac2
   ```
   ```
   [~DeviceA-aaa-domain-isp2] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
3. Configure DeviceB that functions as the LNS.
   
   
   
   # Create two VPN instances.
   
   ```
   [~DeviceB] ip vpn-instance vrf1
   ```
   ```
   [*DeviceB-vpn-instance-vrf1] route-distinguisher 100:1
   ```
   ```
   [*DeviceB-vpn-instance-vrf1] apply-label per-instance
   ```
   ```
   [*DeviceB-vpn-instance-vrf1] vpn-target 100:1 both
   ```
   ```
   [*DeviceB-vpn-instance-vrf1] commit
   ```
   ```
   [~DeviceB-vpn-instance-vrf1] quit
   ```
   ```
   [~DeviceB] ip vpn-instance vrf2
   ```
   ```
   [*DeviceB-vpn-instance-vrf2] route-distinguisher 100:2
   ```
   ```
   [*DeviceB-vpn-instance-vrf2] apply-label per-instance
   ```
   ```
   [*DeviceB-vpn-instance-vrf2] vpn-target 100:2 both
   ```
   ```
   [*DeviceB-vpn-instance-vrf2] commit
   ```
   ```
   [~DeviceB-vpn-instance-vrf2] quit
   ```
   
   # Create loopback interfaces.
   
   ```
   [~DeviceB] interface loopback0
   ```
   ```
   [*DeviceB-LoopBack0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceB-LoopBack0] ip address 10.3.1.3 255.255.255.0
   ```
   ```
   [*DeviceB-LoopBack0] commit
   ```
   ```
   [~DeviceB-LoopBack0] quit
   ```
   ```
   [~DeviceB] interface loopback1
   ```
   ```
   [*DeviceB-LoopBack1] ip binding vpn-instance vrf2
   ```
   ```
   [*DeviceB-LoopBack1] ip address 10.4.1.3 255.255.255.0
   ```
   ```
   [*DeviceB-LoopBack1] commit
   ```
   ```
   [~DeviceB-LoopBack1] quit
   ```
   
   # Create VT1.
   
   ```
   [~DeviceB] interface virtual-template 1
   ```
   ```
   [*DeviceB-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceB-Virtual-Template1] commit
   ```
   ```
   [~DeviceB-Virtual-Template1] quit
   ```
   
   # Enable the L2TP service and configure an L2TP group.
   
   ```
   [~DeviceB] l2tp enable
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] l2tp-group lns1
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel name lns1
   ```
   ```
   [*DeviceB-l2tp-lns1] allow l2tp virtual-template 1 remote lac1
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-l2tp-lns1] commit
   ```
   ```
   [~DeviceB-l2tp-lns1] quit
   ```
   ```
   [~DeviceB] l2tp-group lns2
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel name lns2
   ```
   ```
   [*DeviceB-l2tp-lns1] allow l2tp virtual-template 1 remote lac2
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel authentication
   ```
   ```
   [*DeviceB-l2tp-lns1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceB-l2tp-lns1] commit
   ```
   ```
   [~DeviceB-l2tp-lns1] quit
   ```
   
   # Create and configure the LNS group named **group1**, and bind the tunnel source interface and tunnel board to the LNS group.
   
   ```
   [~DeviceB] lns-group group1
   ```
   ```
   [*DeviceB-lns-group-group1] bind slot 1 
   ```
   ```
   [*DeviceB-lns-group-group1] bind source LoopBack0
   ```
   ```
   [*DeviceB-lns-group-group1] bind source LoopBack1
   ```
   ```
   [*DeviceB-lns-group-group1] commit
   ```
   ```
   [~DeviceB-lns-group-group1] quit
   ```
   
   # Configure address pools from which addresses are assigned to users.
   
   ```
   [~DeviceB] ip pool pool1 bas local
   ```
   ```
   [*DeviceB-ip-pool-pool1] gateway 192.168.0.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool1] section 0 192.168.0.10 192.168.0.100
   ```
   ```
   [*DeviceB-ip-pool-pool1] commit
   ```
   ```
   [~DeviceB-ip-pool-pool1] quit
   ```
   ```
   [~DeviceB] ip pool pool2 bas local
   ```
   ```
   [*DeviceB-ip-pool-pool2] gateway 172.30.0.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool2] section 0 172.30.0.10 172.30.0.100
   ```
   ```
   [*DeviceB-ip-pool-pool2] commit
   ```
   ```
   [~DeviceB-ip-pool-pool2] quit
   ```
   
   # Configure a RADIUS server group.
   
   ```
   [~DeviceB] radius-server group radius1
   ```
   ```
   [*DeviceB-radius-radius1] radius-server authentication 10.1.20.1 1812
   ```
   ```
   [*DeviceB-radius-radius1] radius-server accounting 10.1.20.1 1813
   ```
   ```
   [*DeviceB-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceB-radius-radius1] commit
   ```
   ```
   [~DeviceB-radius-radius1] quit
   ```
   
   # Configure user access domains.
   
   ```
   [~DeviceB] aaa
   ```
   ```
   [*DeviceB-aaa] domain isp1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] authentication-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] accounting-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] ip-pool pool1
   ```
   ```
   [*DeviceB-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceB-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceB-aaa] domain isp2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] radius-server group radius1
   ```
   ```
   [*DeviceB-aaa-domain-isp2] authentication-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp2] accounting-scheme default1
   ```
   ```
   [*DeviceB-aaa-domain-isp2] ip-pool pool2
   ```
   ```
   [*DeviceB-aaa-domain-isp2] commit
   ```
   ```
   [~DeviceB-aaa-domain-isp2] quit
   ```
   ```
   [~DeviceB-aaa] quit
   ```
4. Verify the configuration.
   
   
   
   # Check that the route between the L2TP tunnel interfaces of the LAC and LNS is reachable.
   
   ```
   [~DeviceA] ping -vpn-instance vrf1 10.3.1.3
   ```
   ```
   PING 10.3.1.3: 56  data bytes, press CTRL_C to break                           
       Reply from 10.3.1.3: bytes=56 Sequence=1 ttl=255 time=12 ms                  
       Reply from 10.3.1.3: bytes=56 Sequence=2 ttl=255 time=10 ms                  
       Reply from 10.3.1.3: bytes=56 Sequence=3 ttl=255 time=5 ms                   
       Reply from 10.3.1.3: bytes=56 Sequence=4 ttl=255 time=8 ms                   
                                                                                   
     --- 10.3.1.3 ping statistics ---                                               
       4 packet(s) transmitted                                                     
       4 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 5/8/12 ms                           
   ```
   ```
   [~DeviceA] ping -vpn-instance vrf2 10.4.1.3
   ```
   ```
   PING 10.4.1.3: 56  data bytes, press CTRL_C to break                           
       Reply from 10.4.1.3: bytes=56 Sequence=1 ttl=255 time=12 ms                  
       Reply from 10.4.1.3: bytes=56 Sequence=2 ttl=255 time=10 ms                  
       Reply from 10.4.1.3: bytes=56 Sequence=3 ttl=255 time=5 ms                   
       Reply from 10.4.1.3: bytes=56 Sequence=4 ttl=255 time=8 ms                   
                                                                                   
     --- 10.4.1.3 ping statistics ---                                               
       4 packet(s) transmitted                                                     
       4 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 5/8/12 ms                           
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceA
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 1.1.1.9
  ```
  ```
   mpls
  ```
  ```
    lsp-trigger all
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
  ```
  ```
   radius-server authentication 10.0.0.249 1812 
  ```
  ```
   radius-server accounting 10.0.0.249 1813 
  ```
  ```
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vrf1
  ```
  ```
  route-distinguisher 100:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vrf2
  ```
  ```
  route-distinguisher 100:2
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:2 export-extcommunity
  ```
  ```
   vpn-target 100:2 import-extcommunity
  ```
  ```
  #
  ```
  ```
  l2tp-group lac1
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lac1
  ```
  ```
   start l2tp ip 10.3.1.3
  ```
  ```
   tunnel source LoopBack0
  ```
  ```
  l2tp-group lac2
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lac2
  ```
  ```
   start l2tp ip 10.4.1.3
  ```
  ```
   tunnel source LoopBack1
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   #
  ```
  ```
   domain isp1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    radius-server group radius1
  ```
  ```
    idle-cut 60 500
  ```
  ```
    l2tp-group lac1
  ```
  ```
   #
  ```
  ```
   domain isp2
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    radius-server group radius1
  ```
  ```
    idle-cut 60 500
  ```
  ```
    l2tp-group lac2
  ```
  ```
  #
  ```
  ```
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0.100
  ```
  ```
   undo shutdown
  ```
  ```
   pppoe-server bind Virtual-Template 1
  ```
  ```
   user-vlan 1 100
  ```
  ```
   bas
  ```
  ```
    access-type layer2-subscriber
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
  ip address 172.16.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 10.1.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip binding vpn-instance vrf2
  ```
  ```
   ip address 10.2.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack2
  ```
  ```
   ip address 1.1.1.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 2.2.2.9 as-number 100
  ```
  ```
   peer 2.2.2.9 connect-interface LoopBack2
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 2.2.2.9 enable
  ```
  ```
  #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 2.2.2.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance vrf1
  ```
  ```
    import-route direct
  ```
  ```
    import-route unr
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance vrf2
  ```
  ```
    import-route direct
  ```
  ```
    import-route unr
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 172.16.1.0 0.0.0.255
  ```
  ```
    network 1.1.1.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceB
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 2.2.2.9
  ```
  ```
   mpls
  ```
  ```
    lsp-trigger all
  ```
  ```
  #
  ```
  ```
  mpls ldp
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
  ```
  ```
   radius-server authentication 10.1.20.1 1812 
  ```
  ```
   radius-server accounting 10.1.20.1 1813 
  ```
  ```
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vrf1
  ```
  ```
  route-distinguisher 100:1
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:1 export-extcommunity
  ```
  ```
   vpn-target 100:1 import-extcommunity
  ```
  ```
  #
  ```
  ```
  ip vpn-instance vrf2
  ```
  ```
  route-distinguisher 100:2
  ```
  ```
   apply-label per-instance
  ```
  ```
   vpn-target 100:2 export-extcommunity
  ```
  ```
   vpn-target 100:2 import-extcommunity
  ```
  ```
  #
  ```
  ```
  l2tp-group lns1
  ```
  ```
   allow l2tp virtual-template 1 remote lac1
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lns1
  ```
  ```
  #
  ```
  ```
  l2tp-group lns2
  ```
  ```
   allow l2tp virtual-template 1 remote lac2
  ```
  ```
   tunnel password cipher %@%##!!!!!!!!!"!!!!"!!!!(!!!!1];16qfZ81fv"uMoKKZ.1k"`AO!X2K2N.b~'NB^V!!!!!!!!!!1!!!!o/4J(q"J1F.!K9%M!6x8%@%#
  ```
  ```
   tunnel name lns2
  ```
  ```
  #
  ```
  ```
  lns-group group1
  ```
  ```
   bind slot 1 
  ```
  ```
   bind source LoopBack0
  ```
  ```
   bind source LoopBack1
  ```
  ```
  #
  ```
  ```
  ip pool pool1 bas local
  ```
  ```
   gateway 192.168.0.1 255.255.255.0
  ```
  ```
   section 0 192.168.0.2 192.168.0.100
  ```
  ```
  #
  ```
  ```
  ip pool pool2  bas local
  ```
  ```
   gateway 172.30.0.1 255.255.255.0
  ```
  ```
   section 0 172.30.0.10 172.30.0.100
  ```
  ```
  #
  ```
  ```
  aaa
  ```
  ```
   #
  ```
  ```
   domain  isp1
  ```
  ```
    radius-server group radius1
  ```
  ```
    authentication-scheme default1
  ```
  ```
    accounting-scheme default1
  ```
  ```
    ip-pool pool1
  ```
  ```
   #
  ```
  ```
   domain  isp2
  ```
  ```
    radius-server group  radius1
  ```
  ```
    authentication-scheme   default1
  ```
  ```
    accounting-scheme   default1
  ```
  ```
    ip-pool pool2
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 10.3.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip binding vpn-instance vrf2
  ```
  ```
   ip address 10.4.1.3 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack2
  ```
  ```
   ip address 2.2.2.9 255.255.255.255
  ```
  ```
  #
  ```
  ```
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.1.2 255.255.255.0
  ```
  ```
    mpls
  ```
  ```
   mpls ldp
  ```
  ```
  #
  ```
  ```
  bgp 100
  ```
  ```
   peer 1.1.1.9 as-number 100
  ```
  ```
   peer 1.1.1.9 connect-interface LoopBack2
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
  ```
  ```
    peer 1.1.1.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpnv4
  ```
  ```
    policy vpn-target
  ```
  ```
    peer 1.1.1.9 enable
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance vrf1
  ```
  ```
    import-route direct
  ```
  ```
    import-route unr
  ```
  ```
   #
  ```
  ```
   ipv4-family vpn-instance vrf2
  ```
  ```
    import-route direct
  ```
  ```
    import-route unr
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 172.17.1.0 0.0.0.255
  ```
  ```
    network 2.2.2.9 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```