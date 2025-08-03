Example for Configuring E-STP Using Inter-AS PWs in LDP Mode
============================================================

To implement E-STP using inter-AS PWs in LDP mode, configure service VSIs and mVSIs on inter-AS and intra-AS NPEs and enable STP for mPWs.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363676__fig_dc_vrp_mstp_cfg_005201), inter-AS PWs in LDP mode are used.

* UPE1 is dual-homed to NPE1 and NPE2, and UPE2 is dual-homed to NPE3 and NPE4. Inter-AS redundant links are available.
* HVPLS is used for inter-AS connectivity. For example, UPE1, NPE1, and NPE2 constitute an HVPLS network, and UPE1 is the UPE peer of NPE1.
* Service PWs between NPE1 and NPE3 and between NPE2 and NPE4 are spoke PWs, and therefore split horizon is not applied to the service PWs.

However, a UPE receives two copies of traffic from a remote UPE. To prevent this problem, configure mPWs between inter-AS NPEs and between intra-AS NPEs and enable STP for the mPWs; configure STP priorities and set the path costs of interfaces to allow NPE3 to function as the root bridge and NPE4 as the backup root bridge so that the inter-AS mPW on NPE2 will be blocked, and accordingly the service VSI tracked by the mVSI is blocked as well. As a result, the traffic from CE1 will travel along the path UPE1 -> NPE1 -> NPE3 -> UPE2 to reach CE2, without any duplicate traffic or loops.

**Figure 1** Configuring E-STP using inter-AS PWs in LDP mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 and subinterface3.1 represent GE0/1/0, GE0/2/0, GE0/3/0, and GE 0/3/0.1, respectively.


  
![](images/fig_dc_vrp_mstp_cfg_005201.png)  

| Device | Interface | IP Address | Device | Interface | IP Address |
| --- | --- | --- | --- | --- | --- |
| UPE1 | GE 0/1/0 | 10.1.1.1/24 | UPE2 | GE 0/1/0 | 10.5.1.2/24 |
| GE 0/2/0 | 10.1.2.1/24 | GE 0/2/0 | 10.5.2.2/24 |
| GE 0/3/0.1 | - | GE 0/3/0.1 | - |
| Loopback1 | 1.1.1.1/32 | Loopback1 | 6.6.6.6/32 |
| NPE1 | GE 0/2/0 | 10.3.1.1/24 | NPE2 | GE 0/2/0 | 10.3.1.2/24 |
| GE 0/3/0 | 10.1.1.2/24 | GE 0/3/0 | 10.1.2.2/24 |
| Loopback1 | 2.2.2.2/32 | Loopback1 | 3.3.3.3/32 |
| NPE3 | GE 0/2/0 | 10.4.1.1/24 | NPE4 | GE 0/2/0 | 10.4.1.2/24 |
| GE 0/3/0 | 10.5.1.1/24 | GE 0/3/0 | 10.5.2.1/24 |
| Loopback1 | 4.4.4.4/32 | Loopback1 | 5.5.5.5/32 |
| CE1 | GE 0/1/0.1 | 192.168.1.1/24 | CE2 | GE 0/1/0.1 | 192.168.1.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the VPLS backbone network to allow intra-AS devices to communicate.
2. Configure basic MPLS functions on the VPLS backbone network.
   * Establish a dynamic LDP LSP between the UPE and NPEs in the same AS.
   * Establish a dynamic LDP LSP between the NPEs in the same AS.
   
   Establish remote LDP sessions if the UPE and an NPE or the NPEs are indirectly connected.
3. Establish VPLS connections between the UPE and NPEs in the same AS.
   * Create service VSIs on the UPE and NPEs in the same AS to exchange service packets.
   * Create mVSIs on the NPEs in the same AS to transmit STP packets over the mPW.
   * Create mVSIs and service VSIs on inter-AS NPEs so that mPWs can transmit STP packets and service PWs can transparently transmit service packets. Configure service VSIs to track the mVSIs.
