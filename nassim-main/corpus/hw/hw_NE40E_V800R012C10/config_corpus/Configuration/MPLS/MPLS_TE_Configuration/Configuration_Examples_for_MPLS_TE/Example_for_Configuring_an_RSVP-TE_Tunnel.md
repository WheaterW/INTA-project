Example for Configuring an RSVP-TE Tunnel
=========================================

Example for Configuring an RSVP-TE Tunnel

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172368312__fig_dc_vrp_te-p2p_cfg_009401), LSRA, LSRB, LSRC, and LSRD are level-2 routers that run IS-IS.

RSVP-TE is used to establish a TE tunnel with 20 Mbit/s bandwidth between LSRA and LSRD. The maximum reservable bandwidth for every link along the TE tunnel is 100 Mbit/s and the BC0 bandwidth is 100 Mbit/s.

**Figure 1** Networking diagram for an RSVP-TE tunnel![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_te-p2p_cfg_009401.png)  


#### Configuration Notes

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface, including the loopback interface whose address is to be used as an LSR ID on each involved node.
2. Enable IS-IS globally; configure the network entity name; set the cost type to enable IS-IS TE; enable IS-IS on involved interfaces, including loopback interfaces.
3. Set an MPLS LSR ID for every LSR and enable MPLS, MPLS TE, RSVP-TE, and CSPF globally.
4. Enable MPLS, MPLS TE, and RSVP-TE on every interface.
5. Configure the maximum reservable link bandwidth and BC bandwidth on the outbound interfaces of each involved tunnel.
6. Create a tunnel interface on the ingress and configure the source and destination IP addresses for the tunnel, tunnel protocol, destination address, and tunnel bandwidth.

#### Data Preparation

To complete the configuration, you need the following data:

* Origin AS number, IS-IS level, and area ID of every LSR
* BC bandwidth and maximum reservable bandwidth on every link along the TE tunnel
* Tunnel interface number, IP address, destination IP address, tunnel ID, and tunnel bandwidth

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and a mask to each interface according to [Figure 1](#EN-US_TASK_0172368312__fig_dc_vrp_te-p2p_cfg_009401). The configuration details are not provided.
2. Configure IS-IS.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] isis 1 
   ```
   ```
   [*LSRA-isis-1] network-entity 00.0005.0000.0000.0001.00
   ```
   ```
   [*LSRA-isis-1] is-level level-2
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
   [*LSRB-isis-1] is-level level-2
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
   [*LSRC-isis-1] network-entity 00.0005.0000.0000.0003.00
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
   [*LSRD-isis-1] network-entity 00.0005.0000.0000.0004.00
   ```
   ```
   [*LSRD-isis-1] is-level level-2
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
   
   After completing the configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on each node. All nodes have learned routes from one another. The following example uses the command output on LSRA.
   
   ```
   [~LSRA] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 13       Routes : 13        
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.9/32  Direct  0    0             D  127.0.0.1       LoopBack1
           2.2.2.9/32  ISIS-L2 15   10            D  10.1.1.2        GigabitEthernet0/1/0
           3.3.3.9/32  ISIS-L2 15   20            D  10.1.1.2        GigabitEthernet0/1/0
           4.4.4.9/32  ISIS-L2 15   30            D  10.1.1.2        GigabitEthernet0/1/0
          10.1.1.0/24  Direct  0    0             D  10.1.1.1        GigabitEthernet0/1/0
          10.1.1.1/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
        10.1.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
          10.2.1.0/24  ISIS-L2 15   20            D  10.1.1.2        GigabitEthernet0/1/0
          10.3.1.0/24  ISIS-L2 15   30            D  10.1.1.2        GigabitEthernet0/1/0
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
3. Configure basic MPLS functions and enable MPLS TE, RSVP-TE, and CSPF.
   
   
   
   # Enable MPLS, MPLS TE, and RSVP-TE globally on each node and on all interfaces along the tunnel, and enable CSPF on the ingress.
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.9
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
   [~LSRB] mpls lsr-id 2.2.2.9
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
   [~LSRC] mpls lsr-id 3.3.3.9
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
   [~LSRD] mpls lsr-id 4.4.4.9
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
   [*LSRD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~LSRD-GigabitEthernet0/1/0] quit
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
   [*LSRA-isis-1] traffic-eng level-2
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
   [*LSRB-isis-1] traffic-eng level-2
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
   [*LSRD-isis-1] traffic-eng level-2
   ```
   ```
   [*LSRD-isis-1] commit
   ```
   ```
   [~LSRD-isis-1] quit
   ```
