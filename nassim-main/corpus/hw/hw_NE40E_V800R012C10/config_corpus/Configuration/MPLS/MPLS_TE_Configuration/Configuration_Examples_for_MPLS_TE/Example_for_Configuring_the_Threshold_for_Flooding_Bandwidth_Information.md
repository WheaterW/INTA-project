Example for Configuring the Threshold for Flooding Bandwidth Information
========================================================================

Example for Configuring the Threshold for Flooding Bandwidth Information

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368338__fig_dc_vrp_te-p2p_cfg_010301), an RSVP-TE tunnel between LSRA and LSRD is established. The bandwidth is 50 Mbit/s. The maximum reservable bandwidth and BC0 bandwidth for every link are 100 Mbit/s. The RDM is used.

The threshold for flooding bandwidth information is set to 20%. This reduces the number of attempts to flood bandwidth information and saves network resources. If the proportion of the bandwidth used or released by an MPLS TE tunnel to the available bandwidth in the TEDB is greater than or equal to 20%, an IGP floods the bandwidth information, and CSPF updates TEDB information.

**Figure 1** Networking diagram for the threshold for flooding bandwidth information![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_009401.png)  


#### Precautions

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an RSVP-TE tunnel. See "Configuration Roadmap" in [Example for Configuring an RSVP-TE Tunnel](dc_vrp_te-p2p_cfg_0094.html).
2. Configure bandwidth and the threshold for flooding bandwidth information

#### Data Preparation

To complete the configuration, you need the following data:

* OSPF process ID and OSPF area ID for every node
* Maximum reservable bandwidth and BC bandwidth for every link along the TE tunnel
* Tunnel interface number, IP address, destination address, tunnel ID, bandwidth for the tunnel, and signaling protocol (RSVP-TE by default)
* Threshold for flooding bandwidth information

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and its mask to every physical interface and configure a loopback interface address as an LSR ID on every node according to [Figure 1](#EN-US_TASK_0172368338__fig_dc_vrp_te-p2p_cfg_010301).
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172368338__section_dc_vrp_te-p2p_cfg_010305) in this section.
2. Configure an IGP.
   
   
   
   Configure OSPF or IS-IS on every node to implement connectivity between them. IS-IS is used in this example.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172368338__section_dc_vrp_te-p2p_cfg_010305) in this section.
3. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   
   
   
   # Enable MPLS, MPLS TE, and RSVP-TE on every LSR and their interfaces along a tunnel, and enable CSPF in the system view of the ingress.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172368338__section_dc_vrp_te-p2p_cfg_010305) in this section.
4. Configure MPLS TE bandwidth attributes for links.
   
   
   
   # Set the maximum reservable bandwidth and BC0 bandwidth for a link on every interface along the TE tunnel.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172368338__section_dc_vrp_te-p2p_cfg_010305) in this section.
5. Configure the threshold for flooding bandwidth information.
   
   
   
   # Set the threshold for flooding bandwidth information to 20% on a physical interface on LSRA. If the proportion of the bandwidth used or released by an MPLS TE tunnel to the available bandwidth in the TEDB is greater than or equal to 20%, an IGP floods the bandwidth information, and CSPF updates TEDB information.
   
   ```
   [~LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] mpls te bandwidth change thresholds up 20
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls te bandwidth change thresholds down 20
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] quit
   ```
   
   Run the [**display mpls te cspf tedb**](cmdqueryname=display+mpls+te+cspf+tedb) command on LSRA. TEDB information is displayed.
   
   ```
   [~LSRA] display mpls te cspf tedb interface 10.1.1.1
   ```
   ```
   Router ID:  1.1.1.9 
     IGP Type:  ISIS       Process Id:  1 
     Link[1]:
      ISIS System ID:  0000.0000.0001.00     Opaque LSA ID: 0000.0000.0001.00:00 
      Interface IP Address:  10.1.1.1 
      DR Address:  10.1.1.1 
      DR ISIS System ID:  0000.0000.0001.01 
      IGP Area:  Level-2 
      Link Type:  Multi-access   Link Status:  Active 
      IGP Metric:  10     TE Metric:  10    Color: 0x0 
      Bandwidth Allocation Model :  - 
      Maximum Link-Bandwidth:  100000  (kbps)
      Maximum Reservable Bandwidth:  100000  (kbps)
      Operational Mode of Router :  TE
      Bandwidth Constraints:          Local Overbooking Multiplier:
         BC[0]:      100000 (kbps)            LOM[0]:          1 
      BW  Unreserved:
           Class  ID:
           [0]:      100000 (kbps),            [1]:      100000 (kbps)
           [2]:      100000 (kbps),            [3]:      100000 (kbps)
           [4]:      100000 (kbps),            [5]:      100000 (kbps)
           [6]:      100000 (kbps),            [7]:      100000 (kbps)
   
   ```