4. Enable STP for the inter-AS and intra-AS mPWs.
   
   Configure STP priorities and set the path costs of interfaces to allow NPE3 to function as the root bridge and NPE4 as the backup root bridge so that the inter-AS PWs between NPE2 and NPE4 are blocked.

#### Data Preparation

To complete the configuration, you need the following data:

* Data required for configuring OSPF: IP address of each interface, OSPF process ID, and OSPF area ID
* Peer IP addresses
* MPLS LSR IDs of the UPEs and NPEs
* VSI IDs
* STP priorities and interfaces' path costs

#### Procedure

1. Configure IP addresses for interfaces on the backbone network. For configuration details, see Configuration Files.
2. Configure an IGP on the VPLS backbone network.
   
   
   
   When configuring OSPF, configure PE1, PE2, and PE3 to advertise their 32-bit IP addresses (used as LSR IDs) of loopback interfaces.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172363676__example_01).
3. Configure MPLS and establish LDP LSPs.
   
   
   
   Configure basic MPLS functions on the backbone network and set up a dynamic LDP LSP between the UPE and NPEs in the same AS.
   
   After the configuration is complete, the UPE and NPEs in the same AS have established LDP LSPs.
   
   The following example uses the command output on UPE1:
   
   ```
   [~UPE1] display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    ------------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    ------------------------------------------------------------------------------
    2.2.2.2:0          Operational DU   Passive   000:00:08   41/41
    3.3.3.3:0          Operational DU   Passive   000:00:08   40/40
    ------------------------------------------------------------------------------
    TOTAL: 2 session(s) Found.
   ```
