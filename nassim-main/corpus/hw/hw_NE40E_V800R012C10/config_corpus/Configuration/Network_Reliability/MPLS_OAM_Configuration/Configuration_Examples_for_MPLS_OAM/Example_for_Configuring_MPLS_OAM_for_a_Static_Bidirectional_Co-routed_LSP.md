Example for Configuring MPLS OAM for a Static Bidirectional Co-routed LSP
=========================================================================

This section provides an example for configuring MPLS OAM to check the connectivity of a static bidirectional co-routed LSP.

#### Context

Static bidirectional co-routed LSPs are widely used on transport networks but their OAM capabilities are insufficient to support network management required for public telecom networks. MPLS OAM can be used to detect faults on a static bidirectional co-routed LSP.

On the network shown in [Figure 1](#EN-US_TASK_0172362370__fig_dc_vrp_mplsoam_cfg_001801), establish a static bidirectional co-routed LSP between LSRA and LSRC to carry OAM packets so that any intermediate node can send back a response packet along the original path.

**Figure 1** Networking diagram for a tunnel protection group consisting of static bidirectional co-routed CR-LSPs  
![](figure/en-us_image_0000001675925732.png)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE 0/1/0 and GE 0/2/0, respectively.



**Table 1** Interfaces and IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| LSRA | Loopback1 | 10.1.1.1/32 |
| interface1 | 10.1.2.1/24 |
| LSRB | Loopback1 | 10.1.1.2/32 |
| interface1 | 10.1.2.2/24 |
| interface2 | 10.1.3.1/24 |
| LSRC | Loopback1 | 10.1.1.3/32 |
| interface2 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a static bidirectional co-routed LSP between LSRA and LSRC.
2. Enable MPLS OAM globally.
3. Configure MPLS OAM parameters in MPLS-OAM view on the nodes at both ends of the static bidirectional co-routed LSP.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the static bidirectional co-routed LSP.

#### Data Preparation

To complete the configuration, you need the following data:

* Tunnel interface numbers, tunnel interface IP addresses, destination addresses, and tunnel IDs on LSRA and LSRC
* Next-hop address and outgoing label on the ingress of the static bidirectional co-routed LSP
* Inbound interface name, next-hop address, and outgoing label on the transit node
* Inbound interface on the egress
* OAM detection packet type and interval at which OAM detection packets are sent

#### Procedure

1. Configure a static bidirectional co-routed LSP.
   
   
   
   Configure a static bidirectional co-routed LSP between LSRA and LSRB. The configuration details are not provided here. For details, see [Example for Configuring a Static Bidirectional Co-routed CR-LSP](dc_vrp_te-p2p_cfg_0168.html) in *HUAWEI NE40E-M2 seriesUniversal Service Router* Configuration Guide - MPLS or Configuration Files in this section.
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
3. Configure MPLS OAM parameters in the MPLS-OAM view on the nodes at both ends of the static bidirectional co-routed LSP.
   
   
   
   # Configure MPLS OAM parameters on LSRA.
   
   ```
   [~LSRA] mpls-oam
   ```
   ```
   [~LSRA-mpls-oam] mpls oam bidirectional-tunnel Tunnel10 type ffd frequency 10 auto-protocol
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
   [~LSRC-mpls-oam] mpls oam bidirectional-tunnel Tunnel20 type ffd frequency 10 auto-protocol
   ```
   ```
   [*LSRC-mpls-oam] commit
   ```
   ```
   [~LSRC-mpls-oam] quit
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the **auto-protocol** is not configured, go to Step 4. Otherwise, skip Step 4 and go to the next step.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the static bidirectional co-routed LSP.
   
   
   
   # Enable LSRA to send OAM detection packets.
   
   ```
   [~LSRA] mpls-oam
   ```
   ```
   [~LSRA-mpls-oam] mpls oam bidirectional-tunnel enable send Tunnel10
   ```
   ```
   [*LSRA-mpls-oam] commit
   ```
   ```
   [~LSRA-mpls-oam] quit
   ```
   
   # Enable LSRC to receive OAM detection packets.
   
   ```
   [~LSRC] mpls-oam
   ```
   ```
   [~LSRC-mpls-oam] mpls oam bidirectional-tunnel enable receive Tunnel20
   ```
   ```
   [*LSRC-mpls-oam] commit
   ```
   ```
   [~LSRC-mpls-oam] quit
   ```
5. Verify the configurations.
   
   
   
   After completing the configuration, run the **display mpls oam bidirectional-tunnel** command on LSRA to view MPLS OAM information of the static bidirectional co-routed LSP.
   
   # Check the configuration results on LSRA.
   
   ```
   <HUAWEI> display mpls oam bidirectional-tunnel all verbose
   --------------------------------------------------------------------------------
   Total OAM Num:                    1
   Total Start OAM Num:              0
   Total Defect OAM Num:             0
   Total Unavailable OAM Num:        0
   --------------------------------------------------------------------------------
   Verbose information about NO.1 OAM
   --------------------------------------------------------------------------------
   Bidirectional Tunnel basic information:
   -------------------------------------------------
   Tunnel-name             : Tunnel10
   Lsp signal status       : Up 
   Lsp establish type      : Static-cr-lsp 
   Lsp ingress lsr-id      : 10.1.1.1 
   Lsp tnl-id              : 100 
   Lsp incoming Label      : 20 
   -------------------------------------------------
   OAM basic information:
   -------------------------------------------------
   OAM Index               : 4
   OAM Select Board        : 3
   OAM Enable Direction    : Send & Receive
   Auto Protocol           : Enable 
   Auto Overtime (s)       : 300 
   Compatibility Mode      : Router Mode 
   -------------------------------------------------
   OAM detect information:
   -------------------------------------------------
   Send Type               : FFD
   Send Frequency          : 10 ms 
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
  #
  mpls
   mpls te
   mpls oam
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
  mpls-oam
   mpls oam bidirectional-tunnel Tunnel10 type ffd frequency 10 auto-protocol 
  # 
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 10.1.1.2
  #
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
  #
  interface GigabitEthernet0/1/1
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
  #
  mpls
   mpls te
   mpls oam
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
  mpls-oam
   mpls oam bidirectional-tunnel Tunnel20 type ffd frequency 10 auto-protocol
  #
  return
  ```