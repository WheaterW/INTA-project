Example for Configuring a DCI Scenario with EVPN VXLAN Accessing MPLS EVPN IRB
==============================================================================

This section provides an example for configuring a DCI scenario with EVPN VXLAN accessing MPLS EVPN IRB. In this example, DC GWs connect to the DCI backbone network over VXLAN tunnels and BGP EVPN is deployed on the DCI backbone network to achieve DC interworking.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370649__fig_dc_vrp_dci_cfg_003001), the DC GWs GW1 and GW2 are connected to the DCI backbone network with BGP EVPN configured. After EVPN and VXLAN tunnels are deployed between the DC GWs and DCI-PEs, VM host IP routes can be exchanged between different DCs, implementing communication between DC A and DC B (for example, communication between VMa1 and VMb2).

**Figure 1** Configuring a DCI scenario with EVPN VXLAN accessing MPLS EVPN IRB![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_dci_cfg_003001.png)  

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| DCI-PE1 | GigabitEthernet 0/1/0 | 192.168.20.1 |
| GigabitEthernet 0/2/0 | 192.168.1.1/24 |
| LoopBack1 | 1.1.1.1/32 |
| LoopBack2 | 11.11.11.11/32 |
| P | GigabitEthernet 0/1/0 | 192.168.1.2/24 |
| GigabitEthernet 0/2/0 | 192.168.10.1/24 |
| LoopBack1 | 2.2.2.2/32 |
| DCI-PE2 | GigabitEthernet 0/1/0 | 192.168.30.1 |
| GigabitEthernet 0/2/0 | 192.168.10.2/24 |
| LoopBack1 | 3.3.3.3/32 |
| LoopBack2 | 33.33.33.33/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on the DCI backbone network to implement communication between DCI-PEs.
2. Configure an MPLS TE tunnel on the DCI backbone network.
3. Configure static routes destined for the loopback interface addresses of DC GWs on DCI-PEs.
4. Configure an EVPN instance and a BD on each DCI-PE.
5. Configure a source address on each DCI-PE.
6. Configure the DCI-PEs to establish a BGP EVPN peer relationship with each other and with DC GWs.
7. Configure a VPN instance on each DCI-PE.
8. Configure VXLAN tunnels between the DCI-PEs and DC GWs.
9. Apply the tunnel policy.
10. Configure route re-origination on each DCI-PE.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the DCI-PEs and P
* VPN instance RD
* VPN targets used for route import and export by the VPN instance
* EVPN instance RD
* VPN targets used for route import and export by the EVPN instance

#### Procedure

1. Configure interface IP addresses, including loopback interface addresses, on each node.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172370649__dc_vrp_dci_cfg_003001).
2. Configure an IGP on the DCI backbone network. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370649__dc_vrp_dci_cfg_003001).
3. Configure a TE tunnel on the DCI backbone network.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370649__dc_vrp_dci_cfg_003001).
4. Configure static routes destined for the loopback interface addresses of DC GWs on DCI-PEs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370649__dc_vrp_dci_cfg_003001).
5. Configure an EVPN instance and a BD on each DCI-PE.
   
   
   
   # Configure DCI-PE1.
   
   ```
   [~DCI-PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*DCI-PE1-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*DCI-PE1-evpn-instance-evrf1] vpn-target 11:1 both
   ```
   ```
   [*DCI-PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*DCI-PE1] bridge-domain 10
   ```
   ```
   [*DCI-PE1-bd10] vxlan vni 5010 split-horizon-mode
   ```
   ```
   [*DCI-PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*DCI-PE1-bd10] esi 0000.1111.1111.4444.5555
   ```
   ```
   [*DCI-PE1-bd10] quit
   ```
   ```
   [*DCI-PE1] interface GigabitEthernet 0/1/0.1 mode l2
   ```
   ```
   [*DCI-PE1-GigabitEthernet0/1/0.1] encapsulation qinq
   ```
   ```
   [*DCI-PE1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*DCI-PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*DCI-PE1] commit
   ```
   
   # Configure DCI-PE2.
   
   ```
   [~DCI-PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*DCI-PE2-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*DCI-PE2-evpn-instance-evrf1] vpn-target 11:1 both
   ```
   ```
   [*DCI-PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*DCI-PE2] bridge-domain 10
   ```
   ```
   [*DCI-PE2-bd10] vxlan vni 5020 split-horizon-mode
   ```
   ```
   [*DCI-PE2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*DCI-PE2-bd10] esi 0000.1111.3333.4444.5555
   ```
   ```
   [*DCI-PE2-bd10] quit
   ```
   ```
   [*DCI-PE2] interface GigabitEthernet 0/1/0.1 mode l2
   ```
   ```
   [*DCI-PE2-GigabitEthernet0/1/0.1] encapsulation qinq
   ```
   ```
   [*DCI-PE2-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*DCI-PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*DCI-PE2] commit
   ```
