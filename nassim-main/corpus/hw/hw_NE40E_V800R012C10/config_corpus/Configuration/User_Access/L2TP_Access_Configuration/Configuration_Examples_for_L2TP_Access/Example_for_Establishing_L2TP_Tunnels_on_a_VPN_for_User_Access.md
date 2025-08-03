Example for Establishing L2TP Tunnels on a VPN for User Access
==============================================================

This section provides an example for establishing L2TP tunnels on a VPN. A networking diagram is provided to help you understand the configuration procedure. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374294__fig_dc_ne_l2tp_cfg_01351401), a carrier wants to use private network addresses, instead of public network addresses, to establish an L2TP tunnel due to considerations of limited public network addresses.

**Figure 1** Establishing L2TP tunnels on a VPN for user access![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE 0/1/1, GE0/2/0.100, and GE0/1/2, respectively.


  
![](images/fig_dc_ne_l2tp_cfg_01351401.png)  

| Device | Tunnel Interface | IP Address | Loopback Interface | IP Address |
| --- | --- | --- | --- | --- |
| DeviceA | GE0/1/1 | 10.0.0.1/24 | loopback0 | 1.1.1.1 |
| DeviceB | GE0/1/1 | 10.0.0.2/24 | loopback0 | 3.3.3.3 |
| DeviceB | GE0/1/2 | 10.10.0.2/24 | loopback1 | 4.4.4.4 |
| DeviceC | GE0/1/1 | 10.10.0.1/24 | loopback1 | 2.2.2.2 |




#### Configuration Roadmap

1. Configure a dial-up connection on the user side.
2. Configure the LAC.
3. Configure the LNS.

#### Data Preparation

To complete the configuration, you need the following data:

* Usernames and passwords of PC1 and PC2
* Tunnel passwords and LNS-side local and remote names
* VPN instance names
* Numbers of two VTs and two L2TP groups
* IDs, address ranges, and address masks of remote address pools

#### Procedure

1. Perform configuration on the user side.
   
   
   
   Create a dial-up connection, with the access number of DeviceA specified to receive addresses assigned by the LNS.
   
   For PC1, enter the username **user1@isp1** and password (which have been registered on the LNS) in the dial-up terminal window that is displayed.
   
   For PC2, enter the username **user1@isp2** and password (which have been registered on the LNS) in the dial-up terminal window that is displayed.
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
   
   # Create a VPN instance.
   
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
   [*DeviceAâvpn-instance-vrf1-af-ipv4] commit
   ```
   ```
   [~DeviceAâvpn-instance-vrf1-af-ipv4] quit
   ```
   ```
   [~DeviceAâvpn-instance] quit
   ```
   
   # Bind the interface connecting the LAC to the LNS to the VPN instance.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA--GigabitEthernet0/1/1] ip address 10.0.0.1 255.255.255.0
   ```
   ```
   [*DeviceA--GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA--GigabitEthernet0/1/1] quit
   ```
   
   # Create a loopback interface.
   
   ```
   [~DeviceA] interface loopback0
   ```
   ```
   [*DeviceA-LoopBack0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-LoopBack0] commit
   ```
   ```
   [~DeviceA-LoopBack0] quit
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
   [*DeviceA-l2tp-lac1] tunnel authentication
   ```
   ```
   [*DeviceA-l2tp-lac1] tunnel source loopback0
   ```
   ```
   [*DeviceA-l2tp-lac1] commit
   ```
   ```
   [~DeviceA-l2tp-lac1] start l2tp ip 3.3.3.3
   ```
   ```
   [~DeviceA-l2tp-lac1] tunnel password cipher YsHsjx_202206
   ```
   ```
   [~DeviceA-l2tp-lac1] quit
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
   [~DeviceA-aaa] domain isp1
   ```
   ```
   [*DeviceA-aaa-domain-isp1] l2tp-group lac1
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
   [*DeviceA-aaa-domain-isp1] idle-cut 60 500
   ```
   ```
   [* DeviceA-aaa-domain-isp1] commit
   ```
   ```
   [~DeviceA-aaa-domain-isp1] quit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
   
   # Configure a route.
   
   ```
   [~DeviceA] ip route-static vpn-instance vrf1 3.3.3.3 255.255.255.255 10.0.0.2
   ```
3. Configure DeviceC that functions as the LAC.
   
   
   
   # Configure VT1.
   
   ```
   <Device> system-view
   ```
   ```
   [~Device] sysname DeviceC
   ```
   ```
   [*DeviceC] interface virtual-template 1
   ```
   ```
   [*DeviceC-Virtual-Template1] ppp authentication-mode chap
   ```
   ```
   [*DeviceC-Virtual-Template1] commit
   ```
   ```
   [~DeviceC-Virtual-Template1] quit
   ```
   
   # Bind VT1 to GE0/2/0.100.
   
   ```
   [~DeviceC] interface gigabitethernet 0/2/0.100
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0.100] pppoe-server bind virtual-template 1
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
   [~DeviceC-GigabitEthernet0/2/0.100] bas
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0.100-bas] access-type layer2-subscriber
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0.100-bas] authentication-method ppp
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0.100-bas] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0.100-bas] quit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0.100] quit
   ```
   
   # Create a VPN instance.
   
   ```
   [~DeviceC] ip vpn-instance vrf2
   ```
   ```
   [*DeviceC-vpn-instance-vrf2] route-distinguisher 100:2
   ```
   ```
   [*DeviceC-vpn-instance-vrf2-af-ipv4] apply-label per-instance
   ```
   ```
   [*DeviceC-vpn-instance-vrf2-af-ipv4] vpn-target 100:2 both
   ```
   ```
   [*DeviceCâvpn-instance-vrf2-af-ipv4] commit
   ```
   ```
   [~DeviceCâvpn-instance-vrf2-af-ipv4] quit
   ```
   ```
   [~DeviceCâvpn-instance-vrf2] quit
   ```
   
   # Bind the LAC interface connected to the LNS to the VPN instance.
   
   ```
   [~DeviceC] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] ip binding vpn-instance vrf2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] ip address 10.10.0.1 255.255.255.0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/1] quit
   ```
   
   # Create a loopback interface.
   
   ```
   [~DeviceC] interface loopback1
   ```
   ```
   [*DeviceC-LoopBack1] ip binding vpn-instance vrf2
   ```
   ```
   [*DeviceC-LoopBack1] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack1] commit
   ```
   ```
   [~DeviceC-LoopBack1] quit
   ```
   
   # Configure an L2TP group and specify related attributes.
   
   ```
   [~DeviceC] l2tp enable
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] l2tp-group lac2
   ```
   ```
   [*DeviceC-l2tp-lac2] tunnel name lac2
   ```
   ```
   [*DeviceC-l2tp-lac2] start l2tp ip 4.4.4.4
   ```
   ```
   [*DeviceC-l2tp-lac2] tunnel authentication
   ```
   ```
   [*DeviceC-l2tp-lac2] tunnel password cipher YsHsjx_202206
   ```
   ```
   [*DeviceC-l2tp-lac2] tunnel source loopback1
   ```
   ```
   [*DeviceC-l2tp-lac2] commit
   ```
   ```
   [~DeviceC-l2tp-lac2] quit
   ```
   
   # Configure a RADIUS server group on LAC2.
   
   ```
   [~DeviceC] radius-server group radius1
   ```
   ```
   [*DeviceC-radius-radius1] radius-server authentication 10.10.0.249 1812
   ```
   ```
   [*DeviceC-radius-radius1] radius-server accounting 10.10.0.249 1813
   ```
   ```
   [*DeviceC-radius-radius1] radius-server shared-key itellin
   ```
   ```
   [*DeviceC-radius-radius1] commit
   ```
   ```
   [~DeviceC-radius-radius1] quit
   ```
   
   # Configure a user access domain on LAC2.
   
   ```
   [~DeviceC] aaa
   ```
   ```
   [~DeviceC-aaa] domain isp2
   ```
   ```
   [*DeviceC-aaa-domain-isp2] l2tp-group lac2
   ```
   ```
   [*DeviceC-aaa-domain-isp2] radius-server group radius1
   ```
   ```
   [*DeviceC-aaa-domain-isp2] authentication-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-isp2] accounting-scheme default1
   ```
   ```
   [*DeviceC-aaa-domain-isp2] idle-cut 60 500
   ```
   ```
   [*DeviceC-aaa-domain-isp2] commit
   ```
   ```
   [~DeviceC-aaa-domain-isp2] quit
   ```
   ```
   [~DeviceC-aaa] quit
   ```
   
   # Configure a route.
   
   ```
   [~DeviceC] ip route-static vpn-instance vrf2 4.4.4.4 255.255.255.255 10.10.0.2
   ```
4. Configure DeviceB that functions as the LNS.
   
   
   
   # Create two VPN instances.
   
   ```
   [~DeviceB] ip vpn-instance vrf1
   ```
   ```
   [*DeviceB-vpn-instance-vrf1] route-distinguisher 100:1
   ```
   ```
   [*DeviceB-vpn-instance-vrf1-af-ipv4] apply-label per-instance
   ```
   ```
   [*DeviceB-vpn-instance-vrf1-af-ipv4] vpn-target 100:1 both
   ```
   ```
   [*DeviceBâvpn-instance-vrf1-af-ipv4] commit
   ```
   ```
   [~DeviceBâvpn-instance-vrf1-af-ipv4] quit
   ```
   ```
   [~DeviceBâvpn-instance] quit
   ```
   ```
   [~DeviceB] ip vpn-instance vrf2
   ```
   ```
   [*DeviceB-vpn-instance-vrf2] route-distinguisher 100:2
   ```
   ```
   [*DeviceB-vpn-instance-vrf2-af-ipv4] apply-label per-instance
   ```
   ```
   [*DeviceB-vpn-instance-vrf2-af-ipv4] vpn-target 100:2 both
   ```
   ```
   [*DeviceBâvpn-instance-vrf2-af-ipv4] commit
   ```
   ```
   [~DeviceBâvpn-instance-vrf2-af-ipv4] quit
   ```
   ```
   [~DeviceBâvpn-instance] quit
   ```
   
   # Create two interfaces.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceB--GigabitEthernet0/1/1] ip address 10.0.0.2 255.255.255.0
   ```
   ```
   [*DeviceB--GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB--GigabitEthernet0/1/1] quit
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ip binding vpn-instance vrf2
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] ip address 10.10.0.2 255.255.255.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/2] quit
   ```
   
   # Create loopback interfaces.
   
   ```
   [~DeviceB] interface loopback0
   ```
   ```
   [*DeviceB-LoopBack0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceB-LoopBack0] ip address 3.3.3.3 255.255.255.255
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
   [*DeviceB-LoopBack1] ip address 4.4.4.4 255.255.255.255
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
   [*DeviceB-ip-pool-pool1] gateway 10.1.10.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool1] commit
   ```
   ```
   [~DeviceB-ip-pool-pool1] section 0 10.1.10.10 10.1.10.100
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
   [*DeviceB-ip-pool-pool2] gateway 10.1.155.1 255.255.255.0
   ```
   ```
   [*DeviceB-ip-pool-pool2] commit
   ```
   ```
   [~DeviceB-ip-pool-pool2] section 0 10.1.155.10 10.1.155.100
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
   [*DeviceB-radius-radius1] radius-server authentication 10.0.0.249 1812
   ```
   ```
   [*DeviceB-radius-radius1] radius-server accounting 10.0.0.249 1813
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
   [~DeviceB-aaa] domain isp1
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
   
   # Configure routes.
   
   ```
   [~DeviceB] ip route-static vpn-instance vrf1 1.1.1.1 255.255.255.255 10.0.0.1
   ```
   ```
   [~DeviceB] ip route-static vpn-instance vrf2 2.2.2.2 255.255.255.255 10.10.0.1
   ```
5. Verify the configuration.
   
   
   ```
   [~DeviceA] ping -vpn-instance vrf1 3.3.3.3
   ```
   ```
   PING 3.3.3.3: 56  data bytes, press CTRL_C to break                           
       Reply from 3.3.3.3: bytes=56 Sequence=1 ttl=255 time=12 ms                  
       Reply from 3.3.3.3: bytes=56 Sequence=2 ttl=255 time=10 ms                  
       Reply from 3.3.3.3: bytes=56 Sequence=3 ttl=255 time=5 ms                   
       Reply from 3.3.3.3: bytes=56 Sequence=4 ttl=255 time=8 ms                   
                                                                                   
     --- 3.3.3.3 ping statistics ---                                               
       4 packet(s) transmitted                                                     
       4 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 5/8/12 ms                           
   ```
   ```
   [~DeviceC] ping -vpn-instance vrf2 4.4.4.4
   ```
   ```
   PING 4.4.4.4: 56  data bytes, press CTRL_C to break                           
       Reply from 4.4.4.4: bytes=56 Sequence=1 ttl=255 time=12 ms                  
       Reply from 4.4.4.4: bytes=56 Sequence=2 ttl=255 time=10 ms                  
       Reply from 4.4.4.4: bytes=56 Sequence=3 ttl=255 time=5 ms                   
       Reply from 4.4.4.4: bytes=56 Sequence=4 ttl=255 time=8 ms                   
                                                                                   
     --- 4.4.4.4 ping statistics ---                                               
       4 packet(s) transmitted                                                     
       4 packet(s) received                                                        
       0.00% packet loss                                                           
       round-trip min/avg/max = 5/8/12 ms                           
   ```
   ```
   [~DeviceA] test l2tp-tunnel l2tp-group lac1 ip-address 3.3.3.3
   ```
   ```
   Testing L2TP tunnel connectivity now....... 
   ```
   ```
   Test L2TP tunnel connectivity success.
   ```
   ```
   [~DeviceC] test l2tp-tunnel l2tp-group lac2 ip-address 4.4.4.4
   ```
   ```
   Testing L2TP tunnel connectivity now....... 
   ```
   ```
   Test L2TP tunnel connectivity success.
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
   l2tp enable
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
  interface LoopBack0
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
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
   start l2tp ip 3.3.3.3
  ```
  ```
   tunnel source LoopBack0
  ```
  ```
  #
  ```
  ```
  aaa
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 10.0.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static vpn-instance vrf1 3.3.3.3 255.255.255.255 10.0.0.2
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
   sysname DeviceC
  ```
  ```
  #
  ```
  ```
   l2tp enable
  ```
  ```
  #
  ```
  ```
  radius-server group radius1
  ```
  ```
   radius-server authentication 10.10.0.249 1812 
  ```
  ```
   radius-server accounting 10.10.0.249 1813 
  ```
  ```
   radius-server shared-key %^%#vS%796FO7%C~pB%CR=q;j}gSCqR-X6+P!.DYI@)%^% 
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
  interface LoopBack1
  ```
  ```
   ip binding vpn-instance vrf2
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
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
   start l2tp ip 4.4.4.4
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
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance vrf2
  ```
  ```
   ip address 10.10.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static vpn-instance vrf2 4.4.4.4 255.255.255.255 10.10.0.2
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
   l2tp enable
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
  interface Virtual-Template1
  ```
  ```
  ppp authentication-mode chap
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
  interface LoopBack0
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
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
   ip address 4.4.4.4 255.255.255.255
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
   gateway 10.1.10.1 255.255.255.0
  ```
  ```
   section 0 10.1.10.10 10.1.10.100
  ```
  ```
  #
  ```
  ```
  ip pool pool2 bas local
  ```
  ```
   gateway 10.1.155.1 255.255.255.0
  ```
  ```
   section 0 10.1.155.10 10.1.155.100
  ```
  ```
  #
  ```
  ```
  aaa
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
  domain  isp2
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
    ip-pool pool2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance vrf1
  ```
  ```
   ip address 10.0.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip binding vpn-instance vrf2
  ```
  ```
   ip address 10.10.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static vpn-instance vrf1 1.1.1.1 255.255.255.255 10.0.0.1
  ```
  ```
   ip route-static vpn-instance vrf2 2.2.2.2 255.255.255.255 10.10.0.1
  ```
  ```
  #
  ```
  ```
  return
  ```