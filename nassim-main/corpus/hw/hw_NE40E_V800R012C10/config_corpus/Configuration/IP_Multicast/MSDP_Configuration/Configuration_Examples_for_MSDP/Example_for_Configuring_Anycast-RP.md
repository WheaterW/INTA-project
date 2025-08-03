Example for Configuring Anycast-RP
==================================

If there are multiple multicast sources and receivers in a PIM-SM domain, you can configure MSDP peer relationships between Candidate-Rendezvous Points (C-RPs) and configure Anycast-RP to implement load sharing.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367032__fig_dc_vrp_multicast_cfg_007501), the PIM-SM domain has multiple multicast sources and receivers. To implement RP load balancing, configure MSDP peer relationships and configure Anycast-RP.

**Figure 1** Configuring Anycast-RP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_007501.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| Device A | GigabitEthernet0/1/0 | 10.110.5.1/24 |
| GigabitEthernet0/2/0 | 10.110.1.2/24 |
| DeviceB | GigabitEthernet0/1/0 | 10.110.6.1/24 |
| GigabitEthernet0/2/0 | 10.110.2.2/24 |
| DeviceC | GigabitEthernet0/1/0 | 192.168.1.1/24 |
| GigabitEthernet0/2/0 | 10.110.1.1/24 |
| GigabitEthernet0/3/0 | 10.110.4.1/24 |
| Loopback0 | 1.1.1.1/32 |
| Loopback1 | 3.3.3.3/32 |
| Loopback10 | 10.1.1.1/32 |
| DeviceD | GigabitEthernet0/1/0 | 192.168.3.1/24 |
| GigabitEthernet0/2/0 | 10.110.2.1/24 |
| GigabitEthernet0/3/0 | 10.110.3.1/24 |
| Loopback0 | 2.2.2.2/32 |
| Loopback1 | 4.4.4.4/32 |
| Loopback10 | 10.1.1.1/32 |
| DeviceE | GigabitEthernet0/1/0 | 192.168.3.2/24 |
| GigabitEthernet0/2/0 | 192.168.1.2/24 |



#### Precautions

When configuring Anycast-RP, note the following precautions:

* PIM-SM must be enabled before IGMP is enabled.
* You need to configure RPs on Loopback interfaces.
* Before configuring Loopback interfaces as C-RPs, enable PIM-SM on the Loopback interfaces.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each Router interface and configure OSPF in the PIM-SM to ensure that unicast routes are reachable between Routers in the domain.
2. Enable multicast routing, enable PIM-SM on each interface, and enable IGMP on interfaces that connect to hosts.
3. Configure the same address for Loopback 10 on DeviceC and DeviceD and configure Loopback 10 on them as C-RPs; configure Loopback 1 as the C-BSR.
4. Configure MSDP peers on Loopback 0 of DeviceC and DeviceD. MSDP accepts the source active (SA) messages received from the source RP based on RPF rules.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address
* Router ID of Device C
* Router ID of Device D

#### Procedure

1. Configure an IP address for each interface and a unicast routing protocol on the Routers. For configuration details, see Configuration Files in this section.
   
   
   
   # Configure an IP address and mask to each Router interface based on [Figure 1](#EN-US_TASK_0172367032__fig_dc_vrp_multicast_cfg_007501) in the PIM-SM domain. Configure OSPF for interworking between Routers. For configuration details, see Configuration Files in this section.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
   
   
   
   # Enable the multicast function on DeviceC and PIM-SM on involved interfaces.
   
   The configurations of other Routers are similar to the configuration of DeviceC. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceC] multicast routing-enable
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] quit
   ```
3. Enable IGMP on interfaces connected to hosts. For configuration details, see Configuration Files in this section.
4. Configure Loopback 1 and Loopback 10 and configure C-BSRs and C-RPs.
   
   
   
   # Configure the same address for Loopback 1 and the same address for Loopback 10 on DeviceC and DeviceD; configure Loopback 1 as the C-BSR and Loopback 10 as the C-RP.
   
   The configuration of DeviceD is similar to the configuration of DeviceC. For configuration details, see Configuration Files in this section.
   
   ```
   [~DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] ip address 3.3.3.3 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack1] pim sm
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   ```
   [*DeviceC] interface loopback 10
   ```
   ```
   [*DeviceC-LoopBack10] ip address 10.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack10] pim sm
   ```
   ```
   [*DeviceC-LoopBack10] quit
   ```
   ```
   [*DeviceC] pim
   ```
   ```
   [*DeviceC-pim] c-bsr loopback 1
   ```
   ```
   [*DeviceC-pim] c-rp loopback 10
   ```
   ```
   [*DeviceC-pim] commit
   ```
   ```
   [~DeviceC-pim] quit
   ```