4. Enable MPLS L2VPN on the UPEs and NPEs.
   
   
   
   # Configure UPE1.
   
   ```
   [~UPE1] mpls l2vpn
   ```
   ```
   [*UPE1-l2vpn] quit
   ```
   ```
   [*UPE1] commit
   ```
   
   # Configure NPE1.
   
   ```
   [~NPE1] mpls l2vpn
   ```
   ```
   [*NPE1-l2vpn] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] mpls l2vpn
   ```
   ```
   [*NPE2-l2vpn] quit
   ```
   ```
   [*NPE2] commit
   ```
   
   Repeat this step for UPE2, NPE3, and NPE4. For configuration details, see [Configuration Files](#EN-US_TASK_0172363676__example_01).
5. Configure VPLS.
   
   
   1. Configure mVSIs on the NPEs and establish mPWs on inter-AS NPEs and intra-AS NPEs.
      
      # Configure NPE1.
      ```
      [~NPE1] vsi m1 static
      ```
      ```
      [*NPE1-vsi-m1] pwsignal ldp
      ```
      ```
      [*NPE1-vsi-m1-ldp] vsi-id 10
      ```
      ```
      [*NPE1-vsi-m1-ldp] peer 3.3.3.3
      ```
      ```
      [*NPE1-vsi-m1-ldp] peer 4.4.4.4
      ```
      ```
      [*NPE1-vsi-m1-ldp] quit
      ```
      ```
      [*NPE1-vsi-m1] admin-vsi
      ```
      ```
      [*NPE1-vsi-m1] quit
      ```
      ```
      [*NPE1] commit
      ```
      
      # Configure NPE2.
      
      ```
      [~NPE2] vsi m1 static
      ```
      ```
      [*NPE2-vsi-m1] pwsignal ldp
      ```
      ```
      [*NPE2-vsi-m1-ldp] vsi-id 10
      ```
      ```
      [*NPE2-vsi-m1-ldp] peer 2.2.2.2
      ```
      ```
      [*NPE2-vsi-m1-ldp] peer 5.5.5.5
      ```
      ```
      [*NPE2-vsi-m1-ldp] quit
      ```
      ```
      [*NPE2-vsi-m1] admin-vsi
      ```
      ```
      [*NPE2-vsi-m1] quit
      ```
      ```
      [*NPE2] commit
      ```
      # Configure NPE3.
      ```
      [~NPE3] vsi m1 static
      ```
      ```
      [*NPE3-vsi-m1] pwsignal ldp
      ```
      ```
      [*NPE3-vsi-m1-ldp] vsi-id 10
      ```
      ```
      [*NPE3-vsi-m1-ldp] peer 2.2.2.2
      ```
      ```
      [*NPE3-vsi-m1-ldp] peer 5.5.5.5
      ```
      ```
      [*NPE3-vsi-m1-ldp] quit
      ```
      ```
      [*NPE3-vsi-m1] admin-vsi
      ```
      ```
      [*NPE3-vsi-m1] quit
      ```
      ```
      [*NPE3] commit
      ```
      
      # Configure NPE4.
      ```
      [~NPE4] vsi m1 static
      ```
      ```
      [*NPE4-vsi-m1] pwsignal ldp
      ```
      ```
      [*NPE4-vsi-m1-ldp] vsi-id 10
      ```
      ```
      [*NPE4-vsi-m1-ldp] peer 3.3.3.3
      ```
      ```
      [*NPE4-vsi-m1-ldp] peer 4.4.4.4
      ```
      ```
      [*NPE4-vsi-m1-ldp] quit
      ```
      ```
      [*NPE4-vsi-m1] admin-vsi
      ```
      ```
      [*NPE4-vsi-m1] quit
      ```
      ```
      [*NPE4] commit
      ```
   2. Configure service VSIs on the UPEs and bind the service VSIs to interfaces. Configure HVPLS on the NPEs and UPE in the same AS, configure LDP peer relationship between inter-AS NPEs, and bind service VSIs to mVSIs on the NPEs.
      
      # Configure UPE1.
      
      ```
      [~UPE1] vsi s1 static
      ```
      ```
      [*UPE1-vsi-s1] pwsignal ldp
      ```
      ```
      [*UPE1-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*UPE1-vsi-s1-ldp] peer 2.2.2.2
      ```
      ```
      [*UPE1-vsi-s1-ldp] peer 3.3.3.3
      ```
      ```
      [*UPE1-vsi-s1-ldp] quit
      ```
      ```
      [*UPE1-vsi-s1] quit
      ```
      ```
      [*UPE1] interface gigabitethernet 0/3/0.1
      ```
      ```
      [*UPE1-GigabitEthernet0/3/0.1] shutdown
      ```
      ```
      [*UPE1-GigabitEthernet0/3/0.1] vlan-type dot1q 10
      ```
      ```
      [*UPE1-GigabitEthernet0/3/0.1] l2 binding vsi s1
      ```
      ```
      [*UPE1-GigabitEthernet0/3/0.1] undo shutdown
      ```
      ```
      [*UPE1-GigabitEthernet0/3/0.1] quit
      ```
      ```
      [*UPE1] commit
      ```
      
      # Configure NPE1.
      
      ```
      [~NPE1] vsi s1 static
      ```
      ```
      [*NPE1-vsi-s1] pwsignal ldp
      ```
      ```
      [*NPE1-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*NPE1-vsi-s1-ldp] peer 1.1.1.1 upe
      ```
      ```
      [*NPE1-vsi-s1-ldp] peer 4.4.4.4
      ```
      ```
      [*NPE1-vsi-s1-ldp] quit
      ```
      ```
      [*NPE1-vsi-s1] track admin-vsi m1
      ```
      ```
      [*NPE1-vsi-s1] quit
      ```
      ```
      [*NPE1] commit
      ```
      
      # Configure NPE2.
      
      ```
      [~NPE2] vsi s1 static
      ```
      ```
      [*NPE2-vsi-s1] pwsignal ldp
      ```
      ```
      [*NPE2-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*NPE2-vsi-s1-ldp] peer 1.1.1.1 upe
      ```
      ```
      [*NPE2-vsi-s1-ldp] peer 5.5.5.5
      ```
      ```
      [*NPE2-vsi-s1-ldp] quit
      ```
      ```
      [*NPE2-vsi-s1] track admin-vsi m1
      ```
      ```
      [*NPE2-vsi-s1] quit
      ```
      ```
      [*NPE2] commit
      ```
      
      # Configure UPE2.
      
      ```
      [~UPE2] vsi s1 static
      ```
      ```
      [*UPE2-vsi-s1] pwsignal ldp
      ```
      ```
      [*UPE2-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*UPE2-vsi-s1-ldp] peer 4.4.4.4
      ```
      ```
      [*UPE2-vsi-s1-ldp] peer 5.5.5.5
      ```
      ```
      [*UPE2-vsi-s1-ldp] quit
      ```
      ```
      [*UPE2-vsi-s1] quit
      ```
      ```
      [*UPE2] interface gigabitethernet 0/3/0.1
      ```
      ```
      [*UPE2-GigabitEthernet0/3/0.1] shutdown
      ```
      ```
      [*UPE2-GigabitEthernet0/3/0.1] vlan-type dot1q 10
      ```
      ```
      [*UPE2-GigabitEthernet0/3/0.1] l2 binding vsi s1
      ```
      ```
      [*UPE2-GigabitEthernet0/3/0.1] undo shutdown
      ```
      ```
      [*UPE2-GigabitEthernet0/3/0.1] quit
      ```
      ```
      [*UPE2] commit
      ```
      
      # Configure NPE3.
      
      ```
      [~NPE3] vsi s1 static
      ```
      ```
      [*NPE3-vsi-s1] pwsignal ldp
      ```
      ```
      [*NPE3-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*NPE3-vsi-s1-ldp] peer 6.6.6.6 upe
      ```
      ```
      [*NPE3-vsi-s1-ldp] peer 2.2.2.2
      ```
      ```
      [*NPE3-vsi-s1-ldp] quit
      ```
      ```
      [*NPE3-vsi-s1] track admin-vsi m1
      ```
      ```
      [*NPE3-vsi-s1] quit
      ```
      ```
      [*NPE3] commit
      ```
      
      # Configure NPE4.
      
      ```
      [~NPE4] vsi s1 static
      ```
      ```
      [*NPE4-vsi-s1] pwsignal ldp
      ```
      ```
      [*NPE4-vsi-s1-ldp] vsi-id 100
      ```
      ```
      [*NPE4-vsi-s1-ldp] peer 6.6.6.6 upe
      ```
      ```
      [*NPE4-vsi-s1-ldp] peer 3.3.3.3
      ```
      ```
      [*NPE4-vsi-s1-ldp] quit
      ```
      ```
      [*NPE4-vsi-s1] track admin-vsi m1
      ```
      ```
      [*NPE4-vsi-s1] quit
      ```
      ```
      [~NPE4] commit
      ```
6. Configure STP.
   
   
   
   Enable STP globally on the NPEs.
   
   # On NPE1, configure MST regions and activate them. This example uses the configuration of NPE1. The configurations of the other three NPEs are similar to that of NPE1.
   
   ```
   [~NPE1] stp region-configuration
   ```
   ```
   [*NPE1-mst-region] region-name RG1
   ```
   ```
   [*NPE1-mst-region] commit
   ```
   ```
   [~NPE1-mst-region] quit
   ```
   ```
   [~NPE1] stp enable
   ```
   ```
   [*NPE1] commit
   ```
   
   # Configure the STP priority 0 for NPE3 in MSTI0.
   
   ```
   [~NPE3] stp instance 0 priority 0
   ```
   ```
   [*NPE3] commit
   ```
   
   # Configure the STP priority 4096 for NPE4 in MSTI0.
   
   ```
   [~NPE4] stp instance 0 priority 4096
   ```
   ```
   [*NPE4] commit
   ```
   
   NPE1 and NPE2 use the default STP priority 32768. Therefore, NPE3 functions as the root bridge, and NPE4 functions as the backup root bridge.
7. Configure E-STP. Enable STP on inter-AS and intra-AS mPWs, and configure the interfaces' path costs in VSIs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To prevent loops in a service VSI, bind the service VSI to the mVSI.
   
   If service VSIs are bound to an mVSI, configure STP for the mVSI but not for the service VSIs. The mVSI status determines the service VSI status.
   
   # Configure NPE1.
   
   ```
   [~NPE1] vsi m1 static
   ```
   ```
   [*NPE1-vsi-m1] pwsignal ldp
   ```
   ```
   [*NPE1-vsi-m1-ldp] peer 3.3.3.3 pw pw1
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw1] stp enable
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw1] stp cost 2
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw1] quit
   ```
   ```
   [*NPE1-vsi-m1-ldp] peer 4.4.4.4 pw pw2
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw2] stp enable
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw2] stp cost 2
   ```
   ```
   [*NPE1-vsi-m1-ldp-pw-pw2] quit
   ```
   ```
   [*NPE1-vsi-m1-ldp] quit
   ```
   ```
   [*NPE1-vsi-m1] quit
   ```
   ```
   [*NPE1] commit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] vsi m1 static
   ```
   ```
   [*NPE2-vsi-m1] pwsignal ldp
   ```
   ```
   [*NPE2-vsi-m1-ldp] peer 2.2.2.2 pw pw1
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw1] stp enable
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw1] stp cost 2
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw1] quit
   ```
   ```
   [*NPE2-vsi-m1-ldp] peer 5.5.5.5 pw pw2
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw2] stp enable
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw2] stp cost 5
   ```
   ```
   [*NPE2-vsi-m1-ldp-pw-pw2] quit
   ```
   ```
   [*NPE2-vsi-m1-ldp] quit
   ```
   ```
   [*NPE2-vsi] quit
   ```
   ```
   [*NPE2] commit
   ```
   
   # Configure NPE3.
   
   ```
   [~NPE3] vsi m1 static
   ```
   ```
   [*NPE3-vsi-m1] pwsignal ldp
   ```
   ```
   [*NPE3-vsi-m1-ldp] peer 5.5.5.5 pw pw1
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw1] stp enable
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw1] stp cost 2
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw1] quit
   ```
   ```
   [*NPE3-vsi-m1-ldp] peer 2.2.2.2 pw pw2
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw2] stp enable
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw2] stp cost 2
   ```
   ```
   [*NPE3-vsi-m1-ldp-pw-pw2] quit
   ```
   ```
   [*NPE3-vsi-m1-ldp] quit
   ```
   ```
   [*NPE3-vsi] quit
   ```
   ```
   [*NPE3] commit
   ```
   
   # Configure NPE4.
   
   ```
   [~NPE4] vsi m1 static
   ```
   ```
   [*NPE4-vsi-m1] pwsignal ldp
   ```
   ```
   [*NPE4-vsi-m1-ldp] peer 4.4.4.4 pw pw1
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw1] stp enable
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw1] stp cost 2
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw1] quit
   ```
   ```
   [*NPE4-vsi-m1-ldp] peer 3.3.3.3 pw pw2
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw2] stp enable
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw2] stp cost 5
   ```
   ```
   [*NPE4-vsi-m1-ldp-pw-pw2] quit
   ```
   ```
   [*NPE4-vsi-m1-ldp] quit
   ```
   ```
   [*NPE4-vsi] quit
   ```
   ```
   [*NPE4] commit
   ```
8. Configure CEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] ip address 192.168.1.1 24
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet 0/1/0.1
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] vlan-type dot1q 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] ip address 192.168.1.2 24
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
9. Verify the configuration.
   
   
   * Run the [**display stp brief**](cmdqueryname=display+stp+brief) command on NPE1 and NPE2 to check STP information.
     
     ```
     [~NPE1] display stp brief
     ```
     ```
      MSTID  Port                        Role  STP State     Protection
         0    m1-pw1                      DESI  FORWARDING      NONE
         0    m1-pw2                      ROOT  FORWARDING      NONE
     ```
     ```
     [~NPE2] display stp brief
     ```
     ```
      MSTID  Port                        Role  STP State     Protection
         0    m1-pw1                       ROOT  FORWARDING      NONE
         0    m1-pw2                       ALTE  DISCARDING      NONE
     ```
     
     The command outputs show that the status of the PW **pw2** between NPE2 and NPE4 is **DISCARDING**.
   * Run the **display vsi name s1 verbose** command on NPE1 and NPE2. The command outputs show that the service VSI **s1** on NPE1 has established a PW with UPE1 and NPE3 and the VSI and PWs are all Up, and the service VSI **s1** on NPE2 has established a PW with UPE1 and NPE4 and the VSI and the PW to UPE1 are Up but the PW to NPE4 is in the Backup state.
     
     | Device | Service VSI Status | Service PW Status |
     | --- | --- | --- |
     | NPE1 | UP | + PW to UPE1: Up + PW to NPE3: Up |
     | NPE2 | UP | + PW to UPE1: Up + PW to NPE4: Backup |
     
     ```
     [~NPE1] display vsi name s1 verbose
     ```
     ```
      ***VSI Name               : s1
         Administrator VSI      : no
         Isolate Spoken         : disable
         VSI Index              : 2
         PW Signaling           : ldp
         Member Discovery Style : static
         Bridge-domain Mode     : disable
         PW MAC Learn Style     : unqualify
         Encapsulation Type     : vlan
         MTU                    : 1500
         Diffserv Mode          : uniform
         Service Class          : --
         Color                  : --
         DomainId               : 255
         Domain Name            :
         Ignore AcState         : disable
         P2P VSI                : disable
         Multicast Fast Switch  : disable
         Create Time            : 0 days, 1 hours, 21 minutes, 42 seconds
         VSI State              : up
         Resource Status        : Valid
     
         VSI ID                 : 100
        *Peer Router ID         : 1.1.1.1
         primary or secondary   : primary
         ignore-standby-state   : no
         VC Label               : 32859
         Peer Type              : dynamic
         Session                : up
         Tunnel ID              : 0x0000000001004c4b41 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : -- 
         CKey                   : 1
         NKey                   : 1862271177
         Stp Enable             : 0
         PwIndex                : 1
         Control Word           : disable
        *Peer Router ID         : 4.4.4.4
         primary or secondary   : primary
         ignore-standby-state   : no
         VC Label               : 32860
         Peer Type              : dynamic
         Session                : up
         Tunnel ID              : 0x0000000001004c4b42 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : -- 
         CKey                   : 2
         NKey                   : 1862271178
         Stp Enable             : 0
         PwIndex                : 2
         Control Word           : disable
      
         Interface Name         : GigabitEthernet0/3/0.1
         State                  : up
         Access Port            : false
         Last Up Time           : 2013/12/27 17:02:19
         Total Up Time          : 0 days, 1 hours, 19 minutes, 38 seconds
     
       **PW Information:
     
        *Peer Ip Address        : 1.1.1.1
         PW State               : up
         Local VC Label         : 32859
         Remote VC Label        : 32890
         Remote Control Word    : disable
         PW Type                : label
         Tunnel ID              : 0x0000000001004c4b41 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : --
         Ckey                   : 1
         Nkey                   : 1862271177
         Main PW Token          : 0x0
         Slave PW Token         : 0x0
         Tnl Type               : ldp
         OutInterface           : LDP LSP
         Backup OutInterface    : --
         Stp Enable             : 0
         Mac Flapping           : 0
         PW Last Up Time        : 2013/12/27 17:02:19
         PW Total Up Time       : 0 days, 1 hours, 19 minutes, 38 seconds  
        *Peer Ip Address        : 4.4.4.4
         PW State               : up
         Local VC Label         : 32860
         Remote VC Label        : 32890
         Remote Control Word    : disable
         PW Type                : label
         Tunnel ID              : 0x0000000001004c4b42 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : --
         Ckey                   : 2
         Nkey                   : 1862271178
         Main PW Token          : 0x0
         Slave PW Token         : 0x0
         Tnl Type               : ldp
         OutInterface           : LDP LSP
         Backup OutInterface    : --
         Stp Enable             : 0
         Mac Flapping           : 0
         PW Last Up Time        : 2013/12/27 17:02:19
         PW Total Up Time       : 0 days, 1 hours, 19 minutes, 38 seconds
     ```
     ```
     [~NPE2] display vsi name s1 verbose
     ```
     ```
      ***VSI Name               : s1
         Administrator VSI      : no
         Isolate Spoken         : disable
         VSI Index              : 2
         PW Signaling           : ldp
         Member Discovery Style : static
         Bridge-domain Mode     : disable
         PW MAC Learn Style     : unqualify
         Encapsulation Type     : vlan
         MTU                    : 1500
         Diffserv Mode          : uniform
         Service Class          : --
         Color                  : --
         DomainId               : 255
         Domain Name            :
         Ignore AcState         : disable
         P2P VSI                : disable
         Multicast Fast Switch  : disable
         Create Time            : 0 days, 1 hours, 23 minutes, 17 seconds
         VSI State              : up
         Resource Status        : Valid
     
         VSI ID                 : 100
        *Peer Router ID         : 1.1.1.1
         primary or secondary   : primary
         ignore-standby-state   : no
         VC Label               : 32830
         Peer Type              : dynamic
         Session                : up
         Tunnel ID              : 0x0000000001004c4b38 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : -- 
         CKey                   : 4
         NKey                   : 218103945
         Stp Enable             : 0
         PwIndex                : 3
         Control Word           : disable
        *Peer Router ID         : 5.5.5.5
         primary or secondary   : primary
         ignore-standby-state   : no
         VC Label               : 32831
         Peer Type              : dynamic
         Session                : up
         Tunnel ID              : 0x0000000001004c4b39
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : -- 
         CKey                   : 5
         NKey                   : 218103944
         Stp Enable             : 0
         PwIndex                : 4
         Control Word           : disable
      
         Interface Name         : GigabitEthernet0/1/0.1
         State                  : up
         Access Port            : false
         Last Up Time           : 2013/12/27 17:36:16
         Total Up Time          : 0 days, 1 hours, 23 minutes, 17 seconds
     
       **PW Information:
     
        *Peer Ip Address        : 1.1.1.1
         PW State               : up
         Local VC Label         : 32881
         Remote VC Label        : 32894
         Remote Control Word    : disable
         PW Type                : label
         Tunnel ID              : 0x0000000001004c4b38 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : --
         Ckey                   : 2
         Nkey                   : 218103945
         Main PW Token          : 0x0
         Slave PW Token         : 0x0
         Tnl Type               : ldp
         OutInterface           : GigabitEthernet0/3/0
         Backup OutInterface    : --
         Stp Enable             : 0
         Mac Flapping           : 0
         PW Last Up Time        : 2013/12/27 17:40:16
         PW Total Up Time       : 0 days, 1 hours, 23 minutes, 17 seconds
        *Peer Ip Address        : 5.5.5.5
         PW State               : backup
         Local VC Label         : 32880
         Remote VC Label        : 32895
         Remote Control Word    : disable
         PW Type                : label
         Tunnel ID              : 0x0000000001004c4b39 
         Broadcast Tunnel ID    : --
         Broad BackupTunnel ID  : --
         Ckey                   : 2
         Nkey                   : 218103944
         Main PW Token          : 0x0
         Slave PW Token         : 0x0
         Tnl Type               : ldp
         OutInterface           : GigabitEthernet0/1/0
         Backup OutInterface    : --
         Stp Enable             : 0
         Mac Flapping           : 0
         PW Last Up Time        : 2013/12/27 17:42:16
         PW Total Up Time       : 0 days, 1 hours, 23 minutes, 17 seconds
     ```
     
     The service PW between NPE1 and NPE4 is blocked.
   * CE1 and CE2 can ping each other successfully.
     
     The following example uses the command output on CE1:
     
     ```
     [*CE1] ping 192.168.1.2
     ```
     ```
       PING 192.168.1.2: 56  data bytes, press CTRL_C to break
         Reply from 192.168.1.2: bytes=56 Sequence=1 ttl=255 time=104 ms
         Reply from 192.168.1.2: bytes=56 Sequence=2 ttl=255 time=112 ms
         Reply from 192.168.1.2: bytes=56 Sequence=3 ttl=255 time=112 ms
         Reply from 192.168.1.2: bytes=56 Sequence=4 ttl=255 time=112 ms
         Reply from 192.168.1.2: bytes=56 Sequence=5 ttl=255 time=112 ms
     
       --- 192.168.1.2 ping statistics ---
         5 packet(s) transmitted
         5 packet(s) received
         0.00% packet loss
         round-trip min/avg/max = 104/108/112 ms
     ```

