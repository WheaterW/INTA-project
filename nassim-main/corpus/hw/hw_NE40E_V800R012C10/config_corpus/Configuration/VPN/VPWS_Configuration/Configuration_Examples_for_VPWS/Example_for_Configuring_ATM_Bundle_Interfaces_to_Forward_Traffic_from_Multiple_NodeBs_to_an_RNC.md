Example for Configuring ATM Bundle Interfaces to Forward Traffic from Multiple NodeBs to an RNC
===============================================================================================

An ATM bundle interface transmits a single type of service from multiple TDM/ATM NodeBs along one PW to an RNC. This relieves the burden on a CSG and allows greater service scalability.

#### Networking Requirements

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section does not apply to the M2K or M2K-B models.

ATM bundling is an extended PWE3 application for transparently transmitting ATM cells. An ATM bundle interface allows various NodeBs to share one PW to transmit a single type of service to an RNC.

On an IP RAN, multiple NodeBs are connected to a CSG through serial interfaces channelized from E1, CE1, or CPOS links. Every NodeB can transmit voice, video, and data services. Therefore, the CSG must create three PVCs for every NodeB before transmitting voice, video, and data services. An increase in the number of NodeBs and service types increases the load on the CSG. An ATM bundle interface forwards a single type of service from multiple NodeBs to an RNC along one PW. This reduces the number of PWs, relieves the load on the CSG, and improves service scalability.