5. Configure MPLS TE bandwidth attributes for links.
   
   
   
   # Set the maximum reservable bandwidth and BC0 bandwidth for a link on every interface along the TE tunnel.
   
   # Configure LSRA.
   
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
   
   # Configure LSRB.
   
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
   
   # Configure LSRC.
   
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
6. Configure an MPLS TE tunnel interface.
   
   
   
   # Create a tunnel interface on the ingress; configure the source and destination IP addresses for the tunnel, tunnel protocol, tunnel ID, and RSVP-TE signaling protocol; run the [**commit**](cmdqueryname=commit) command to make the configurations take effect.
   
   # Configure LSRA.
   
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
   [*LSRA-Tunnel1] destination 4.4.4.9
   ```
   ```
   [*LSRA-Tunnel1] mpls te tunnel-id 1
   ```
   ```
   [*LSRA-Tunnel1] mpls te bandwidth ct0 20000
   ```
   ```
   [*LSRA-Tunnel1] commit
   ```
   ```
   [~LSRA-Tunnel1] quit
   ```
7. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display interface tunnel**](cmdqueryname=display+interface+tunnel) command on LSRA. The tunnel interface is **Up**.
   
   ```
   [~LSRA] display interface tunnel 1
   ```
   ```
   Tunnel1 current state : Up (ifindex: 29)  
   Line protocol current state : Up 
   Last line protocol up time : 2012-11-30 05:58:08
   Description: 
   Route Port,The Maximum Transmit Unit is 1500, Current BW: 20Mbps 
   Internet Address is unnumbered, using address of LoopBack1(1.1.1.9/32)
   Encapsulation is TUNNEL, loopback not set
   Tunnel destination 4.4.4.9
   Tunnel up/down statistics 1
   Tunnel protocol/transport MPLS/MPLS, ILM is available,
   primary tunnel id is 0x61, secondary tunnel id is 0x0
   Current system time: 2012-11-30 05:58:10
       300 seconds output rate 0 bits/sec, 0 packets/sec
       0 seconds output rate 0 bits/sec, 0 packets/sec
       126 packets output,  34204 bytes
       0 output error
       18 output drop
       Last 300 seconds input utility rate:  0.00%
       Last 300 seconds output utility rate: 0.00%
   ```
   
   Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command on LSRA. Detailed information about the tunnel interface is displayed.
   
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
       Explicit Path Name  : main                             Hop Limit: -
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
   
   Run the [**display mpls te cspf tedb all**](cmdqueryname=display+mpls+te+cspf+tedb+all) command on LSRA. Link information in the TEDB is displayed.
   
   ```
   [~LSRA] display mpls te cspf tedb all
   ```
   ```
                                                                                   
   Current Total Node Number: 4                  
   Current Total Link Number: 6                  
   Current Total SRLG Number: 0                  
                                                                                   
   Id      Router-Id       IGP       Process-Id      Area             Link-Count   
   1       1.1.1.9         ISIS      1               Level-2          1            
   2       2.2.2.9         ISIS      1               Level-2          2            
   3       3.3.3.9         ISIS      1               Level-2          2            
   4       4.4.4.9         ISIS      1               Level-2          1            
   ```

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
   mpls te
   mpls te cspf
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   traffic-eng level-2
   network-entity 00.0005.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 100000
   mpls te bandwidth bc0 100000
   isis enable 1
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.9
   mpls te bandwidth ct0 20000
   mpls te tunnel-id 1
  #
  return
  ```
* LSRB configuration file
  
  ```
  #
  sysname LSRB
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
   mpls te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   traffic-eng level-2
   network-entity 00.0005.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls te
   isis enable 1
   mpls rsvp-te
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 100000
   mpls te bandwidth bc0 100000
   isis enable 1
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRC configuration file
  
  ```
  #
  sysname LSRC
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
   mpls te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   traffic-eng level-2
   network-entity 00.0005.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 100000
   mpls te bandwidth bc0 100000
   isis enable 1
   mpls rsvp-te
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls te
   isis enable 1
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #
  return
  ```
* LSRD configuration file
  
  ```
  #
  sysname LSRD
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
   mpls te
   mpls rsvp-te
  #
  isis 1
   is-level level-2
   cost-style wide
   traffic-eng level-2
   network-entity 00.0005.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls te
   isis enable 1
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1
  #
  return
  ```