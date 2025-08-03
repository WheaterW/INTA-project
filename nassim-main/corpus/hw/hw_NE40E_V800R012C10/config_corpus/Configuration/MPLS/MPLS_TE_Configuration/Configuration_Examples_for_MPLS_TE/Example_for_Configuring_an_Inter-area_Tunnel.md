Example for Configuring an Inter-area Tunnel
============================================

Example for Configuring an Inter-area Tunnel

#### Networking Requirements

[Figure 1](#EN-US_TASK_0172368335__fig_dc_vrp_te-p2p_cfg_009801) illustrates a network:

* IS-IS runs on LSRA, LSRB, LSRC, LSRD, and LSRE.
  
  + LSRA and LSRE are level-1 routers.
  + LSRB and LSRD are level-1-2 routers.
  + LSRC is a level-2 router.
* RSVP-TE is used to establish a TE tunnel between LSRA and LSRE over IS-IS areas. The bandwidth for the TE tunnel is 20 Mbit/s.
* Both the maximum reservable bandwidth and BC0 bandwidth for every link along the TE tunnel are 100 Mbit/s.

**Figure 1** Inter-area tunnel networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_009801.png)  


#### Configuration Notes

None.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to every interface and configure a loopback address that is used as an LSR ID on every LSR.
2. Enable IS-IS globally and enable IS-IS TE.
3. Configure a loose explicit path on which LSRB, LSRC, and LSRD functioning as area border routers (ABRs) are located.
4. Configure MPLS RSVP-TE.
5. Set bandwidth attributes for every outbound interface on every LSR along the TE tunnel.
6. Create a tunnel interface on the ingress and configure the source and destination IP addresses, protocol, ID, RSVP-TE signaling protocol, and bandwidth for the tunnel.

#### Data Preparation

To complete the configuration, you need the following data:

* Origin AS number, IS-IS level, and area ID of every LSR
* Maximum reservable bandwidth and BC bandwidth for every link along the TE tunnel
* Tunnel interface number, IP address, destination address, tunnel ID, signaling protocol (RSVP-TE), and tunnel bandwidth

#### Procedure

