Example for Configuring Packet DM for a PW
==========================================

This section provides an example for configuring packet delay measurement (DM) for a pseudo wire (PW).

#### Networking Requirements

As a connection-oriented packet switching technology, Multiprotocol Label Switching Transport Profile (MPLS-TP) is designed to convert a circuit switched transport network to a packet switched transport network. The purpose is to increase the transmission rate on the transport network.

Link reliability must be ensured when MPLS-TP is used. Voice services are used as an example. The coding and decoding of voice packets plus the transmission delay make the delay in VoIP transmission much longer than that in common circuit switched voice transmission. If the delay is longer than 400 ms, the voice quality is affected. If the delay is longer than 2 seconds, VoIP services are unavailable. In addition, if the delay variation (jitter) is longer than the transmission duration of a voice packet, voice quality will drop greatly.

Packet DM can be used to collect delay and jitter statistics and evaluate link performance. DM is a performance monitoring function provided by MPLS-TP and is classified as one-way packet DM or two-way packet DM.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of two-way packet DM is used as an example in this section. Regardless of one-way or two-way, DM configurations on LSRs are the same except the statistics display configurations.


On the network shown in [Figure 1](#EN-US_TASK_0172362438__fig_dc_vrp_mpls-tp_oam_cfg_002401), LSRA, LSRB, and LSRC are connected using a PW built over a bidirectional label switched path (LSP). The following deployment is made to ensure connectivity between LSRA and LSRC:

* LSRA and LSRC serve as MEPs.
* LSRB serves as a MIP.

**Figure 1** PW over a bidirectional LSP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-tp_oam_cfg_002401.png)  

**Table 1** Interfaces and IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| LSRA | Loopback1 | 10.1.1.1/32 |
| GigabitEthernet0/1/0 | 10.1.2.1/24 |
| LSRB | Loopback1 | 10.1.1.2/32 |
| GigabitEthernet0/1/0 | 10.1.2.2/24 |
| GigabitEthernet0/2/0 | 10.1.3.1/24 |
| LSRC | Loopback1 | 10.1.1.3/32 |
| GigabitEthernet0/2/0 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create an ME instance and bind it to a PW.
2. Enable continuity check (CC) and connectivity verification (CV) on the MEP and its remote MEP (RMEP).
3. Enable two-way packet DM.

#### Data Preparation

To complete the configuration, you need the following data:

* MEG name
* ID of the virtual circuit (VC) bound to the ME

#### Procedure

1. Configure a PW over a bidirectional LSP.
   
   
   
   For configuration details, see "[Configuration Examples](dc_vrp_vpws_cfg_3012.html)" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or Configuration Files.
2. Create an ME instance and bind it to the PW.
   
   # Create an ME instance named **test** on LSRA and bind it to the PW.
   ```
   [~LSRA] mpls-tp meg test
   [*LSRA-mpls-tp-meg-test] me l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan mep-id 1 remote-mep-id 2
   ```
   
   # Create an ME instance named **test** on LSRC and bind it to the PW.
   ```
   [~LSRC] mpls-tp meg test
   [*LSRC-mpls-tp-meg-test] me l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan mep-id 2 remote-mep-id 1
   ```
3. Enable CC and CV on the MEP and RMEP.
   
   # Enable CC and CV on LSRA.
   ```
   [~LSRA-mpls-tp-meg-test] cc send enable
   [~LSRA-mpls-tp-meg-test] cc receive enable
   ```
   
   # Enable CC and CV on LSRC.
   ```
   [~LSRC-mpls-tp-meg-test] cc send enable
   [~LSRC-mpls-tp-meg-test] cc receive enable
   ```
4. Enable two-way packet DM.
   
   
   ```
   [~LSRA-mpls-tp-meg-test] delay-measure two-way
   Two-way delay measure statistics      
   delay(us):        delay variation(us):
   100               --
   100               0                 
   100               0                 
   99                1                 
   100               1                 
   The Max delay:100, The Max delay variation:1                         
   The Min delay:99, The Min delay variation:0                         
   The delay average:100, The delay variation average:1                         
   Total sent Packets Number:5, Total received Packets Number: 5
   
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
   sysname LSRA
  #
   mpls lsr-id 10.1.1.1
   mpls
    mpls te
  #
   mpls l2vpn
  #
   bidirectional static-cr-lsp ingress Tunnel10
    forward nexthop 10.1.2.2 out-label 20
    backward in-label 20
  #
  pw-template tpatoc
   peer-address 10.1.1.3
   control-word
   tnl-policy tpatoc
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls
   mpls static-l2vc pw-template tpatoc 30000 transmit-vpn-label 101 receive-vpn-label 101
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 10.1.1.2
   mpls te signal-protocol cr-static
   mpls te tunnel-id 100
   mpls te bidirectional
   mpls te reserved-for-binding
  #
   ip route-static 10.1.1.2 255.255.255.255 10.1.2.2
   ip route-static 10.1.1.3 255.255.255.255 10.1.2.2
  #
  tunnel-policy tpatoc
   tunnel binding destination 10.1.1.2 te Tunnel10
  #
   mpls-tp meg test
    me l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan mep-id 1 remote-mep-id 2
    cc send enable
    cc receive enable
  #
  delay-measure two-way
  #
  return 
  ```
* LSRB configuration file
  
  ```
  #
   sysname LSRB
  #
   mpls lsr-id 10.1.1.2
   mpls
    mpls te
  #
   bidirectional static-cr-lsp transit lsp1
    forward in-label 20 nexthop 10.1.3.2 out-label 40
    backward in-label 16 nexthop 10.1.2.1 out-label 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls te
   ais enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls te
   ais enable
  #
  interface LoopBack1
   ip address 10.1.1.2 255.255.255.255
  #
   ip route-static 10.1.1.1 255.255.255.255 10.1.2.1
   ip route-static 10.1.1.3 255.255.255.255 10.1.3.2
  #
  return  
  ```
* LSRC configuration file
  
  ```
  #
   sysname LSRC
  #
   mpls lsr-id 10.1.1.3
   mpls
    mpls te
  #
   mpls l2vpn
  #
   bidirectional static-cr-lsp egress lsp1
    forward in-label 40 lsrid 10.1.1.1 tunnel-id 100
    backward nexthop 10.1.3.1 out-label 16
  #
  pw-template tpctoa
   peer-address 10.1.1.1
   control-word
   tnl-policy tpctoa
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls te
  
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1
   mpls static-l2vc pw-template tpctoa 30000 transmit-vpn-label 101 receive-vpn-label 101
  #
  interface LoopBack1
   ip address 10.1.1.3 255.255.255.255
  #
  interface Tunnel20
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 10.1.1.1
   mpls te signal-protocol cr-static
   mpls te tunnel-id 200
   mpls te passive-tunnel
   mpls te binding bidirectional static-cr-lsp egress lsp1
   mpls te reserved-for-binding
  #
   ip route-static 10.1.1.1 255.255.255.255 10.1.3.1
   ip route-static 10.1.1.2 255.255.255.255 10.1.3.1
  #
  tunnel-policy tpctoa
   tunnel binding destination 10.1.1.1 te Tunnel10
  #
   mpls-tp meg test
    me l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan mep-id 2 remote-mep-id 1
    cc send enable
    cc receive enable
  #
  return  
  ```