5. Configure loopback 0 interfaces and MSDP peers.
   
   
   
   # Configure an MSDP peer on Loopback 0 on Device C.
   
   ```
   [~DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceC-LoopBack0] pim sm
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] msdp
   ```
   ```
   [*DeviceC-msdp] originating-rp loopback0
   ```
   ```
   [*DeviceC-msdp] peer 2.2.2.2 connect-interface loopback0
   ```
   ```
   [*DeviceC-msdp] commit
   ```
   ```
   [~DeviceC-msdp] quit
   ```
   
   # Configure an MSDP peer on Loopback 0 on Device D.
   
   ```
   [~DeviceD] interface loopback 0
   ```
   ```
   [*DeviceD-LoopBack0] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*DeviceD-LoopBack0] pim sm
   ```
   ```
   [*DeviceD-LoopBack0] commit
   ```
   ```
   [~DeviceD-LoopBack0] quit
   ```
   ```
   [~DeviceD] msdp
   ```
   ```
   [*DeviceD-msdp] originating-rp loopback0
   ```
   ```
   [*DeviceD-msdp] peer 1.1.1.1 connect-interface loopback0
   ```
   ```
   [*DeviceD-msdp] commit
   ```
   ```
   [~DeviceD-msdp] quit
   ```
6. Verify the configuration.
   
   
   
   # Run the **display msdp brief** command. The command output shows MSDP peer relationships established between Routers. The detailed information about MSDP peers on DeviceC and DeviceD is displayed as follows:
   
   ```
   [~DeviceC] display msdp brief
   ```
   ```
   MSDP Peer Brief Information of VPN-Instance: public net
   ```
   ```
     Configured   Up           Listen       Connect      Shutdown     Down
   ```
   ```
     1            1            0            0            0            0
   ```
   ```
     Peer's Address     State     Up/Down time    AS     SA Count   Reset Count
   ```
   ```
     2.2.2.2            Up        00:10:17        ?      0          0
   ```
   ```
   [~DeviceD] display msdp brief
   ```
   ```
   MSDP Peer Brief Information of VPN-Instance: public net
   ```
   ```
     Configured   Up           Listen       Connect      Shutdown     Down
   ```
   ```
     1            1            0            0            0            0
   ```
   ```
     Peer's Address     State     Up/Down time    AS     SA Count   Reset Count
   ```
   ```
     1.1.1.1            Up        00:10:18        ?      0          0
   ```
   
   # Run the **display pim routing-table** command to check PIM routing tables on Routers. In the PIM-SM domain, S1 (10.110.5.100/24) sends multicast data to G (225.1.1.1). Host1 that joins G can receive the multicast data sent to G. By comparing the display of PIM routes on DeviceC and DeviceD, you can find that the currently valid RP is DeviceC. S1 registers with DeviceC, and Host1 sends Join messages to DeviceC.
   
   ```
   <DeviceC> display pim routing-table
   ```
   ```
   VPN-Instance: public net
   ```
   ```
    Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
    (*, 225.1.1.1)
   ```
   ```
        RP: 10.1.1.1 (local)
   ```
   ```
        Protocol: pim-sm, Flag: WC
   ```
   ```
        UpTime: 00:28:49
   ```
   ```
        Upstream interface: Register, Refresh time: 00:28:49
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/3/0
   ```
   ```
                Protocol: static, UpTime: 00:28:49, Expires: -
   ```
   ```
    (10.110.5.100, 225.1.1.1)
   ```
   ```
        RP: 10.1.1.1 (local)
   ```
   ```
        Protocol: pim-sm, Flag: SPT 2MSDP ACT
   ```
   ```
        UpTime: 00:02:26
   ```
   ```
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:02:26
   ```
   ```
            Upstream neighbor: 10.110.1.2
   ```
   ```
            RPF prime neighbor: 10.110.1.2
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/3/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:02:26, Expires: -
   ```
   ```
   <DeviceD> display pim routing-table
   ```
   
   There is no display.
   
   # Host 1 leaves G, and S1 stops sending multicast data to G. You can run the **reset pim routing-table all** command to clear the multicast routing entries on DeviceC.
   
   ```
   <DeviceC> reset pim routing-table all
   ```
   
   # Host 2 joins G, and S2 (10.110.6.100/24) begins to send multicast data to G. By comparing with the display of PIM routes on DeviceC and DeviceD, you can find that the current valid RP is DeviceD. S2 registers with DeviceD, and Host2 sends Join messages to DeviceD.
   
   ```
   <DeviceC> display pim routing-table
   ```
   
   There is no display.
   
   ```
   <DeviceD> display pim routing-table
   ```
   ```
   VPNâInstance: public net  
   ```
   ```
   Total 1 (*, G) entry; 1 (S, G) entry
   ```
   ```
   (*, 225.1.1.1)
   ```
   ```
        RP: 10.1.1.1 (local)
   ```
   ```
        Protocol: pim-sm, Flag: WC RPT
   ```
   ```
        UpTime: 00:07:23
   ```
   ```
        Upstream interface: NULL, Refresh time: 00:07:23
   ```
   ```
            Upstream neighbor: NULL
   ```
   ```
            RPF prime neighbor: NULL
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/3/0,
   ```
   ```
                Protocol: pim-sm, UpTime: 00:07:23, Expires:-
   ```
   ```
    (10.110.6.100, 225.1.1.1)
   ```
   ```
        RP: 10.1.1.1 (local)
   ```
   ```
        Protocol: pim-sm, Flag: SPT 2MSDP ACT
   ```
   ```
        UpTime: 00:10:20
   ```
   ```
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:10:20
   ```
   ```
            Upstream neighbor: 10.110.2.2
   ```
   ```
            RPF prime neighbor: 10.110.2.2
   ```
   ```
        Downstream interface(s) information:
   ```
   ```
        Total number of downstreams: 1
   ```
   ```
            1: GigabitEthernet0/3/0
   ```
   ```
                Protocol: pim-sm, UpTime: 00:10:22, Expires: -
   ```