1. Assign an IP address and its mask to every interface.
   
   
   
   Assign an IP address and a mask to each interface according to [Figure 1](#EN-US_TASK_0172368335__fig_dc_vrp_te-p2p_cfg_009801). The configuration details are not provided.
2. Configure IS-IS.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] isis 1
   ```
   ```
   [*LSRA-isis-1] network-entity 00.0005.0000.0000.0001.00
   ```
   ```
   [*LSRA-isis-1] is-level level-1
   ```
   ```
   [*LSRA-isis-1] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRA] interface loopback 1
   ```
   ```
   [*LSRA-LoopBack1] isis enable 1
   ```
   ```
   [*LSRA-LoopBack1] commit
   ```
   ```
   [~LSRA-LoopBack1] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] isis 1
   ```
   ```
   [*LSRB-isis-1] network-entity 00.0005.0000.0000.0002.00
   ```
   ```
   [*LSRB-isis-1] is-level level-1-2
   ```
   ```
   [*LSRB-isis-1] import-route isis level-2 into level-1
   ```
   ```
   [*LSRB-isis-1] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*LSRB] interface loopback 1
   ```
   ```
   [*LSRB-LoopBack1] isis enable 1
   ```
   ```
   [*LSRB-LoopBack1] commit
   ```
   ```
   [~LSRB-LoopBack1] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] isis 1
   ```
   ```
   [*LSRC-isis-1] network-entity 00.0006.0000.0000.0003.00
   ```
   ```
   [*LSRC-isis-1] is-level level-2
   ```
   ```
   [*LSRC-isis-1] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*LSRC] interface loopback 1
   ```
   ```
   [*LSRC-LoopBack1] isis enable 1
   ```
   ```
   [*LSRC-LoopBack1] commit
   ```
   ```
   [~LSRC-LoopBack1] quit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] isis 1
   ```
   ```
   [*LSRD-isis-1] network-entity 00.0007.0000.0000.0004.00
   ```
   ```
   [*LSRD-isis-1] is-level level-1-2
   ```
   ```
   [*LSRD-isis-1] import-route isis level-2 into level-1
   ```
   ```
   [*LSRD-isis-1] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] isis enable 1
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*LSRD] interface loopback 1
   ```
   ```
   [*LSRD-LoopBack1] isis enable 1
   ```
   ```
   [*LSRD-LoopBack1] commit
   ```
   ```
   [~LSRD-LoopBack1] quit
   ```
   
   # Configure LSRE.
   
   ```
   [~LSRE] isis 1
   ```
   ```
   [*LSRE-isis-1] network-entity 00.0007.0000.0000.0005.00
   ```
   ```
   [*LSRE-isis-1] is-level level-1
   ```
   ```
   [*LSRE-isis-1] quit
   ```
   ```
   [*LSRE] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] isis enable 1
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRE] interface loopback 1
   ```
   ```
   [*LSRE-LoopBack1] isis enable 1
   ```
   ```
   [*LSRE-LoopBack1] commit
   ```
   ```
   [~LSRE-LoopBack1] quit
   ```
   
   After completing the configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on every node. All nodes have learned routes from one another.
3. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF on the ingress of the TE tunnel.
   
   
   
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
   [*LSRA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] mpls lsr-id 2.2.2.2
   ```
   ```
   [*LSRB] mpls
   ```
   ```
   [*LSRB-mpls] mpls te
   ```
   ```
   [*LSRB-mpls] mpls rsvp-te
   ```
   ```
   [*LSRB-mpls] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls rsvp-te
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] mpls lsr-id 3.3.3.3
   ```
   ```
   [*LSRC] mpls
   ```
   ```
   [*LSRC-mpls] mpls te
   ```
   ```
   [*LSRC-mpls] mpls rsvp-te
   ```
   ```
   [*LSRC-mpls] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] mpls rsvp-te
   ```
   ```
   [*LSRC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] mpls lsr-id 4.4.4.4
   ```
   ```
   [*LSRD] mpls
   ```
   ```
   [*LSRD-mpls] mpls te
   ```
   ```
   [*LSRD-mpls] mpls rsvp-te
   ```
   ```
   [*LSRD-mpls] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/2/0
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] mpls rsvp-te
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRD-GigabitEthernet0/2/0] quit
   ```
   
   # Configure LSRE.
   
   ```
   [~LSRE] mpls lsr-id 5.5.5.5
   ```
   ```
   [*LSRE] mpls
   ```
   ```
   [*LSRE-mpls] mpls te
   ```
   ```
   [*LSRE-mpls] mpls rsvp-te
   ```
   ```
   [*LSRE-mpls] quit
   ```
   ```
   [*LSRE] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*LSRE-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRE-GigabitEthernet0/1/0] quit
   ```