6. Configure a source address on each DCI-PE.
   
   
   
   # Configure DCI-PE1.
   
   ```
   [~DCI-PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*DCI-PE1] commit
   ```
   
   # Configure DCI-PE2.
   
   ```
   [~DCI-PE2] evpn source-address 3.3.3.3
   ```
   ```
   [*DCI-PE2] commit
   ```
7. Configure the DCI-PEs to establish a BGP EVPN peer relationship with each other and with DC GWs.
   
   
   
   # Configure DCI-PE1.
   
   ```
   [~DCI-PE1] bgp 100
   ```
   ```
   [*DCI-PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*DCI-PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*DCI-PE1-bgp] peer 4.4.4.4 as-number 65410
   ```
   ```
   [*DCI-PE1-bgp] peer 4.4.4.4 ebgp-max-hop 255
   ```
   ```
   [*DCI-PE1-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*DCI-PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 advertise encap-type vxlan
   ```
   ```
   [*DCI-PE1-bgp-af-evpn] quit
   ```
   ```
   [*DCI-PE1-bgp] quit
   ```
   ```
   [*DCI-PE1] commit
   ```
   
   # Configure DCI-PE2.
   
   ```
   [~DCI-PE2] bgp 100
   ```
   ```
   [*DCI-PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DCI-PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*DCI-PE2-bgp] peer 5.5.5.5 as-number 65420
   ```
   ```
   [*DCI-PE2-bgp] peer 5.5.5.5 ebgp-max-hop 255
   ```
   ```
   [*DCI-PE2-bgp] peer 5.5.5.5 connect-interface loopback 1
   ```
   ```
   [*DCI-PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 enable
   ```
   ```
   [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 advertise encap-type vxlan
   ```
   ```
   [*DCI-PE2-bgp-af-evpn] quit
   ```
   ```
   [*DCI-PE2-bgp] quit
   ```
   ```
   [*DCI-PE2] commit
   ```
8. Configure a VPN instance.
   
   
   
   # Configure DCI-PE1.
   
   ```
   [~DCI-PE1] ip vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 11:11
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1-af-ipv4] vpn-target 11:1 both evpn
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1] vxlan vni 555
   ```
   ```
   [*DCI-PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*DCI-PE1] interface Vbdif10
   ```
   ```
   [*DCI-PE1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-Vbdif10] ip address 10.10.10.1 255.255.255.0
   ```
   ```
   [*DCI-PE1-Vbdif10] arp collect host enable
   ```
   ```
   [*DCI-PE1-Vbdif10] quit
   ```
   ```
   [*DCI-PE1] commit
   ```
   
   # Configure DCI-PE2.
   
   ```
   [~DCI-PE2] ip vpn-instance vpn1
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 11:11
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1-af-ipv4] vpn-target 11:1 both evpn
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1] vxlan vni 555
   ```
   ```
   [*DCI-PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*DCI-PE2] interface Vbdif10
   ```
   ```
   [*DCI-PE2-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*DCI-PE2-Vbdif10] ip address 10.20.10.1 255.255.255.0
   ```
   ```
   [*DCI-PE2-Vbdif10] arp collect host enable
   ```
   ```
   [*DCI-PE2-Vbdif10] quit
   ```
   ```
   [*DCI-PE2] commit
   ```
9. Configure VXLAN tunnels between the DCI-PEs and DC GWs.
   
   
   
   # Configure DCI-PE1.
   
   ```
   [~DCI-PE1] interface nve 1
   ```
   ```
   [*DCI-PE1-Nve1] source 11.11.11.11
   ```
   ```
   [*DCI-PE1-Nve1] quit
   ```
   ```
   [*DCI-PE1] commit
   ```
   
   # Configure DCI-PE2.
   
   ```
   [~DCI-PE2] interface nve 1
   ```
   ```
   [*DCI-PE2-Nve1] source 33.33.33.33
   ```
   ```
   [*DCI-PE2-Nve1] quit
   ```
   ```
   [*DCI-PE2] commit
   ```
