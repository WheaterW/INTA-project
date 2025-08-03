Example for Configuring IPv4 User-Side Multicast for a VPN
==========================================================

This section describes how to configure IPv4 user-side multicast for a VPN.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367671__fig_dc_vrp_bras-multicast_cfg_001101), users access the network in IPoE mode through sub-interface interface 2 on a broadband remote access server (BRAS). The users and multicast source belong to the same VPN instance named **red**. It is required that the user can order programs from the multicast source in the local VPN.

**Figure 1** Configuring IPv4 user-side multicast for a VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2, and interface 3 stand for GE 0/1/0, GE 0/1/1 (with the sub-interface 0/1/1.1), and GE 0/1/2, respectively.


  
![](images/fig_dc_vrp_bras-multicast_cfg_001101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure multicast VPN functions. An NG MVPN over an mLDP P2MP tunnel is used as an example.
   
   1. Configure a BGP MPLS/IP VPN and ensure that the unicast VPN is working properly.
   2. Enable mLDP globally on PE1 and PE2.
   3. Establish a BGP MVPN peer relationship between PE1 and PE2.
   4. Configure an mLDP I-PMSI tunnel on PE1.
   5. Bind an interface on PE2 to the VPN instance.
   6. Configure IGMP on the interface that connects the multicast-capable device to the user network segment.
2. Configure an IPv4 address pool.
3. Configure AAA schemes.
4. Configure a domain.
5. Configure the IPoE access mode.
   
   1. Configure an authentication scheme.
   2. Bind a sub-interface to a VLAN.
   3. Configure a BAS interface and specify a user access type for the interface.
6. Configure a multicast replication mode. Multicast replication by multicast VLAN is used as an example.
7. Configure basic multicast functions.
8. Bind an interface to the VPN instance.

#### Data Preparation

* IP addresses of loopback 0 on the BRAS and PE2: 1.1.1.1 and 2.2.2.2, respectively
* Public network OSPF process ID: 1; area ID: 0
* MPLS LSR IDs of the BRAS and PE2: 1.1.1.1 and 2.2.2.2, respectively
* MVPN IDs of the BRAS and PE2: 1.1.1.1 and 2.2.2.2, respectively
* Names, RDs, and VPN targets of the VPN instances on the BRAS and PE2: red, 1:1, and 1:1, respectively
* IPv4 address pool
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* BAS interface parameters

#### Procedure

1. Configure NG MVPN over an mLDP P2MP tunnel. For details, see Example for Configuring a Single-AS NG MVPN to Carry Multicast Traffic over an mLDP P2MP Tunnel.
2. Configure an IPv4 address pool.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] ip pool vpn bas local
   ```
   ```
   [*BRAS-ip-pool-vpn] vpn-instance red
   ```
   ```
   [*BRAS-ip-pool-vpn] gateway 10.0.0.1 255.255.0.0
   ```
   ```
   [*BRAS-ip-pool-vpn] commit
   ```
   ```
   [*BRAS-ip-pool-vpn] section 255 10.0.0.1 10.0.0.255
   ```
   ```
   [*BRAS-ip-pool-vpn] quit
   ```
   ```
   [*BRAS] commit
   ```
3. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-authen-radius] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-radius] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS-aaa] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*BRAS-aaa-accounting-none] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
4. Configure a RADIUS server group.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   [~BRAS] radius-server group shiva
   ```
   
   # Configure an IP address and port numbers for the primary RADIUS authentication and accounting server.
   
   ```
   [*BRAS-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*BRAS-radius-shiva] radius-server accounting 10.7.66.66 1813
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*BRAS-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*BRAS-radius-shiva] radius-server retransmit 2
   ```
   ```
   [*BRAS-radius-shiva] commit
   ```
   ```
   [~BRAS-radius-shiva] quit
   ```
5. Configure a domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] domain vpn
   ```
   ```
   [*BRAS-aaa-domain-vpn] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-domain-vpn] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-domain-vpn] radius-server group shiva
   ```
   ```
   [*BRAS-aaa-domain-vpn] ip-pool vpn
   ```
   ```
   [*BRAS-aaa-domain-vpn] vpn-instance red
   ```
   ```
   [*BRAS-aaa-domain-vpn] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