4. Configure IS-IS TE.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] isis 1
   ```
   ```
   [~LSRA-isis-1] cost-style wide
   ```
   ```
   [*LSRA-isis-1] traffic-eng level-1
   ```
   ```
   [*LSRA-isis-1] commit
   ```
   ```
   [~LSRA-isis-1] quit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] isis 1
   ```
   ```
   [~LSRB-isis-1] cost-style wide
   ```
   ```
   [*LSRB-isis-1] traffic-eng level-1-2
   ```
   ```
   [*LSRB-isis-1] commit
   ```
   ```
   [~LSRB-isis-1] quit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] isis 1
   ```
   ```
   [~LSRC-isis-1] cost-style wide
   ```
   ```
   [*LSRC-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRC-isis-1] commit
   ```
   ```
   [~LSRC-isis-1] quit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] isis 1
   ```
   ```
   [~LSRD-isis-1] cost-style wide
   ```
   ```
   [*LSRD-isis-1] traffic-eng level-1-2
   ```
   ```
   [*LSRD-isis-1] commit
   ```
   ```
   [~LSRD-isis-1] quit
   ```
   
   # Configure LSRE.
   
   ```
   [~LSRE] isis 1
   ```
   ```
   [~LSRE-isis-1] cost-style wide
   ```
   ```
   [*LSRE-isis-1] traffic-eng level-1
   ```
   ```
   [*LSRE-isis-1] commit
   ```
   ```
   [~LSRE-isis-1] quit
   ```
5. Configure a loose explicit path.
   
   
   ```
   [~LSRA] explicit-path atoe
   ```
   ```
   [*LSRA-explicit-path-atoe] next hop 10.1.1.2 include loose
   ```
   ```
   [*LSRA-explicit-path-atoe] next hop 10.2.1.2 include loose
   ```
   ```
   [*LSRA-explicit-path-atoe] next hop 10.3.1.2 include loose
   ```
   ```
   [*LSRA-explicit-path-atoe] next hop 10.4.1.2 include loose
   ```
   ```
   [*LSRA-explicit-path-atoe] commit
   ```
6. Configure MPLS TE attributes for links.
   
   
   
   # Set the maximum reservable bandwidth and BC0 bandwidth for links on LSRA.
   
   ```
   [~LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls te bandwidth bc0 100000
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRA-GigabitEthernet0/1/0] quit
   ```
   
   # Set the maximum bandwidth and reservable bandwidth for links on LSRB.
   
   ```
   [~LSRB] interface gigabitethernet 0/2/0
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] mpls te bandwidth bc0 100000
   ```
   ```
   [*LSRB-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRB-GigabitEthernet0/2/0] quit
   ```
   
   # Set the maximum bandwidth and reservable bandwidth for links on LSRC.
   
   ```
   [~LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [~LSRC-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls te bandwidth bc0 100000
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRC-GigabitEthernet0/1/0] quit
   ```
   
   # Set the maximum bandwidth and reservable bandwidth for links on LSRD.
   
   ```
   [~LSRD] interface gigabitethernet 0/2/0
   ```
   ```
   [~LSRD-GigabitEthernet0/2/0] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] mpls te bandwidth bc0 100000
   ```
   ```
   [*LSRD-GigabitEthernet0/2/0] commit
   ```
   ```
   [~LSRD-GigabitEthernet0/2/0] quit
   ```
7. Configure an MPLS TE tunnel.
   
   
   
   # Configure the MPLS TE tunnel on LSRA.
   
   ```
   [~LSRA] interface tunnel1
   ```
   ```
   [*LSRA-Tunnel1] ip address unnumbered interface loopback 1
   ```
   ```
   [*LSRA-Tunnel1] tunnel-protocol mpls te
   ```
   ```
   [*LSRA-Tunnel1] destination 5.5.5.5
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] mpls te bandwidth ct0 20000
   ```
   ```
   [*LSRA-Tunnel1] mpls te path explicit-path atoe
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
8. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) command on LSRA. The tunnel interface is **Up**.
   
   ```
   [~LSRA] display interface Tunnel
   ```
   ```
   Tunnel1 current state : UP (ifindex: 26)
   Line protocol current state : UP 
   Last line protocol up time : 2012-03-08 04:52:40
   Description:
   Route Port,The Maximum Transmit Unit is 1500 
   Internet Address is unnumbered, using address of LoopBack1(1.1.1.1/32)
   Encapsulation is TUNNEL, loopback not set
   Tunnel destination 5.5.5.5
   Tunnel up/down statistics 1
   Tunnel protocol/transport MPLS/MPLS, ILM is available,
   primary tunnel id is 0x97, secondary tunnel id is 0x0
   Current system time: 2012-03-08 08:33:55
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
       Ingress LSR ID      : 1.1.1.1               Egress LSR ID: 5.5.5.5
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
       Explicit Path Name  : main                             Hop Limit: -
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
  explicit-path atoe
  ```
  ```
   next hop 10.1.1.2 include loose
  ```
  ```
   next hop 10.2.1.2 include loose
  ```
  ```
   next hop 10.3.1.2 include loose
  ```
  ```
   next hop 10.4.1.2 include loose
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1
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
   destination 5.5.5.5
  ```
  ```
   mpls te tunnel-id 1
  ```
  ```
   mpls te bandwidth ct0 20000
  ```
  ```
   mpls te path explicit-path atoe
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
   mpls rsvp-te
  ```
  ```
  #
  ```
  ```
  isis 1
  ```
  ```
   is-level level-1-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   import-route isis level-2 into level-1
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
   network-entity 00.0006.0000.0000.0003.00
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
   is-level level-1-2
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1-2
  ```
  ```
   network-entity 00.0007.0000.0000.0004.00
  ```
  ```
   import-route isis level-2 into level-1
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
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.4.1.1 255.255.255.0
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
   is-level level-1
  ```
  ```
   cost-style wide
  ```
  ```
   traffic-eng level-1
  ```
  ```
   network-entity 00.0007.0000.0000.0005.00
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
   ip address 10.4.1.2 255.255.255.0
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