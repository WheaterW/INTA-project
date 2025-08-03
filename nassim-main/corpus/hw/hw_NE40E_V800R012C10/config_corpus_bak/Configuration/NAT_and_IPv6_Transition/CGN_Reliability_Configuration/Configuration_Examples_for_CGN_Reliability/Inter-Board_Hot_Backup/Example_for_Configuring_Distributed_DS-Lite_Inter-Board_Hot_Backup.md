Example for Configuring Distributed DS-Lite Inter-Board Hot Backup
==================================================================

Example_for_Configuring_Distributed_DS-Lite_Inter-Board_Hot_Backup

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172362464__fig_01), a terminal user assigned a private IPv4 address accesses an IPv6 metropolitan area network (MAN) through a customer premises equipment (CPE). The CPE establishes a Dual-Stack Lite (DS-Lite) tunnel to a DS-Lite device. The CPE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the DS-Lite device. The DS-Lite device decapsulates traffic, uses a Network Address Translation (NAT) technique to translate the private IPv4 address to a public IPv4 address, and forwards traffic to the IPv4 Internet. The DS-Lite device is equipped with DS-Lite boards in slots 1 and 2, respectively. The DS-Lite device's GE 0/1/1 is connected to an IPv6 MAN, and GE 0/1/2 is connected to the Internet. IPv4 residential users need to access the IPv4 Internet through the IPv6 MAN. The broadband remote access server (BRAS) performs DS-Lite translation for user packets. The users log in to the BRAS using IPv6. The CGN boards on the BRAS perform 1:1 inter-board hot backup.

