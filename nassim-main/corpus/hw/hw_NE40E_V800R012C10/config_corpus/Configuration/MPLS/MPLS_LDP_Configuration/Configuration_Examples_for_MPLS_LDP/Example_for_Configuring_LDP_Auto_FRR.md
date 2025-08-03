Example for Configuring LDP Auto FRR
====================================

This section provides an example for configuring LDP Auto FRR. The configuration procedure involves enabling MPLS, MPLS LDP, and IS-IS Auto FRR globally.

#### Networking Requirements

Modern network services, such as VoIP, online games, and online video services, have higher requirements on real-time performance. Many services are based on VPNs, and VPN services usually use LDP tunnels. Data loss due to link faults adversely affects these services.

To minimize the adverse impact, LDP manual FRR can be configured. If a fault occurs on a public network, LDP manual FRR switches the VPN services to a backup LSP before the primary LSP routes re-converge and the primary LSP is reestablished. Traffic loss during fault detection and traffic switchover to the backup LSP lasts less than 50 ms. However, after route re-convergence is complete, the time for a VPN service to switch to the new primary LSP depends on the VPN implementation. In order to keep the VPN service interruption time within 50 ms, the speed of switching the VPN service to the new primary LSP needs to be improved. Configure LDP Auto FRR to address this need.