6. Bind a sub-interface to a VLAN.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] user-vlan 1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-vlan-1-1] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
7. Configure a BAS interface and specify a user access type for the interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication vpn
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] authentication-method bind
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
8. Configure multicast replication by multicast VLAN.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1] multicast user-aggregation qinq pe-vid 2 ce-vid 9
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
9. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] igmp enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] quit
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~PE2] interface gigabitethernet 0/1/2
   ```
   ```
   [~PE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] ip address 10.1.2.1 255.255.255.0
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE2] commit
   ```
10. Bind the interface to a VPN instance.
    
    
    ```
    [~BRAS] interface gigabitethernet 0/1/1
    ```
    ```
    [~BRAS-GigabitEthernet0/1/1] multicast binding vpn-instance red
    ```
    ```
    [*BRAS-GigabitEthernet0/1/1] quit
    ```
    ```
    [*BRAS] commit
    ```
11. Verify the configuration.
    
    # Run the **display multicast group-ip** command to view information about users that join a specified multicast group in the VPN instance **red**. The command output shows that the users with IDs 96 and 97 in the VPN instance named **red** join the multicast program of which the group address is 225.0.0.1.
    ```
    [~BRAS] display multicast group-ip 225.0.0.1 out-interface GigabitEthernet 0/1/1.1 vpn-instance red
    ```
    ```
      User ID    User IP                     User type    Interface
    
      96         10.0.0.250                  Local        GigabitEthernet0/1/1.1
      97         10.0.0.249                  Local        GigabitEthernet0/1/1.1
    
      Local user number :2
      Remote user number:0
      Total user number :2
    ```
    
    # Run the **display multicast user-ip** command to display information about the multicast programs ordered by a specified user in the VPN instance **red** on the BAS interface. The following uses the user whose IP address is 10.0.0.250 as an example:
    ```
    [~BRAS] display multicast user-ip 10.0.0.250 vpn-instance red
      User information:
      User ID             :96
      User IPv4 address   :10.0.0.250
      Gateway IPv4 address:10.0.0.1
      BRAS interface      :GigabitEthernet0/1/1.1
      User MAC-address    :00-e0-fc-12-34-56
      MAX program list    :4
    
      User order program:
      Group IP           Source IP
      225.0.0.1          0.0.0.0
    
      Total:1
    ```
    
    # Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) *vpn-instance-name* **routing-table** command to view PIM routing entries of a specified VPN instance. For example:
    ```
    [~BRAS] display pim vpn-instance red routing-table
     VPN-Instance: red
     Total 1 (S, G) entry
    
     (10.1.2.100, 225.0.0.1)
         Protocol: pim-ssm, Flag: SG_RCVR
         UpTime: 00:00:38
         Upstream interface: through-BGP, Refresh time: 00:00:38
             Upstream neighbor: 2.2.2.2
             RPF prime neighbor: 2.2.2.2
         Downstream interface(s) information:
         Total number of downstreams: 1
            1: GigabitEthernet0/1/1(bas)
                 Protocol: igmp, UpTime: 00:00:38, Expires: -
    ```
    ```
    [~PE2] display pim vpn-instance red routing-table
     VPN-Instance: red
     Total 0 (*, G) entry; 1 (S, G) entry
    
     (10.1.2.100, 225.0.0.1)
         RP: NULL
         Protocol: pim-sm, Flag: SPT LOC ACT SG_RCVR
         UpTime: 16:29:06
         Upstream interface: GigabitEthernet0/1/2, Refresh time: 16:29:06
             Upstream neighbor: NULL
             RPF prime neighbor: NULL
         Downstream interface(s) information:
         Total number of downstreams: 1
            1: pseudo
                 Protocol: BGP, UpTime: 00:13:57, Expires: -
    ```
    
    # Run the [**display multicast vpn-instance**](cmdqueryname=display+multicast+vpn-instance) *vpn-instance-name* **routing-table** command to view multicast routing entries of a specified VPN instance. For example:
    ```
    [~BRAS] display multicast vpn-instance red routing-table
    Multicast routing table of VPN-Instance: red
     Total 1 entry
    
     00001. (10.1.2.100, 225.0.0.1)
           Uptime: 00:12:28
           Upstream Interface: pseudo
           List of 1 downstream interface
               1: GigabitEthernet0/1/1(bas)
    ```
    ```
    [~PE2] display multicast vpn-instance red routing-table
    Multicast routing table of VPN-Instance: red
     Total 1 entry
    
     00001. (10.1.2.100, 225.0.0.1)
           Uptime: 16:29:28
           Upstream Interface: GigabitEthernet0/1/2
           List of 1 downstream interface
               1: pseudo
    ```

#### Configuration Files

* BRAS configuration file
  
  ```
  #
  sysname BRAS
  #
  multicast routing-enable
  #
  multicast mvpn 1.1.1.1
  #
  ip vpn-instance red
   ipv4-family
    route-distinguisher 1:1
   apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     ipmsi-tunnel
      mldp
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  ip pool vpn bas local
   vpn-instance red
   gateway 10.0.0.1 255.255.0.0
   section 255 10.0.0.1 10.0.0.255
  #
  radius-server group shiva                                                       
   radius-server authentication 10.7.66.66 1812 weight 0                                             
   radius-server accounting 10.7.66.66 1813 weight 0                                                        
   radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
   radius-server retransmit 2                                                    
  # 
  aaa
   #
   authentication-scheme none
    authentication-mode none
   #
   accounting-scheme none
    accounting-mode none
   #
   domain vpn
    authentication-scheme radius
    accounting-scheme none
    radius-server group shiva
    ip-pool vpn
    vpn-instance red
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
    multicast binding vpn-instance red
   pim sm
   igmp enable
  #
  interface GigabitEthernet0/1/1.1
   user-vlan 1
   multicast user-aggregation qinq pe-vid 2 ce-vid 9
   bas
   #
    access-type layer2-subscriber default-domain authentication vpn
    authentication-method bind
   #
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance red
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 1.1.1.1 0.0.0.0
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 2.2.2.2
  #
  ip vpn-instance red
   ipv4-family
    route-distinguisher 1:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     ipmsi-tunnel
      mldp
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance red
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
   #
   ipv4-family vpn-instance red
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  return
  ```