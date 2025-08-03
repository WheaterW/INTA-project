Example for Configuring TWAMP Light on an L3 VXLAN
==================================================

This section provides an example for configuring TWAMP Light functions on an L3 VXLAN.

#### Networking Requirements

On the L3 VXLAN shown in [Figure 1](#EN-US_TASK_0172373299__fig_dc_vrp_vxlan_cfg_106101), DeviceA functions as the Responder and DeviceB functions as the Controller.

* DeviceA: responds to the packets received over a test session.
* DeviceB: sends and receives packets over a test session, collects and calculates performance statistics, and reports the statistics to the performance management system.

**Figure 1** Configuring TWAMP Light on an L3 VXLAN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GigabitEthernet 0/1/0.


  
![](images/fig_dc_vrp_cfg_twamp-light_011102.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VXLAN tunnel between DeviceA and DeviceB.
2. Configure the TWAMP Light Responder on DeviceA.
3. Configure the TWAMP Light Controller on DeviceB.
4. Configure the Controller to send statistics to the performance management system through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the interfaces connecting devices
* IP addresses and UDP port numbers of the Responder and Controller and IP address and gRPC port number of the performance management system.

#### Procedure

1. Assign IP addresses to node interfaces, including loopback interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373299__dc_vrp_dci_cfg_001601).
2. Configure an IGP (IS-IS in this example) on the backbone network.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373299__dc_vrp_dci_cfg_001601).
3. Configure a VXLAN tunnel between DeviceA and DeviceB.
   
   
   
   For the configuration roadmap, see [VXLAN Configuration](dc_vrp_vxlan_cfg_1082.html). For configuration details, see [Configuration Files](#EN-US_TASK_0172373299__dc_vrp_dci_cfg_001601).
   
   After a VXLAN tunnel is established, you can run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) command on DeviceA to display VXLAN tunnel information. The following example uses the command output on DeviceA.
   
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
5. Configure the TWAMP Light Responder.
   
   
   ```
   [*DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] responder
   ```
   ```
   [*DeviceA-twamp-light-responder] test-session 1 local-ip 192.168.2.2 remote-ip 192.168.1.1 local-port 2010 remote-port 2001
   ```
   ```
   [*DeviceA-twamp-light-responder] commit
   ```
   ```
   [~DeviceA-twamp-light-responder] quit
   ```
   ```
   [~DeviceA-twamp-light] quit
   ```
6. Configure the TWAMP Light Controller.
   
   
   ```
   [*DeviceB] nqa twamp-light
   ```
   ```
   [*DeviceB-twamp-light] client
   ```
   ```
   [*DeviceB-twamp-light-client] test-session 1 sender-ip 192.168.1.1 reflector-ip 192.168.2.2 sender-port 2001 reflector-port 2010
   ```
   ```
   [*DeviceB-twamp-light-client] commit
   ```
   ```
   [~DeviceB-twamp-light-client] quit
   ```
   ```
   [~DeviceB-twamp-light] sender
   ```
   ```
   [*DeviceB-twamp-light-sender] commit
   ```
   ```
   [~DeviceB-twamp-light-sender] test start-continual test-session 1 period 10
   ```
   ```
   [*DeviceB-twamp-light-sender] commit
   ```
   ```
   [~DeviceB-twamp-light-sender] quit
   ```
   ```
   [~DeviceB-twamp-light] quit
   ```
7. Verify the configuration.
   
   
   
   # Check real-time TWAMP Light session statistics on DeviceB.
   
   ```
   [~DeviceB] display twamp-light test-session 1
   ```
   ```
   Session ID                       : 1
   State                            : active
   Type                             : continual
   Sender IP                        : 192.168.1.1
   Sender Port                      : 2001
   Reflector IP                     : 192.168.2.2
   Reflector Port                   : 2010
   Mode                             : unauthenticated
   DSCP                             : 0
   Padding Length                   : 128
   Padding Type                     : 00
   VPN Instance                     : -
   Link-Bundle Interface            : -
   Last Start Time                  : 2017-04-13 15:33:52
   Last Stop Time                   : never
   Regular Time(in minute)          : - 
   Period Time(in millisecond)      : 10
   Time Out(in second)              : 5
   Duration Time(in second)         : -
   Packet Count                     : - 
   ```
   
   # Check two-way delay statistics of a TWAMP Light session on DeviceB.
   
   ```
   [~DeviceB] display twamp-light statistic-type twoway-delay test-session 1
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
   
   # Check two-way packet loss statistics of a TWAMP Light session on DeviceB.
   
   ```
   [~DeviceB] display twamp-light statistic-type twoway-loss test-session 1
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
8. Configure DeviceB to send statistics to the performance management system through telemetry.
   
   
   ```
   [~DeviceB] telemetry
   ```
   ```
   [~DeviceB-telemetry] destination-group twamp
   ```
   ```
   [*DeviceB-telemetry-destination-group-twamp] ipv4-address 192.168.100.100 port 10001 protocol grpc no-tls
   ```
   ```
   [*DeviceB-telemetry-destination-group-twamp] quit
   ```
   ```
   [*DeviceB-telemetry] sensor-group twamp
   ```
   ```
   [*DeviceB-telemetry-sensor-group-twamp] sensor-path huawei-twamp-controller:twamp-controller/client/sessions/session/huawei-twamp-statistics:statistics
   ```
   ```
   [*DeviceB-telemetry-sensor-group-twamp] quit
   ```
   ```
   [*DeviceB-telemetry] subscription twamp
   ```
   ```
   [*DeviceB-telemetry-subscription-twamp] sensor-group twamp sample-interval 5000
   ```
   ```
   [*DeviceB-telemetry-subscription-twamp] destination-group twamp
   ```
   ```
   [*DeviceB-telemetry-subscription-twamp] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure devices to send data using a secure TLS encryption mode. For details, see *Telemetry Configuration*.

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
  nqa twamp-light
   responder
    test-session 1 local-ip 192.168.2.2 remote-ip 192.168.1.1 local-port 2010 remote-port 2001
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
  nqa twamp-light
   client
    test-session 1 sender-ip 192.168.1.1 reflector-ip 192.168.2.2 sender-port 2001 reflector-port 2010
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
  global-gre forward-mode loopback
  #
  return
  ```