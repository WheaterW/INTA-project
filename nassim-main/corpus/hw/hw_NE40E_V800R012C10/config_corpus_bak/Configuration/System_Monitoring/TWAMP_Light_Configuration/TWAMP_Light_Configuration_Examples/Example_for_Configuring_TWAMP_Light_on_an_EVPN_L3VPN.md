Example for Configuring TWAMP Light on an EVPN L3VPN
====================================================

This section provides an example for configuring TWAMP Light functions on an EVPN L3VPN.

#### Networking Requirements

On the EVPN L3VPN shown in [Figure 1](#EN-US_TASK_0172373302__fig_dc_vrp_vxlan_cfg_106101), DeviceB functions as the Responder and DeviceA functions as the Controller.

* DeviceA: sends and receives packets over a test session, collects and calculates performance statistics, and reports the statistics to the performance management system.
* DeviceB: responds to the packets received over a test session.

**Figure 1** Configuring TWAMP Light on an EVPN L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GigabitEthernet 0/1/0, and interface2 represents GigabitEthernet 0/2/0.


  
![](images/fig_dc_vrp_twamp_cfg_001004.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an EVPN L3VPN.
2. Configure the TWAMP Light Controller.
3. Configure the TWAMP Light Responder.
4. Configure the Controller to send statistics to the performance management system through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the interfaces connecting devices
* IP address and UDP port number of DeviceA (Controller)
  + IP Addresses: 192.168.2.2
  + UDP port number: 2000
* IP address and UDP port number of DeviceB (Responder)
  + IP address: 192.168.1.1
  + UDP port number: 3000
* IP address and gRPC port number of the performance management system
  + IP address: 192.168.100.100
  + gRPC port number: 10001

#### Procedure

1. Assign IP addresses to node interfaces, including loopback interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373302__dc_vrp_dci_cfg_001601).
2. Configure an IGP (IS-IS in this example) on the backbone network. 
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373302__dc_vrp_dci_cfg_001601).
3. Configure an IS-IS SR-MPLS BE tunnel between DeviceA and DeviceB.
   
   
   
   For the configuration roadmap, see [Configuring an IS-IS SR-MPLS BE Tunnel](dc_vrp_sr-be_cfg_0008.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373302__dc_vrp_dci_cfg_001601).
4. Configure an EVPN L3VPN between DeviceA and DeviceB.
   
   
   
   For details about the configuration roadmap, see [Configuring an EVPN to Carry Layer 3 Services](dc_vrp_evpn_cfg_0038.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373302__dc_vrp_dci_cfg_001601).
