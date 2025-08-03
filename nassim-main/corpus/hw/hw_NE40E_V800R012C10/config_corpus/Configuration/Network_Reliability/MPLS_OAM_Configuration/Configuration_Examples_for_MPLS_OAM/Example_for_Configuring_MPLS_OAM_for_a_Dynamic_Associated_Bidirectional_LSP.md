Example for Configuring MPLS OAM for a Dynamic Associated Bidirectional LSP
===========================================================================

This section provides an example for configuring MPLS OAM to check the connectivity of a dynamic associated bidirectional LSP.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001842733617__fig10148142971313), two dynamic LSPs in opposite directions exist between LSRA and LSRB on the network. To implement bidirectional protection switching, bind each LSP to the ingress of its reverse LSP to form an associated bidirectional LSP.

IS-IS runs between LSRA and LSRB, which belong to Level-1.

#### 

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Networking diagram for an RSVP-TE tunnel  
![](figure/en-us_image_0000001796033258.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish a dynamic associated bidirectional LSP from LSRA to LSRB.
2. Enable MPLS OAM globally.
3. Configure MPLS OAM parameters in the system view on the nodes at both ends of the dynamic associated bidirectional LSP.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the dynamic associated bidirectional LSP.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS area ID, originating system ID, and IS-IS level of each node
* Tunnel interface number, IP address, destination IP address, and tunnel ID

#### Procedure

1. Configure dynamic associated bidirectional LSPs.
   
   
   
   Configure a dynamic associated bidirectional LSP between LSRA and LSRB. The configuration details are not provided here. For configuration details, see the configuration files.
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
   
   # Enable MPLS OAM globally on LSRB.
   ```
   [~LSRB] mpls
   ```
   ```
   [*LSRB-mpls] mpls oam
   ```
   ```
   [*LSRB-mpls] commit
   ```
   ```
   [~LSRB-mpls] quit
   ```
3. Configure MPLS OAM in the system view on the nodes at both ends of the dynamic associated bidirectional LSP.
   
   
   
   # Configure MPLS OAM for the ingress on LSRA.
   
   ```
   [~LSRA] mpls oam ingress Tunnel1 backward-lsp lsr-id 2.2.2.2 tunnel-id 1
   ```
   ```
   [~LSRA] mpls oam ingress enable Tunnel1
   ```
   
   # Configure MPLS OAM for the egress on LSRB.
   
   ```
   [~LSRB] mpls oam egress lsr-id 1.1.1.1 tunnel-id 1 type cv backward-lsp Tunnel1
   ```
   
   # Configure MPLS OAM for the egress on LSRA.
   
   ```
   [~LSRA] mpls oam egress lsr-id 2.2.2.2 tunnel-id 1 type cv backward-lsp Tunnel1
   ```
   
   # Configure MPLS OAM for the ingress on LSRB.
   
   ```
   [~LSRB] mpls oam ingress Tunnel1 backward-lsp lsr-id 1.1.1.1 tunnel-id 1
   ```
   ```
   [~LSRB] mpls oam ingress enable Tunnel
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the **auto-protocol** parameter has been configured for the egress, Step 4 does not need to be performed.
4. (Optional) Enable MPLS OAM on the nodes at both ends of the dynamic associated bidirectional LSP.
   
   
   
   # Enable MPLS OAM for the egress on LSRA.
   
   ```
   [~LSRA] mpls oam egress enable lsr-id 2.2.2.2 tunnel-id 1
   ```
   ```
   [*LSRA] commit
   ```
   
   # Enable MPLS OAM for the egress on LSRB.
   
   ```
   [~LSRB] mpls oam egress enable lsr-id 1.1.1.1 tunnel-id 1
   ```
   ```
   [*LSRB] commit
   ```
5. Verify the configuration.
   
   
   
   After completing the configuration, run the **display mpls oam ingress all verbose** command to view MPLS OAM parameter and status information on the ingress end of the dynamic associated bidirectional LSP.
   
   # Check the configuration on LSRA.
   
   ```
   <HUAWEI> display mpls oam ingress all verbose
   ```
   ```
   --------------------------------------------------------------------------------
   
   Verbose information about NO.1 OAM at the ingress
   --------------------------------------------------------------------------------
   
   
   LSP basic information:                   OAM basic information:
   --------------------------------------- ----------------------------------------
   Tunnel-name         : Tunnel1            OAM-Index           : 3
   Tunnel-name Index   : 1                  MEG-name Index      : 2147483651
   Lsp signal status   : Up                 OAM select board    : 2
   Lsp establish type  : Rsvp lsp           Enable-state        : Manual enable 
   Lsp ingress lsr-id  : 1.1.1.1            Ttsi/lsr-id         : 1.1.1.1 
   Lsp tnl-id          : 1                  Ttsi/tunnel-id      : 1 
   Lsp-id              : 2730               Compatibility Mode  : Router Mode 
   
   OAM detect information:                  OAM backward information:
   --------------------------------------- ----------------------------------------
   Type                : CV                 Share attribute     : Private 
   Frequency           : 1 s                Lsp-name            : -- 
   Detect State        : Start              Lsp ingress lsr-id  : 2.2.2.2 
   Defect State        : Non-defect         Lsp tnl-id          : 1 
   Available-state     : Available          Lsp-id              : 2732 
   Unavailable time (s): 0                  Lsp-inLabel         : 2112 
   Packet-priority     : 7                  Lsp signal status   : Up 
   Bdi-frequency       : Detect frequency   
   Hardware Error Info : No error 
   BDI Defect State    : -- 
   
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
   mpls rsvp-te
   mpls te cspf
   mpls oam
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
   isis enable 1
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 2.2.2.2 tunnel-id 1
   mpls te tunnel-id 1
  #
  mpls oam ingress Tunnel1 backward-lsp lsr-id 2.2.2.2 tunnel-id 1
  mpls oam ingress enable Tunnel1
  mpls oam egress lsr-id 2.2.2.2 tunnel-id 1 type cv backward-lsp Tunnel1
  mpls oam egress enable lsr-id 2.2.2.2 tunnel-id 1
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
   mpls rsvp-te
   mpls te cspf
   mpls oam
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te reverse-lsp protocol rsvp-te ingress-lsr-id 1.1.1.1 tunnel-id 1
   mpls te tunnel-id 1
  #
  mpls oam ingress Tunnel1 backward-lsp lsr-id 1.1.1.1 tunnel-id 1
  mpls oam ingress enable Tunnel1
  mpls oam egress lsr-id 1.1.1.1 tunnel-id 1 type cv backward-lsp Tunnel1
  mpls oam egress enable lsr-id 1.1.1.1 tunnel-id 1
  #
  return
  ```