10. Apply a tunnel policy.
    
    
    
    # Configure DCI-PE1.
    
    ```
    [~DCI-PE1] tunnel-policy te-lsp1
    ```
    ```
    [*DCI-PE1-tunnel-policy-te-lsp1] tunnel select-seq cr-lsp load-balance-number 1
    ```
    ```
    [*DCI-PE1-tunnel-policy-te-lsp1] quit
    ```
    ```
    [*DCI-PE1] ip vpn-instance vpn1
    ```
    ```
    [*DCI-PE1-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*DCI-PE1-vpn-instance-vpn1-af-ipv4] tnl-policy te-lsp1 evpn
    ```
    ```
    [*DCI-PE1-vpn-instance-vpn1-af-ipv4] quit
    ```
    ```
    [*DCI-PE1-vpn-instance-vpn1] quit
    ```
    ```
    [*DCI-PE1] evpn vpn-instance evrf1 bd-mode
    ```
    ```
    [*DCI-PE1-evpn-instance-evrf1] tnl-policy te-lsp1
    ```
    ```
    [*DCI-PE1-evpn-instance-evrf1] quit
    ```
    ```
    [*DCI-PE1] commit
    ```
    
    # Configure DCI-PE2.
    
    ```
    [~DCI-PE2] tunnel-policy te-lsp1
    ```
    ```
    [*DCI-PE2-tunnel-policy-te-lsp1] tunnel select-seq cr-lsp load-balance-number 1
    ```
    ```
    [*DCI-PE2-tunnel-policy-te-lsp1] quit
    ```
    ```
    [*DCI-PE2] ip vpn-instance vpn1
    ```
    ```
    [*DCI-PE2-vpn-instance-vpn1] ipv4-family
    ```
    ```
    [*DCI-PE2-vpn-instance-vpn1-af-ipv4] tnl-policy te-lsp1 evpn
    ```
    ```
    [*DCI-PE2-vpn-instance-vpn1-af-ipv4] quit
    ```
    ```
    [*DCI-PE2-vpn-instance-vpn1] quit
    ```
    ```
    [*DCI-PE2] evpn vpn-instance evrf1 bd-mode
    ```
    ```
    [*DCI-PE2-evpn-instance-evrf1] tnl-policy te-lsp1
    ```
    ```
    [*DCI-PE2-evpn-instance-evrf1] quit
    ```
    ```
    [*DCI-PE2] commit
    ```
11. Enable each DCI-PE to advertise re-originated routes to its EVPN peer.
    
    
    
    # Configure DCI-PE1.
    
    ```
    [~DCI-PE1] bgp 100
    ```
    ```
    [*DCI-PE1-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCI-PE1-bgp-vpn1] import-route direct
    ```
    ```
    [*DCI-PE1-bgp-vpn1] advertise l2vpn evpn
    ```
    ```
    [*DCI-PE1-bgp-vpn1] quit
    ```
    ```
    [*DCI-PE1-bgp] l2vpn-family evpn
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 import reoriginate
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated evpn mac-ip
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated evpn mac
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated evpn ip
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 3.3.3.3 advertise irb
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 import reoriginate
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 advertise route-reoriginated evpn mac-ip
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 advertise route-reoriginated evpn ip
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] peer 4.4.4.4 advertise irb
    ```
    ```
    [*DCI-PE1-bgp-af-evpn] quit
    ```
    ```
    [*DCI-PE1-bgp] quit
    ```
    ```
    [*DCI-PE1] commit
    ```
    
    # Configure DCI-PE2.
    
    ```
    [~DCI-PE2] bgp 100
    ```
    ```
    [*DCI-PE2-bgp] ipv4-family vpn-instance vpn1
    ```
    ```
    [*DCI-PE2-bgp-vpn1] import-route direct
    ```
    ```
    [*DCI-PE2-bgp-vpn1] advertise l2vpn evpn
    ```
    ```
    [*DCI-PE2-bgp-vpn1] quit
    ```
    ```
    [*DCI-PE2-bgp] l2vpn-family evpn
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 import reoriginate
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn mac-ip
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn mac
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 advertise route-reoriginated evpn ip
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 1.1.1.1 advertise irb
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 import reoriginate
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 advertise route-reoriginated evpn mac-ip
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 advertise route-reoriginated evpn ip
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] peer 5.5.5.5 advertise irb
    ```
    ```
    [*DCI-PE2-bgp-af-evpn] quit
    ```
    ```
    [*DCI-PE2-bgp] quit
    ```
    ```
    [*DCI-PE2] commit
    ```
