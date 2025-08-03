Example for Configuring MPLS OAM for a PW
=========================================

This section provides an example for configuring MPLS OAM to check the connectivity of a PW.

#### Networking Requirements

On the MPLS network shown in [Figure 1](#EN-US_TASK_0172362373__fig_dc_vrp_mplsoam_cfg_001801), a static SS-PW is established between LSRA and LSRC.

Configure MPLS OAM to check the connectivity of the PW. If MPLS OAM detects a fault on the PW, it sends a BDI packet along the PW and reports the fault to the OAM module.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Configuring a PW over a bidirectional LSP  
![](figure/en-us_image_0000001718861544.png)

**Table 1** Interfaces and IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| LSRA | Loopback1 | 10.1.1.1/32 |
| Interface1 | 10.1.2.1/24 |
| LSRB | Loopback1 | 10.1.1.2/32 |
| Interface1 | 10.1.2.2/24 |
| Interface2 | 10.1.3.1/24 |
| LSRC | Loopback1 | 10.1.1.3/32 |
| Interface2 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable MPLS OAM globally.
2. Establish a PW over a bidirectional LSP between LSRA and LSRC.
3. Configure MPLS OAM parameters in the MPLS-OAM view on the nodes at both ends of the PW.
4. (Optional) Enable MPLS OAM.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses at both ends of the PW
* OAM detection packet type and interval at which OAM detection packets are sent
* (Optional) Timeout period of the auto protocol![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  A timeout period must be configured in automatic negotiation mode. In manual mode, you do not need to set this parameter.

#### Procedure

1. Configure a PW over a bidirectional LSP.
   
   
   
   The configuration procedure for a bidirectional PW between LSRA and LSRC is not provided here. For configuration details, see [Configuration Examples for VPWS](dc_vrp_vpws_cfg_3012.html) in *HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - VPN* or Configuration Files in this section.
2. Enable MPLS OAM globally.
   
   # Enable MPLS OAM globally on LSRA.
   ```
   [~LSRA] mpls
   ```
   ```
   [*LSRA-mpls] mpls oam
   ```
   ```
   [*LSRA-mpls] commit
   ```
   ```
   [~LSRA-mpls] quit
   ```
   
   # Enable MPLS OAM globally on LSRC.
   ```
   [~LSRC] mpls
   ```
   ```
   [*LSRC-mpls] mpls oam
   ```
   ```
   [*LSRC-mpls] commit
   ```
   ```
   [~LSRC-mpls] quit
   ```
3. Configure MPLS OAM parameters in the MPLS-OAM view on the nodes at both ends of the PW.
   
   
   
   # Configure MPLS OAM parameters on LSRA.
   
   ```
   [~LSRA] mpls-oam
   ```
   ```
   [~LSRA-mpls-oam] mpls oam l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan type cv auto-protocol overtime 0
   ```
   ```
   [*LSRA-mpls-oam] commit
   ```
   ```
   [~LSRA-mpls-oam] quit
   ```
   
   # Configure MPLS OAM parameters for the egress on LSRC.
   
   ```
   [~LSRC] mpls-oam
   ```
   ```
   [~LSRC-mpls-oam] mpls oam l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan type cv auto-protocol overtime 0
   ```
   ```
   [*LSRC-mpls-oam] commit
   ```
   ```
   [~LSRC-mpls-oam] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configuration, run the **display mpls oam l2vc** command on LSRA to view PW detection information.
   
   # Check the configuration on LSRA.
   
   ```
   <HUAWEI> display mpls oam l2vc all verbose 
   --------------------------------------------------------------------------------
   Total OAM Num:                    1                                             
   Total Start OAM Num:              0                                             
   Total Defect OAM Num:             0                                             
   Total Unavailable OAM Num:        0                                             
   --------------------------------------------------------------------------------
   Verbose information about NO.1 OAM at the TPE 
   --------------------------------------------------------------------------------
   PW basic information:                                                           
   ------------------------------------------------- 
   Service Type            : VLL PW 
   PW Status               : Up  
   Peer IP                 : 10.1.1.3  
   VC Type                 : vlan 
   VC ID                   : 30000 
   Local VC Label          : 101 
   Remote VC Label         : 101 
   AC Interface            : Ethernet3/0/0.1  
   PW Type                 : Primary 
   ------------------------------------------------- 
   OAM basic information:  
   ------------------------------------------------- 
   OAM Index               : 1  
   OAM Select Board        : 3 
   OAM Enable Direction    : Send & Receive  
   Auto Protocol           : Enable 
   Auto Overtime (s)       : 0 
   Remote Peer IP          : --  
   Remote VC Type          : --  
   Remote VC ID            : --  
   Compatibility Mode      : Router Mode   
   -------------------------------------------------                               
   OAM detect information:  
   -------------------------------------------------     
   Send Type               : CV  
   Send Frequency          : 1 s 
   Receive Type            : CV 
   Receive Frequency       : 1 s 
   Detect State            : Start  
   Defect State            : Non-defect 
   BDI Defect State        : -- 
   Bdi-frequency           : Detect frequency 
   Available State         : Available 
   Unavailable Time (s)    : 0 
   Hardware Error Info     : No error
   Packet-priority         : 7
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
  mpls oam
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
   destination 10.1.1.3
   mpls te signal-protocol cr-static
   mpls te tunnel-id 100
   mpls te bidirectional
   mpls te reserved-for-binding
  #
  ip route-static 10.1.1.2 255.255.255.255 10.1.2.2
  ip route-static 10.1.1.3 255.255.255.255 10.1.2.2
  #
  tunnel-policy tpatoc
   tunnel binding destination 10.1.1.3 te Tunnel10
  #
  mpls-oam
   mpls oam l2vc peer-ip 10.1.1.3 vc-id 30000 vc-type vlan type cv auto-protocol overtime 0
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
   mpls oam
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
   mpls oam
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
   mpls
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
   tunnel binding destination 10.1.1.1 te Tunnel20
  #
  mpls-oam
    mpls oam l2vc peer-ip 10.1.1.1 vc-id 30000 vc-type vlan type cv auto-protocol overtime 0
  #
  return  
  ```