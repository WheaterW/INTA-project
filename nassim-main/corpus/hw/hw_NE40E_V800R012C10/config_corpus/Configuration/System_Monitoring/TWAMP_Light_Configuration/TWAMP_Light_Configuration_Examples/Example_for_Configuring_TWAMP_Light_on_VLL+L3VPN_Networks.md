Example for Configuring TWAMP Light on VLL+L3VPN Networks
=========================================================

This section provides an example for configuring TWAMP Light functions on VLL+L3VPN networks.

#### Networking Requirements

On the VLL+L3VPN networks shown in [Figure 1](#EN-US_TASK_0172373308__fig_dc_vrp_feature_new_twamp-light_010802), DeviceA functions as the Responder and is deployed on the last hop of the link connecting to a base station. DeviceB functions as the Controller and is deployed on the aggregation node.

* DeviceA: responds to the packets received over a test session.
* DeviceB: sends and receives packets over a test session and collects and calculates performance statistics on the Layer 3 network, and reports the statistics to the performance management system.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and Interface 2 in this example represent GigabitEthernet 0/1/1 and GigabitEthernet 0/1/0, respectively.


**Figure 1** Configuring TWAMP Light on VLL+L3VPN networks  
![](figure/en-us_image_0180214735.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VLL and L3VPN networks.
2. Configure the TWAMP Light Responder.
3. Configure devices at the edge of Layer 2 and Layer 3 networks.
4. Configure the TWAMP Light Controller.
5. Configure the Controller to send statistics to the performance management system through telemetry.


#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the interfaces connecting devices
* IP addresses and UDP port numbers of the Responder and Controller and IP address and gRPC port number of the performance management system.

#### Procedure

1. Assign IP addresses to node interfaces, including loopback interfaces.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373308__dc_vrp_dci_cfg_001602).
2. Configure an IGP on the backbone network. OSPF is used in this example.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373308__dc_vrp_dci_cfg_001602).
3. Configure an MPLS tunnel between DeviceA and DeviceC, and between DeviceC and DeviceB.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172373308__dc_vrp_dci_cfg_001602).
   
   After an MPLS tunnel is established, you can run the [**display mpls ldp**](cmdqueryname=display+mpls+ldp) command on DeviceA to display LDP information. Take the display on DeviceA as an example:
   
   ```
   [~DeviceA] display mpls ldp
   ```
   ```
    LDP Global Information
    ------------------------------------------------------------------------------
    Protocol Version        : V1            Neighbor Liveness     : 600 Sec
    Graceful Restart        : Off           FT Reconnect Timer    : 300 Sec
    MTU Signaling           : On            Recovery Timer        : 300 Sec
    Capability-Announcement : On            Longest-match         : Off
    mLDP P2MP Capability    : Off           mLDP MBB Capability   : Off
    mLDP MP2MP Capability   : Off           mLDP Recursive-fec    : Off
   
                             LDP Instance Information
    ------------------------------------------------------------------------------
    Instance ID             : 0             VPN-Instance          : 
    Instance Status         : Active        LSR ID                : 1.1.1.1
    Hop Count Limit         : 32            Path Vector Limit     : 32
    Loop Detection          : Off
    DU Re-advertise Timer   : 10 Sec        DU Re-advertise Flag  : Off
    DU Explicit Request     : Off           Request Retry Flag    : Off
    Label Distribution Mode : Ordered       
    Label Retention Mode    : Liberal(DU)/Conservative(DOD)
    Graceful-Delete         : Off           Graceful-Delete Timer : 5 Sec
    Igp-sync-delay Timer    : 10 Sec
    ------------------------------------------------------------------------------
   ```