12. Verify the configuration.
    
    
    
    Run the **display ip routing-table vpn-instance vpn1** command on a DCI-PE to check VPN routes. The command output shows that routes received from the peer DC GW recurse to the VXLAN tunnel and routes received from the remote DCI-PE recurse to the MPLS TE tunnel. The following example uses the command output on DCI-PE1.
    
    ```
    [~DCI-PE1] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 4        Routes : 4         
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
           10.1.1.0/24  EBGP    255  0             RD  4.4.4.4         VXLAN
           10.2.1.0/24  IBGP    255  0             RD  3.3.3.3         Tunnel1
          127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```

#### Configuration Files

* DCI-PE1 configuration file
  
  ```
  #
  sysname DCI-PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   tnl-policy te-lsp1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy te-lsp1 evpn
    evpn mpls routing-enable
   vxlan vni 555
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  bridge-domain 10
   vxlan vni 5010 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.10.10.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.20.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation qinq
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface LoopBack2
   ip address 11.11.11.11 255.255.255.255
  #
  interface Nve1
   source 11.11.11.11
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te tunnel-id 100
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 4.4.4.4 as-number 65410
   peer 4.4.4.4 ebgp-max-hop 255
   peer 4.4.4.4 connect-interface LoopBack2
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
    peer 3.3.3.3 import reoriginate
    peer 3.3.3.3 advertise route-reoriginated evpn mac-ip
    peer 3.3.3.3 advertise route-reoriginated evpn mac
    peer 3.3.3.3 advertise route-reoriginated evpn ip
    peer 4.4.4.4 enable
    peer 4.4.4.4 advertise irb
    peer 4.4.4.4 advertise encap-type vxlan
    peer 4.4.4.4 import reoriginate
    peer 4.4.4.4 advertise route-reoriginated evpn mac-ip
    peer 4.4.4.4 advertise route-reoriginated evpn ip
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    mpls-te enable
  #
  ip route-static 4.4.4.4 255.255.255.255 192.168.20.2
  #
  tunnel-policy te-lsp1
   tunnel select-seq cr-lsp load-balance-number 1
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.10.0 0.0.0.255
    mpls-te enable
  #
  return
  ```
* DCI-PE2 configuration file
  
  ```
  #
  sysname DCI-PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   tnl-policy te-lsp1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy te-lsp1 evpn
    evpn mpls routing-enable
   vxlan vni 555
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  bridge-domain 10
   vxlan vni 5020 split-horizon-mode
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ip address 10.20.10.1 255.255.255.0
   arp collect host enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.30.1 255.255.255.0
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation qinq
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.2 255.255.255.0
   mpls           
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface LoopBack2
   ip address 33.33.33.33 255.255.255.255
  #
  interface Nve1
   source 33.33.33.33
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te tunnel-id 100
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 5.5.5.5 as-number 65420
   peer 5.5.5.5 ebgp-max-hop 255
   peer 5.5.5.5 connect-interface LoopBack2
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irb
    peer 1.1.1.1 import reoriginate
    peer 1.1.1.1 advertise route-reoriginated evpn mac-ip
    peer 1.1.1.1 advertise route-reoriginated evpn mac
    peer 1.1.1.1 advertise route-reoriginated evpn ip
    peer 5.5.5.5 enable
    peer 5.5.5.5 advertise irb
    peer 5.5.5.5 advertise encap-type vxlan
    peer 5.5.5.5 import reoriginate
    peer 5.5.5.5 advertise route-reoriginated evpn mac-ip
    peer 5.5.5.5 advertise route-reoriginated evpn ip
  #
  ospf 1          
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.10.0 0.0.0.255
    mpls-te enable
  #
  ip route-static 5.5.5.5 255.255.255.255 192.168.30.2
  #
  tunnel-policy te-lsp1
   tunnel select-seq cr-lsp load-balance-number 1
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* GW1 configuration file
  
  See the configuration file of a DC device.
* Device1 configuration file
  
  See the configuration file of a DC device.
* Device2 configuration file
  
  See the configuration file of a DC device.
* GW2 configuration file
  
  See the configuration file of a DC device.
* Device3 configuration file
  
  See the configuration file of a DC device.
* Device4 configuration file
  
  See the configuration file of a DC device.