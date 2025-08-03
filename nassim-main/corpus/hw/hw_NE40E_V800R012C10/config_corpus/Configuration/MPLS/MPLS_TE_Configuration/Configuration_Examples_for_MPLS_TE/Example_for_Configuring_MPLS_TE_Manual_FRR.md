Example for Configuring MPLS TE Manual FRR
==========================================

Example for Configuring MPLS TE Manual FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368339__fig_dc_vrp_te-p2p_cfg_010501), a primary LSP is along the path LSRA -> LSRB -> LSRC -> LSRD. FRR is enabled on LSRB to protect traffic on the link between LSRB and LSRC.

A bypass CR-LSP is established over the path LSRB -> LSRE -> LSRC. LSRB is a PLR, and LSRC is an MP.

Explicit paths are used to establish the primary and bypass CR-LSPs. RSVP-TE is used as a signaling protocol.

**Figure 1** Networking diagram for MPLS TE manual FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_010501.png)

#### Configuration Notes

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a primary CR-LSP and enable TE FRR on the tunnel interface of the primary CR-LSP.
2. Configure a bypass CR-LSP on the PLR (ingress) and specify the interface of the protected link.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS area ID, originating system ID, and IS-IS level of each node
* Explicit paths for the primary and bypass CR-LSPs
* Tunnel interface number, source and destination IP addresses, ID, and RSVP-TE signaling protocol for each of the primary and bypass CR-LSPs
* Protected bandwidth and type and number of the interface on the protected link

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and its mask to every physical interface and configure a loopback interface address as an LSR ID on every node shown in [Figure 1](#EN-US_TASK_0172368339__fig_dc_vrp_te-p2p_cfg_010501). For configuration details, see [Configuration Files](#EN-US_TASK_0172368339__section_dc_vrp_te-p2p_cfg_010505) in this section.
2. Configure an IGP.
   
   
   
   Configure IS-IS on all nodes to advertise host routes. For configuration details, see [Configuration Files](#EN-US_TASK_0172368339__section_dc_vrp_te-p2p_cfg_010505) in this section.
   
   After completing the configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on every node. All nodes have learned routes from each other.
3. Configure basic MPLS functions and enable MPLS TE, CSPF, RSVP-TE, and IS-IS TE.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.1
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] mpls te
   ```
   ```
   [*LSRA-mpls] mpls rsvp-te
   ```
   ```
   [*LSRA-mpls] mpls te cspf
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRA] isis
   ```
   ```
   [*LSRA-isis-1] cost-style wide
   ```
   ```
   [*LSRA-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRA-isis-1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of LSRB, LSRC, LSRD and LSRE are similar to the configuration of LSRA. For configuration details, see [Configuration Files](#EN-US_TASK_0172368339__section_dc_vrp_te-p2p_cfg_010505) in this section. CSPF needs to be enabled only on LSRA and LSRB, which are ingress nodes of the primary and bypass CR-LSPs, respectively.
4. Configure an MPLS TE tunnel on LSRA.
   
   
   
   # Configure an explicit path for the primary CR-LSP.
   
   ```
   [~LSRA] explicit-path pri-path
   ```
   ```
   [*LSRA-explicit-path-pri-path] next hop 10.21.1.2
   ```
   ```
   [*LSRA-explicit-path-pri-path] next hop 10.31.1.2
   ```
   ```
   [*LSRA-explicit-path-pri-path] next hop 10.41.1.2
   ```
   ```
   [*LSRA-explicit-path-pri-path] next hop 4.4.4.4
   ```
   ```
   [*LSRA-explicit-path-pri-path] quit
   ```
   
   # Configure the MPLS TE tunnel for the primary CR-LSP.
   
   ```
   [*LSRA] interface tunnel 1
   ```
   ```
   [*LSRA-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel1] destination 4.4.4.4
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] mpls te path explicit-path pri-path
   ```
   
   # Enable FRR.
   
   ```
   [*LSRA-Tunnel1] mpls te fast-reroute
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
   
   After completing the configuration, run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) command on LSRA. **Tunnel1** is **Up**.
   
   ```
   [~LSRA] display interface tunnel
   ```
   ```
   Tunnel1 current state : UP (ifindex: 20)
   Line protocol current state : UP 
   Last line protocol up time : 2011-05-31 06:30:58
   Description:
   Route Port,The Maximum Transmit Unit is 1500, Current BW: 50Mbps 
   Internet Address is unnumbered, using address of LoopBack1(1.1.1.1/32)
   Encapsulation is TUNNEL, loopback not set
   Tunnel destination 4.4.4.4
   Tunnel up/down statistics 1
   Tunnel protocol/transport MPLS/MPLS, ILM is available,
   primary tunnel id is 0x321, secondary tunnel id is 0x0
   Current system time: 2011-05-31 07:32:31
       300 seconds output rate 0 bits/sec, 0 packets/sec
       0 seconds output rate 0 bits/sec, 0 packets/sec
       126 packets output,  34204 bytes
       0 output error
       18 output drop
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
   
   # Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command on LSRA. Detailed information about the TE tunnel interface is displayed.
   
   ```
   [~LSRA] display mpls te tunnel-interface
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP                                       
       Traffic Switch      : - 
       Session ID          : 1
       Ingress LSR ID      : 1.1.1.1               Egress LSR ID: 4.4.4.4
       Admin State         : UP                    Oper State   : UP
       Signaling Protocol  : RSVP
       FTid                : 1
       Tie-Breaking Policy : None                  Metric Type  : None
       Bfd Cap             : None                  
       Reopt               : Disabled              Reopt Freq   : -              
       Inter-area Reopt    : Disabled 
       Auto BW             : Disabled              Threshold    : 0 percent
       Current Collected BW: 0 kbps                Auto BW Freq : 0
       Min BW              : 0 kbps                Max BW       : 0 kbps
       Offload             : Disabled              Offload Freq : - 
       Low Value           : -                     High Value   : - 
       Readjust Value      : - 
       Offload Explicit Path Name: 
       Tunnel Group        : -                                              
       Interfaces Protected: -
       Excluded IP Address : -
       Referred LSP Count  : 0  
       Primary Tunnel      : -                     Pri Tunn Sum : -              
       Backup Tunnel       : -                                                    
       Group Status        : Up                    Oam Status   : -             
       IPTN InLabel        : -                     Tunnel BFD Status : -                               
       BackUp LSP Type     : Hot-Standby           BestEffort   : Enabled
       Secondary HopLimit  : -
       BestEffort HopLimit  : -
       Secondary Explicit Path Name: -
       Secondary Affinity Prop/Mask: 0x0/0x0
       BestEffort Affinity Prop/Mask: 0x0/0x0  
       IsConfigLspConstraint: -
       Hot-Standby Revertive Mode:  Revertive
       Hot-Standby Overlap-path:  Disabled
       Hot-Standby Switch State:  CLEAR
       Bit Error Detection:  Disabled
       Bit Error Detection Switch Threshold:  -
       Bit Error Detection Resume Threshold:  -
       Ip-Prefix Name    : -
       P2p-Template Name : -
       PCE Delegate      : No                    LSP Control Status : Local control
       Path Verification : -
       Entropy Label     : None 
       Auto BW Remain Time : 200 s               Reopt Remain Time  : 100 s
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : - 
       Self-Ping         : Disable               Self-Ping Duration : 1800 sec
       FRR Attr Source   : -                     Is FRR degrade down : No
   
       Primary LSP ID      : 1.1.1.1:19
       LSP State           : UP                    LSP Type     : Primary
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 10000           CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 10000           CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : pri-path                         Hop Limit: -
       Record Route        : Disabled              Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled 
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : EXPLICIT
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   
       Backup LSP ID       : 1.1.1.1:46945
       IsBestEffortPath    : No
       LSP State           : UP                    LSP Type     : Hot-Standby
       Setup Priority      : 7                     Hold Priority: 7
       IncludeAll          : 0x0
       IncludeAny          : 0x0
       ExcludeAny          : 0x0
       Affinity Prop/Mask  : 0x0/0x0               Resv Style   :  SE
       Configured Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Actual Bandwidth Information:
       CT0 Bandwidth(Kbit/sec): 0               CT1 Bandwidth(Kbit/sec): 0
       CT2 Bandwidth(Kbit/sec): 0               CT3 Bandwidth(Kbit/sec): 0
       CT4 Bandwidth(Kbit/sec): 0               CT5 Bandwidth(Kbit/sec): 0
       CT6 Bandwidth(Kbit/sec): 0               CT7 Bandwidth(Kbit/sec): 0
       Explicit Path Name  : -                                Hop Limit: -
       Record Route        : Enabled               Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled
       Reroute Flag        : Enabled
       Pce Flag            : Normal
       Path Setup Type     : CSPF
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   ```
5. Configure a bypass CR-LSP on LSRB that functions as the PLR.
   
   
   
   # Configure an explicit path for the bypass CR-LSP.
   
   ```
   [~LSRB] explicit-path by-path
   ```
   ```
   [*LSRB-explicit-path-by-path] next hop 10.32.1.2
   ```
   ```
   [*LSRB-explicit-path-by-path] next hop 10.33.1.2
   ```
   ```
   [*LSRB-explicit-path-by-path] next hop 3.3.3.3
   ```
   ```
   [*LSRB-explicit-path-by-path] quit
   ```
   
   # Configure the bypass CR-LSP.
   
   ```
   [*LSRB] interface tunnel 3
   ```
   ```
   [*LSRB-Tunnel3] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRB-Tunnel3] tunnel-protocol mpls te
   ```
   ```
   [*LSRB-Tunnel3] destination 3.3.3.3
   ```
   ```
   [*LSRB-Tunnel3] mpls te tunnel-id 2
   ```
   ```
   [*LSRB-Tunnel3] mpls te path explicit-path by-path
   ```
   ```
   [*LSRB-Tunnel3] mpls te bypass-tunnel
   ```
   
   # Bind the bypass CR-LSP to the interface of the protected link.
   
   ```
   [*LSRB-Tunnel3] mpls te protected-interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRB-Tunnel3] commit
   ```
   ```
   [~LSRB-Tunnel3] quit
   ```
   
   After completing the configuration, run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) command on LSRB. The tunnel named **Tunnel3** is **Up**.
   
   Run the [**display mpls te tunnel name Tunnel1 verbose**](cmdqueryname=display+mpls+te+tunnel+name+Tunnel1+verbose) command on LSRB. The bypass tunnel is bound to the outbound interface GE 0/2/0 and is not in use.
   
   ```
   [~LSRB] display mpls te tunnel name Tunnel1 verbose
   ```
   ```
       No                      :  1
       Tunnel-Name             :  Tunnel1
       Tunnel Interface Name   :  Tunnel1
       TunnelIndex             :  - 
       Session ID              :  1           LSP ID            :  95
       Lsr Role                :  Transit
       Ingress LSR ID          :  1.1.1.1
       Egress LSR ID           :  4.4.4.4
       In-Interface            :  GE0/1/0
       Out-Interface           :  GE0/2/0
       Sign-Protocol           :  RSVP TE     Resv Style        :  SE
       IncludeAnyAff           :  0x0         ExcludeAnyAff     :  0x0
       IncludeAllAff           :  0x0  
       ER-Hop Table Index      :  -           AR-Hop Table Index:  -
       C-Hop Table Index       :  -
       PrevTunnelIndexInSession:  -           NextTunnelIndexInSession:  -
       PSB Handle              :  -
       Created Time            :  2012/02/01 04:53:22
       --------------------------------
                 DS-TE Information
       --------------------------------
       Bandwidth Reserved Flag :  Reserved
       CT0 Bandwidth(Kbit/sec) :  10000       CT1 Bandwidth(Kbit/sec):  0
       CT2 Bandwidth(Kbit/sec) :  0           CT3 Bandwidth(Kbit/sec):  0
       CT4 Bandwidth(Kbit/sec) :  0           CT5 Bandwidth(Kbit/sec):  0
       CT6 Bandwidth(Kbit/sec) :  0           CT7 Bandwidth(Kbit/sec):  0
       Setup-Priority          :  7           Hold-Priority          :  7
       --------------------------------
                   FRR Information
       --------------------------------
       Primary LSP Info
       Bypass In Use           :  Not Used
       Bypass Tunnel Id        :  1
       BypassTunnel          :  Tunnel Index[Tunnel3], InnerLabel[16]
       Bypass Lsp ID           :  8           FrrNextHop        :  10.33.1.1
       ReferAutoBypassHandle   :  -
       FrrPrevTunnelTableIndex :  -           FrrNextTunnelTableIndex:  -
       Bypass Attribute
       Setup Priority          :  7           Hold Priority     :  7
       HopLimit                :  32          Bandwidth         :  0
       IncludeAnyGroup         :  0           ExcludeAnyGroup   :  0
       IncludeAllGroup         :  0
       Bypass Unbound Bandwidth Info(Kbit/sec)
       CT0 Unbound Bandwidth   :  -         CT1 Unbound Bandwidth:  -
       CT2 Unbound Bandwidth   :  -         CT3 Unbound Bandwidth:  -
       CT4 Unbound Bandwidth   :  -         CT5 Unbound Bandwidth:  -
       CT6 Unbound Bandwidth   :  -         CT7 Unbound Bandwidth:  -
       --------------------------------
                  BFD Information
       --------------------------------
       NextSessionTunnelIndex  :  -           PrevSessionTunnelIndex:  -
       NextLspId               :  -           PrevLspId         :  - 
   ```
6. Verify the configuration.
   
   
   
   # Shut down the outbound interface of the protected link on the PLR.
   
   ```
   [~LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] shutdown
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] commit
   ```
   
   Run the [**display interface tunnel 1**](cmdqueryname=display+interface+tunnel+1) command on LSRA. The tunnel interface of the primary CR-LSP is still **Up**.
   
   Run the [**tracert lsp te tunnel1**](cmdqueryname=tracert+lsp+te+tunnel1) command on LSRA. The path through which the primary CR-LSP passes is displayed.
   
   ```
   [~LSRA] tracert lsp te tunnel1
   ```
   ```
     LSP Trace Route FEC: TE TUNNEL IPV4 SESSION QUERY Tunnel1 , press CTRL_C to break.
   TTL    Replier            Time    Type      Downstream
   0                                 Ingress   10.21.1.2/[25 ]
   1      10.21.1.2          3       Transit   10.32.1.2/[16 16 ]
   2      10.32.1.2          4       Transit   10.33.1.2/[3 ]
   3      10.33.1.2          4       Transit   10.41.1.2/[3 ]
   4      4.4.4.4            3       Egress  
   ```
   
   The preceding command output shows that traffic has switched to the bypass CR-LSP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command is run immediately after FRR switching has been performed, two CR-LSPs are both Up. This is because FRR uses the make-before-break mechanism to establish a bypass CR-LSP. The original CR-LSP will be deleted after a new CR-LSP has been established.
   
   Run the [**display mpls te tunnel name Tunnel1 verbose**](cmdqueryname=display+mpls+te+tunnel+name+Tunnel1+verbose) command on LSRB. The bypass CR-LSP is being used.
   
   ```
   [~LSRB] display mpls te tunnel name Tunnel1 verbose
   ```
   ```
       No                      :  1
       Tunnel-Name             :  Tunnel1
       Tunnel Interface Name   :  Tunnel1
       TunnelIndex             :  - 
       Session ID              :  1           LSP ID            :  95
       Lsr Role                :  Transit
       Ingress LSR ID          :  1.1.1.1
       Egress LSR ID           :  4.4.4.4
       In-Interface            :  GE0/1/0
       Out-Interface           :  GE0/2/0
       Sign-Protocol           :  RSVP TE     Resv Style        :  SE
       IncludeAnyAff           :  0x0         ExcludeAnyAff     :  0x0
       IncludeAllAff           :  0x0  
       ER-Hop Table Index      :  -           AR-Hop Table Index:  -
       C-Hop Table Index       :  -
       PrevTunnelIndexInSession:  -           NextTunnelIndexInSession:  -
       PSB Handle              :  -
       Created Time            :  2012/02/01 04:53:22
       --------------------------------
                 DS-TE Information
       --------------------------------
       Bandwidth Reserved Flag :  Reserved
       CT0 Bandwidth(Kbit/sec) :  10000       CT1 Bandwidth(Kbit/sec):  0
       CT2 Bandwidth(Kbit/sec) :  0           CT3 Bandwidth(Kbit/sec):  0
       CT4 Bandwidth(Kbit/sec) :  0           CT5 Bandwidth(Kbit/sec):  0
       CT6 Bandwidth(Kbit/sec) :  0           CT7 Bandwidth(Kbit/sec):  0
       Setup-Priority          :  7           Hold-Priority          :  7
       --------------------------------
                   FRR Information
       --------------------------------
       Primary LSP Info
       Bypass In Use           :  In Use
       Bypass Tunnel Id        :  1
       BypassTunnel            :  Tunnel Index[Tunnel3], InnerLabel[16]
       Bypass Lsp ID           :  8           FrrNextHop        :  3.3.3.3
       ReferAutoBypassHandle   :  -
       FrrPrevTunnelTableIndex :  -           FrrNextTunnelTableIndex:  -
       Bypass Attribute
       Setup Priority          :  7           Hold Priority     :  7
       HopLimit                :  32          Bandwidth         :  0
       IncludeAnyGroup         :  0           ExcludeAnyGroup   :  0
       IncludeAllGroup         :  0
       Bypass Unbound Bandwidth Info(Kbit/sec)
       CT0 Unbound Bandwidth   :  -         CT1 Unbound Bandwidth:  -
       CT2 Unbound Bandwidth   :  -         CT3 Unbound Bandwidth:  -
       CT4 Unbound Bandwidth   :  -         CT5 Unbound Bandwidth:  -
       CT6 Unbound Bandwidth   :  -         CT7 Unbound Bandwidth:  -
       --------------------------------
                  BFD Information
       --------------------------------
       NextSessionTunnelIndex  :  -           PrevSessionTunnelIndex:  -
       NextLspId               :  -           PrevLspId         :  - 
   ```
   
   # Start the outbound interface of the protected link on the PLR.
   
   ```
   [~LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] commit
   ```
   
   Run the [**display interface tunnel1**](cmdqueryname=display+interface+tunnel1) command on LSRA. The tunnel interface of the primary CR-LSP is **UP**.
   
   After specified period of time elapses, run the [**display mpls te tunnel name tunnel1 verbose**](cmdqueryname=display+mpls+te+tunnel+name+tunnel1+verbose) command on LSRB. Tunnel1's **Bypass In Use** status is **Not Used**, indicating that traffic has switched back to GE 0/2/0.

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  ```
  ```
  sysname LSRA
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te cspf
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  explicit-path pri-path
  ```
  ```
   next hop 10.21.1.2
  ```
  ```
   next hop 10.31.1.2
  ```
  ```
   next hop 10.41.1.2
  ```
  ```
   next hop 4.4.4.4
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-2
  ```
  ```
   network-entity 00.0005.0000.0000.0001.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.21.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Tunnel1
  ```
  ```
   ip address unnumbered interface LoopBack1
  ```
  ```
   tunnel-protocol mpls te
  ```
  ```
   destination 4.4.4.4
  ```
  ```
   mpls te tunnel-id 1
  ```
  ```
   mpls te record-route label
  ```
  ```
   mpls te path explicit-path pri-path
  ```
  ```
   mpls te fast-reroute
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRB configuration file
  
  ```
  #
  ```
  ```
  sysname LSRB
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te cspf
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  explicit-path by-path
  ```
  ```
   next hop 10.32.1.2
  ```
  ```
   next hop 10.33.1.2
  ```
  ```
   next hop 3.3.3.3
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-2
  ```
  ```
   network-entity 00.0005.0000.0000.0002.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.21.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.31.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.32.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  interface Tunnel3
  ```
  ```
   ip address unnumbered interface LoopBack1
  ```
  ```
   tunnel-protocol mpls te
  ```
  ```
   destination 3.3.3.3
  ```
  ```
   mpls te tunnel-id 2
  ```
  ```
   mpls te record-route
  ```
  ```
   mpls te path explicit-path by-path
  ```
  ```
   mpls te bypass-tunnel
  ```
  ```
   mpls te protected-interface GigabitEthernet 0/2/0
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRC configuration file
  
  ```
  #
  ```
  ```
  sysname LSRC
  ```
  ```
  #
  ```
  ```
   mpls lsr-id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-2
  ```
  ```
   network-entity 00.0005.0000.0000.0003.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.41.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.31.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.33.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRD configuration file
  
  ```
  #
  ```
  ```
  sysname LSRD
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-2
  ```
  ```
   network-entity 00.0005.0000.0000.0004.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.41.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 4.4.4.4 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```
* LSRE configuration file
  
  ```
  #
  ```
  ```
  sysname LSRE
  ```
  ```
  #
  ```
  ```
  mpls lsr-id 5.5.5.5
  ```
  ```
  #
  ```
  ```
  mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-2
  ```
  ```
   network-entity 00.0005.0000.0000.0005.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.32.1.2 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.33.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   isis enable 1
  ```
  ```
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  interface LoopBack1
  ```
  ```
   ip address 5.5.5.5 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
  #
  ```
  ```
  return
  ```