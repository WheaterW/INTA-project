Example for Configuring Packet DM for an LSP
============================================

This section provides an example for configuring packet delay measurement (DM) for a bidirectional label switched path (LSP).

#### Networking Requirements

As a connection-oriented packet switching technology, Multiprotocol Label Switching Transport Profile (MPLS-TP) is designed to convert a circuit switched transport network to a packet switched transport network. The purpose is to increase the transmission rate on the transport network.

Link reliability must be ensured when MPLS-TP is used. Voice services are used as an example. The coding and decoding of voice packets plus the transmission delay make the delay in VoIP transmission much longer than that in common circuit switched voice transmission. If the delay is longer than 400 ms, the voice quality is affected. If the delay is longer than 2 seconds, VoIP services are unavailable. In addition, if the delay variation (jitter) is longer than the transmission duration of a voice packet, voice quality will drop greatly.

Packet DM can be used to collect delay and jitter statistics and evaluate link performance. DM is a performance monitoring function provided by MPLS-TP and is classified as one-way packet DM or two-way packet DM.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration of two-way packet DM is used as an example in this section. Regardless of one-way or two-way, DM configurations on LSRs are the same except the statistics display configurations.

On the network shown in [Figure 1](#EN-US_TASK_0172362434__fig_dc_vrp_mpls-tp_oam_cfg_002401), a bidirectional LSP is established to connect label switching routers (LSRs) A, B, and C. The following deployment is made to ensure connectivity between LSRA and LSRC:

* LSRA and LSRC serve as MEPs.
* LSRB serves as a MIP.

**Figure 1** Bidirectional LSP![](../../../../public_sys-resources/note_3.0-en-us.png) 

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

1. Create a maintenance entity (ME) instance and bind it to a bidirectional LSP.
2. Configure an interval at which CCMs are sent and a priority for CCMs.
3. Enable continuity check (CC) and connectivity verification (CV) on the MEP and its remote MEP (RMEP).
4. Enable two-way packet DM.

#### Data Preparation

To complete the configuration, you need the following data:

* MEG name
* Name of the tunnel interface to which an ME instance is bound

#### Procedure

1. Configure a bidirectional LSP.
   
   
   
   For configuration details, see "[Example for Configuring a Static Bidirectional Co-routed CR-LSP](dc_vrp_te-p2p_cfg_0168.html)" in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - MPLS* or Configuration Files.
2. Create an ME instance and bind it to the bidirectional LSP.
   
   # Create an ME instance named **test** on LSRA and bind it to Tunnel 10.
   ```
   [~LSRA] mpls-tp meg test
   [~LSRA-mpls-tp-meg-test] me te interface Tunnel 10 mep-id 1 remote-mep-id 2
   [*LSRA-mpls-tp-meg-test] commit
   ```
   
   # Create an ME instance named **test** on LSRC and bind it to Tunnel 20.
   ```
   [~LSRC] mpls-tp meg test
   [~LSRC-mpls-tp-meg-test] me te interface Tunnel 20 mep-id 2 remote-mep-id 1
   [*LSRC-mpls-tp-meg-test] commit
   ```
3. Configure an interval at which CCMs are sent and a priority for CCMs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The same interval at which CCMs are sent and priority of CCMs must be configured on the MEP and RMEP. If the configurations at both ends are different, an alarm indicating an error is reported.
   
   
   # Set the interval at which CCMs are sent to 100 ms and the priority of CCMs to 6 on LSRA.
   ```
   [~LSRA-mpls-tp-meg-test] cc interval 100
   [*LSRA-mpls-tp-meg-test] cc exp 6
   [*LSRA-mpls-tp-meg-test] commit
   ```
   
   # Set the interval at which CCMs are sent to 100 ms and the priority of CCMs to 6 on LSRC.
   ```
   [~LSRC-mpls-tp-meg-test] cc interval 100
   [*LSRC-mpls-tp-meg-test] cc exp 6
   [*LSRA-mpls-tp-meg-test] commit
   ```
4. Enable CC and CV.
   
   # Enable CC and CV on LSRA.
   ```
   [~LSRA-mpls-tp-meg-test] cc send enable
   [*LSRA-mpls-tp-meg-test] cc receive enable
   [*LSRA-mpls-tp-meg-test] return
   ```
   
   # Enable CC and CV on LSRC.
   ```
   [~LSRC-mpls-tp-meg-test] cc send enable
   [*LSRC-mpls-tp-meg-test] cc receive enable
   [*LSRA-mpls-tp-meg-test] commit
   ```
5. Enable two-way packet DM.
   
   
   ```
   [~LSRA-mpls-tp-meg-test] delay-measure two-way
   Two-way delay measure statistics      
   delay(us):        delay variation(us):
   182               --
   182               0                 
   182               0                 
   183               1                 
   182               1                 
   The Max delay:183, The Max delay variation:1                         
   The Min delay:182, The Min delay variation:0                         
   The delay average:182, The delay variation average:1                         
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
   bidirectional static-cr-lsp ingress Tunnel10
    forward nexthop 10.1.2.2 out-label 20
    backward in-label 20
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 10.1.1.3
   mpls te signal-protocol cr-static
   mpls te tunnel-id 100
   mpls te bidirectional
  #
   ip route-static 10.1.1.2 255.255.255.255 10.1.2.2
   ip route-static 10.1.1.3 255.255.255.255 10.1.2.2
  #
   mpls-tp meg test
    me te interface Tunnel10 mep-id 1 remote-mep-id 2
    cc interval 100
    cc exp 6
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
   bidirectional static-cr-lsp egress lsp1
    forward in-label 40 lsrid 10.1.1.1 tunnel-id 100
    backward nexthop 10.1.3.1 out-label 16
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   mpls
   mpls te
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
  #
   ip route-static 10.1.1.1 255.255.255.255 10.1.3.1
   ip route-static 10.1.1.2 255.255.255.255 10.1.3.1
  #
   mpls-tp meg test
    me te interface Tunnel20 mep-id 2 remote-mep-id 1
    cc interval 100
    cc exp 6
    cc send enable
    cc receive enable
  #
  delay-measure two-way
  #
  return  
  ```