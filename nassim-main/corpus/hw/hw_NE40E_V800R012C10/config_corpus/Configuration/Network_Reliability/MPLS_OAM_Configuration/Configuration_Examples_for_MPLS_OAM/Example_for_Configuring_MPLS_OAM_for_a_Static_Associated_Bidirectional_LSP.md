Example for Configuring MPLS OAM for a Static Associated Bidirectional LSP
==========================================================================

This section provides an example for configuring MPLS OAM to check the connectivity of a static associated bidirectional LSP.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172362367__fig_dc_vrp_mplsoam_cfg_001701), a forward LSP and a reverse LSP are established between LSRA and LSRC. To implement bidirectional protection switching, bind each LSP to the ingress of its reverse LSP to form a static associated bidirectional LSP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Associated bidirectional static CR-LSP  
![](figure/en-us_image_0000001686329460.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a static associated bidirectional LSP between LSRA and LSRC.
2. Enable MPLS OAM globally.
3. Configure MPLS OAM parameters in the system view on the nodes at both ends of the static associated bidirectional LSP.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the static associated bidirectional LSP.

#### Data Preparation

To complete the configuration, you need the following data:![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, the LSP from LSRA to LSRC is a forward LSP, and the LSP from LSRC to LSRA is a reverse LSP.



**Table 1** Data to be prepared
| Device | Parameter | Value |
| --- | --- | --- |
| **LSRA** | Tunnel interface number of the forward LSP | Tunnel10 |
| Tunnel ID of the forward LSP | 100 |
| Outgoing label of the forward LSP | 20 |
| Name of the reverse LSP | Tunnel20 |
| Incoming label of the reverse LSP | 130 |
| **LSRB** | Name of the forward LSP | Tunnel10 |
| Incoming label of the forward LSP | 20 |
| Outgoing label of the forward LSP | 30 |
| Name of the reverse LSP | Tunnel20 |
| Incoming label of the reverse LSP | 120 |
| Outgoing label of the reverse LSP | 130 |
| **LSRC** | Tunnel interface number of the reverse LSP | Tunnel20 |
| Tunnel ID of the reverse CR-LSP | 200 |
| Outgoing label of the reverse LSP | 120 |
| Name of the forward LSP | Tunnel10 |
| Incoming label of the forward LSP | 30 |



#### Procedure

1. Configure a static associated bidirectional LSP.
   
   
   
   Configure a static associated bidirectional LSP between LSRA and LSRC. The configuration details are not provided here. For configuration details, see the configuration files.
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
3. Configure MPLS OAM parameters in the system view on the nodes at both ends of the static associated bidirectional LSP.
   
   
   
   # Configure MPLS OAM parameters for the ingress on LSRA.
   
   ```
   [~LSRA] mpls oam ingress Tunnel 10 type ffd frequency 3
   ```
   ```
   [~LSRA] mpls oam ingress enable Tunnel10
   ```
   
   # Configure MPLS OAM parameters for the egress on LSRC.
   
   ```
   [~LSRC] mpls oam egress lsp-name Tunnel10 type ffd frequency 3 backward-lsp Tunnel20
   ```
   
   # Configure MPLS OAM parameters for the egress on LSRA.
   
   ```
   [~LSRA] mpls oam egress lsp-name Tunnel20 type ffd frequency 3 backward-lsp Tunnel10
   ```
   
   # Configure MPLS OAM parameters for the ingress on LSRC.
   
   ```
   [~LSRC] mpls oam ingress Tunnel20 type ffd frequency 3
   ```
   ```
   [~LSRC] mpls oam ingress enable Tunnel20
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the **auto-protocol** parameter has been configured for the egress, Step 4 does not need to be performed.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the static associated bidirectional LSP.
   
   
   
   # Enable MPLS OAM for the egress on LSRA.
   
   ```
   [~LSRA] mpls oam egress enable lsp-name Tunnel10
   ```
   ```
   [*LSRA] commit
   ```
   
   # Enable MPLS OAM for the egress on LSRC.
   
   ```
   [~LSRC] mpls oam egress enable lsp-name Tunnel10
   ```
   ```
   [*LSRC] commit
   ```
5. Verify the configurations.
   
   
   
   After completing the configuration, run the **display mpls oam ingress all verbose** command to view MPLS OAM parameter and status information on the ingress end of the static associated bidirectional LSP.
   
   # Check the configuration results on LSRA.
   
   ```
   <HUAWEI> display mpls oam ingress all verbose
   ```
   ```
   --------------------------------------------------------------------------------
   
   Verbose information about NO.1 OAM at the ingress
   --------------------------------------------------------------------------------
   
   
   LSP basic information:                   OAM basic information:
   --------------------------------------- --------------------------------------
   Tunnel-name         : Tunnel10        OAM-Index           : 4
   Lsp signal status   : Up                 OAM select board    : 9
   Lsp establish type  : Static-cr-lsp      Enable-state        : Manual enable 
   Lsp ingress lsr-id  : 1.1.1.1            Ttsi/lsr-id         : 1.1.1.1            
   
   Lsp tnl-id          : 100                Ttsi/tunnel-id      : 100               
   
   Lsp-id              : --                 Compatibility Mode  : Router Mode 
   
   OAM detect information:                  OAM backward information:
   --------------------------------------- --------------------------------------
   Type                : FFD                Share attribute     : Private 
   Frequency           : 3.3 s              Lsp-name            : Tunnel20
   Detect-state        : Start              Lsp ingress lsr-id  : 3.3.3.3
   Defect-state        : Non-defect         Lsp tnl-id          : 1
   Available-state     : Available          Lsp-id              : 1
   Unavailable time (s): 0                  Lsp-inLabel         : 20
   Packet-priority     : 7                  Lsp signal status   : Up
   Bdi-frequency       : Detect frequency          
   Hardware Error Info : --                
    
   --------------------------------------------------------------------------------
   
   Total OAM Num:                1
   Total Start OAM Num:          1
   Total Defect OAM Num:         0
   Total Unavailable OAM Num:    0
   ```

#### Configuration Files

* LSRA configuration file
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls oam
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  static-cr-lsp egress Tunnel20 incoming-interface GigabitEthernet0/1/0 in-label 130
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te signal-protocol cr-static
   mpls te reverse-lsp protocol static lsp-name Tunnel20
   mpls te tunnel-id 100
  #
  static-cr-lsp ingress tunnel-interface Tunnel10 destination 3.3.3.3 nexthop 10.1.1.2 out-label 20
  # 
  ip route-static 2.2.2.2 255.255.255.255 10.1.1.2
  ip route-static 3.3.3.3 255.255.255.255 10.1.1.2
  #
  mpls oam ingress Tunnel10 type ffd frequency 3
  mpls oam ingress enable Tunnel10
  mpls oam egress lsp-name Tunnel20 type ffd frequency 3 backward-lsp Tunnel10
  mpls oam egress enable lsp-name Tunnel20
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls oam
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls te
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ip route-static 1.1.1.1 255.255.255.255 10.1.1.1
  ip route-static 3.3.3.3 255.255.255.255 10.2.1.2
  #
  static-cr-lsp transit Tunnel10 incoming-interface GigabitEthernet0/1/0 in-label 20 nexthop 10.2.1.2 out-label 30 
  #
  static-cr-lsp transit Tunnel20 incoming-interface GigabitEthernet0/2/0 in-label 120 nexthop 10.1.1.1 out-label 130 
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls oam
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  static-cr-lsp egress Tunnel10 incoming-interface GigabitEthernet0/2/0 in-label 30
  #
  interface Tunnel20
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te signal-protocol cr-static
   mpls te reverse-lsp protocol static lsp-name Tunnel10
   mpls te tunnel-id 200
  #
  static-cr-lsp ingress tunnel-interface Tunnel20 destination 1.1.1.1 nexthop 10.2.1.1 out-label 120
  #
  ip route-static 1.1.1.1 255.255.255.255 10.2.1.1
  ip route-static 2.2.2.2 255.255.255.255 10.2.1.1
  #
  mpls oam ingress Tunnel20 type ffd frequency 3
  mpls oam ingress enable Tunnel20
  mpls oam egress lsp-name Tunnel10 type ffd frequency 3 backward-lsp Tunnel20
  mpls oam egress enable lsp-name Tunnel10
  #
  return
  ```