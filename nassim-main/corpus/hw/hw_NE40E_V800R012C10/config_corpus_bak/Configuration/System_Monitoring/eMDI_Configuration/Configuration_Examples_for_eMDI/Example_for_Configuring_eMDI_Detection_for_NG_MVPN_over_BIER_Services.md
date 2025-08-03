Example for Configuring eMDI Detection for NG MVPN over BIER Services
=====================================================================

This section provides an example for configuring eMDI detection for NG MVPN over BIER services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0285719149__fig35284409229), next-generation multicast VPN (NG MVPN) over BIER services is deployed to resolve multicast service traffic congestion, reliability, and security issues on the carrier's backbone network. In addition, BIER eMDI is deployed on the root, P, Leaf1, and Leaf2 nodes to detect the quality of multicast services. Network maintenance personnel can view the real-time detection results reported through telemetry on the monitor platform and quickly demarcate and locate network faults based on the detection results.

**Figure 1** NG MVPN over BIER networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/1/1, respectively.


  
![](figure/en-us_image_0285783129.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure NG MVPN over BIER.
2. Configure BIER eMDI detection on the root node.
   1. Configure a channel group for BIER eMDI.
   2. Configure a board group for BIER eMDI.
   3. Bind the channel group to the board group.
3. Configure BIER eMDI on P, Leaf 1, and Leaf 2.
   1. Configure a board group for BIER eMDI.
   2. Bind the channel group to the board group.
4. Configure telemetry.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces (shown in [Figure 1](#EN-US_TASK_0285719149__fig35284409229))
* Multicast group address: 225.1.1.1/24
* Multicast source address: 192.168.0.100/24
* Name of a multicast VPN instance: VPNA
* ID of a BIER sub-domain: 0
* BIER BSL: 256
* Name of the channel group for BIER eMDI: BIER-channel
* Name of the board group for BIER eMDI: BIER-lpu

#### Procedure

1. Configure NG MVPN over BIER. For common configuration details, see [Configuring NG MVPN over BIER](../vrp/dc_bier_cfg_01.html). For configuration details in this example, see [Configuration Files](#EN-US_TASK_0285719149__example_dc_vrp_cfg_ngmvpn_001301).
2. Configure a channel group for BIER eMDI.
   
   A channel group for BIER eMDI is required only on the root node.
   ```
   [~Root] emdi
   ```
   ```
   [~Root-emdi] emdi channel-group BIER-channel
   ```
   ```
   [*Root-emdi-channel-group-BIER-channel] emdi channel 1 source 192.168.0.100 group 225.1.1.1 vpn-instance VPNA sub-domain 0 bsl 256
   ```
   ```
   [*Root-emdi-channel-group-BIER-channel] quit
   ```
   ```
   [*Root-emdi] quit
   ```
   ```
   [*Root] commit
   ```
3. Configure a board group for BIER eMDI.
   
   The configurations of the root, P, Leaf1, and Leaf2 nodes are similar. The following uses the root node as an example. For detailed configurations of other nodes, see [Configuration Files](#EN-US_TASK_0285719149__example_dc_vrp_cfg_ngmvpn_001301).
   ```
   [~Root] emdi
   ```
   ```
   [~Root-emdi] emdi lpu-group BIER-lpu
   ```
   ```
   [*Root-emdi-lpu-group-BIER-lpu] emdi bind slot all
   ```
   ```
   [*Root-emdi-lpu-group-BIER-lpu] quit
   ```
   ```
   [*Root-emdi] quit
   ```
   ```
   [*Root] commit
   ```
4. Bind the channel group to the board group.
   
   The configurations of the root, P, Leaf1, and Leaf2 nodes are similar. The following uses the root node as an example. For detailed configurations of other nodes, see [Configuration Files](#EN-US_TASK_0285719149__example_dc_vrp_cfg_ngmvpn_001301).
   ```
   [~Root] emdi
   ```
   ```
   [~Root-emdi] emdi bier bind lpu-group BIER-lpu
   ```
   ```
   [*Root-emdi] quit
   ```
   ```
   [*Root] commit
   ```
5. After the preceding configurations are complete, run the [**display emdi statistics history bier channel**](cmdqueryname=display+emdi+statistics+history+bier+channel) command to query the detection result when BIER packets are forwarded by the detected device. The following uses the P node as an example to describe how to query the detection result of outgoing traffic on the P node.
   
   
   ```
   [~P] display emdi statistics history bier outbound channel slot 3
   ```
   ```
   Source Address:192.168.0.100    Group Address:225.1.1.1        Vpn Label:256                                                        
   Bfir Id:1      Sub Domain:0      Bsl:256    SI:0   Token:9
   Interface      : gigabitethernet0/1/1
   Total Records  : 3         Latest Rate(pps) : 188226              Latest Detect Time : 2021-02-18 21:30:50
   -----------------------------------------------------------------------------------------------------------------------------------------------
   Record          Record        Monitor   Monitor    Received      Rate         Rate         RTP-LC      RTP-SE        RTP-LR       RTP-SER
   Index           Time         Period(s)  Status     Packets       pps          bps                                   (1/100000)   (1/100000)
   -----------------------------------------------------------------------------------------------------------------------------------------------
   1       2019-08-08:21-11-20     10      Normal     4393232      439323     4871215641       6700          6633         152           151
   2       2019-08-08:21-11-10     10      Normal     4388533      438853     4866005390       6700          6633         152           151
   3       2019-08-08:21-11-00     60      Normal     4388218      438821     4865656118       6700          6633         152           151
   -----------------------------------------------------------------------------------------------------------------------------------------------
   ```
6. Configure telemetry.
   
   
   
   The configurations of the root, P, Leaf1, and Leaf2 nodes are similar. The following uses the root node as an example. For detailed configurations of other nodes, see [Configuration Files](#EN-US_TASK_0285719149__example_dc_vrp_cfg_ngmvpn_001301) (Only key configurations are provided here. For details, see Telemetry Configuration).
   
   * Configure a destination collector.
     ```
     [~Root] telemetry
     ```
     ```
     [*Root-telemetry] destination-group Monitor
     ```
     ```
     [*Root-telemetry-destination-group-Monitor] ipv4-address 10.1.7.2 port 10001 protocol grpc
     ```
     ```
     [*Root-telemetry-destination-group-Monitor] commit
     ```
     ```
     [~Root-telemetry-destination-group-Monitor] quit
     ```
   * Configure sampling paths.
     ```
     [~Root-telemetry] sensor-group emdimonitor
     ```
     ```
     [*Root-telemetry-sensor-group-emdimonitor] sensor-path huawei-emdi:emdi/bier-out-telem-reps/bier-out-telem-rep
     ```
     ```
     [*Root-telemetry-sensor-group-emdimonitor] sensor-path huawei-emdi:emdi/bier-out-telem-rtps/bier-out-telem-rtp
     ```
     ```
     [*Root-telemetry-sensor-group-emdimonitor] commit
     ```
     ```
     [~Root-telemetry-sensor-group-emdimonitor] quit
     ```
   * Create a static subscription.
     ```
     [~Root-telemetry] subscription EMDI
     ```
     ```
     [*Root-telemetry-subscription-EMDI] sensor-group emdimonitor
     ```
     ```
     [*Root-telemetry-subscription-EMDI] destination-group Monitor
     ```
     ```
     [*Root-telemetry-subscription-EMDI] commit
     ```
   
   After completing the configuration, check the BIER eMDI detection result reported through telemetry on the monitor platform.

#### Configuration Files

* Root node configuration file
  ```
  #
  sysname Root
  #
  multicast routing-enable
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 4:4 export-extcommunity
    vpn-target 3:3 import-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      bier   
     spmsi-tunnel
      group 224.0.0.0 255.255.255.0 source 192.168.1.0 255.255.255.0 bier limit 16
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide-compatible
   network-entity 10.0000.0000.0001.00
   bier enable
  #
  interface GigabitEthernet0/1/0 
   undo shutdown
   ip address 192.168.0.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface LoopBack1
   ip binding vpn-instance VPNA
   ip address 1.1.1.2 255.255.255.255
  #
  bgp 100
   peer 4.4.4.1 as-number 100
   peer 4.4.4.1 connect-interface LoopBack0
   peer 5.5.5.1 as-number 100
   peer 5.5.5.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.1 enable
    peer 5.5.5.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
  #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  bier
   sub-domain 0
    bfr-id 1
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  emdi
   emdi channel-group BIER-channel
    emdi channel 1 source 192.168.0.100 group 225.1.1.1 vpn-instance VPNA sub-domain 0 bsl 256
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group BIER-lpu
    emdi bind slot all
   emdi bier bind lpu-group BIER-lpu
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/bier-out-telem-reps/bier-out-telem-rep
    sensor-path huawei-emdi:emdi/bier-out-telem-rtps/bier-out-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  return
  ```
* P node configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide-compatible
   network-entity 10.0000.0000.0004.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0 
   undo shutdown
   ip address 192.168.0.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.45.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 2.2.2.1 255.255.255.255
   isis enable 1
  #
  bier
   sub-domain 0
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  #
  emdi
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group BIER-lpu
    emdi bind slot all
   emdi bier bind lpu-group BIER-lpu
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/bier-out-telem-reps/bier-out-telem-rep
    sensor-path huawei-emdi:emdi/bier-out-telem-rtps/bier-out-telem-rtp
    sensor-path huawei-emdi:emdi/bier-telem-reps/bier-telem-rep
    sensor-path huawei-emdi:emdi/bier-telem-rtps/bier-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  return
  ```
* Leaf1 node configuration file
  
  ```
  #
  sysname Leaf1
  #
  multicast routing-enable
  #
  multicast mvpn 4.4.4.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 4.4.4.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide-compatible
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.45.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp       
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 4.4.4.1 255.255.255.255
   pim sm
   isis enable 1
  # 
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
   #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  bier
   sub-domain 0
    bfr-id 4
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  emdi
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group BIER-lpu
    emdi bind slot all
   emdi bier bind lpu-group BIER-lpu
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/bier-telem-reps/bier-telem-rep
    sensor-path huawei-emdi:emdi/bier-telem-rtps/bier-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  return
  ```
* Leaf2 node configuration file
  
  ```
  #
  sysname Leaf2
  #
  multicast routing-enable
  #
  multicast mvpn 5.5.5.1
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 400:1
    apply-label per-instance
    vpn-target 4:4 export-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 5.5.5.1
  #
  mpls
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   cost-style wide-compatible
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
   bier enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.45.3 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPN
   ip address 192.168.3.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 5.5.5.1 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
   #
  pim vpn-instance VPNA
   static-rp 1.1.1.2
  #
  lldp enable
  #
  bier
   sub-domain 0
    bfr-id 5
    bfr-prefix interface LoopBack0
    protocol isis
    encapsulation-type mpls bsl 256 max-si 2
  #
  emdi
   emdi lpu-group _default_
    emdi bind slot all
   emdi lpu-group BIER-lpu
    emdi bind slot all
   emdi bier bind lpu-group BIER-lpu
  #
  telemetry
   #
   sensor-group emdimonitor
    sensor-path huawei-emdi:emdi/bier-telem-reps/bier-telem-rep
    sensor-path huawei-emdi:emdi/bier-telem-rtps/bier-telem-rtp
  #
   destination-group Monitor
    ipv4-address 10.1.7.2 port 10001 protocol grpc
   #
   subscription EMDI
    sensor-group emdimonitor
    destination-group Monitor
  #
  return
  ```