#### Configuration Files

* UPE1 configuration file
  
  ```
  #
  sysname UPE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 2.2.2.2
    peer 3.3.3.3
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1
   vlan-type dot1q 10
   l2 binding vsi s1
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  return
  
  ```
* UPE2 configuration file
  
  ```
  #
  sysname UPE2
  #
  mpls lsr-id 6.6.6.6
  #
  mpls
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 4.4.4.4
    peer 5.5.5.5
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.5.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.5.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
  #
  interface GigabitEthernet0/3/0.1
   vlan-type dot1q 10
   l2 binding vsi s1
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
    network 10.5.1.0 0.0.0.255
    network 10.5.2.0 0.0.0.255
  #
  return
  
  ```
* NPE1 configuration file
  
  ```
  #
  sysname NPE1
  #
  stp enable
  #
  stp region-configuration
   region-name RG1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi m1 static
   pwsignal ldp
    vsi-id 10
    peer 3.3.3.3
    peer 3.3.3.3 pw pw1
      stp enable
      stp cost 2
    peer 4.4.4.4
    peer 4.4.4.4 pw pw2
      stp enable
      stp cost 2
   admin-vsi
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 1.1.1.1 upe
    peer 4.4.4.4 
   track admin-vsi m1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.6.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.8.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
    network 10.8.1.0 0.0.0.255
   #
  return
  
  ```