**Figure 1** Distributed DS-Lite networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](images/fig_dc_ne_ds-lite_0008.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Load a GTL license that enables DS-Lite and configure DS-Lite sessions on service boards.
2. Enable HA hot backup.
3. Configure a RADIUS server group named **rad-ser**.
4. Enable IPv6 and set a DUID for a DHCPv6 server.
5. Create an IPv6 ND address pool and an IPv6 PD address pool.
6. Create a DS-Lite instance and bind it to the service-instance group.
7. Configure basic DS-Lite functions.
8. Configure user information and RADIUS authentication on the BRAS.
9. Configure a distributed DS-Lite traffic diversion policy.
10. Enable the DS-Lite device to advertise public routes.

#### Procedure

1. Load a GTL license that enables DS-Lite and configure DS-Lite sessions on service boards.
   
   
   ```
   <BRAS> system-view
   ```
   ```
   [~BRAS] vsm on-board-mode disable
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] display license
   ```
   ```
    Item name Item type Value Description
    -------------------------------------------------------------
    LME0CONN01 Resource 64 Concurrent Users(1k)
    LME0NATDS01 Resource 32 2M NAT Session
    
   ```
   ```
   [~BRAS] License
   ```
   ```
   [*BRAS-license] active nat session-table size 16 slot 1
   ```
   ```
   [*BRAS-license] active nat session-table size 16 slot 2
   ```
   ```
   [*BRAS-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS-license] active nat bandwidth-enhance 40 slot 2
   ```
   ```
   [*BRAS-license] active ds-lite vsuf slot 1
   ```
   ```
   [*BRAS-license] active ds-lite vsuf slot 2
   ```
   ```
   [*BRAS-license] commit
   ```
   ```
   [~BRAS-license] quit
   ```
2. Enable HA hot backup.
   
   
   ```
   [~BRAS] service-ha hot-backup enable
   ```
   ```
   [*BRAS] commit
   ```
3. Configure a RADIUS server group named **rad-ser**.
   
   
   ```
   [~BRAS] radius-server group rad-ser
   ```
   ```
   [*BRAS-radius-rad-ser] radius-server authentication 192.168.10.10 1824 weight 0
   ```
   ```
   [*BRAS-radius-rad-ser] radius-server accounting 192.168.10.10 1825 weight 0
   ```
   ```
   [*BRAS-radius-rad-ser] radius-server shared-key-cipher YsHsjx_2022063
   ```
   ```
   [*BRAS-radius-rad-ser] commit
   ```
   ```
   [~BRAS-radius-rad-ser] quit
   ```
4. Enable IPv6 and set a DUID for a DHCPv6 server.
   
   
   ```
   [~BRAS] ipv6
   ```
   ```
   [*BRAS] dhcpv6 duid llt
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] quit
   ```
5. Create an IPv6 ND address pool and an IPv6 PD address pool.
   
   
   1. Create an IPv6 ND prefix pool.
      
      ```
      [~BRAS] ipv6 prefix ipv6-pppoe-nd-1 delegation
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-nd-1] prefix 2001:db8:D000::/41
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-nd-1] slaac-unshare-only
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-nd-1] commit
      ```
      ```
      [~BRAS-ipv6-prefix-ipv6-pppoe-nd-1] quit
      ```
   2. Create an IPv6 ND address pool.
      ```
      [~BRAS] ipv6 pool ipv6-pppoe-nd-1 bas delegation
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-nd-1] dns-server 2001:db8:1:1:1::10
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-nd-1] prefix ipv6-pppoe-nd-1
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-nd-1] commit
      ```
      ```
      [~BRAS-ipv6-pool-ipv6-pppoe-nd-1] quit
      ```
   3. Create an IPv6 PD prefix pool.
      ```
      [~BRAS] ipv6 prefix ipv6-pppoe-pd-1 delegation
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-pd-1] prefix 2001:db8:D080::/41 delegating-prefix-length 56
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-pd-1] pd-unshare-only
      ```
      ```
      [*BRAS-ipv6-prefix-ipv6-pppoe-pd-1] commit
      ```
      ```
      [~BRAS-ipv6-prefix-ipv6-pppoe-pd-1] quit
      ```
   4. Create an IPv6 PD address pool and specify an address family transition router (AFTR) name.
      ```
      [~BRAS] ipv6 pool ipv6-pppoe-pd-1 bas delegation
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-pd-1] dns-server 2001:db8:1:1:1::10
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-pd-1] aftr-name zj-hz-aftr1.dualstack-lite.com
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-pd-1] prefix ipv6-pppoe-pd-1
      ```
      ```
      [*BRAS-ipv6-pool-ipv6-pppoe-pd-1] prefix ipv6-pppoe-pd-1
      ```
      ```
      [~BRAS-ipv6-pool-ipv6-pppoe-pd-1] quit
      ```
6. Create a DS-Lite instance and bind it to the HA service-instance group.
   
   
   1. Create a CGN HA backup group and bind it to service boards.
      ```
      [~BRAS] service-location 1
      ```
      ```
      [*BRAS-service-location-1] location slot 10 backup slot 11
      ```
      ```
      [*BRAS-service-location-1] commit
      ```
      ```
      [~BRAS-service-location-1] quit
      ```
   2. Create a CGN HA service-instance group and bind it to the CGN HA backup group.
      ```
      [~BRAS] service-instance-group service-instance-group1
      ```
      ```
      [*BRAS-instance-group-service-instance-group1] service-location 1
      ```
      ```
      [*BRAS-instance-group-service-instance-group1] commit
      ```
      ```
      [~BRAS-instance-group-service-instance-group1] quit
      ```
   3. Create a DS-Lite instance and bind it to the service-instance group.
      ```
      [~BRAS] ds-lite instance ds-lite-1 id 100
      ```
      ```
      [*BRAS-ds-lite-instance-ds-lite-1] service-instance-group service-instance-group1
      ```
      ```
      [*BRAS-ds-lite-instance-ds-lite-1] commit
      ```
      ```
      [*BRAS-ds-lite-instance-ds-lite-1] quit
      ```
7. Configure basic DS-Lite functions.
   
   
   ```
   [~BRAS] acl ipv6 3000
   ```
   ```
   [*BRAS-acl6-adv-3000] rule 5 permit ipv6 source 2001:db8:D000::/41 destination 2001:db8:2:2:2::12/128
   ```
   ```
   [*BRAS-acl6-adv-3000] commit
   ```
   ```
   [~BRAS-acl6-adv-3000] quit
   ```
   ```
   [~BRAS] ds-lite instance ds-lite-1 id 100
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] ds-lite tunnel prefix-length 64
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] port-range 4096
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] ds-lite address-group dt-addr-group group-id 1
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1-ds-lite-address-group-dt-addr-group] section 0 11.1.1.1 mask 24
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1-ds-lite-address-group-dt-addr-group] quit
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] ds-lite outbound 3000 address-group dt-addr-group
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] local-ipv6 2001:db8:2:2:2::12 prefix-length 128
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] remote-ipv6 2001:db8:D000:: prefix-length 41
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] ds-lite alg all
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] ds-lite filter mode full-cone
   ```
   ```
   Warning: The command will rebuild all session tables of this instance. Continue? [Y/N]: Y
   ```
   ```
   [*BRAS-ds-lite-instance-ds-lite-1] commit
   ```
   ```
   [~BRAS-ds-lite-instance-ds-lite-1] quit
   ```
8. Configure a user group of which users access the Internet.
   
   
   ```
   [~BRAS] user-group ds-lite-1
   ```
   ```
   Info: Create a new user group 
   ```
   ```
   [*BRAS] commit
   ```
9. Configure a domain from which users access the Internet.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [~BRAS-aaa] authentication-scheme auth1
   ```
   ```
   [*BRAS-aaa-authen-auth1] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-auth1] quit
   ```
   ```
   [*BRAS-aaa-accounting-acct1] accounting-scheme acct1
   ```
   ```
   [*BRAS-aaa-accounting-acct1] accounting-mode radius
   ```
   ```
   [*BRAS-aaa-accounting-acct1] accounting start-fail online
   ```
   ```
   [*BRAS-aaa-accounting-acct1] quit
   ```
   ```
   [~BRAS-aaa] domain ds-lite-domain
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] authentication-scheme auth1
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] accounting-scheme acct1
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] prefix-assign-mode unshared
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] ipv6-pool ipv6-pppoe-nd-1
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] ipv6-pool ipv6-pppoe-pd-1
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] radius-server group rad-ser
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] user-group ds-lite-1 bind ds-lite instance ds-lite-1
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] user-basic-service-ip-type ipv6
   ```
   ```
   [*BRAS-aaa-domain-ds-lite-domain] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
   ```
   [~BRAS-aaa] quit
   ```
