Example for Configuring Basic MBGP Functions
============================================

This section describes how to configure basic MBGP functions to construct an MBGP network.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172367067__fig_dc_vrp_multicast_cfg_103201), the receiver and the source reside in different ASs. To enable the receiver to receive VoD information in multicast mode, establish an MBGP peer relationship between RouterA and RouterB to transmit multicast routing information.

**Figure 1** Configuring basic MBGP functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_multicast_cfg_103201.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 192.168.1.1/24 |
| GigabitEthernet0/2/0 | 10.10.10.1/24 |
| Loopback0 | 1.1.1.1/32 |
| DeviceB | GE 0/1/0 | 192.168.1.2/24 |
| GigabitEthernet0/2/0 | 192.168.2.1/24 |
| GigabitEthernet0/3/0 | 192.168.3.1/24 |
| Loopback0 | 2.2.2.2/32 |
| DeviceC | GE 0/1/0 | 192.168.4.1/24 |
| GigabitEthernet0/2/0 | 10.22.22.1/24 |
| GigabitEthernet0/3/0 | 192.168.3.2/24 |
| Loopback0 | 3.3.3.3/32 |
| DeviceD | GE 0/1/0 | 192.168.4.2/24 |
| GigabitEthernet0/2/0 | 192.168.2.2/24 |
| Loopback0 | 4.4.4.4/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each Router interface.
2. Establish MBGP peer relationships to exchange inter-AS multicast routes.
3. Configure MBGP to import routes.
4. Enable multicast routing on each Router.
5. Configure basic PIM-SM functions in each AS, and enable IGMP on interfaces that connect to user hosts.
6. Configure BSR boundaries on interfaces directly connecting RouterA and RouterB.
7. Establish MSDP peer relationships to transmit inter-AS multicast source information.
8. Verify the configuration.

#### Data Preparation

To complete the configuration, you need the following data:

* AS number of DeviceA: 100
* AS numbers of DeviceB, DeviceC, and Device D: 200
* Multicast group address: 225.1.1.1; multicast source address: 10.10.10.10/24

#### Procedure

1. Configure an IP address for each Router interface and configure OSPF in each AS. 
   
   
   
   # Configure an IP address and a mask for each Router interface and configure OSPF in each AS to ensure that DeviceB, DeviceC, DeviceD, and Receiver in AS 200 can communicate at the network layer, learn the routes to each other's loopback interfaces, and the Routers dynamically update routes between each other using a unicast routing protocol. OSPF process 1 is used as an example. For configuration details, see Configuration Files in this section.
2. Configure BGP, enable MBGP, and configure MBGP peer relationships.
   
   
   
   # On DeviceA, enable BGP and configure the MBGP peer relationship.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 192.168.1.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceA-bgp-af-multicast] peer 192.168.1.2 enable
   ```
   ```
   [*DeviceA-bgp-af-multicast] commit
   ```
   ```
   [~DeviceA-bgp-af-multicast] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # On DeviceB, enable BGP and configure the MBGP peer relationship.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 192.168.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 192.168.3.2 as-number 200
   ```
   ```
   [*DeviceB-bgp] peer 192.168.2.2 as-number 200
   ```
   ```
   [*DeviceB-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceB-bgp-af-multicast] peer 192.168.1.1 enable
   ```
   ```
   [*DeviceB-bgp-af-multicast] peer 192.168.3.2 enable
   ```
   ```
   [*DeviceB-bgp-af-multicast] peer 192.168.2.2 enable
   ```
   ```
   [*DeviceB-bgp-af-multicast] commit
   ```
   ```
   [~DeviceB-bgp-af-multicast] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # On DeviceC, enable BGP and configure the MBGP peer relationship.
   
   ```
   [~DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] peer 192.168.3.1 as-number 200
   ```
   ```
   [*DeviceC-bgp] peer 192.168.4.2 as-number 200
   ```
   ```
   [*DeviceC-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceC-bgp-af-multicast] peer 192.168.3.1 enable
   ```
   ```
   [*DeviceC-bgp-af-multicast] peer 192.168.4.2 enable
   ```
   ```
   [*DeviceC-bgp-af-multicast] commit
   ```
   ```
   [~DeviceC-bgp-af-multicast] quit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # On DeviceD, enable BGP and configure the MBGP peer relationship.
   
   ```
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] peer 192.168.2.1 as-number 200
   ```
   ```
   [*DeviceD-bgp] peer 192.168.4.1 as-number 200
   ```
   ```
   [*DeviceD-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceD-bgp-af-multicast] peer 192.168.2.1 enable
   ```
   ```
   [*DeviceD-bgp-af-multicast] peer 192.168.4.1 enable
   ```
   ```
   [*DeviceD-bgp-af-multicast] commit
   ```
   ```
   [~DeviceD-bgp-af-multicast] quit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
