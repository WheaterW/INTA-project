Example for Configuring 2:1 Boards for Inter-Board Hot Backup in Distributed NAT444
===================================================================================

This section provides an example for configuring 2:1 boards for inter-board hot backup in distributed NAT444.

#### Networking Requirements

In a distributed networking scenario shown in [Figure 1](#EN-US_TASK_0172362461__fig16647104911398), a BRAS is equipped with three CGN boards in slots 1, 2, and 3. CPU 0 in slot 1 and CPU 0 in slot 2 perform inter-board hot backup for NAT444 services. Users get online using PPPoE. The BRAS assigns a private IP address range to each CPE, and each CPE assigns IP addresses from the range to terminal PCs. After the CPEs perform NAT for user traffic, the BRAS performs NAT again. As the user traffic is in a large volume, capacity expansion is required. Based on the 1:1 master/backup NAT board solution, a service board is added to slot 3 and its backup board is in slot 2. In 1:1 solution, the service board in 1 is the master, and that in 2 is the backup.

**Figure 1** 2:1 board expansion for inter-board hot backup in distributed NAT444![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/2/0.10.


  
![](figure/en-us_image_0205135985.png)

#### Networking Solution

* Traffic diversion policy: The routes of the public address pool are advertised by BGP using the **network** command.
* Port allocation policy: Ports are allocated in semi-dynamic mode, which flexibly increases the number of user ports.
* User source tracing policy: RADIUS user logs are used to reduce the load on the BRAS and RADIUS server.
* Backup policy: 2:1 board expansion for inter-board hot backup on a single device is used to ensure the reliability of NAT services.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Apply and load a GTL license that enables NAT and configure NAT sessions on service boards.
2. Enable HA hot backup.
3. Configure a RADIUS service group named **nat-pppoe-radius**.
4. Configure user information and RADIUS authentication on the BRAS.
5. Configure a private network address pool named **nat-pppoe-pool-1**.
6. Create a basic ACL used to match against the private address pool.
7. Configure basic functions of the NAT instance named **nat444-1**.
8. Configure a distributed NAT traffic diversion policy.
9. Enable the device to advertise public routes.
10. Configure a private network domain and bind a NAT instance to it.


#### Procedure

1. Apply and load a GTL license that enables NAT and configure NAT sessions on service boards.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
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
   LME0NATDS00 Resource 16 2M NAT Session
   Item name (View)Resource License Command-line
   -------------------------------------------------------------
   LME0NATDS00 (Sys)nat session-table size table-size slot slot-id
   Master board license state: Normal.
   ```
   ```
   [~BRAS] license
   ```
   ```
   [*BRAS-license] active nat session-table size 6 slot 1
   ```
   ```
   [*BRAS-license] active nat session-table size 6 slot 2
   ```
   ```
   [*BRAS-license] active nat session-table size 6 slot 3
   ```
   ```
   [*BRAS-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*BRAS-license] active nat bandwidth-enhance 40 slot 2
   ```
   ```
   [*BRAS-license] active nat bandwidth-enhance 40 slot 3
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
3. Configure a RADIUS service group named **nat-pppoe-radius**.
   
   
   ```
   [~BRAS] radius-server group nat-pppoe-radius
   ```
   ```
   [*BRAS-radius-nat-pppoe-radius] radius-server authentication 192.168.10.10 1824 weight 0
   ```
   ```
   [*BRAS-radius-nat-pppoe-radius] radius-server accounting 192.168.10.10 1825 weight 0
   ```
   ```
   [*BRAS-radius-nat-pppoe-radius] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*BRAS-radius-nat-pppoe-radius] commit
   ```
   ```
   [~BRAS-radius-nat-pppoe-radius] quit
   ```
4. Configure a private network address pool named **nat-pppoe-pool-1** and bind it to a DNS server.
   
   
   ```
   [~BRAS] ip pool nat-pppoe-pool-1 bas local
   ```
   ```
   [*BRAS-ip-pool-nat-pppoe-pool-1] gateway 10.1.0.1 255.255.0.0
   ```
   ```
   [*BRAS-ip-pool-nat-pppoe-pool-1] section 0 10.1.0.2 10.1.0.255
   ```
   ```
   [*BRAS-ip-pool-nat-pppoe-pool-1] dns-server 192.168.224.68 192.168.225.68
   ```
   ```
   [*BRAS-ip-pool-nat-pppoe-pool-1] commit
   ```
   ```
   [~BRAS-ip-pool-nat-pppoe-pool-1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In consideration of the planned number of online private network users, configure an address pool using the [**ip pool**](cmdqueryname=ip+pool) command and multiple sections in the pool. In capacity expansion, add sections in the private address pool or private address pools.
5. Create a basic ACL used to match against the private address pool.
   
   
   ```
   [~BRAS] acl number 2011
   ```
   ```
   [*BRAS-acl-basic-2011] rule permit source 10.1.0.0 0.0.255.255
   ```
   ```
   [*BRAS-acl-basic-2011] commit
   ```
   ```
   [~BRAS-acl-basic-2011] quit
   ```
6. Configure basic functions of the NAT instance named **nat444-1**.
   
   
   1. Bind a service-location to a service board for capacity expansion.
      
      ```
      [~BRAS] service-location 1
      ```
      ```
      [*BRAS-service-location-1] location slot 1 backup slot 2//Slot 1 houses the active service board, and slot 2 houses the standby service board.
      ```
      ```
      [*BRAS-service-location-1] commit
      ```
      ```
      [~BRAS-service-location-1] quit
      ```
   2. Create a service-instance group.
      
      ```
      [~BRAS] service-instance-group nat444-group1
      ```
      ```
      [*BRAS-service-instance-group-nat444-group1] service-location 1
      ```
      ```
      [*BRAS-service-instance-group-nat444-group1] commit
      ```
      ```
      [~BRAS-service-instance-group-nat444-group1] quit
      ```
      ```
      [~BRAS] service-instance-group nat444-group2
      ```
      ```
      [*BRAS-service-instance-group-nat444-group2] service-location 2
      ```
      ```
      [*BRAS-service-instance-group-nat444-group2] commit
      ```
      ```
      [~BRAS-service-instance-group-nat444-group2] quit
      ```
   3. Create a NAT instance and bind it to a service-instance group to specify service board resources.
      
      ```
      [~BRAS] nat instance nat444-1 id 1
      ```
      ```
      [*BRAS-nat-instance-nat444-1] service-instance-group nat444-group1
      ```
   4. Start the port semi-dynamic allocation mode to enable the device to pre-allocate 4096 ports to a single user for the first time and allocate 1024 incrementally each time out of the maximum of three times.
      
      ```
      [*BRAS-nat-instance-nat444-1] port-range 4096 extended-port-range 1024 extended-times 3
      ```
   5. Configure a private network address pool named **pppoe-public-1**.
      
      ```
      [*BRAS-nat-instance-nat444-1] nat address-group pppoe-public-1 group-id 1
      ```
   6. Configure a public IP address.
      
      ```
      [*BRAS-nat-instance-nat444-1-nat-address-group-pppoe-public-1] section 0 1.1.1.0 mask 24
      ```
      ```
      [*BRAS-nat-instance-nat444-1-nat-address-group-pppoe-public-1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Specifying a mask to configure public IP addresses enables the device to advertise a UNR to the network segment, without summarizing the routes. In this example, a UNR to 1.1.1.0/24 is advertised.
   7. Configure a translation policy for the NAT address pool.
      
      ```
      [*BRAS-nat-instance-nat444-1] nat outbound 2011 address-group pppoe-public-1
      ```
   8. Enable the ALG function for all protocols, including FTP, PPTP, RTSP, and SIP.
      
      ```
      [*BRAS-nat-instance-nat444-1] nat alg all
      ```
   9. Configure the 3-tuple mode.
      
      ```
      [*BRAS-nat-instance-nat444-1] nat filter mode full-cone
      ```
      ```
      [*BRAS-nat-instance-nat444-1] commit
      ```
      ```
      [~BRAS-nat-instance-nat444-1] quit
      ```
   10. Configure a user group of which users access the Internet.
       
       ```
       [~BRAS] user-group pppoe-nat-1
       ```
       ```
       [*BRAS] commit
       ```
7. Configure basic functions of the NAT instance named **nat444-2**.
   
   
   1. Bind a service-location to a service board for capacity expansion.
      
      ```
      [~BRAS] service-location 2
      ```
      ```
      [*BRAS-service-location-2] location slot 3 backup slot 2
      ```
      ```
      [*BRAS-service-location-2] commit
      ```
      ```
      [~BRAS-service-location-2] quit
      ```
   2. Create a service-instance group.
      
      ```
      [~BRAS] service-instance-group nat444-group2
      ```
      ```
      [*BRAS-service-instance-group-nat444-group2] service-location 2
      ```
      ```
      [*BRAS-service-instance-group-nat444-group2] commit
      ```
      ```
      [~BRAS-service-instance-group-nat444-group2] quit
      ```
   3. Create a NAT instance and bind it to a service-instance group to specify service board resources.
      
      ```
      [~BRAS] nat instance nat444-2 id 1
      ```
      ```
      [*BRAS-nat-instance-nat444-2] service-instance-group nat444-group2
      ```
   4. Start the port semi-dynamic allocation mode to enable the device to pre-allocate 4096 ports to a single user for the first time and allocate 1024 incrementally each time out of the maximum of three times.
      
      ```
      [*BRAS-nat-instance-nat444-2] port-range 4096 extended-port-range 1024 extended-times 3
      ```
   5. Configure a private network address pool named **pppoe-public-2**.
      
      ```
      [*BRAS-nat-instance-nat444-2] nat address-group pppoe-public-2 group-id 1
      ```
   6. Configure a public IP address.
      
      ```
      [*BRAS-nat-instance-nat444-2-nat-address-group-pppoe-public-2] section 0 1.1.2.0 mask 24
      ```
      ```
      [*BRAS-nat-instance-nat444-2-nat-address-group-pppoe-public-2] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Specifying a mask to configure public IP addresses enables the device to advertise a UNR to the network segment, without summarizing the routes. In this example, a UNR to 1.1.2.0/24 is advertised.
   7. Configure a translation policy for the NAT address pool.
      
      ```
      [*BRAS-nat-instance-nat444-2] nat outbound 2011 address-group pppoe-public-1
      ```
   8. Enable the ALG function for all protocols, including FTP, PPTP, RTSP, and SIP.
      
      ```
      [*BRAS-nat-instance-nat444-2] nat alg all
      ```
   9. Configure the 3-tuple mode.
      
      ```
      [*BRAS-nat-instance-nat444-2] nat filter mode full-cone
      ```
      ```
      [*BRAS-nat-instance-nat444-2] commit
      ```
      ```
      [~BRAS-nat-instance-nat444-2] quit
      ```
   10. Configure a user group of which users access the Internet.
       
       ```
       [~BRAS] user-group pppoe-nat-2
       ```
       ```
       [*BRAS] commit
       ```
8. Configure a distributed NAT traffic diversion policy.
   
   
   1. Create an ACL for directing distributed NAT traffic to service boards.
      
      ```
      [~BRAS] acl 7001
      ```
      ```
      [*BRAS-acl-ucl-7001] rule permit ip source user-group pppoe-nat-1
      ```
      ```
      [*BRAS-acl-ucl-7001] commit
      ```
      ```
      [~BRAS-acl-ucl-7001] quit
      ```
      ```
      [~BRAS] acl 7002
      ```
      ```
      [*BRAS-acl-ucl-7002] rule permit ip source user-group pppoe-nat-2
      ```
      ```
      [*BRAS-acl-ucl-7002] commit
      ```
      ```
      [~BRAS-acl-ucl-7002] quit
      ```
   2. Configure a traffic classifier.
      
      ```
      [~BRAS] traffic classifier pppoe-nat-1 operator or
      ```
      ```
      [*BRAS-classifier-pppoe-nat-1] if-match acl 7001
      ```
      ```
      [*BRAS-classifier-pppoe-nat-1] commit
      ```
      ```
      [~BRAS-classifier-pppoe-nat-1] quit
      ```
      ```
      [~BRAS] traffic classifier pppoe-nat-2 operator or
      ```
      ```
      [*BRAS-classifier-pppoe-nat-2] if-match acl 7002
      ```
      ```
      [*BRAS-classifier-pppoe-nat-2] commit
      ```
      ```
      [~BRAS-classifier-pppoe-nat-2] quit
      ```
   3. Configure a traffic behavior.
      
      ```
      [~BRAS] traffic behavior pppoe-nat-1
      ```
      ```
      [*BRAS-behavior-pppoe-nat-1] nat bind instance nat444-1
      ```
      ```
      [*BRAS-behavior-pppoe-nat-1] commit
      ```
      ```
      [~BRAS-behavior-pppoe-nat-1] quit
      ```
      ```
      [~BRAS] traffic behavior pppoe-nat-2
      ```
      ```
      [*BRAS-behavior-pppoe-nat-2] nat bind instance nat444-2
      ```
      ```
      [*BRAS-behavior-pppoe-nat-2] commit
      ```
      ```
      [~BRAS-behavior-pppoe-nat-2] quit
      ```
   4. Bind a C-B pair to a global traffic distribution policy.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If no traffic distribution policy is used globally, add one and apply it in the system view. If a traffic distribution policy is used globally, bind the C-B pair to it. If multiple C-B pairs are configured in a traffic distribution policy, packets are matched against them in a top-to-bottom order.
      
      ```
      [~BRAS] traffic policy global-policy
      ```
      ```
      [*BRAS-trafficpolicy-global-policy] classifier pppoe-nat-1 behavior pppoe-nat-1
      ```
      ```
      [*BRAS-trafficpolicy-global-policy] classifier pppoe-nat-2 behavior pppoe-nat-2
      ```
      ```
      [*BRAS-trafficpolicy-global-policy] commit
      ```
      ```
      [~BRAS-trafficpolicy-global-policy] quit
      ```
9. Enable the device to advertise public routes. In the following example, BGP is used.
   
   
   ```
   [~BRAS] bgp 64640
   ```
   ```
   [*BRAS-bgp-64640] network 1.1.1.0 24
   ```
   ```
   [*BRAS-bgp-64640] commit
   ```
   ```
   [~BRAS-bgp-64640] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Select a proper routing protocol to advertise public network routes. In this example, BGP is used to advertise the route to the public address pool in network mode. If a public address pool is configured using a mask, run the **network** command to advertise a route. Do not configure a black-hole summary route, which prevents a failure to forward reverse traffic.
10. Configure a private network domain and bind a NAT instance to it.
    
    
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
    [*BRAS-aaa-authen-auth1] commit
    ```
    ```
    [~BRAS-aaa-authen-auth1] quit
    ```
    ```
    [~BRAS-aaa] accounting-scheme acct1
    ```
    ```
    [*BRAS-aaa-accounting-acct1] accounting-mode radius
    ```
    ```
    [~BRAS-aaa-accounting-acct1] commit
    ```
    ```
    [~BRAS-aaa-accounting-acct1] quit
    ```
    ```
    [~BRAS-aaa] domain nat-pppoe
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] ip-pool nat-pppoe-pool-1
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] user-group pppoe-nat-1 bind nat instance nat444-1
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] user-group pppoe-nat-2 bind nat instance nat444-2
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] radius-server group nat-pppoe-radius
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] commit
    ```
    ```
    [*BRAS-aaa-domain-nat-pppoe] quit
    ```
11. Verify the configuration.
    
    
    
    # Verify that the public network routes are properly advertised.
    
    ```
    <BRAS> display ip routing-table
    ```
    ```
    Route Flags: R - relay, D - download to fib
    ---------------------------------------------------------------------
    Routing Table: Public
    Destinations : 2 Routes : 2
    Destination/Mask Proto Pre Cost Flags NextHop Interface
    10.1.0.0/16 Unr 61 10 D 127.0.0.1 NULL0
    1.1.1.0/24 Unr 64 10 D 127.0.0.1 InLoopBack0
    ```
    
    # Verify that the master/backup status in the service-location is correct.
    
    ```
    <BRAS> display service-location 1
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
    ```
    <BRAS> display service-location 2
    ```
    ```
    service-location 1
    Location slot ID: 3 
    Current location slot ID: 3 
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
    ----------------------------------------------------------------
    User Type                             : NAT444
    CPE IP                                : 10.1.0.253
    User ID                               : 1132
    VPN Instance                          : -
    Address Group                         : pppoe-public-1
    NAT Instance                          : nat444-1
    Public IP                             : 192.0.2.0
    Start Port                            : 1024
    Port Range                            : 4096
    Port Total                            : 4096
    Extend Port Alloc Times               : 0
    Extend Port Alloc Number              : 0
    First/Second/Third Extend Port Start  : 0/0/0
    Total/TCP/UDP/ICMP Session Limit      : 8192/10240/10240/512
    Total/TCP/UDP/ICMP Session Current    : 709/0/709/0
    Total/TCP/UDP/ICMP Rev Session Limit  : 8192/10240/10240/512
    Total/TCP/UDP/ICMP Rev Session Current: 0/0/0/0
    Total/TCP/UDP/ICMP Port Limit         : 0/0/0/0
    Total/TCP/UDP/ICMP Port Current       : 709/0/709/0
    Nat ALG Enable                        : ALL
    Token/TB/TP                           : 0/0/0
    Port Forwarding Flag                  : Non Port Forwarding
    Port Forwarding Ports                 : 0 0 0 0 0
    Aging Time(s)                         : -
    Left Time(s)                          : -
    Port Limit Discard Count              : 0
    Session Limit Discard Count           : 0
    Fib Miss Discard Count                : 0
    -->Transmit Packets                   : 5041
    -->Transmit Bytes                     : 2272053
    -->Drop Packets                       : 0
    <--Transmit Packets                   : 3330
    <--Transmit Bytes                     : 1794897
    <--Drop Packets                       : 0
    -----------------------------------------------------------------
    ```
    ```
    <BRAS> display nat user-information slot 2 verbose
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 2 
    Total number: 1.
    ----------------------------------------------------------------
    User Type                            : NAT444
    CPE IP                               : 10.1.0.253
    User ID                              : 1132
    VPN Instance                         : -
    Address Group                        : pppoe-public-1
    NAT Instance                         : nat444-1
    Public IP                            : 192.0.2.0
    Start Port                           : 1024
    Port Range                           : 4096
    Port Total                           : 4096
    Extend Port Alloc Times              : 0
    Extend Port Alloc Number             : 0
    First/Second/Third Extend Port Start : 0/0/0
    Total/TCP/UDP/ICMP Session Limit     : 8192/10240/10240/512
    Total/TCP/UDP/ICMP Session Current   : 709/0/709/0
    Total/TCP/UDP/ICMP Rev Session Limit : 8192/10240/10240/512
    Total/TCP/UDP/ICMP Rev Session Current: 0/0/0/0
    Total/TCP/UDP/ICMP Port Limit        : 0/0/0/0
    Total/TCP/UDP/ICMP Port Current      : 709/0/709/0
    Nat ALG Enable                       : ALL
    Token/TB/TP                          : 0/0/0
    Port Forwarding Flag                 : Non Port Forwarding
    Port Forwarding Ports                : 0 0 0 0 0
    Aging Time(s)                        : -
    Left Time(s)                         : -
    Port Limit Discard Count             : 0
    Session Limit Discard Count          : 0
    Fib Miss Discard Count               : 0
    -->Transmit Packets                  : 0
    -->Transmit Bytes                    : 0
    -->Drop Packets                      : 0
    <--Transmit Packets                  : 0
    <--Transmit Bytes                    : 0
    <--Drop Packets                      : 0
    -----------------------------------------------------------------
    ```
    
    # Verify that session table information on the master and backup service boards is correct.
    
    ```
    <BRAS> display nat session table slot 1
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 1 
    Current total sessions: 709.
    udp: 10.1.0.253:28195[192.0.2.0:1723]-->*:*
    udp: 10.1.0.253:20069[192.0.2.0:1727]--> *:*
    udp: 10.1.0.253:59556[192.0.2.0:1085]--> *:*
    udp: 10.1.0.253:28384[192.0.2.0:2047]--> *:*
    ```
    ```
    <BRAS> display nat session table slot 2
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 2 
    Current total sessions: 709.
    udp: 10.1.0.253:28195[192.0.2.0:1723]-->*:*
    udp: 10.1.0.253:20069[192.0.2.0:1727]--> *:*
    udp: 10.1.0.253:59556[192.0.2.0:1085]--> *:*
    udp: 10.1.0.253:28384[192.0.2.0:2047]--> *:*
    ```
    
    # Run the **display nat statistics** command to view the number of sent and received packets on the master service board.
    
    ```
    <BRAS> display nat statistics received slot 1
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 1 
    ---------------------------------------------------------------------
    Packets received from interface :632014772
    Packets received from mainboard :29450
    Packets received by nat entry :255587842
    receive hrp packets from peer device :0
    receive boardhrp packets from peer board :0
    ---------------------------------------------------------------------------
    ```
    ```
    <BRAS> display nat statistics transmitted slot 1
    ```
    ```
    This operation will take a few minutes. Press 'Ctrl+C' to break
    Slot: 1 
    ---------------------------------------------------------------------
    Packets transmitted to interface   :159142427
    Packets transmitted to mainboard   :22219
    Seclog packets transmitted         :0
    Syslog packets transmitted         :0
    Userinfo log msg transmitted to cp :0
    Transparent packet with nat        :65080312
    Transparent packet without nat     :0
    sessions sent by hrp               :0
    UserTbl sent by hrp                :0
    UserTbl sent by Boardhrp           :0
    sessions sent by Boardhrp          :0
    -----------------------------------------------------------------
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
   active nat session-table size 6 slot 1 
   active nat session-table size 6 slot 2 
   active nat session-table size 6 slot 3 
   active nat bandwidth-enhance 40 slot 1
   active nat bandwidth-enhance 40 slot 2
   active nat bandwidth-enhance 40 slot 3
  #
  radius-server group nat-pppoe-radius
   radius-server authentication 192.168.10.10 1824 weight 0
   radius-server accounting 192.168.10.10 1825 weight 0
   radius-server shared-key-cipher %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
  #
  ip pool nat-pppoe-pool-1 bas local
   gateway 10.1.0.1 255.255.0.0
   section 0 10.1.0.2 10.1.0.255
   dns-server 192.168.224.68 192.168.225.68
  #
  acl number 2011
   rule permit source 10.1.0.0 0.0.255.255
  #
  acl number 7001
   rule permit ip source user-group pppoe-nat-1
  #
  acl number 7002
   rule permit ip source user-group pppoe-nat-2
  #
  traffic classifier pppoe-nat-1 operator or
   if-match acl 7001 precedence 1
  #
  traffic classifier pppoe-nat-2 operator or
   if-match acl 7002 precedence 1
  #
  traffic behavior pppoe-nat-1
   nat bind instance nat444-1
  #
  traffic behavior pppoe-nat-2
   nat bind instance nat444-2
  #
  traffic policy global-policy
   share-mode
   classifier pppoe-nat-1 behavior pppoe-nat-1 precedence 1
   classifier pppoe-nat-2 behavior pppoe-nat-2 precedence 2
  #
  traffic-policy global-policy inbound
  #
  bgp 64640
   network 1.1.1.0 24
  #
  service-ha hot-backup enable
  service-ha delay-time 10
  #
  service-location 1
   location slot 1 backup slot 2  
  #
  service-location 2
   location slot 3 backup slot 2  
  #
  service-instance-group nat444-group1
   service-location 1
  #
  service-instance-group nat444-group2
   service-location 2
  #
  nat instance nat444-1 id 1
   service-instance-group nat444-group1
   port-range 4096 extended-port-range 1024 extended-times 3
   nat address-group pppoe-public-1 group-id 1
    section 0 1.1.1.0 mask 24
   nat outbound 2011 address-group pppoe-public-1
   nat alg all
   nat filter mode full-cone
  #
  nat instance nat444-2 id 1
   service-instance-group nat444-group2
   port-range 4096 extended-port-range 1024 extended-times 3
   nat address-group pppoe-public-2 group-id 1
    section 0 1.1.2.0 mask 24
   nat outbound 2011 address-group pppoe-public-2
   nat alg all
   nat filter mode full-cone
  #
  user-group pppoe-nat-1
  user-group pppoe-nat-2
  #
  ip pool natbras bas local
   gateway 192.168.0.1 255.255.0.0
   section 0 192.168.0.2 192.168.0.254
  #
  aaa
   authentication-scheme auth1
    authentication-mode radius
   accounting-scheme acct1
    accounting-mode radius
   domain nat-pppoe
    authentication-scheme auth1
    accounting-scheme acct1
    ip-pool nat-pppoe-pool-1
    user-group pppoe-nat-1 bind nat instance nat444-1 
    user-group pppoe-nat-2 bind nat instance nat444-2
    radius-server group nat-pppoe-radius
  #
  interface Virtual-Template1
   ppp authentication-mode auto
  #
  interface GigabitEthernet0/2/0.10
   user-vlan 2010
   pppoe-server bind Virtual-Template 1
   bas
    access-type layer2-subscriber default-domain authentication nat-pppoe
    authentication-method ppp
  #
  return
  ```