10. Configure a distributed DS-Lite traffic diversion policy.
    
    
    
    # Configure a classifier-behavior (C-B) pair to distribute user traffic in a user group named **ds-lite-1** to a DS-Lite instance named **ds-lite-1**.
    
    ```
    [~BRAS] acl ipv6 number 9001
    ```
    ```
    [*BRAS-acl6-ucl-9001] rule 5 permit ipv6 source user-group ds-lite-1 destination ipv6-address 2001:db8:2:2:2::12/128
    ```
    ```
    [*BRAS-acl6-ucl-9001] commit
    ```
    ```
    [~BRAS-acl6-ucl-9001] quit
    ```
    ```
    [~BRAS] traffic classifier ds-classifier1 operator or
    ```
    ```
    [*BRAS-classifier-ds-classifier1] if-match ipv6 acl 9001
    ```
    ```
    [*BRAS-classifier-ds-classifier1] commit
    ```
    ```
    [*BRAS-classifier-ds-classifier1] quit
    ```
    ```
    [~BRAS] traffic behavior ds-behavior1
    ```
    ```
    [*BRAS-behavior-ds-behavior1] ds-lite bind instance ds-lite-1
    ```
    ```
    [*BRAS-behavior-ds-behavior1] commit
    ```
    ```
    [~BRAS-behavior-ds-behavior1] quit
    ```
    ```
    [~BRAS] traffic policy service-control
    ```
    ```
    [*BRAS-trafficpolicy-service-control] share-mode
    ```
    ```
    [*BRAS-trafficpolicy-service-control] classifier ds-classifier1 behavior ds-behavior1
    ```
    ```
    [*BRAS-trafficpolicy-service-control] commit
    ```
    ```
    [~BRAS-trafficpolicy-service-control] quit
    ```
    ```
    [~BRAS] traffic-policy service-control inbound
    ```
    ```
    [*BRAS] commit
    ```