On the network shown in [Figure 1](#EN-US_TASK_0172368590__fig_dc_vrp_ldp-p2p_cfg_005401), primary and backup LSPs are established from LSRA to LSRC. The LSP over the path LSRA -> LSRC is the primary one, and the LSP over the path LSRA -> LSRB -> LSRC is the backup one. To allow traffic to rapidly switch to the backup LSP if the primary LSP fails, configure LDP Auto FRR on LSRA to enable LSRA to automatically establish a backup LSP. Traffic can then be rapidly switched to the backup LSP if a fault occurs in the primary LSP, minimizing traffic loss.

**Figure 1** Networking diagram of LDP Auto FRR  
![](images/fig_dc_vrp_ldp-p2p_cfg_005401.png)

**Table 1** Interfaces and IP addresses
| Device Name | Interface Name | IP Address |
| --- | --- | --- |
| LSRA | Loopback0 | 1.1.1.9/32 |
| GigabitEthernet0/1/0 | 10.1.1.1/24 |
| GigabitEthernet0/1/1 | 10.1.2.1/24 |
| LSRB | Loopback0 | 2.2.2.9/32 |
| GigabitEthernet0/1/0 | 10.1.1.2/24 |
| GigabitEthernet0/1/1 | 10.1.3.1/24 |
| LSRC | Loopback0 | 3.3.3.9/32 |
| GigabitEthernet0/1/0 | 10.1.4.1/24 |
| GigabitEthernet0/1/0 | 10.1.2.2/24 |
| GigabitEthernet0/1/2 | 10.1.3.2/24 |
| LSRD | Loopback0 | 4.4.4.9/32 |
| GigabitEthernet0/1/0 | 10.1.4.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign IP addresses to interfaces on each node and configure the loopback addresses to be used as LSR IDs.
2. Configure IS-IS to advertise the route to each network segment to which each interface is connected and to advertise the host route to each LSR ID.
3. Enable MPLS and MPLS LDP on each node and interfaces.
4. Enable IS-IS Auto FRR on the ingress LSR to protect traffic.
5. Configure a policy for triggering LDP LSP establishment based on all routes.
6. Configure a policy for triggering backup LDP LSP establishment on ingress LSR.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of every interface on every node shown in [Figure 1](#EN-US_TASK_0172368590__fig_dc_vrp_ldp-p2p_cfg_005401), IS-IS process ID, and level of each router
* Policy for triggering backup LDP LSP establishment

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address and a mask to each interface (including loopback interfaces) according to [Figure 1](#EN-US_TASK_0172368590__fig_dc_vrp_ldp-p2p_cfg_005401).
2. Configure IS-IS to advertise the route to each network segment to which each interface is connected and to advertise the host route to each LSR ID.
   
   
   
   # Configure LSRA.
   
   ```
   <LSRA> system-view
   ```
   ```
   [~LSRA] isis 1
   ```
   ```
   [*LSRA-isis-1] network-entity 10.0000.0000.0001.00
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
   [*LSRA] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRA] interface loopBack 0
   ```
   ```
   [*LSRA-LoopBack0] isis enable 1
   ```
   ```
   [*LSRA-LoopBack0] quit
   ```
   ```
   [*LSRA] commit
   ```
   
   # Configure LSRB.
   
   ```
   <LSRB> system-view
   ```
   ```
   [~LSRB] isis 1
   ```
   ```
   [*LSRB-isis-1] network-entity 10.0000.0000.0002.00
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
   [*LSRB] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRB] interface loopBack 0
   ```
   ```
   [*LSRB-LoopBack0] isis enable 1
   ```
   ```
   [*LSRB-LoopBack0] quit
   ```
   ```
   [*LSRB] commit
   ```
   
   # Configure LSRC.
   
   ```
   <LSRC> system-view
   ```
   ```
   [~LSRC] isis 1
   ```
   ```
   [*LSRC-isis-1] network-entity 10.0000.0000.0003.00
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
   [*LSRC] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] isis enable 1
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/2
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] isis enable 1
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*LSRC] interface loopBack 0
   ```
   ```
   [*LSRC-LoopBack0] isis enable 1
   ```
   ```
   [*LSRC-LoopBack0] quit
   ```
   ```
   [*LSRC] commit
   ```
   
   # Configure LSRD.
   
   ```
   <LSRD> system-view
   ```
   ```
   [~LSRD] isis 1
   ```
   ```
   [*LSRD-isis-1] network-entity 10.0000.0000.0004.00
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
   [*LSRD] interface loopBack 0
   ```
   ```
   [*LSRD-LoopBack0] isis enable 1
   ```
   ```
   [*LSRD-LoopBack0] quit
   ```
   ```
   [*LSRD] commit
   ```
3. Configure MPLS and MPLS LDP globally and on interfaces on each node so that the network can forward MPLS traffic. Then, check information about established LSPs.
   
   
   
   # Configure LSRA.
   
   ```
   [~LSRA] mpls lsr-id 1.1.1.9
   ```
   ```
   [*LSRA] mpls
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] mpls ldp
   ```
   ```
   [*LSRA-mpls-ldp] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRA] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRA] commit
   ```
   
   # Configure LSRB.
   
   ```
   [~LSRB] mpls lsr-id 2.2.2.9
   ```
   ```
   [*LSRB] mpls
   ```
   ```
   [*LSRB-mpls] quit
   ```
   ```
   [*LSRB] mpls ldp
   ```
   ```
   [*LSRB-mpls-ldp] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRB] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRB-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRB] commit
   ```
   
   # Configure LSRC.
   
   ```
   [~LSRC] mpls lsr-id 3.3.3.9
   ```
   ```
   [*LSRC] mpls
   ```
   ```
   [*LSRC-mpls] quit
   ```
   ```
   [*LSRC] mpls ldp
   ```
   ```
   [*LSRC-mpls-ldp] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/1
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/1] quit
   ```
   ```
   [*LSRC] interface gigabitethernet 0/1/2
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*LSRC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*LSRC] commit
   ```
   
   # Configure LSRD.
   
   ```
   [~LSRD] mpls lsr-id 4.4.4.9
   ```
   ```
   [*LSRD] mpls
   ```
   ```
   [*LSRD-mpls] quit
   ```
   ```
   [*LSRD] mpls ldp
   ```
   ```
   [*LSRD-mpls-ldp] quit
   ```
   ```
   [*LSRD] interface gigabitethernet 0/1/0
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*LSRD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*LSRD] commit
   ```
   
   # After completing the configuration, run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command on LSRA to check information about the established LSP.
   
   ```
   [~LSRA] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.9/32         3/NULL          -/-                            
   2.2.2.9/32         NULL/3          -/GE0/1/0                      
   2.2.2.9/32         1024/3          -/GE0/1/0                      
   3.3.3.9/32         NULL/3          -/GE0/1/1                      
   3.3.3.9/32         1025/3          -/GE0/1/1                      
   4.4.4.9/32         NULL/1026       -/GE0/1/1                      
   4.4.4.9/32         1026/1026       -/GE0/1/1                      
   ```
   
   The command output shows that host routes with 32-bit masks are used to trigger LDP LSP establishment. This is the default triggering policy.
4. Enable IS-IS Auto FRR on LSRA and check routing information and backup LSP information.
   
   
   
   # Enable IS-IS Auto FRR on LSRA.
   
   ```
   [~LSRA] isis
   ```
   ```
   [~LSRA-isis-1] frr
   ```
   ```
   [*LSRA-isis-1-frr] loop-free-alternate
   ```
   ```
   [*LSRA-isis-1-frr] quit
   ```
   ```
   [*LSRA-isis-1] quit
   ```
   ```
   [*LSRA] commit
   ```
   
   # Display routing information of direct links between LSRA and LSRC and between LSRC and LSRD.
   
   ```
   [~LSRA] display ip routing-table 10.1.4.0 verbose
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination: 10.1.4.0/24
        Protocol: ISIS            Process ID: 1
      Preference: 15                    Cost: 20
         NextHop: 10.1.2.2         Neighbour: 0.0.0.0
           State: Active Adv             Age: 00h05m38s
             Tag: 0                 Priority: low
           Label: NULL               QoSInfo: 0x0
      IndirectID: 0x0
    RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/1/1
        TunnelID: 0x0                  Flags: D
       BkNextHop: 10.1.1.2       BkInterface: GigabitEthernet0/1/0
         BkLabel: NULL           SecTunnelID: 0x0
    BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
    BkIndirectID: 0x0
   ```
   
   The command output shows that a backup IS-IS route is generated after IS-IS Auto FRR is enabled.
   
   # Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command on LSRA to check LSP information.
   
   ```
   [~LSRA] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.9/32         3/NULL          -/-                            
   2.2.2.9/32         NULL/3          -/GE0/1/0                      
   2.2.2.9/32         23/3            -/GE0/1/0                      
      **LDP FRR**     NULL/17         -/GE0/1/1                      
      **LDP FRR**     23/17           -/GE0/1/1                      
   3.3.3.9/32         NULL/18         -/GE0/1/1                      
   3.3.3.9/32         24/18           -/GE0/1/1                      
      **LDP FRR**     NULL/18         -/GE0/1/0                      
      **LDP FRR**     24/18           -/GE0/1/0                      
   4.4.4.9/32         NULL/3          -/GE0/1/1                      
   4.4.4.9/32         25/3            -/GE0/1/1                      
      **LDP FRR**     NULL/19         -/GE0/1/0                      
      **LDP FRR**     25/19           -/GE0/1/0                      
   ```
   
   The command output shows that backup routes with 32-bit masks are used to trigger backup LDP LSP establishment. This is the default triggering policy.
5. Configure a policy to allow all routes to be used to trigger LDP LSP establishment and check LSP information.
   
   
   
   # Run the [**lsp-trigger**](cmdqueryname=lsp-trigger) command on LSRA to allow all routes to be used to trigger LDP LSP establishment and check LSP information.
   
   ```
   [~LSRA] mpls
   ```
   ```
   [~LSRA-mpls] lsp-trigger all
   ```
   ```
   [*LSRA-mpls] quit
   ```
   ```
   [*LSRA] commit
   ```
   
   # Run the [**lsp-trigger**](cmdqueryname=lsp-trigger) command on LSRB to allow all routes to be used to trigger LDP LSP establishment and check LSP information.
   
   ```
   [~LSRB] mpls
   ```
   ```
   [~LSRB-mpls] lsp-trigger all
   ```
   ```
   [*LSRB-mpls] quit
   ```
   ```
   [*LSRB] commit
   ```
   
   # Run the [**lsp-trigger**](cmdqueryname=lsp-trigger) command on LSRC to allow all routes to be used to trigger LDP LSP establishment and check LSP information.
   
   ```
   [~LSRC] mpls
   ```
   ```
   [~LSRC-mpls] lsp-trigger all
   ```
   ```
   [*LSRC-mpls] quit
   ```
   ```
   [*LSRC] commit
   ```
   
   # Run the [**lsp-trigger**](cmdqueryname=lsp-trigger) command on LSRD to allow all routes to be used to trigger LDP LSP establishment and check LSP information.
   
   ```
   [~LSRD] mpls
   ```
   ```
   [~LSRD-mpls] lsp-trigger all
   ```
   ```
   [*LSRD-mpls] quit
   ```
   ```
   [*LSRD] commit
   ```
   
   # Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command on LSRA to check LSP information.
   
   ```
   [~LSRA] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.9/32         3/NULL          -/-                            
   2.2.2.9/32         NULL/3          -/GE0/1/0                      
   2.2.2.9/32         23/3            -/GE0/1/0                      
      **LDP FRR**     NULL/17         -/GE0/1/1                      
      **LDP FRR**     23/17           -/GE0/1/1                      
   3.3.3.9/32         NULL/18         -/GE0/1/1                      
   3.3.3.9/32         24/18           -/GE0/1/1                      
      **LDP FRR**     NULL/18         -/GE0/1/0                      
      **LDP FRR**     24/18           -/GE0/1/0                      
   4.4.4.9/32         NULL/3          -/GE0/1/1                      
   4.4.4.9/32         25/3            -/GE0/1/1                      
      **LDP FRR**     NULL/19         -/GE0/1/0                      
      **LDP FRR**     25/19           -/GE0/1/0                      
   10.1.1.0/24        3/NULL          -/-                            
   10.1.2.0/24        3/NULL          -/-                            
   10.1.3.0/24        NULL/3          -/GE0/1/0                      
   10.1.3.0/24        28/3            -/GE0/1/0                      
   10.1.3.0/24        NULL/3          -/GE0/1/1                      
   10.1.3.0/24        28/3            -/GE0/1/1                      
   10.1.4.0/24        NULL/3          -/GE0/1/1                      
   10.1.4.0/24        29/3            -/GE0/1/1                      
   ```
   
   The command output shows that routes to addresses with 24-bit masks are used to trigger LSP establishment.
6. Configure a policy for triggering backup LDP LSP establishment based all routes.
   
   
   
   # Run the [**auto-frr lsp-trigger**](cmdqueryname=auto-frr+lsp-trigger) command on LSRA to allow LDP to use all backup routes to establish backup LSPs.
   
   ```
   [~LSRA] mpls ldp
   ```
   ```
   [~LSRA-mpls-ldp] auto-frr lsp-trigger all
   ```
   ```
   [*LSRA-mpls-ldp] quit
   ```
   ```
   [*LSRA] commit
   ```
7. Verify the configuration.
   
   
   
   After completing the preceding configuration, run the **display mpls lsp** command on LSRA to check information about backup LSPs.
   
   ```
   [~LSRA] display mpls lsp
   ```
   ```
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP 
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label    In/Out IF                      Vrf Name
   1.1.1.9/32         3/NULL          -/-                            
   2.2.2.9/32         NULL/3          -/GE0/1/0                      
   2.2.2.9/32         23/3            -/GE0/1/0                      
      **LDP FRR**     NULL/17         -/GE0/1/1                      
      **LDP FRR**     23/17           -/GE0/1/1                      
   3.3.3.9/32         NULL/18         -/GE0/1/1                      
   3.3.3.9/32         24/18           -/GE0/1/1                      
      **LDP FRR**     NULL/18         -/GE0/1/0                      
      **LDP FRR**     24/18           -/GE0/1/0                      
   4.4.4.9/32         NULL/3          -/GE0/1/1                      
   4.4.4.9/32         25/3            -/GE0/1/1                      
      **LDP FRR**     NULL/19         -/GE0/1/0                      
      **LDP FRR**     25/19           -/GE0/1/0                      
   10.1.1.0/24        3/NULL          -/-                            
   10.1.2.0/24        3/NULL          -/-                            
   10.1.3.0/24        NULL/3          -/GE0/1/0                      
   10.1.3.0/24        28/3            -/GE0/1/0                      
   10.1.3.0/24        NULL/3          -/GE0/1/1                      
   10.1.3.0/24        28/3            -/GE0/1/1                      
   10.1.4.0/24        NULL/3          -/GE0/1/1                      
   10.1.4.0/24        29/3            -/GE0/1/1                      
      **LDP FRR**     NULL/26         -/GE0/1/0                      
      **LDP FRR**     29/26           -/GE0/1/0                      
   ```
   
   The command output shows that a backup LSP has been established for the primary LSP on the direct link LSRA -> LSRC -> LSRD.

#### Configuration Files

* LSRA configuration file
  
  ```
  #
  sysname LSRA
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
   lsp-trigger all
  #
  mpls ldp
   #
   ipv4-family
    auto-frr lsp-trigger all
  #
  isis 1
   frr
    loop-free-alternate level-1
    loop-free-alternate level-2
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 1.1.1.9 255.255.255.255
   isis enable 1
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
   lsp-trigger all
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
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
   lsp-trigger all
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.3.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
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
   lsp-trigger all
  #
  mpls ldp
   #
   ipv4-family
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.4.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 4.4.4.9 255.255.255.255
   isis enable 1
  #
  return
  ```