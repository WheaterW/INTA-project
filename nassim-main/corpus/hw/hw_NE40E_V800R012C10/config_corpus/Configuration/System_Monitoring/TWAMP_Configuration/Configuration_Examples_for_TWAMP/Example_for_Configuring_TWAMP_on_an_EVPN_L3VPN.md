Example for Configuring TWAMP on an EVPN L3VPN
==============================================

This section provides an example for configuring TWAMP on an EVPN L3VPN.

#### Networking Requirements

On the EVPN L3VPN shown in [Figure 1](#EN-US_TASK_0172373257__fig_dc_vrp_vxlan_cfg_106101), DeviceB functions as the Server (supports only passive measurement) in a TWAMP test. DeviceA functions as the Control-Client. It initiates statistics collection by specifying the IP address of DeviceB. DeviceA then sends collected statistics to the performance management system.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

DeviceA must be able to function as the Controller. Data is sent using data collection technology such as telemetry. For details about the configuration procedure, see the corresponding third-party product manual.


**Figure 1** Example for configuring TWAMP on an EVPN L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GigabitEthernet 0/1/0, and interface2 represents GigabitEthernet 0/2/0.


  
![](images/fig_dc_vrp_twamp_cfg_001003.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an EVPN L3VPN.
2. Configure the Server.
3. Configure the Session-Reflector.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces connecting devices
* TCP port number

#### Procedure

1. Assign an IP address to each node interface, including the loopback interface.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373257__dc_vrp_dci_cfg_001601).
2. Configure an IGP (IS-IS in this example) on the backbone network. 
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373257__dc_vrp_dci_cfg_001601).
3. Configure an IS-IS SR-MPLS BE tunnel between DeviceA and DeviceB.
   
   
   
   For details about the configuration roadmap, see [Configuring an IS-IS SR-MPLS BE Tunnel](dc_vrp_sr-be_cfg_0008.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373257__dc_vrp_dci_cfg_001601).
4. Configure an EVPN L3VPN between DeviceA and DeviceB.
   
   
   
   For configuration details, see [Configuring an EVPN to Carry Layer 3 Services](dc_vrp_evpn_cfg_0038.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373257__dc_vrp_dci_cfg_001601).
5. Configure the Server.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa twamp
   ```
   ```
   [~DeviceB-twamp] server
   ```
   ```
   [*DeviceB-twamp-srv] tcp listen-mode any-ip
   ```
   ```
   [*DeviceB-twamp-srv] tcp port 65530 vpn-instance vpna
   ```
   ```
   [*DeviceB-twamp-srv] quit
   ```
   ```
   [*DeviceB-twamp] quit
   ```
   ```
   [*DeviceB] commit
   ```
6. Configure the Session-Reflector.
   
   
   ```
   [~DeviceB] nqa twamp
   ```
   ```
   [~DeviceB-twamp] reflector
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
   
   
   
   # View TWAMP test session information on DeviceB.
   
   ```
   [~DeviceB] display twamp test-session verbose
   ```
   ```
   State                : active
   Sender IP            : 192.168.2.2
   Sender Port          : 65530
   Reflector IP         : 192.168.1.1
   Reflector Port       : 65530
   Session ID           : 192.168.2.2:1039033631:FCF9C6DA
   Control Session ID   : 1
   Mode                 : unauthenticated
   DSCP                 : 03
   Padding Length       : 128
   VPN Instance         : vpna
   Create Time          : 2012-08-05 16:47:55
   Last Start Time      : 2012-08-05 16:47:55
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
  ip vpn-instance vpna
   ipv4-family    
    route-distinguisher 200:1
    apply-label per-instance
    tnl-policy SR-MPLS-BE
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  mpls lsr-id 1.1.1.3
  #
  mpls
  #
  segment-routing
   tunnel-prefer segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0012.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 200000 201000
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna   
   ip address 192.168.2.2 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown   
   ip address 172.16.1.1 255.255.255.0
   isis enable 1
   mpls
  #
  interface LoopBack0
   ip address 1.1.1.3 255.255.255.255
   isis enable 1
   isis prefix-sid index 20
  #
  bgp 100
   peer 1.1.1.2 as-number 100
   peer 1.1.1.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 1.1.1.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.2 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 1.1.1.2 as-number 100
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.2 enable
  #
  tunnel-policy SR-MPLS-BE
   tunnel select-seq lsp load-balance-number 1
  #
  return 
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #               
  ip vpn-instance vpna
   ipv4-family    
    route-distinguisher 100:1
    apply-label per-instance
    tnl-policy SR-MPLS-BE
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #               
  mpls lsr-id 1.1.1.2
  #
  mpls
  #
  segment-routing
   tunnel-prefer segment-routing
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 00.0005.0000.0000.0010.00
   traffic-eng level-2
   segment-routing mpls
   segment-routing global-block 200000 201000
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna   
   ip address 192.168.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown   
   ip address 172.17.1.1 255.255.255.0
   isis enable 1
   mpls
  #
  interface LoopBack0
   ip address 1.1.1.2 255.255.255.255
   isis enable 1
   isis prefix-sid index 10
  #
  bgp 100
   peer 1.1.1.3 as-number 100
   peer 1.1.1.3 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 1.1.1.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.3 enable
   #
   ipv4-family vpn-instance vpna
    import-route direct
    peer 1.1.1.3 as-number 100
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.3 enable
  #
  nqa twamp       
   server
    tcp listen-mode any-ip
    tcp port 65530 vpn-instance vpna
   reflector
  #
  tunnel-policy SR-MPLS-BE
   tunnel select-seq lsp load-balance-number 1
  #
  return 
  ```