11. Enable the DS-Lite device to advertise public routes. In the following example, Intermediate System to Intermediate System (IS-IS) is used.
    
    
    1. Configure IS-IS.
       
       ```
       [~BRAS] isis 100
       ```
       ```
       [*BRAS-isis-100] network-entity 10.1000.1000.1000.00
       ```
       ```
       [*BRAS-isis-100] commit
       ```
       ```
       [*BRAS-isis-100] quit
       ```
       ```
       [~BRAS] isis 1000
       ```
       ```
       [*BRAS-isis-1000] network-entity 10.1000.1000.1002.00
       ```
       ```
       [*BRAS-isis-1000] ipv6 enable
       ```
       ```
       [*BRAS-isis-1000] commit
       ```
       ```
       [~BRAS-isis-1000] quit
       ```
    2. Configure the DS-Lite device's interface connected to the IPv6 network.
       
       ```
       [~BRAS] interface gigabitethernet0/1/1
       ```
       ```
       [~BRAS-GigabitEthernet0/1/1] ipv6 enable
       ```
       ```
       [*BRAS-GigabitEthernet0/1/1] isis ipv6 enable 1000
       ```
       ```
       [*BRAS-GigabitEthernet0/1/1] commit
       ```
       ```
       [~BRAS-GigabitEthernet0/1/1] quit
       ```
    3. Configure the DS-Lite device's interface connected to the IPv4 network.
       
       ```
       [~BRAS] interface gigabitethernet0/1/2
       ```
       ```
       [~BRAS-GigabitEthernet0/1/2] ip address 2.2.2.1 24
       ```
       ```
       [*BRAS-GigabitEthernet0/1/2] isis enable 100
       ```
       ```
       [*BRAS-GigabitEthernet0/1/2] commit
       ```
       ```
       [~BRAS-GigabitEthernet0/1/2] quit
       ```
    4. Enable the DS-Lite device to advertise local IP routes to the IPv6 network and address pool routes to the IPv4 network. Import local IP routes and address pool routes to the IS-IS routing table.
       
       ```
       [~BRAS] isis 1000
       ```
       ```
       [*BRAS-isis-1000] ipv6 import-route unr
       ```
       ```
       [*BRAS-isis-1000] commit
       ```
       ```
       [~BRAS-isis-1000] quit
       ```
       ```
       [~BRAS] isis 100
       ```
       ```
       [*BRAS-isis-100] import-route unr
       ```
       ```
       [*BRAS-isis-100] commit
       ```
       ```
       [~BRAS-isis-100] quit
       ```![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If a public address pool is configured using a mask, run the **network** command to advertise a route. Do not configure a black-hole summary route, which prevents a failure to forward reverse traffic.
12. Verify the configuration.
    
    
    
    # Run the **display device** command to view the status of the master and slave service boards.
    
    ```
    <BRAS> display device
    ```
    ```
    NE40E's Device status:
    Slot #    Type       Online    Register      Status      Primary
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1         VSU        Present   Registered    Normal      NA     
    2         VSU        Present   Registered    Normal      NA     
    17        MPU        Present   NA            Normal      Master 
    18        MPU        Present   Registered    Normal      Slave  
    19        SFU        Present   Registered    Normal      NA     
    21        SFU        Present   Registered    Normal      NA     
    23        CLK        Present   Registered    Normal      Master 
    24        CLK        Present   Registered    Normal      Slave  
    25        PWR        Present   Registered    Normal      NA     
    26        PWR        Present   Registered    Normal      NA     
    27        FAN        Present   Registered    Normal      NA     
    28        FAN        Present   Registered    Normal      NA     
    29        FAN        Present   Registered    Normal      NA     
    30        FAN        Present   Registered    Normal      NA
    ```
    
    # Verify that the public network routes are properly advertised.
    
    ```
    <BRAS> display ip routing-table
    ```
    ```
    Route Flags: R - relay, D - download to fib       
    ----------------------------------------------------------------------
    Routing Table: Public                            
             Destinations : 21813    Routes : 21814   
                                                      
    Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
                                                      
         11.1.1.0/24    Unr     64   10          D   127.0.0.1       InLoopBack0
         2.2.2.0/24     Direct  15   20          D   2.2.2.2         GigabitEthernet0/1/2
         2.2.2.1/32     Direct  0    0           D   127.0.0.1       GigabitEthernet0/1/2
    ```
    ```
    <BRAS> display ipv6 routing-table 2001:db8:2:2:2::12:100
    ```
    ```
    Routing Table :              
    Summary Count : 1            
                
     Destination  : 2001:db8:D000::                  PrefixLength : 128               
     NextHop      : 2001:db8:2:2:2::12:100           Preference   : 64               
     Cost         : 10                               Protocol     : Unr              
     RelayNextHop : ::                               TunnelID     : 0x0              
     Interface    : GigabitEthernet0/1/1              Flags        : D  
    ```
    
    # Verify that the master/backup status in the service-location is correct.
    
    ```
    <BRAS> display service-location  1 
    ```
    ```
    service-location 1                             
     Location slot ID: 1                
     Current location slot ID: 1         
     Backup slot ID: 2                
     Current backup slot ID: 2          
     Bound service-instance-group number: 1           
     Batch-backup state: finished  
    ```
    
    # Verify that user table information on the master and slave service boards is correct.
    
    ```
    <BRAS> display nat user-information slot 1 verbose
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 1
    Total number: 1.
      ---------------------------------------------------------------------------
      User Type                             :  DS-Lite
      CPE IP                                :  124.7.200.1
      User ID                               :  1
      VPN Instance                          :  -
      Address Group                         :  test_nat_03
      NoPAT Address Group                   :  -
      NAT Instance                          :  test_nat_03
      Public IP                             :  143.15.31.142
      NoPAT Public IP                       :  -
      Start Port                            :  1024
      Port Range                            :  64512
      Port Total                            :  64512
      Radius Specific PCP Port              :  NO
      PCP authentication                    :  True
      Extend Port Alloc Times               :  0
      Extend Port Alloc Number              :  0
      First/Second/Third Extend Port Start  :  0/0/0
      Total/TCP/UDP/ICMP Session Limit      :  0/0/0/0
      Total/TCP/UDP/ICMP Session Current    :  0/0/0/0
      Total/TCP/UDP/ICMP Rev Session Limit  :  8192/10240/10240/512
      Total/TCP/UDP/ICMP Rev Session Current:  0/0/0/0
      Total/TCP/UDP/ICMP Port Limit         :  0/0/0/0
      Total/TCP/UDP/ICMP Port Current       :  0/0/0/0
      Nat ALG Enable                        :  ALL
      Port Reuse                            :  False
      Token/TB/TP                           :  0/0/0
      Token/TB/TP                           :  0/0/0
      Port Forwarding Flag                  :  Non Port Forwarding
      Port Forwarding Ports                 :  0 0 0 0 0
      Create Time                           :  2023-10-25 10:27:41
      Aging Time(s)                         :  -
      Left Time(s)                          :  -
      Port Limit Discard Count              :  0
      Session Limit Discard Count           :  0
      Fib Miss Discard Count                :  0
      -->Transmit Packets                   :  0
      -->Transmit Bytes                     :  0
      -->Drop Packets                       :  0
      <--Transmit Packets                   :  0
      <--Transmit Bytes                     :  0
      <--Drop Packets                       :  0
      Fast-forwarding Statistics ID         :  -
      -->Hit Fast-fwd session Packets       :  -
      -->NP transmit to multi-core Packets  :  -
      <--Hit Fast-fwd session Packets       :  -
      <--NP transmit to multi-core Packets  :  -
      Is UP-Escape User                     :  False
      ---------------------------------------------------------------------------
    ```
    
    # Verify that session table information on the master and backup service boards is correct.
    
    ```
    <BRAS> display nat session table slot 1 verbose
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break ...
    Slot: 1 
    Current total sessions: 1.
    udp: 192.168.1.2:1024[11.1.1.1:1024]--> *:* 
    *:* -->11.1.1.1:1024[192.168.1.2:1024] 
    DS-Lite Instance: ds-lite-1
    VPN:--->-
    Tag:0x2,FixedTag:0x1, Status:hit, NPFlag:0x6, Create:2015-9-30 11:37:04,TTL:00:04:00 ,Left:00:04:00 , Master
    AppProID: 0x0, CPEIP:2001:db8:2:2:2::12, FwdType:DSLITE
    Dest-ip:1.1.1.2,Dest-port:1024
    ```
    ```
    <BRAS> display nat session table slot 2 verbose
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break ...
    Slot: 2 
    Current total sessions: 1.
    udp: 192.168.1.2:1024[11.1.1.1:1024]--> *:* 
    *:* -->11.1.1.1:1024[192.168.1.2:1024] 
    DS-Lite Instance: ds-lite-1
    VPN:--->-
    Tag:0x2,FixedTag:0x1, Status:hit, NPFlag:0x6, Create:2015-9-30 11:37:04,TTL:00:04:00 ,Left:00:04:00 , Master
    AppProID: 0x0, CPEIP:2001:db8:2001:db8:2:2:2::12:200, FwdType:DSLITE
    Dest-ip:1.1.1.2,Dest-port:1024
    ```
    
    # Run the **display nat statistics** command to view the number of sent and received packets on the master service board.
    
    ```
    <BRAS> display nat statistics received slot 1 
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break 
    Slot: 1                                  
    ---------------------------------------------------------------------------
     Packets received from interface                :632014772      
     Packets received from mainboard                :29450          
     Packets received by nat entry                  :255587842      
     receive hrp packets from peer device           :0
     receive boardhrp packets from peer board       :0
    ---------------------------------------------------------------------------
    ```
    ```
    <BRAS> display nat statistics transmitted slot 1
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break 
    Slot: 1                                  
    --------------------------------------------------------------------------
     Packets transmitted to interface               :159142427      
     Packets transmitted to mainboard               :22219          
     Seclog packets transmitted                     :0
     Syslog packets transmitted                     :0
     Userinfo log msg transmitted to cp             :0
     Transparent packet with nat                    :65080312       
     Transparent packet without nat                 :0
     sessions sent by hrp                           :0
     UserTbl sent by hrp                            :0
     UserTbl sent by Boardhrp                       :0
     sessions sent by Boardhrp                      :0
    ---------------------------------------------------------------------------
    ```

#### Configuration Files

* BRAS configuration file
  
  ```
  #
  sysname BRAS
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 16 slot 1 
   active nat session-table size 16 slot 2 
   active nat bandwidth-enhance 40 slot 1
   active nat bandwidth-enhance 40 slot 2
   active ds-lite vsuf slot 1
   active ds-lite vsuf slot 2
  #
  service-ha hot-backup enable
  #
  radius-server group rad-ser
   radius-server authentication 192.168.10.10 1824 weight 0
   radius-server accounting 192.168.10.10 1825 weight 0
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
  #
  ipv6
  dhcpv6 duid llt
  #
  ipv6 prefix ipv6-pppoe-nd-1 delegation
   prefix 2001:db8:D000::/41
   slaac-unshare-only
  #
  ipv6 pool ipv6-pppoe-nd-1 bas delegation
   dns-server 2001:db8:1:1:1::10
   prefix ipv6-pppoe-nd-1
  #
  ipv6 prefix ipv6-pppoe-pd-1 delegation
   prefix 2001:db8:D080::/41 delegating-prefix-length 56
   pd-unshare-only
  #
  ipv6 pool ipv6-pppoe-pd-1 bas delegation
   dns-server 2001:db8:1:1:1::10
   aftr-name zj-hz-aftr1.dualstack-lite.com
   prefix ipv6-pppoe-pd-1
  #
  acl ipv6 3000
   rule 5 permit ipv6 source 2001:db8:D000::/41 destination 2001:db8:2:2:2::12/128
  #
  acl ipv6 number 9001
   rule 5 permit ipv6 source user-group ds-lite-1 destination ipv6-address 2001:db8:2:2:2::12/128
  #
  traffic classifier ds-classifier1 operator or
   if-match ipv6 acl 9001 precedence 1
  #
  traffic behavior ds-behavior1
   ds-lite bind instance ds-lite-1
  #
  traffic policy service-control
   share-mode
   classifier ds-classifier1 behavior ds-behavior1 precedence 1
  #
  traffic-policy service-control inbound
  #
  isis 100
   network-entity 10.1000.1000.1000.00
   import-route unr
  #
  isis 1000
   network-entity 10.1000.1000.1002.00
   ipv6 import-route unr
   ipv6 enable
  #
  service-location 1
   location slot 10 backup slot 11
  #
  service-instance-group service-instance-group1
   service-location 1
  #
  ds-lite instance ds-lite-1 id 100
   service-instance-group service-instance-group1
   ds-lite tunnel prefix-length 64
   port-range 4096
   ds-lite address-group dt-addr-group group-id 1
    section 0 11.1.1.1 mask 24
   ds-lite outbound 3000 address-group dt-addr-group
   local-ipv6 2001:db8:2:2:2::12 prefix-length 128
   remote-ipv6 2001:db8:D000:: prefix-length 41
   ds-lite alg all
   ds-lite filter mode full-cone
  #
  user-group ds-lite-1
  #
  aaa
   authentication-scheme auth1
   accounting-scheme acct1
    accounting start-fail online
  #
   domain ds-lite-domain
    authentication-scheme auth1
    accounting-scheme acct1
    prefix-assign-mode unshared
    ipv6-pool ipv6-pppoe-nd-1 
    ipv6-pool ipv6-pppoe-pd-1
    radius-server group rad-ser
    user-group ds-lite-1 bind ds-lite instance ds-lite-1
    user-basic-service-ip-type ipv6
  #
  interface gigabitethernet0/1/1
   ipv6 enable
   isis ipv6 enable 1000
  #
  interface gigabitethernet0/1/2
   ip address 2.2.2.1 24
   isis enable 100
  #
  return
  ```