3. Configure MBGP to import routes.
   
   
   
   # On DeviceA, configure MBGP to import routes.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] import-route direct
   ```
   ```
   [*DeviceA-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceA-bgp-af-multicast] network 1.1.1.1 32
   ```
   ```
   [*DeviceA-bgp-af-multicast] commit
   ```
   ```
   [~DeviceA-bgp-af-multicast] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # On DeviceB, configure MBGP to import routes.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] import-route direct
   ```
   ```
   [*DeviceB-bgp] import-route ospf 1
   ```
   ```
   [*DeviceB-bgp] ipv4-family multicast
   ```
   ```
   [*DeviceB-bgp-af-multicast] network 2.2.2.2 32
   ```
   ```
   [*DeviceB-bgp-af-multicast] commit
   ```
   ```
   [~DeviceB-bgp-af-multicast] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
4. Enable multicast on the Routers and interfaces connecting the Routers.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   ```
   ```
   [*DeviceA] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet0/2/0
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
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] multicast routing-enable
   ```
   ```
   [*DeviceB] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] multicast routing-enable
   ```
   ```
   [*DeviceC] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] igmp enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] pim sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] multicast routing-enable
   ```
   ```
   [*DeviceD] interface GigabitEthernet0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
5. Configure a BSR and an RP in each AS.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface loopback 0
   ```
   ```
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   ```
   ```
   [*DeviceA-LoopBack0] pim sm
   ```
   ```
   [*DeviceA-LoopBack0] quit
   ```
   ```
   [*DeviceA] pim
   ```
   ```
   [*DeviceA-pim] c-bsr loopback 0
   ```
   ```
   [*DeviceA-pim] c-rp loopback 0
   ```
   ```
   [*DeviceA-pim] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface loopback 0
   ```
   ```
   [*DeviceB-LoopBack0] ip address 2.2.2.2 255.255.255.255
   ```
   ```
   [*DeviceB-LoopBack0] pim sm
   ```
   ```
   [*DeviceB-LoopBack0] quit
   ```
   ```
   [*DeviceB] pim
   ```
   ```
   [*DeviceB-pim] c-bsr loopback 0
   ```
   ```
   [*DeviceB-pim] c-rp loopback 0
   ```
   ```
   [*DeviceB] quit
   ```
   ```
   [*DeviceB] commit
   ```
6. Configure BSR boundaries on interfaces directly connecting DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface GigabitEthernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] pim bsr-boundary
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface GigabitEthernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] pim bsr-boundary
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
7. Configure the MSDP peer relationship.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] msdp
   ```
   ```
   [*DeviceA-msdp] peer 192.168.1.2 connect-interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-msdp] commit
   ```
   ```
   [~DeviceA-msdp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] msdp
   ```
   ```
   [*DeviceB-msdp] peer 192.168.1.1 connect-interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-msdp] commit
   ```
   ```
   [~DeviceB-msdp] quit
   ```