6. Configure an MPLS TE tunnel.
   
   
   
   # Configure a tunnel named **Tunnel1** on LSRA.
   
   ```
   [~LSRA]interface tunnel1
   ```
   ```
   [*LSRA-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRA-Tunnel1] destination 4.4.4.9
   ```
   ```
   [*LSRA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel1] mpls te bandwidth ct0 10000
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
   
   After completing the configuration, run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command on LSRA. The tunnel interface is **Up**.
   
   ```
   [~LSRA] display mpls te tunnel-interface tunnel1
   ```
   ```
       Tunnel Name       : Tunnel1
       Signalled Tunnel Name: -
       Tunnel State Desc : CR-LSP is Up
       Tunnel Attributes   :     
       Active LSP          : Primary LSP                                       
       Traffic Switch      : - 
       Session ID          : 1
       Ingress LSR ID      : 1.1.1.9               Egress LSR ID: 4.4.4.9
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
       BackUp LSP Type     : None                  BestEffort   : Enabled
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
       PCE Delegate      : No             LSP Control Status : Local control
       Path Verification : --
       Entropy Label     : None 
       Auto BW Remain Time : 200 s   Reopt Remain Time  : 100 s
       Metric Inherit IGP : None
       Binding Sid       : -                     Reverse Binding Sid : - 
       Self-Ping         : Disable               Self-Ping Duration : 1800 sec 
       FRR Attr Source   : -                     Is FRR degrade down : No
       
       Primary LSP ID      : 1.1.1.9:19
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
       Explicit Path Name  : -                                Hop Limit: -
       Record Route        : Disabled              Record Label : Disabled
       Route Pinning       : Disabled
       FRR Flag            : Disabled
       IdleTime Remain     : -
       BFD Status          : -
       Soft Preemption     : Enabled 
       Reroute Flag        : Disabled
       Pce Flag            : Normal
       Path Setup Type     : CSPF
       Create Modify LSP Reason: -
       Self-Ping Status    : -
   ```
   
   Run the [**display mpls te cspf tedb**](cmdqueryname=display+mpls+te+cspf+tedb) command on LSRA. Bandwidth information is unchanged.
   
   ```
   [~LSRA] display mpls te cspf tedb interface 10.1.1.1
   ```
   ```
   Router ID:  1.1.1.9 
     IGP Type:  ISIS       Process Id:  1 
     Link[1]:
      ISIS System ID:  0000.0000.0001.00     Opaque LSA ID: 0000.0000.0001.00:00 
      Interface IP Address:  10.1.1.1 
      DR Address:  10.1.1.1 
      DR ISIS System ID:  0000.0000.0001.01 
      IGP Area:  Level-2 
      Link Type:  Multi-access   Link Status:  Active 
      IGP Metric:  10     TE Metric:  10    Color: 0x0 
      Bandwidth Allocation Model :  - 
      Maximum Link-Bandwidth:  100000  (kbps)
      Maximum Reservable Bandwidth:  100000  (kbps)
      Operational Mode of Router :  TE
      Bandwidth Constraints:          Local Overbooking Multiplier:
         BC[0]:      100000 (kbps)            LOM[0]:          1 
      BW  Unreserved:
           Class  ID:
           [0]:      100000 (kbps),            [1]:      100000 (kbps)
           [2]:      100000 (kbps),            [3]:      100000 (kbps)
           [4]:      100000 (kbps),            [5]:      100000 (kbps)
           [6]:      100000 (kbps),            [7]:      100000 (kbps)
   
   ```
7. Verify the configuration.
   
   
   
   After completing the configuration, change the bandwidth to 20000 kbit/s.
   
   ```
   [~LSRA] interface tunnel1
   ```
   ```
   [~LSRA-Tunnel1] mpls te bandwidth ct0 20000
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
   
   Run the [**display mpls te cspf tedb interface 10.1.1.1**](cmdqueryname=display+mpls+te+cspf+tedb+interface+10.1.1.1) command. TEDB information shows that the TE tunnel named Tunnel1 has been reestablished successfully. Its bandwidth is 20,000 kbit/s, reaching 20%, the threshold for flooding bandwidth information. This indicates that CSPF TEDB information has been updated.
   
   ```
   [~LSRA]  display mpls te cspf tedb interface 10.1.1.1
   ```
   ```
   Router ID:  1.1.1.9 
     IGP Type:  ISIS       Process Id:  1 
     Link[1]:
      ISIS System ID:  0000.0000.0001.00     Opaque LSA ID: 0000.0000.0001.00:00 
      Interface IP Address:  10.1.1.1 
      DR Address:  10.1.1.1 
      DR ISIS System ID:  0000.0000.0001.01 
      IGP Area:  Level-2 
      Link Type:  Multi-access   Link Status:  Active 
      IGP Metric:  10     TE Metric:  10    Color: 0x0 
      Bandwidth Allocation Model :  - 
      Maximum Link-Bandwidth:  100000  (kbps)
      Maximum Reservable Bandwidth:  100000  (kbps)
      Operational Mode of Router :  TE
      Bandwidth Constraints:          Local Overbooking Multiplier:
         BC[0]:      100000 (kbps)            LOM[0]:          1 
      BW  Unreserved:
           Class  ID:
           [0]:      100000 (kbps),            [1]:      100000 (kbps)
           [2]:      100000 (kbps),            [3]:      100000 (kbps)
           [4]:      100000 (kbps),            [5]:      100000 (kbps)
           [6]:      100000 (kbps),            [7]:       80000 (kbps)
   ```

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
  mpls lsr-id 1.1.1.9
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
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te bandwidth max-reservable-bandwidth 100000
  ```
  ```
   mpls te bandwidth bc0 100000
  ```
  ```
   mpls te bandwidth change thresholds up 20
  ```
  ```
   mpls te bandwidth change thresholds down 20
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
   ip address 1.1.1.9 255.255.255.255
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
   destination 4.4.4.9
  ```
  ```
   mpls te tunnel-id 1
  ```
  ```
   mpls te bandwidth ct0 10000
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
  mpls lsr-id 2.2.2.9
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
   ip address 10.1.1.2 255.255.255.0
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
   ip address 10.2.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te bandwidth max-reservable-bandwidth 100000
  ```
  ```
   mpls te bandwidth bc0 100000
  ```
  ```
   mpls te bandwidth change thresholds up 20
  ```
  ```
   mpls te bandwidth change thresholds down 20
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
   ip address 2.2.2.9 255.255.255.255
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
  mpls lsr-id 3.3.3.9
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
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
   mpls
  ```
  ```
   mpls te
  ```
  ```
   mpls te bandwidth max-reservable-bandwidth 100000
  ```
  ```
   mpls te bandwidth bc0 100000
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
   ip address 10.2.1.2 255.255.255.0
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
   ip address 3.3.3.9 255.255.255.255
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
  mpls lsr-id 4.4.4.9
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
   ip address 10.3.1.2 255.255.255.0
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
   ip address 4.4.4.9 255.255.255.255
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