* NPE2 configuration file
  
  ```
  #
  sysname NPE2
  #
  stp enable
  #
  stp region-configuration
   region-name RG1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  vsi m1 static
   pwsignal ldp
    vsi-id 10
    peer 2.2.2.2
    peer 2.2.2.2 pw pw1
      stp enable
      stp cost 2
    peer 5.5.5.5
    peer 5.5.5.5 pw pw2
      stp enable
      stp cost 5
   admin-vsi
  #
  mpls l2vpn
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 1.1.1.1 upe
    peer 5.5.5.5
   track admin-vsi m1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.7.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.8.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.252.0
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
    network 10.8.1.0 0.0.0.255
  #
  return
  
  ```
* NPE3 configuration file
  
  ```
  #
  sysname NPE3
  #
  stp instance 0 priority 0
  stp enable
  #
  stp region-configuration
   region-name RG1
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  vsi m1 static
   pwsignal ldp
    vsi-id 10
    peer 2.2.2.2
    peer 2.2.2.2 pw pw2
      stp enable
      stp cost 2
    peer 5.5.5.5
    peer 5.5.5.5 pw pw1
      stp enable
      stp cost 2
   admin-vsi
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 2.2.2.2
    peer 6.6.6.6 upe
   track admin-vsi m1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.6.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.9.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.5.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.5.1.0 0.0.0.255
    network 10.6.1.0 0.0.0.255
    network 10.9.1.0 0.0.0.255
  #
  return
  
  ```
* NPE4 configuration file
  
  ```
  #
  sysname NPE4
  #
  stp instance 0 priority 4096
  stp enable
  #
  stp region-configuration
   region-name RG1
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
  #
  mpls l2vpn
  #
  vsi m1 static
   pwsignal ldp
    vsi-id 10
    peer 3.3.3.3
    peer 3.3.3.3 pw pw2
      stp enable
      stp cost 5
    peer 4.4.4.4
    peer 4.4.4.4 pw pw1
      stp enable
      stp cost 2
   admin-vsi
  #
  vsi s1 static
   pwsignal ldp
    vsi-id 100
    peer 3.3.3.3
    peer 6.6.6.6 upe
   track admin-vsi m1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.7.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.9.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.5.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 10.5.2.0 0.0.0.255
    network 10.7.1.0 0.0.0.255
    network 10.9.1.0 0.0.0.255
  #
  return
  
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 192.168.1.1 255.255.255.0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 10
   ip address 192.168.1.2 255.255.255.0
  #
  return
  ```