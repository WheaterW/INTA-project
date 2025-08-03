Example for Configuring TWAMP on an L3 VXLAN
============================================

This section provides an example for configuring TWAMP functions on an L3 VXLAN.

#### Networking Requirements

On the L3 VXLAN shown in [Figure 1](#EN-US_TASK_0172373254__fig_dc_vrp_vxlan_cfg_106101), DeviceB functions as the Server (supports only passive measurement) in a TWAMP test. DeviceA functions as the Control-Client. It initiates statistics collection by specifying the IP address of DeviceB. DeviceA then sends collected statistics to the performance management system.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

DeviceA must be able to function as the Controller. Data is sent using data collection technology such as telemetry. For details about the configuration procedure, see the corresponding third-party product manual.


**Figure 1** Configuring TWAMP on an L3 VXLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GigabitEthernet0/1/0.


  
![](images/fig_dc_vrp_twamp_cfg_001002.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VXLAN tunnel between DeviceA and DeviceB.
2. Configure the Server on DeviceB.
3. Configure the Session-Reflector on DeviceB.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces connecting devices
* TCP port number

#### Procedure

1. Assign an IP address to each node interface, including the loopback interface.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373254__dc_vrp_dci_cfg_001601).
2. Configure an IGP (IS-IS in this example) on the backbone network. 
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373254__dc_vrp_dci_cfg_001601).
3. Configure a VXLAN tunnel between DeviceA and DeviceB.
   
   
   
   For details about the configuration roadmap, see [VXLAN Configuration](dc_vrp_vxlan_cfg_1082.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373254__dc_vrp_dci_cfg_001601).
   
   After a VXLAN tunnel is established, you can run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on DeviceA to view VXLAN tunnel information.
   
   ```
   [~DeviceA] display vxlan tunnel
   ```
   ```
   Number of vxlan tunnel : 1
   Tunnel ID   Source                Destination           State  Type     Uptime
   -----------------------------------------------------------------------------------
   4026531841  1.1.1.1               2.2.2.2               up     dynamic  00:12:56  
   ```
4. Set the forwarding mode of the VXLAN tunnel to hardware loopback.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] global-gre forward-mode loopback
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] global-gre forward-mode loopback
   ```
5. Configure the Server.
   
   
   ```
   [*DeviceB] nqa twamp
   ```
   ```
   [*DeviceB-twamp] server
   ```
   ```
   [*DeviceB-twamp-srv] tcp listen-mode any-ip
   ```
   ```
   [*DeviceB-twamp-srv] tcp port 65530 vpn-instance vpn1
   ```
   ```
   [*DeviceB-twamp-srv] quit
   ```
6. Configure the Session-Reflector.
   
   
   ```
   [*DeviceB-twamp] reflector
   ```
   ```
   [*DeviceB-twamp-ref] quit
   ```
   ```
   [*DeviceB-twamp] quit
   ```
   ```
   [*DeviceB] commit
   ```
7. Verify the configuration.
   
   
   
   # View global TWAMP information on DeviceB.
   
   ```
   [~DeviceB] display twamp global-info
   ```
   ```
   Start Time                       : 2019-08-05 16:47:55
   Control Session Numbers          : 10
   Control Session Rejected Numbers : 0
   Test Session Numbers             : 10
   Test Session Completed Numbers   : 10
   Test Session Aborted Numbers     : 0
   Test Tx Numbers                  : 100
   Test Rx Numbers                  : 100
   ```
   
   # View TWAMP control session information on DeviceB.
   
   ```
   [~DeviceB] display twamp control-session verbose
   ```
   ```
   State                : active
   Control Session ID   : 0
   Client IP            : 192.168.1.1
   Client Port          : 65530
   Server IP            : 192.168.2.2
   Server Port          : 65530
   VPN Instance         : -
   Mode                 : unauthenticated
   Inactivity Time(s)   : -
   Test Session Number  : 10 
   Created Time         : 2019-08-05 16:47:55
   Normal Stop          : 100
   Abort Stop           : 10
   ```
   
   # View TWAMP test session information on DeviceB.
   
   ```
   [~DeviceB] display twamp test-session verbose
   ```
   ```
   State                : active
   Sender IP            : 192.168.1.1
   Sender Port          : 65530
   Reflector IP         : 192.168.2.2
   Reflector Port       : 65530
   Session ID           : 192.168.2.1:1039033631:FCF9C6DA
   Control Session ID   : 1
   Mode                 : unauthenticated
   DSCP                 : 03
   Padding Length       : 128
   VPN Instance         : vpn1
   Create Time          : 2019-08-05 16:47:55
   Last Start Time      : 2019-08-05 16:47:55
   Last Stop Time       : never
   Sequence Number      : 2000
   Test Tx Numbers      : 100
   Test Rx Numbers      : 100
   Test Discard Numbers : 0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 10:1
   apply-label per-instance
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 10
   vxlan vni 10 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.1.1.1 255.255.255.0
   arp distribute-gateway enable
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   isis enable 1
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface Nve1
   source 1.1.1.1
   vni 10 head-end peer-list protocol bgp
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
    peer 2.2.2.2 advertise encap-type vxlan
  #
  global-gre forward-mode loopback
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  evpn vpn-instance evrf3 bd-mode
   route-distinguisher 20:1
   apply-label per-instance
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 22:22
    apply-label per-instance
    vpn-target 2:2 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
   vxlan vni 5010
  #
  bridge-domain 20
   vxlan vni 20 split-horizon-mode
   evpn binding vpn-instance evrf3
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface Vbdif20
   ip binding vpn-instance vpn1
   ip address 10.2.1.1 255.255.255.0
   arp distribute-gateway enable
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.2.2 255.255.255.0
   isis enable 1
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface Nve1
   source 2.2.2.2
   vni 20 head-end peer-list protocol bgp
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 1.1.1.1 advertise encap-type vxlan
  #
  nqa twamp       
   server
    tcp listen-mode any-ip
    tcp port 65530 vpn-instance vpn1
   reflector
  #
  global-gre forward-mode loopback
  #
  return
  ```