On the network shown in [Figure 1](#EN-US_TASK_0172369978__fig_dc_vrp_vpws_cfg_601101), NodeB1 and NodeB2 connect to a CSG through serial links. Each NodeB transmits both voice and data services. It is required that two PWs, PW1 and PW2, be set up between the CSG and RSG to transmit the services separately. ATM bundle 1 and ATM bundle 2 are created on the CSG, and PW1 and PW2 are configured on each of the ATM bundle interfaces. The PVC configured to transmit voice services joins ATM bundle 1, and the other PVC configured to transmit data services joins ATM bundle 2. This allows multiple NodeBs to share the same PW to transmit the same type of service to an RNC. [Figure 1](#EN-US_TASK_0172369978__fig_dc_vrp_vpws_cfg_601101) describes the mapping relationships between interfaces and services.

**Table 1** Mapping relationships between interfaces and services
| NodeB | CSG Sub-interface | Service Type | PVC Configuration (VPI/VCI Values) | ATM Bundle ID |
| --- | --- | --- | --- | --- |
| NodeB1 | Serial0/2/0:0.1 | Voice | 1/33 | ATM Bundle 1 |
| Serial0/2/0:0.2 | Data | 2/33 | ATM Bundle 2 |
| NodeB2 | Serial0/2/1:0.1 | Voice | 3/33 | ATM Bundle 1 |
| Serial0/2/1:0.2 | Data | 4/33 | ATM Bundle 2 |


**Figure 1** Networking diagram for configuring ATM bundle interfaces to forward traffic from multiple NodeBs to an RNC![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1 represents GE0/1/0.

  
![](images/fig_dc_vrp_vpws_cfg_601101.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to and configure a routing protocol on each interface.
2. Configure basic MPLS functions and TE tunnels:
   
   * Enable MPLS TE, RSVP-TE, OSPF TE, and CSPF.
   * Configure MPLS TE tunnel interfaces.
   * Configure a tunnel policy.
3. Configure ATM bundle interfaces:
   
   * Configure ATM bundle interfaces.
   * Add AC sub-interfaces connecting the CSG to NodeBs to ATM bundle interfaces.
4. Configure PWE3:
   
   * Configure a remote LDP session between the CSG and RSG.
   * Enable L2VPN and configure PWE3.

#### Data Preparation

To complete the configuration, you need the following data:

* Interface number, interface IP address, and OSPF process ID
* LSR ID, VC ID, and VC type
* ATM bundle interface number and PVC VPI/VCI values

#### Procedure

1. Assign an IP address to and configure a routing protocol on each interface.
   1. Assign an IP address to each interface.
   2. Configure a routing protocol on the CSG and RSG to establish connectivity. OSPF is used in this example.
   
   
   
   After completing the preceding configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on CSG and RSG. Both have learned routes from each other. Note that when configuring OSPF, advertise 32-bit loopback interface addresses (LSR IDs) of the CSG and RSG.
   
   The configuration procedure is not provided.
2. Configure basic MPLS functions and TE tunnels.
   1. Enable MPLS TE, RSVP-TE, OSPF TE, and CSPF.
      
      
      
      # Configure the CSG.
      
      ```
      [~CSG] mpls lsr-id 1.1.1.1
      ```
      ```
      [*CSG] mpls
      ```
      ```
      [*CSG-mpls] mpls te
      ```
      ```
      [*CSG-mpls] mpls rsvp-te
      ```
      ```
      [*CSG-mpls] mpls te cspf
      ```
      ```
      [*CSG-mpls] quit
      ```
      ```
      [*CSG] interface gigabitethernet 0/1/0
      ```
      ```
      [*CSG-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*CSG-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*CSG-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*CSG-GigabitEthernet0/1/0] quit
      ```
      ```
      [*CSG] ospf 100
      ```
      ```
      [*CSG-ospf-100] opaque-capability enable
      ```
      ```
      [*CSG-ospf-100] area 0
      ```
      ```
      [*CSG-ospf-100-area-0.0.0.0] mpls-te enable
      ```
      ```
      [*CSG-ospf-100-area-0.0.0.0] quit
      ```
      ```
      [*CSG-ospf-100] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] mpls lsr-id 2.2.2.2
      ```
      ```
      [*RSG] mpls
      ```
      ```
      [*RSG-mpls] label advertise non-null
      ```
      ```
      [*RSG-mpls] mpls te
      ```
      ```
      [*RSG-mpls] mpls rsvp-te
      ```
      ```
      [*RSG-mpls] mpls te cspf
      ```
      ```
      [*RSG-mpls] quit
      ```
      ```
      [*RSG] interface gigabitethernet 0/1/0
      ```
      ```
      [*RSG-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*RSG-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*RSG-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*RSG-GigabitEthernet0/1/0] quit
      ```
      ```
      [*RSG] ospf 100
      ```
      ```
      [*RSG-ospf-100] opaque-capability enable
      ```
      ```
      [*RSG-ospf-100] area 0
      ```
      ```
      [*RSG-ospf-100-area-0.0.0.0] mpls-te enable
      ```
      ```
      [*RSG-ospf-100-area-0.0.0.0] quit
      ```
      ```
      [*RSG-ospf-100] quit
      ```
      ```
      [*RSG] commit
      ```
   2. Configure an MPLS TE tunnel interface.
      
      
      
      # Configure the CSG.
      
      ```
      [~CSG] interface Tunnel11
      ```
      ```
      [*CSG-Tunnel11] ip address unnumbered interface loopback 1
      ```
      ```
      [*CSG-Tunnel11] tunnel-protocol mpls te
      ```
      ```
      [*CSG-Tunnel11] destination 2.2.2.2
      ```
      ```
      [*CSG-Tunnel11] mpls te tunnel-id 100
      ```
      ```
      [*CSG-Tunnel11] mpls te signal-protocol rsvp-te
      ```
      ```
      [*CSG-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*CSG-Tunnel11] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] interface Tunnel11
      ```
      ```
      [*RSG-Tunnel11] ip address unnumbered interface loopback 1
      ```
      ```
      [*RSG-Tunnel11] tunnel-protocol mpls te
      ```
      ```
      [*RSG-Tunnel11] destination 1.1.1.1
      ```
      ```
      [*RSG-Tunnel11] mpls te tunnel-id 100
      ```
      ```
      [*RSG-Tunnel11] mpls te signal-protocol rsvp-te
      ```
      ```
      [*RSG-Tunnel11] mpls te reserved-for-binding
      ```
      ```
      [*RSG-Tunnel11] quit
      ```
      ```
      [*RSG] commit
      ```
   3. Configure a tunnel policy.
      
      
      
      # Configure the CSG.
      
      ```
      [~CSG] tunnel-policy policy1
      ```
      ```
      [*CSG-tunnel-policy-policy1] tunnel binding destination 2.2.2.2 te Tunnel11
      ```
      ```
      [*CSG-tunnel-policy-policy1] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [*RSG] tunnel-policy policy1
      ```
      ```
      [*RSG-tunnel-policy-policy1] tunnel binding destination 1.1.1.1 te Tunnel11
      ```
      ```
      [*RSG-tunnel-policy-policy1] quit
      ```
      ```
      [*RSG] commit
      ```
3. Configure ATM bundling.
   1. Create ATM bundle interfaces.
      
      
      
      # Create two ATM bundle interfaces on the CSG.
      
      ```
      [~CSG] interface atm-bundle 1
      ```
      ```
      [*CSG-Atm-Bundle1] quit
      ```
      ```
      [*CSG] interface atm-bundle 2
      ```
      ```
      [*CSG-Atm-Bundle2] quit
      ```
      ```
      [*CSG] commit
      ```
   2. Add AC sub-interfaces connecting the CSG to NodeBs to the ATM bundle interfaces.
      
      
      
      # Add AC sub-interfaces connecting the CSG to NodeB1 to both ATM bundle interfaces.
      
      ```
      [~CSG] interface serial0/2/0:0
      ```
      ```
      [*CSG-Serial0/2/0:0] link-protocol atm
      ```
      ```
      [*CSG-Serial0/2/0:0] undo shutdown
      ```
      ```
      [*CSG-Serial0/2/0:0] quit
      ```
      ```
      [*CSG] interface serial0/2/0:0.1
      ```
      ```
      [*CSG-Serial0/2/0:0.1] pvc 1/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/0:0.1-1/33] quit
      ```
      ```
      [*CSG-Serial0/2/0:0.1] atm-bundle 1
      ```
      ```
      [*CSG-Serial0/2/0:0.1] quit
      ```
      ```
      [*CSG] interface serial0/2/0:0.2
      ```
      ```
      [*CSG-Serial0/2/0:0.2] pvc 2/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/0:0.2-2/33] quit
      ```
      ```
      [*CSG-Serial0/2/0:0.2] atm-bundle 2
      ```
      ```
      [*CSG-Serial0/2/0:0.2] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Add AC sub-interfaces connecting the CSG to NodeB2 to both ATM bundle interfaces.
      
      ```
      [~CSG] interface serial0/2/1:0
      ```
      ```
      [*CSG-Serial0/2/1:0] link-protocol atm
      ```
      ```
      [*CSG-Serial0/2/1:0] undo shutdown
      ```
      ```
      [*CSG-Serial0/2/1:0] quit
      ```
      ```
      [*CSG] interface serial0/2/1:0.1
      ```
      ```
      [*CSG-Serial0/2/1:0.1] pvc 3/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/1:0.1-3/33] quit
      ```
      ```
      [*CSG-Serial0/2/1:0.1] atm-bundle 1
      ```
      ```
      [*CSG-Serial0/2/1:0.1] quit
      ```
      ```
      [*CSG] interface serial0/2/1:0.2
      ```
      ```
      [*CSG-Serial0/2/1:0.2] pvc 4/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/1:0.2-4/33] quit
      ```
      ```
      [*CSG-Serial0/2/1:0.2] atm-bundle 2
      ```
      ```
      [*CSG-Serial0/2/1:0.2] quit
      ```
      ```
      [*CSG] commit
      ```
4. Configure PWE3.
   1. Configure a remote MPLS LDP session between the CSG and RSG.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      In this example, TE tunnels are configured between the CSG and RSG, and MPLS LDP is not required. PWE3 uses extended LDP signaling to distribute VPN labels. Therefore, a remote MPLS LDP session has to be configured between the CSG and RSG.
      
      # Configure the CSG.
      
      ```
      [~CSG] mpls ldp
      ```
      ```
      [*CSG-mpls-ldp] quit
      ```
      ```
      [*CSG] mpls ldp remote-peer 2.2.2.2
      ```
      ```
      [*CSG-mpls-ldp-remote-2.2.2.2] remote-ip 2.2.2.2
      ```
      ```
      [*CSG-mpls-ldp-remote-2.2.2.2] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure the RSG.
      
      ```
      [~RSG] mpls ldp
      ```
      ```
      [*RSG-mpls-ldp] quit
      ```
      ```
      [*RSG] mpls ldp remote-peer 1.1.1.1
      ```
      ```
      [*RSG-mpls-ldp-remote-1.1.1.1] remote-ip 1.1.1.1
      ```
      ```
      [*RSG-mpls-ldp-remote-1.1.1.1] quit
      ```
      ```
      [*RSG] commit
      ```
      
      # Verify the configuration. # Run the **display mpls ldp session all** command on the CSG and RSG to check whether the LDP session is in the **Operational** state. The following example uses the command output on the CSG.
      
      ```
      [~CSG] display mpls ldp session all
      ```
      ```
       LDP Session(s) in Public Network
       Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
       An asterisk (*) before a session means the session is being deleted.
       ------------------------------------------------------------------------------
       PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
       ------------------------------------------------------------------------------
       2.2.2.2:0          Operational DU   Passive  0000:00:47  190/190
       3.3.3.3:0          Operational DU   Passive  0000:00:47  190/190
       ------------------------------------------------------------------------------
       TOTAL: 2 session(s) Found.    
      ```
   2. Enable L2VPN and configure PWE3.
      
      
      
      # Configure PWE3 on the ATM bundle interfaces of the CSG.
      
      ```
      [~CSG] mpls l2vpn
      ```
      ```
      [*CSG-l2vpn] quit
      ```
      ```
      [*CSG] interface atm-bundle 1 
      ```
      ```
      [*CSG-Atm-Bundle1] mpls l2vc 2.2.2.2 100 tunnel-policy policy1 control-word
      ```
      ```
      [*CSG-Atm-Bundle1] quit
      ```
      ```
      [*CSG] interface atm-bundle 2 
      ```
      ```
      [*CSG-Atm-Bundle2] mpls l2vc 2.2.2.2 200 tunnel-policy policy1 control-word
      ```
      ```
      [*CSG-Atm-Bundle2] quit
      ```
      ```
      [*CSG] commit
      ```
      
      # Configure PWE3 on the AC sub-interfaces of the RSG.
      
      ```
      [~CSG] interface serial0/2/0:0
      ```
      ```
      [*CSG-Serial0/2/0:0] link-protocol atm
      ```
      ```
      [*CSG-Serial0/2/0:0] undo shutdown
      ```
      ```
      [*CSG-Serial0/2/0:0] quit
      ```
      ```
      [*CSG] interface serial0/2/0:0.1
      ```
      ```
      [*CSG-Serial0/2/0:0.1] pvc 1/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/0:0.1-1/33] quit
      ```
      ```
      [*RSG-Serial-pvc-Serial0/2/0:0.1] mpls l2vc 1.1.1.1 100 tunnel-policy policy1 control-word
      ```
      ```
      [*RSG-Serial-pvc-Serial0/2/0:0.1] quit
      ```
      ```
      [*RSG-Serial0/2/0:0.1] quit
      ```
      ```
      [*CSG] interface serial0/2/0:0.2
      ```
      ```
      [*CSG-Serial0/2/0:0.2] pvc 2/33
      ```
      ```
      [*CSG-Serial-pvc-Serial0/2/0:0.2-2/33] quit
      ```
      ```
      [*RSG-Serial-pvc-Serial0/2/0:0.2] mpls l2vc 1.1.1.1 200 tunnel-policy policy1 control-word
      ```
      ```
      [*RSG-Serial-pvc-Serial0/2/0:0.2] quit
      ```
      ```
      [*RSG-Serial0/2/0:0.2] quit
      ```
      ```
      [*RSG] commit
      ```
5. Verify the configuration.
   
   
   
   Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) command on the CSG and RSG. Both PWs are **Up**.
   
   # Display PW information on ATM bundle 1.
   
   ```
   <CSG> display mpls l2vc interface atm-bundle 1
   ```
   ```
    *client interface       : Atm-Bundle1 is up
     Administrator PW       : no
     session state          : up
     AC status               : up
     VC state               : up
     Label state            : 0
     Token state            : 0
     VC ID                  : 100
     VC type                : ATM Nto1 VCC
     destination            : 2.2.2.2
     local group ID         : 0            remote group ID      : 0
     local VC label         : 1025         remote VC label      : 1028
     max ATM cells          : 28
     ATM pack overtime      : 1000
     seq-number             : disable
     local AC OAM State     : up
     local PSN State        : up
     local forwarding state : forwarding
     local status code      : 0x0
     remote AC OAM state    : up
     remote PSN state       : up
     remote forwarding state: forwarding
     remote status code     : 0x0
     ignore standby state   : no
     BFD for PW             : unavailable
     VCCV State             : up
     manual fault           : not set
     active state           : active
     forwarding entry       : exist
     link state             : up
     local VC MTU           : 1500         remote VC MTU        : 1500
     local VCCV             : cw alert ttl lsp-ping bfd
     remote VCCV            : cw alert ttl lsp-ping bfd
     local control word     : enable       remote control word  : enable
     tunnel policy name     : policy1
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     Switchover Flag        : false
     VC tunnel/token info   : 1 tunnels/tokens
       NO.0  TNL type       : cr lsp, TNL ID : 0x800001
       Backup TNL type      : lsp   , TNL ID : 0x0
     create time            : 0 days, 1 hours, 0 minutes, 5 seconds
     up time                : 0 days, 1 hours, 0 minutes, 5 seconds
     last change time       : 0 days, 1 hours, 0 minutes, 5 seconds
     VC last up time        : 2010/11/10 11:16:04
     VC total up time       : 0 days, 1 hours, 0 minutes, 5 seconds
     CKey                   : 4
     NKey                   : 3
     PW redundancy mode     : frr
     AdminPw interface      : --
     AdminPw link state     : --   
     Forward state          : send inactive, receive inactive 
   
   ```
   
   # Display PW information on ATM bundle 2.
   
   ```
   <CSG> display mpls l2vc interface atm-bundle 2
   ```
   ```
    *client interface       : Atm-Bundle2 is up
     Administrator PW       : no
     session state          : up
     AC status               : up
     VC state               : up
     Label state            : 0
     Token state            : 0
     VC ID                  : 100
     VC type                : ATM Nto1 VCC
     destination            : 2.2.2.2
     local group ID         : 0            remote group ID      : 0
     local VC label         : 1027         remote VC label      : 1032
     max ATM cells          : 28
     ATM pack overtime      : 1000
     seq-number             : disable
     local AC OAM State     : up
     local PSN State        : up
     local forwarding state : forwarding
     local status code      : 0x0
     remote AC OAM state    : up
     remote PSN state       : up
     remote forwarding state: forwarding
     remote status code     : 0x0
     ignore standby state   : no
     BFD for PW             : unavailable
     VCCV State             : up
     manual fault           : not set
     active state           : active
     forwarding entry       : exist
     link state             : up
     local VC MTU           : 1500         remote VC MTU        : 1500
     local VCCV             : cw alert ttl lsp-ping bfd
     remote VCCV            : cw alert ttl lsp-ping bfd
     local control word     : enable       remote control word  : enable
     tunnel policy name     : policy1
     traffic behavior name  : --
     PW template name       : --
     primary or secondary   : primary
     Switchover Flag        : false
     VC tunnel/token info   : 1 tunnels/tokens
       NO.0  TNL type       : cr lsp, TNL ID : 0x800001
       Backup TNL type      : lsp   , TNL ID : 0x0
     create time            : 0 days, 1 hours, 0 minutes, 5 seconds
     up time                : 0 days, 1 hours, 0 minutes, 5 seconds
     last change time       : 0 days, 1 hours, 0 minutes, 5 seconds
     VC last up time        : 2010/11/10 11:16:04
     VC total up time       : 0 days, 1 hours, 0 minutes, 5 seconds
     CKey                   : 4
     NKey                   : 3
     PW redundancy mode     : frr
     AdminPw interface      : --
     AdminPw link state     : --   
     Forward state          : send inactive, receive inactive 
   
   ```