4. Configure the TWAMP Light Responder.
   
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] responder
   ```
   ```
   [*DeviceA-twamp-light-responder] test-session 1 local-ip 192.168.1.1 remote-ip 192.168.2.2 local-port 6000 remote-port 6000 interface GigabitEthernet0/1/0.1
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
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When DeviceA functions as the reflector, the local IP address in the command for creating a session is the IP address of the base station, and the remote IP address is the IP address of DeviceB.
5. Configure the TWAMP Light Controller.
   
   
   ```
   <DeviceB> system-view
   ```
   ```
   [~DeviceB] nqa twamp-light
   ```
   ```
   [*DeviceB-twamp-light] client
   ```
   ```
   [*DeviceB-twamp-light-client] test-session 1 sender-ip 192.168.2.2 reflector-ip 192.168.1.1 sender-port 6000 reflector-port 6000 vpn-instance vpna
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
6. When the base station is offline, you need to configure static ARP on DeviceC to specify the mapping between the IP address and the MAC address of the base station.
   
   
   ```
   <DeviceC> system-view
   ```
   ```
   [~DeviceC] arp static 192.168.1.1 00e0-fc12-3456 vid 26 interface Virtual-Ethernet0/1/1.31
   ```
   ```
   [*DeviceC] commit
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
   Sender IP                        : 192.168.2.2
   Sender Port                      : 6000
   Reflector IP                     : 192.168.1.1
   Reflector Port                   : 6000
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
  mpls
  #
  mpls lsr-id 10.0.0.1
  #
  mpls
  #
  mpls ldp
   outbound peer all split-horizon
   accept target-hello all
   #
   ipv4-family
  #
  mpls ldp remote-peer 10.0.0.2
   mpls ldp timer hello-hold 45
   mpls ldp timer keepalive-hold 45
   remote-ip 10.0.0.2
  #
  ospf 1 router-id 10.0.0.1
   area 0.0.0.1
    network 3.0.0.0 0.0.0.3
    network 10.0.0.1 0.0.0.0
  #
  interface loopback0
   ip address 10.0.0.1 255.255.255.255
  #
  interface GigabitEthernet0/1/1.31
   vlan-type dot1q 31
   mtu 9500
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mtu 9500
   mpls l2vc 10.0.0.2 26 control-word raw
  #
  nqa twamp-light
   responder
    test-session 1 local-ip 192.168.1.1 remote-ip 192.168.2.2 local-port 6000 remote-port 6000 interface GigabitEthernet0/1/0.1
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  mpls
  #
  mpls lsr-id 10.0.0.3
  #
  mpls
  #
  mpls ldp
  #
   ipv4-family
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0003.00
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 4134:3060
    apply-label per-instance
    arp vlink-direct-route advertise
    vpn-target 4134:306000 export-extcommunity
    vpn-target 4134:306000 import-extcommunity
  #
  interface loopback0
   ip address 10.0.0.3 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/0.31
   vlan-type dot1q 31
   mtu 9500
   ip address 3.0.0.6 255.255.255.252
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1.31
   vlan-type dot1q 1
   ip binding vpn-instance vpna
   ip address 192.168.2.2 255.255.255.0
  #
  nqa twamp-light
   client
    test-session 1 sender-ip 192.168.2.2 reflector-ip 192.168.1.1 sender-port 6000 reflector-port 6000 vpn-instance vpna
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
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  mpls
  #
  mpls lsr-id 10.0.0.2
  #
  mpls
  #
  mpls ldp remote-peer 10.0.0.1
   mpls ldp timer hello-hold 45
   mpls ldp timer keepalive-hold 45
   remote-ip 10.0.0.1
  #
  ospf 1
   stub-router on-startup
   area 0.0.0.1
    network 3.0.0.0 0.0.0.3
    network 10.0.0.2 0.0.0.0
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0002.00
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 4134:3060
    apply-label per-instance
    arp vlink-direct-route advertise
    vpn-target 4134:306000 export-extcommunity
    vpn-target 4134:306000 import-extcommunity
  #
  interface loopback0
   ip address 10.0.0.2 255.255.255.255
   isis enable 1
  #
  interface GigabitEthernet0/1/1.31
   vlan-type dot1q 31
   mtu 9500
   ip address 3.0.0.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/0.31
   vlan-type dot1q 31
   mtu 9500
   ip address 3.0.0.5 255.255.255.252
   isis enable 1
   mpls
   mpls ldp
  #
  interface Virtual-Ethernet0/1/0
   ve-group 1 l3-access
  # 
  interface Virtual-Ethernet0/1/0.2
   mtu 9500
   ip binding vpn-instance vpna
   ip address 192.168.1.3 255.255.0.0
   encapsulation dot1q-termination
   dot1q termination vid 26 to 50
   arp broadcast enable
   arp-proxy enable
   arp-proxy inter-sub-vlan-proxy enable
   arp-proxy inner-sub-vlan-proxy enable
   ipv6 nd ns multicast-enable
   ipv6 nd na glean
   ipv6 nd proxy inter-access-vlan enable
  #
  interface Virtual-Ethernet0/1/1
   ve-group 1 l2-terminate 
  #
  interface Virtual-Ethernet0/1/1.26
   vlan-type dot1q 26
   mtu 9500
   mpls l2vc 10.0.0.1 26 control-word raw ignore-standby-state
  #
  arp static 192.168.1.1 00e0-fc12-3456 vid 26 interface Virtual-Ethernet0/1/1.31
  #
  return
  ```