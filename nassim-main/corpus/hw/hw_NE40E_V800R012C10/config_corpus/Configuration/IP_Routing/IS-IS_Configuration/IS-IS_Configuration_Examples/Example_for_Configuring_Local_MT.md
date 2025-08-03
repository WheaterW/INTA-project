Example for Configuring Local MT
================================

This section provides an example showing how to configure local MT on IS-IS networks so that multicast packets can be transmitted on a TE tunnel.

#### Networking Requirements

When both multicast and IGP shortcut-capable MPLS TE tunnel are configured on a network, the outbound interface of the route calculated by IS-IS using SPF may not be a physical interface but a TE tunnel interface that is up. Multicast packets are forwarded through the TE tunnel according to the IS-IS routing table. Consequently, the Router bypassed by the TE tunnel is unaware of the multicast packets, unable to generate multicast forwarding entries. As a result, these multicast packets are discarded.

Local MT allows a separate multicast topology to be created on the local device. When the outbound interface of a route calculated by an IGP is an IGP Shortcut-enabled (AA) TE tunnel interface, one or a group of physical outbound interfaces are calculated for the route, resolving the conflict between a TE tunnel and multicast.

As shown in [Figure 1](#EN-US_TASK_0172366119__fig_dc_vrp_isis_cfg_011601):

* DeviceA, DeviceB, DeviceC, DeviceD, and DeviceE run IS-IS, and they are Level-2 devices.
* A TE tunnel is established between DeviceB and DeviceD.
* IGP Shortcut is enabled on DeviceB.

**Figure 1** Local IS-IS MT networking  
![](images/fig_dc_vrp_isis_cfg_011601.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE0/1/0 | 172.16.1.1/24 |
| GE0/2/0 | 10.0.0.1/24 |
| DeviceB | GE0/1/0 | 10.0.0.2/24 |
| GE0/2/0 | 10.0.1.2/24 |
| DeviceC | GE0/1/0 | 10.0.1.1/24 |
| GE0/2/0 | 10.0.2.2/24 |
| DeviceD | GE0/1/0 | 10.0.3.1/24 |
| GE0/2/0 | 10.0.2.1/24 |
| DeviceE | GE0/1/0 | 10.0.3.3/24 |
| GE0/2/0 | 192.168.3.1/24 |



#### Precautions

To improve security, you are advised to configure IS-IS authentication. For details, see "Configuring IS-IS Authentication." IS-IS interface authentication is used as an example. For details, see Example for Configuring Basic IS-IS Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic IS-IS functions on each Router.
2. Configure the Protocol Independent Multicast Sparse Mode (PIM-SM).
3. Configure an MPLS Resource Reservation Protocol (RSVP) TE tunnel and enable IGP Shortcut.
4. Enable local MT.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of each Router interface (as shown in [Figure 1](#EN-US_TASK_0172366119__fig_dc_vrp_isis_cfg_011601)), area address 10, system ID starting from 0000.0000.0001, and level (Level-2) of the Routers
* Tunnel interface TE Tunnel 10, IP address of Loopback 0, tunnel encapsulation protocol MPLS TE, destination address 4.4.4.4, and tunnel ID 100

#### Procedure

1. Assign an IP address for each interface and enable IS-IS.
   
   
   
   In [Figure 1](#EN-US_TASK_0172366119__fig_dc_vrp_isis_cfg_011601), assign an IP address and the mask for each interface and enable IS-IS. For configuration details, see [Configuration Files](#EN-US_TASK_0172366119__section_dc_vrp_isis_cfg_011605) in this section.
2. Configure PIM-SM.
   
   
   
   # Enable multicast on all Routers and enable PIM-SM on all interfaces. The configurations on DeviceB, DeviceC, DeviceD, and DeviceE are similar to those on DeviceA. For detailed configurations, see Configuration Files.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Enable IGMP on the interface through which DeviceA is connected to hosts.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] igmp version 3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   
   # Configure a C-BSR and a C-RP. Set the service range of the RP on DeviceD and specify the locations of the C-BSR and the C-RP.
   
   ```
   [~DeviceD] pim
   ```
   ```
   [*DeviceD-pim] c-bsr LoopBack0
   ```
   ```
   [*DeviceD-pim] c-rp LoopBack0
   ```
   ```
   [*DeviceD-pim] commit
   ```
   
   # Run the **display multicast routing-table** command to view the multicast routing table of a Router. DeviceC is used as an example:
   
   ```
   [~DeviceC] display multicast routing-table
   Multicast routing table of VPN-Instance: public net
    Total 1 entry
   
    00001. (192.168.3.2, 224.31.31.31)
          Uptime: 15:03:04
          Upstream Interface: GigabitEthernet0/2/0
          List of 1 downstream interface
              1:  GigabitEthernet0/1/0
   ```
3. Configure an MPLS RSVP-TE tunnel.
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] mpls lsr-id 2.2.2.2
   ```
   ```
   [*DeviceB] mpls
   ```
   ```
   [*DeviceB-mpls] mpls te
   ```
   ```
   [*DeviceB-mpls] mpls rsvp-te
   ```
   ```
   [*DeviceB-mpls] mpls te cspf
   ```
   ```
   [*DeviceB-mpls] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] mpls rsvp-te
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] cost-style wide
   ```
   ```
   [*DeviceB-isis-1] traffic-eng level-2
   ```
   ```
   [*DeviceB-isis-1] commit
   ```
   ```
   [~DeviceB-isis-1] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] mpls lsr-id 3.3.3.3
   ```
   ```
   [*DeviceC] mpls
   ```
   ```
   [*DeviceC-mpls] mpls te
   ```
   ```
   [*DeviceC-mpls] mpls rsvp-te
   ```
   ```
   [*DeviceC-mpls] mpls te cspf
   ```
   ```
   [*DeviceC-mpls] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] mpls te
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] mpls rsvp-te
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] cost-style wide
   ```
   ```
   [*DeviceC-isis-1] traffic-eng level-2
   ```
   ```
   [*DeviceC-isis-1] commit
   ```
   ```
   [~DeviceC-isis-1] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] mpls lsr-id 4.4.4.4
   ```
   ```
   [*DeviceD] mpls
   ```
   ```
   [*DeviceD-mpls] mpls te
   ```
   ```
   [*DeviceD-mpls] mpls rsvp-te
   ```
   ```
   [*DeviceD-mpls] mpls te cspf
   ```
   ```
   [*DeviceD-mpls] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] mpls te
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] mpls rsvp-te
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] cost-style wide
   ```
   ```
   [*DeviceD-isis-1] traffic-eng level-2
   ```
   ```
   [*DeviceD-isis-1] commit
   ```
   ```
   [~DeviceD-isis-1] quit
   ```
   
   # Configure an MPLS TE tunnel and enable IGP Shortcut.
   
   Configure an MPLS TE tunnel on DeviceB and enable IGP Shortcut.
   
   ```
   [~DeviceB] interface Tunnel 10
   ```
   ```
   [~DeviceB-Tunnel10] ip address unnumbered interface loopback 0
   ```
   ```
   [*DeviceB-Tunnel10] tunnel-protocol mpls te
   ```
   ```
   [*DeviceB-Tunnel10] destination 4.4.4.4
   ```
   ```
   [*DeviceB-Tunnel10] mpls te tunnel-id 100
   ```
   ```
   [*DeviceB-Tunnel10] mpls te igp shortcut isis
   ```
   ```
   [*DeviceB-Tunnel10] mpls te igp metric relative -10
   ```
   ```
   [*DeviceB-Tunnel10] isis enable 1
   ```
   ```
   [*DeviceB-Tunnel10] commit
   ```
   ```
   [~DeviceB-Tunnel10] quit
   ```
   
   # Display the routing table on DeviceB. You can find that IGP Shortcut is enabled.
   
   ```
   [~DeviceB] display isis route
   
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
    IPV4 Destination     IntCost    ExtCost ExitInterface   NextHop          Flags
   --------------------------------------------------------------------------------
    3.3.3.3/32           10         NULL    GE0/2/0         10.0.1.1       A/-/-/-
    172.16.1.0/24        20         NULL    GE0/1/0         10.0.0.1       A/-/-/-
    2.2.2.2/32           0          NULL    Loop0           Direct         D/-/L/-
    192.168.3.0/24       25         NULL    Tun0/1/0        2.2.2.2        A/S/-/-
    5.5.5.5/32           15         NULL    Tun0/1/0        2.2.2.2        A/S/-/-
    10.0.0.0/24          10         NULL    GE0/1/0         Direct         D/-/L/-
    10.0.1.0/24          10         NULL    GE0/2/0         Direct         D/-/L/-
    4.4.4.4/32           5          NULL    Tun0/1/0        2.2.2.2        A/S/-/-
    10.0.2.0/24          15         NULL    Tun0/1/0        2.2.2.2        A/S/-/-
    10.0.3.0/24          15         NULL    Tun0/1/0        2.2.2.2        A/S/-/-
   
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                  U-Up/Down Bit Set, LP-Local Prefix-Sid
        Protect Type: L-Link Protect, N-Node Protect
   ```
   
   # Check the multicast routing table on DeviceC bypassed by the TE tunnel.
   
   ```
   [~DeviceC] display multicast routing-table
   ```
   
   No multicast routing entry is displayed, indicating that multicast packets have been discarded.
4. Configure local MT.
   
   
   
   # Enable local MT on DeviceB.
   
   ```
   [~DeviceB] isis
   ```
   ```
   [~DeviceB-isis-1] local-mt enable
   ```
   ```
   [*DeviceB-isis-1] commit
   ```
5. Verify the configuration.
   
   
   
   # Display the multicast routing table on DeviceC again. The command output shows that multicast routes are displayed.
   
   ```
   [~DeviceC] display multicast routing-table
   Multicast routing table of VPN-Instance: public net
    Total 1 entry
   
    00001. (192.168.3.2, 224.31.31.31)
          Uptime: 00:00:19
          Upstream Interface: GigabitEthernet0/2/0
          List of 1 downstream interface
              1:  GigabitEthernet0/1/0
   ```
   
   # Display the MIGP routing table on DeviceB.
   
   ```
   [~DeviceB] display migp routing-table
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table: MIGP
            Destinations : 5        Routes : 5
   
   Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface
   
         4.4.4.4/32    ISIS   15   20             10.0.1.1        GE0/2/0
         5.5.5.5/32    ISIS   15   30             10.0.1.1        GE0/2/0
        10.0.2.0/24    ISIS   15   20             10.0.1.1        GE0/2/0
        10.0.3.0/24    ISIS   15   30             10.0.1.1        GE0/2/0
     192.168.3.0/24    ISIS   15   40             10.0.1.1        GE0/2/0
   ```
   
   The MIGP routing table shows that the original outbound interface (TE tunnel interface) has been replaced with a physical interface.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  router id 1.1.1.1
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
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
   network-entity 10.0000.0000.0001.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.0.0.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 172.16.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
   igmp version 3
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  router id 2.2.2.2
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
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
   mpls te cspf
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
   network-entity 10.0000.0000.0002.00
  ```
  ```
   traffic-eng level-2
  ```
  ```
   local-mt enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.0.0.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.0.1.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
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
  interface LoopBack0
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface Tunnel10
  ```
  ```
   ip address unnumbered interface LoopBack0
  ```
  ```
   tunnel-protocol mpls te
  ```
  ```
   destination 4.4.4.4
  ```
  ```
   mpls te tunnel-id 100
  ```
  ```
   mpls te igp shortcut isis
  ```
  ```
   mpls te igp metric relative -10
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   C-BSR LoopBack0
  ```
  ```
   C-RP LoopBack0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  router id 3.3.3.3
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
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
   mpls te cspf
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
   network-entity 10.0000.0000.0003.00
  ```
  ```
   traffic-eng level-2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.0.1.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
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
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.0.2.2 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
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
  interface LoopBack0
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
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  router id 4.4.4.4
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
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
   mpls te cspf
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
   network-entity 10.0000.0000.0004.00
  ```
  ```
   traffic-eng level-2
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.0.3.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 10.0.2.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
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
  interface LoopBack0
  ```
  ```
   ip address 4.4.4.4 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   C-BSR LoopBack0
  ```
  ```
   C-RP LoopBack0
  ```
  ```
  #
  ```
  ```
  return
  ```
* DeviceE configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceE
  ```
  ```
  #
  ```
  ```
  router id 5.5.5.5
  ```
  ```
  #
  ```
  ```
  multicast routing-enable
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
   network-entity 10.0000.0000.0005.00
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   ip address 10.0.3.3 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   ip address 192.168.3.1 255.255.255.0
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 5.5.5.5 255.255.255.255
  ```
  ```
   isis enable 1
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  return
  ```