#### Configuration Files

* Configuration file of the CSG
  
  ```
  #
  sysname CSG
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  mpls l2vpn
  #
  mpls ldp
  #
  #
  mpls ldp remote-peer 2.2.2.2
   remote-ip 2.2.2.2
  #
  interface Atm-Bundle1
   mpls l2vc 2.2.2.2 100 tunnel-policy policy1 control-word
  #
  interface Atm-Bundle2
   mpls l2vc 2.2.2.2 200 tunnel-policy policy1 control-word
  #
  interface Serial0/2/0:0
   link-protocol atm
   undo shutdown
  #
  interface Serial0/2/0:0.1
   pvc 1/33
   atm-bundle 1
  #
  interface Serial0/2/0:0.2
   pvc 2/33
   atm-bundle 2
  #
  interface Serial0/2/1:0
   link-protocol atm
   undo shutdown
  #
  interface Serial0/2/1:0.1
   pvc 3/33
   atm-bundle 1
  #
  interface Serial0/2/1:0.2
   pvc 4/33
   atm-bundle 2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.1.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te tunnel-id 100
   mpls te signal-protocol rsvp-te
   mpls te reserved-for-binding
  #
  ospf 100
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.0.1.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy policy1
   tunnel binding destination 2.2.2.2 te Tunnel11
  #
  return 
  ```
* Configuration file of the RSG
  
  ```
  #
  sysname RSG
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   label advertise non-null
   mpls rsvp-te
   mpls te cspf
  #
  mpls l2vpn
  #
  mpls ldp
  #
  mpls ldp remote-peer 1.1.1.1
   remote-ip 1.1.1.1
  #
  interface Serial0/2/0:0
   link-protocol atm
   undo shutdown
  #
  interface Serial0/2/0:0.1
   pvc 1/33
   mpls l2vc 1.1.1.1 100 tunnel-policy policy1 control-word
  #
  interface Serial0/2/0:0.2
   pvc 2/33
   mpls l2vc 1.1.1.1 200 tunnel-policy policy1 control-word
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.0.1.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te tunnel-id 100
   mpls te signal-protocol rsvp-te
   mpls te reserved-for-binding
  #
  ospf 100
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.0.1.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy policy1
   tunnel binding destination 1.1.1.1 te Tunnel11
  #
  return 
  ```