#### Configuration Files

* Device C configuration file
  
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
  multicast routing-enable
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
   ip address 192.168.1.1 255.255.255.0
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
   undo shutdown
  ```
  ```
   ip address 10.110.1.1 255.255.255.0
  ```
  ```
   pim sm
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
   ip address 10.110.4.1 255.255.255.0
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
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
   pim sm
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
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack10
  ```
  ```
   ip address 10.1.1.1 255.255.255.255
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
   c-bsr LoopBack1
  ```
  ```
   c-rp LoopBack10
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.110.1.0 0.0.0.255
  ```
  ```
    network 10.110.4.0 0.0.0.255
  ```
  ```
    network 1.1.1.1 0.0.0.0
  ```
  ```
    network 3.3.3.3 0.0.0.0
  ```
  ```
    network 10.1.1.1 0.0.0.0
  ```
  ```
    network 192.168.1.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  msdp
  ```
  ```
   originating-rp LoopBack0
  ```
  ```
   peer 2.2.2.2 connect-interface LoopBack0
  ```
  ```
  #
  ```
  ```
  return 
  ```
* Device D configuration file
  
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
  multicast routing-enable
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
   ip address 192.168.3.1 255.255.255.0
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
   undo shutdown
  ```
  ```
   ip address 10.110.2.1 255.255.255.0
  ```
  ```
   pim sm
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
   ip address 10.110.3.1 255.255.255.0
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
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
   pim sm
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
   pim sm
  ```
  ```
  #
  ```
  ```
  interface LoopBack10
  ```
  ```
   ip address 10.1.1.1 255.255.255.255
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
   c-bsr LoopBack1
  ```
  ```
   c-rp LoopBack10
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 10.110.2.0 0.0.0.255
  ```
  ```
    network 10.110.3.0 0.0.0.255
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 4.4.4.4 0.0.0.0
  ```
  ```
    network 10.1.1.1 0.0.0.0
  ```
  ```
    network 192.168.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  msdp
  ```
  ```
   originating-rp LoopBack0
  ```
  ```
   peer 1.1.1.1 connect-interface LoopBack0
  ```
  ```
  #
  ```
  ```
  return 
  ```