5. Create a TWAMP Light test session on DeviceB (Responder).
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa twamp-light
   ```
   ```
   [*DeviceB-twamp-light] responder
   ```
   ```
   [*DeviceB-twamp-light-responder] test-session 1 local-ip 192.168.1.1 remote-ip 192.168.2.2 local-port 3000 remote-port 2000 vpn-instance vpna
   ```
   ```
   [*DeviceB-twamp-light-responder] commit
   ```
   ```
   [~DeviceB-twamp-light-responder] quit
   ```
   ```
   [~DeviceB-twamp-light] quit
   ```
6. Create a TWAMP Light test session on DeviceA (Controller).
   
   
   ```
   <DeviceA> system-view
   ```
   
   
   ```
   [~DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] client
   ```
   ```
   [*DeviceA-twamp-light-client] test-session 1 sender-ip 192.168.2.2 reflector-ip 192.168.1.1 sender-port 2000 reflector-port 3000 vpn-instance vpna padding 1454
   ```
   ```
   [*DeviceA-twamp-light-client] commit
   ```
   ```
   [~DeviceA-twamp-light-client] quit
   ```
   ```
   [~DeviceA-twamp-light] sender
   ```
   ```
   [*DeviceA-twamp-light-sender] commit
   ```
   ```
   [~DeviceA-twamp-light-sender] test start-continual test-session 1 period 10
   ```
   ```
   [*DeviceA-twamp-light-sender] commit
   ```
   ```
   [~DeviceA-twamp-light-sender] quit
   ```
   ```
   [~DeviceA-twamp-light] quit
   ```
7. Verify the configuration.
   
   
   
   # Check the brief information about all test sessions.
   
   ```
   [~DeviceA] display twamp-light test-session
   ```
   ```
   Total number  : 1                                                               
   Active number : 1                                                               
   --------------------------------------------------------------------------------
     ID        Sender-IP   Sender-Port     Reflector-IP    Reflector-Port  State   
   --------------------------------------------------------------------------------
      1        192.168.2.2  2000            192.168.1.1    3000            active  
   
   ```
   
   # Check two-way delay statistics of a specified session.
   
   ```
   [~DeviceA] display twamp-light statistic-type twoway-delay test-session 1
   ```
   ```
   Latest two-way delay statistics(usec): 
   -------------------------------------------------------------------------------- 
        Index      Delay(Avg)     Jitter(Avg)     Tx-Jitter(Avg)    Rx-Jitter(Avg) 
   -------------------------------------------------------------------------------- 
        11027             345               5                 3                 4 
        11028             345               5                 3                 4 
        11029             345               5                 4                 4 
        11030             347               5                 3                 4 
        11031             347               4                 3                 4 
        11032             347               4                 3                 4 
        11033             347               4                 3                 4 
        11034             346               4                 3                 4 
        11035             346               5                 3                 4 
        11036             346               5                 3                 4 
        11037             346               5                 3                 4 
        11038             346               4                 4                 3 
        11039             347               4                 4                 3 
        11040             347               4                 4                 3 
        11041             347               4                 4                 3 
        11042             347               4                 4                 3 
        11043             347               5                 3                 4 
        11044             346               5                 3                 4
        11045             346               5                 3                 4
        11046             346               5                 3                 4
        11047             346               5                 3                 4 
        11048             346               5                 3                 4 
        11049             346               4                 3                 4 
        11050             346               4                 3                 4 
        11051             345               4                 3                 3 
        11052             345               4                 3                 3 
        11053             345               5                 4                 3 
        11054             345               5                 4                 3 
        11055             345               4                 4                 3  
        11056             345               4                 3                 3  
   -------------------------------------------------------------------------------- 
   Average Delay    :          346    Average Jitter   :          5 
   Maximum Delay    :          370    Maximum Jitter   :          32 
   Minimum Delay    :          328    Minimum Jitter   :          0 
   Average TxJitter :            3    Average RxJitter :          4 
   Maximum TxJitter :           29    Maximum RxJitter :          23 
   Minimum TxJitter :            0    Minimum RxJitter :          0 
   ```
   
   # Check two-way packet loss statistics of a specified test session.
   
   ```
   [~DeviceA] display twamp-light statistic-type twoway-loss test-session 1
   ```
   ```
   Latest two-way loss statistics:
   --------------------------------------------------------------------------------
        Index      Loss count      Loss ratio      Error count      Error ratio
   --------------------------------------------------------------------------------
       108196               0         0.0000%                0          0.0000%
       108197               0         0.0000%                0          0.0000%
       108198               0         0.0000%                0          0.0000%
       108199               0         0.0000%                0          0.0000%
       108200               0         0.0000%                0          0.0000%
       108201               0         0.0000%                0          0.0000%
       108202               0         0.0000%                0          0.0000%
       108203               0         0.0000%                0          0.0000%
       108204               0         0.0000%                0          0.0000%
       108205               0         0.0000%                0          0.0000%
       108206               0         0.0000%                0          0.0000%
       108207               0         0.0000%                0          0.0000%
       108208               0         0.0000%                0          0.0000%
       108209               0         0.0000%                0          0.0000%
       108210               0         0.0000%                0          0.0000%
       108211               0         0.0000%                0          0.0000%
       108212               0         0.0000%                0          0.0000%
       108213               0         0.0000%                0          0.0000%
       108214               0         0.0000%                0          0.0000%
       108215               0         0.0000%                0          0.0000%
       108216               0         0.0000%                0          0.0000%
       108217               0         0.0000%                0          0.0000%
       108218               0         0.0000%                0          0.0000%
       108219               0         0.0000%                0          0.0000%
       108220               0         0.0000%                0          0.0000%
       108221               0         0.0000%                0          0.0000%
       108222               0         0.0000%                0          0.0000%
       108223               0         0.0000%                0          0.0000%
       108224               0         0.0000%                0          0.0000%
       108225               0         0.0000%                0          0.0000%
   --------------------------------------------------------------------------------
   Average Loss Count   :          0    Average Loss Ratio   :   0.0000%
   Maximum Loss Count   :          0    Maximum Loss Ratio   :   0.0000%
   Minimum Loss Count   :          0    Minimum Loss Ratio   :   0.0000%
   Average RxError Count:          0    Average RxError Ratio:   0.0000%
   Maximum RxError Count:          0    Maximum RxError Ratio:   0.0000%
   Minimum RxError Count:          0    Minimum RxError Ratio:   0.0000%
   ```
8. Configure DeviceA to send statistics to the performance management system through telemetry.
   
   
   ```
   [~DeviceA] telemetry
   ```
   ```
   [~DeviceA-telemetry] destination-group twamp
   ```
   ```
   [*DeviceA-telemetry-destination-group-twamp] ipv4-address 192.168.100.100 port 10001 protocol grpc no-tls
   ```
   ```
   [*DeviceA-telemetry-destination-group-twamp] quit
   ```
   ```
   [*DeviceA-telemetry] sensor-group twamp
   ```
   ```
   [*DeviceA-telemetry-sensor-group-twamp] sensor-path huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
   ```
   ```
   [*DeviceA-telemetry-sensor-group-twamp] quit
   ```
   ```
   [*DeviceA-telemetry] subscription twamp
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] sensor-group twamp sample-interval 5000
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] destination-group twamp
   ```
   ```
   [*DeviceA-telemetry-subscription-twamp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

#### Configuration Files

* DeviceA configuration File
  
  ```
  #
  sysname DeviceA
  #               
  ip vpn-instance vpna
   ipv4-family    
    route-distinguisher 200:1
    tnl-policy SR-MPLS-BE evpn
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
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
  nqa twamp-light
   client
    test-session 1 sender-ip 192.168.2.2 reflector-ip 192.168.1.1 sender-port 2000 reflector-port 3000 vpn-instance vpna padding 1454
   sender
    test start-continual test-session 1 period 10
  #
  telemetry
   #
   sensor-group twamp
    sensor-path huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
   #
   destination-group twamp
    ipv4-address 192.168.100.100 port 10001 protocol grpc no-tls
   #
   subscription twamp
    sensor-group twamp sample-interval 5000
    destination-group twamp
  #
  tunnel-policy SR-MPLS-BE
   tunnel select-seq sr-lsp load-balance-number 1
  #
  return  
  ```
* DeviceB configuration File
  
  ```
  #
  sysname DeviceB
  #               
  ip vpn-instance vpna
   ipv4-family    
    route-distinguisher 100:1
    tnl-policy SR-MPLS-BE evpn
    vpn-target 111:1 export-extcommunity evpn
    vpn-target 111:1 import-extcommunity evpn
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
  nqa twamp-light
   responder
    test-session 1 local-ip 192.168.1.1 remote-ip 192.168.2.2 local-port 3000 remote-port 2000 vpn-instance vpna
  #
  tunnel-policy SR-MPLS-BE
   tunnel select-seq sr-lsp load-balance-number 1
  #
  return  
  ```