8. Verify the configuration.
   
   
   
   # Run the **display bgp multicast peer** command to check the MBGP peer relationships between Routers. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display bgp multicast peer
   ```
   ```
   BGP local router ID : 1.1.1.1
   ```
   ```
    Local AS number : 100
   ```
   ```
    Total number of peers : 1                 Peers in established state : 1
   ```
   ```
     Peer        V   AS   MsgRcvd  MsgSent  OutQ  Up/Down   State     PrefRcv
   ```
   ```
     192.168.1.2   4   200  82       75       0     00:30:29  Established    17
   ```
   
   # Run the **display msdp brief** command to check the MSDP peer relationships between Routers. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display msdp brief
   ```
   ```
   MSDP Peer Brief Information of VPN-Instance: public net
   ```
   ```
     Configured      Up        Listen       Connect      Shutdown     Down
   ```
   ```
     1                 1          0             0             0             0
   ```
   ```
     Peer's Address     State     Up/Down time    AS     SA Count    Reset Count
   ```
   ```
     192.168.1.1            Up        00:07:17        100     1            0
   ```

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
   pim bsr-boundary
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
   ip address 10.10.10.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  #
  ```
  ```
  interface loopback 0
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
  bgp 100
  ```
  ```
   peer 192.168.1.2 as-number 200
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
    import-route direct
  ```
  ```
    peer 192.168.1.2 enable
  ```
  ```
  #
  ```
  ```
   ipv4-family multicast
  ```
  ```
    undo synchronization
    network 1.1.1.1 32
  ```
  ```
    peer 192.168.1.2 enable
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   c-bsr loopback 0
  ```
  ```
   c-rp loopback 0
  ```
  ```
  #
  ```
  ```
  msdp
  ```
  ```
   peer 192.168.1.2 connect-interface GigabitEthernet 0/1/0
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
  multicast routing-enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.1.2 255.255.255.0
  ```
  ```
   pim bsr-boundary 
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface GigabitEthernet 0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.2.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface GigabitEthernet 0/3/0
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
  interface loopback 0
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
  bgp 200
  ```
  ```
   peer 192.168.1.1 as-number 100
  ```
  ```
   peer 192.168.3.2 as-number 200
  ```
  ```
   peer 192.168.2.2 as-number 200
  ```
  ```
  # 
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
    import-route direct
  ```
  ```
    import-route ospf 1
  ```
  ```
    peer 192.168.1.1 enable
  ```
  ```
    peer 192.168.3.2 enable
  ```
  ```
    peer 192.168.2.2 enable
  ```
  ```
  # 
  ```
  ```
   ipv4-family multicast
  ```
  ```
    undo synchronization
    network 2.2.2.2 32
  ```
  ```
    peer 192.168.1.1 enable
  ```
  ```
    peer 192.168.3.2 enable
  ```
  ```
    peer 192.168.2.2 enable
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
    network 192.168.3.0 0.0.0.255
  ```
  ```
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
  #
  ```
  ```
  pim
  ```
  ```
   c-bsr loopback 0
  ```
  ```
   c-rp loopback 0
  ```
  ```
  # 
  ```
  ```
  msdp
  ```
  ```
   peer 192.168.1.1 connect-interface GigabitEthernet 0/1/0
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
   ip address 192.168.4.1 255.255.255.0
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
  ip address 10.22.22.1 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   igmp enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet 0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.3.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
   # 
  ```
  ```
  interface loopback 0
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
  bgp 200
  ```
  ```
   peer 192.168.3.1 as-number 200
  ```
  ```
   peer 192.168.4.2 as-number 200
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
    peer 192.168.3.1 enable
  ```
  ```
    peer 192.168.4.2 enable
  ```
  ```
  #
  ```
  ```
   ipv4-family multicast
  ```
  ```
    undo synchronization
    peer 192.168.3.1 enable
  ```
  ```
    peer 192.168.4.2 enable
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
    network 192.168.3.0 0.0.0.255
  ```
  ```
    network 192.168.4.0 0.0.0.255
  ```
  ```
    network 10.22.22.0 0.0.0.255
  ```
  ```
    network 3.3.3.3 0.0.0.0
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
  ip address 192.168.4.2 255.255.255.0
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
   ip address 192.168.2.2 255.255.255.0
  ```
  ```
   pim sm
  ```
  ```
  # 
  ```
  ```
  interface loopback 0
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
  bgp 200
  ```
  ```
   peer 192.168.2.1 as-number 200
  ```
  ```
   peer 192.168.4.1 as-number 200
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
    peer 192.168.2.1 enable
  ```
  ```
    peer 192.168.4.1 enable
  ```
  ```
  #
  ```
  ```
   ipv4-family multicast
  ```
  ```
    undo synchronization
    peer 192.168.2.1 enable
  ```
  ```
    peer 192.168.4.1 enable
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
    network 192.168.2.0 0.0.0.255
  ```
  ```
    network 192.168.4.0 0.0.0.255
  ```
  ```
    network 4.4.4.4 0.0.0.0
  ```
  ```
  #
  ```
  ```
  return
  ```