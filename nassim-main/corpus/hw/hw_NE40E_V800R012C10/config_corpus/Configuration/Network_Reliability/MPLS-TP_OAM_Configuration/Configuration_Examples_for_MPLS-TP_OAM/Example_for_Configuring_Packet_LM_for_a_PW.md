Example for Configuring Packet LM for a PW
==========================================

This section provides an example for configuring packet loss measurement (LM) for a pseudo wire (PW).

#### Networking Requirements

As a connection-oriented packet switching technology, Multiprotocol Label Switching Transport Profile (MPLS-TP) is designed to convert a circuit switched transport network to a packet switched transport network. The purpose is to increase the transmission rate on the transport network.

Link reliability must be ensured when MPLS-TP is used. For example, users will not sense any change in voice quality if the packet loss rate on voice links is lower than 10%. However, if the packet loss rate is higher than 20%, user experience obviously degrades.

Packet LM can be used to collect packet loss statistics and evaluate link performance. LM is a performance monitoring function provided by MPLS-TP and is classified as single-ended packet LM or dual-ended packet LM.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of dual-ended packet LM is used as an example in this section. Regardless of single-ended or dual-ended, DM configurations on PEs are the same except the statistics display configurations.


On the network shown in [Figure 1](#EN-US_TASK_0172362437__fig_dc_vrp_mpls-tp_oam_cfg_002401), LSRA, LSRB, and LSRC are connected using a PW built over a bidirectional label switched path (LSP). The following deployment is made to ensure connectivity between LSRA and LSRC:

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

1. Create a maintenance entity (ME) instance and bind it to a PW.
2. Enable continuity check (CC) and connectivity verification (CV) on the MEP and its remote MEP (RMEP).
3. Configure an alarm threshold for lost packets.
4. Enable dual-ended packet LM.

#### Data Preparation

To complete the configuration, you need the following data:

* MEG name
* ID of the virtual circuit (VC) bound to the ME
* Alarm threshold for lost packets

#### Procedure

1. Configure a PW over a bidirectional LSP.
   
   
   
   For configuration details, see "[Configuration Examples](dc_vrp_vpws_cfg_3012.html)" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or "Configuration Files" in this section.
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
4. Enable dual-ended packet LM.
   
   # Enable dual-ended packet LM on LSRA.
   ```
   [~LSRA-mpls-tp-meg-test] lost-measure dual-ended enable
   [~LSRA-mpls-tp-meg-test] return
   ```
   
   # Enable dual-ended packet LM on LSRC.
   ```
   [~LSRC-mpls-tp-meg-test] lost-measure dual-ended enable
   [~LSRC-mpls-tp-meg-test] return
   ```
5. Verify the configuration.
   
   
   
   After completing the configurations, run the [**display mpls-tp oam**](cmdqueryname=display+mpls-tp+oam) command on LSRA to view packet loss statistics.
   
   ```
   <LSRA> display mpls-tp oam meg test statistic-type lost-measure dual-ended
   Dual-end loss measurement statistics:
   Index Near-end lost frames Loss ratio Far-end lost frames Loss ratio
   1     10                   12.50%     10                  12.50%
   Max near-end lost frames:10,frame loss ratio:12.50%
   Min near-end lost frames:10,frame loss ratio:12.50%
   Average near-end lost frames:10,frame loss ratio:12.50%
   Max far-end lost frames:10,frame loss ratio:12.50%
   Min far-end lost frames:10,frame loss ratio:12.50%
   Average far-end lost frames:10,frame loss ratio:12.50%   
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
   mpls l2vpn pw traffic-statistics enable
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
  lost-measure dual-ended enable
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
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   mpls
   mpls te
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
   mpls static-l2vc pw-template tpctoa 30000 transmit-vpn-label 101 receive-vpn-label 
  101
   mpls l2vpn pw traffic-statistics enable
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
  lost-measure dual-ended enable
  #
  return  
  ```