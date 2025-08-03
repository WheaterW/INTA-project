Example for Configuring Centralized NAT64 Inter-Board Hot Backup
================================================================

This section provides an example for configuring centralized NAT64 inter-board hot backup.

#### Networking Requirements

In a centralized NAT64 networking scenario shown in [Figure 1](#EN-US_TASK_0172362475__fig_01), a NAT64 CGN device is deployed close to the CR on the MAN core and equipped with two CGN boards. IPv6 users access the IPv4 network through a BRAS, CR, and NAT64 CGN device in sequence. The NAT64 CGN device translates IPv6 addresses of enterprise users to external IPv4 addresses so that the enterprise users can access the IPv4 Internet. **Figure 1** Networking of inter-board hot backup in a centralized NAT64 scenario  
![](images/fig_dc_ne_cgn_0014.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Apply for and configure NAT64 session resources and configure a NAT64 GTL license file.
2. Bind the CPU of each service board to the NAT64 instance.
3. Configure basic NAT64 functions.
4. Configure a traffic classification rule, a NAT64 traffic behavior, and a NAT64 traffic distribution policy, and apply the NAT64 traffic distribution policy.
5. Enable the NAT64 device to advertise public routes.


#### Procedure

1. Apply for and configure NAT64 session resources and configure a NAT64 GTL license file.
   
   
   ```
   <HUAWEI> display license
   ```
   ```
   Item name     Item type Value  Description
    -------------------------------------------------------------
    LME0CONN01     Resource  64    Concurrent Users(1k)
    LME0NATDS00    Resource  16    2M NAT Session
     
   ..................................................
    Item name     (View)Resource License Command-line
    -------------------------------------------------------------
    LME0NATDS00    (Sys)nat session-table size table-size slot slot-id 
    Master board license state: Normal.
   
   ```
   ```
   [~HUAWEI] sysname NAT64_CGN
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~NAT64] vsm on-board-mode disable
   ```
   ```
   [*NAT64] commit
   ```
   ```
   [~NAT64_CGN] License
   ```
   ```
   [~NAT64_CGN-license] active nat session-table size 16 slot 1 
   ```
   ```
   [*NAT64_CGN-license] active nat session-table size 16 slot 2 
   ```
   ```
   [*NAT64_CGN-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*NAT64_CGN-license] active nat bandwidth-enhance 40 slot 2
   ```
   ```
   [*NAT64_CGN-license] active nat64 vsuf slot 1
   ```
   ```
   [*NAT64_CGN-license] active nat64 vsuf slot 2
   ```
   ```
   [*NAT64_CGN-license] commit
   ```
   ```
   [~NAT64_CGN-license] quit
   ```
2. Bind the CPU of each service board to the NAT64 instance.
   
   
   ```
   [~NAT64_CGN] service-location 1
   ```
   ```
   [*NAT64_CGN-service-location-1] location slot 1 backup slot 2
   ```
   ```
   [*NAT64_CGN-service-location-1] commit
   ```
   ```
   [~NAT64_CGN-service-location-1] quit
   ```
   ```
   [~NAT64_CGN] service-instance-group group1
   ```
   ```
   [*NAT64_CGN-instance-group-group1] service-location 1
   ```
   ```
   [*NAT64_CGN-instance-group-group1] commit
   ```
   ```
   [~NAT64_CGN-instance-group-group1] quit
   ```
   ```
   [~NAT64_CGN] nat64 instance nat64-1 id 1
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] service-instance-group group1
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] commit
   ```
   ```
   [~NAT64_CGN-nat64-instance-nat64-1] quit
   ```
3. Configure basic NAT64 functions.
   
   
   ```
   [~NAT64_CGN] nat64 instance nat64-1 id 1
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] port-range 4096
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 alg ftp
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 alg http
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 address-group nat64-group1 group-id 1
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1-nat64-address-group-nat64-group1] section 0 11.1.1.0 mask 24
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1-nat64-address-group-nat64-group1] quit
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 log host 1.1.1.1 514 source 2.2.2.2 514 name loghost
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 log user enable
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 filter mode full-cone
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] nat64 prefix 64:FF9B:: prefix-length 96 1
   ```
   ```
   [*NAT64_CGN-nat64-instance-nat64-1] commit
   ```
   ```
   [~NAT64_CGN-nat64-instance-nat64-1] quit
   ```
4. Configure a traffic classification rule, a NAT64 traffic behavior, and a NAT64 traffic distribution policy, and apply the NAT64 traffic distribution policy.
   
   
   1. Configure an ACL-based traffic classification rule so that only hosts on internal network segment 64:FF9B/96 can access the network segment 192.168.0.133/30 on the IPv4 Internet.
      
      ```
      [~NAT64_CGN] acl ipv6 number 3003
      ```
      ```
      [*NAT64_CGN-acl6-adv-3003] rule 5 permit ipv6 source 2001:db8::1:1112 126 destination 64:FF9B::C0A8:85 96
      ```
      ```
      [*NAT64_CGN-acl6-adv-3003] commit
      ```
      ```
      [~NAT64_CGN-acl6-adv-3003] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A NAT64 user packet's destination IP address is an IPv6 address combined by an IPv4 address and a NAT64 prefix. You are advised to use source+destination addresses for traffic diversion, with the destination address being the same as the NAT64 prefix.
   2. Configure a traffic classifier.
      
      ```
      [~NAT64_CGN] traffic classifier c1
      ```
      ```
      [*NAT64_CGN-classifier-c1] if-match ipv6 acl 3003
      ```
      ```
      [*NAT64_CGN-classifier-c1] commit
      ```
      ```
      [~NAT64_CGN-classifier-c1] quit
      ```
   3. Configure a traffic behavior and bind the traffic behavior to the NAT64 instance.
      
      ```
      [~NAT64_CGN] traffic behavior b1
      ```
      ```
      [*NAT64_CGN-behavior-b1] nat64 bind instance nat64-1
      ```
      ```
      [*NAT64_CGN-behavior-b1] commit
      ```
      ```
      [~NAT64_CGN-behavior-b1] quit
      ```
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If multiple behavior settings are configured, packets are matched against them in a top-to-bottom order.
   4. Configure a traffic policy and associate the ACL-based traffic classification rule with the traffic behavior.
      
      ```
      [~NAT64_CGN] traffic policy p1
      ```
      ```
      [*NAT64_CGN-trafficpolicy-p1] classifier c1 behavior b1
      ```
      ```
      [*NAT64_CGN-trafficpolicy-p1] commit
      ```
      ```
      [~NAT64_CGN-trafficpolicy-p1] quit
      ```
   5. Configure an IPv6 address in the user-side interface view.
      
      ```
      [~NAT64_CGN] interface GigabitEthernet 0/1/1
      ```
      ```
      [~NAT64_CGN-GigabitEthernet0/1/1] ipv6 enable
      ```
      ```
      [*NAT64_CGN-GigabitEthernet0/1/1] ipv6 address 2001:db8::1:110e 126
      ```
   6. Apply the NAT64 traffic diversion policy in the user-side interface view.
      
      ```
      [*NAT64_CGN-GigabitEthernet0/1/1] traffic-policy p1 inbound
      ```
      ```
      [*NAT64_CGN-GigabitEthernet0/1/1] commit
      ```
      ```
      [~NAT64_CGN-GigabitEthernet0/1/1] quit
      ```
   7. Enable the NAT64 device to advertise public routes.
      
      The NAT64 device must advertise private prefix routes and public address pool rules. Private network VPNs are not supported.
5. Verify the configuration.
   
   
   
   # Verify the status of the active and standby service boards.
   
   # Verify that the public network routes are properly advertised.
   
   ```
   [NAT64_CGN] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib
   -------------------------------------------------------------------
   Routing Table: Public
   Destinations  : 21813            Routes : 21814
   Destination/Mask Proto Pre Cost Flags NextHop Interface
   11.1.1.0/24     Unr 64   10   D  127.0.0.1 InLoopBack0
   ```
   
   # Verify that the master/backup status in the service-location is correct.
   
   ```
   [NAT64_CGN] display service-location 1
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
   
   # Verify that the license resources are correct.
   
   ```
   [NAT64_CGN] display nat session-table size slot 1
   ```
   ```
   --------------------------------------------------------------
   TotalSize :64M
   UsedSize :32 M
   FreeSize :32 M
   SlotID CpuID CurSessTblSize CfgSessTblSize ValidFlag
   1 0(engine) 16 M 16 M Valid
   2 0(engine) 16 M 16 M Valid
   -----------------------------------------------------------------
   ```
   
   # Verify that user table information on the master and slave service boards is correct.
   
   ```
   [NAT64_CGN] display nat user-information slot 1 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break
   Slot: 1
   Total number: 2.
   --------------------------------------------------------------
   User Type                             : NAT64
   IPv6Address                           : 2001:db8:2068::0002/128
   User ID                               : -
   VPN Instance                          : -
   Address Group                         : nat64-group1-1
   NoPAT Address Group                   : -
   NAT64 Instance                        : nat64-1
   Public IP                             : 198.51.100.0
   NoPAT Public IP                       : 0.0.0.0
   Start Port                            : 1024
   Port Range                            : 4096
   Port Total                            : 4096
   MTU                                   : 1500
   Extend Port Alloc Times               : 0
   Extend Port Alloc Number              : 0
   First/Second/Third Extend Port Start  : 0/0/0
   Total/TCP/UDP/ICMP Session Limit      : 8192/10240/10240/512
   Total/TCP/UDP/ICMP Session Current    : 3/0/2/1
   Total/TCP/UDP/ICMP Rev Session Limit  : 0/0/0/0
   Total/TCP/UDP/ICMP Rev Session Current: 0/0/0/0
   Nat ALG Enable                        : FTP/HTTP
   Token/TB/TP                           : 0/0/0
   Port Forwarding Flag                  : Non Port Forwarding
   Port Forwarding Ports                 : 0 0 0 0 0
   Aging Time(s)                         : -
   Left Time(s)                          : -
   Port Limit Discard Count              : 0
   Session Limit Discard Count           : 0
   Fib Miss Discard Count                : 0
   -->Transmit Packets                   : 230853
   -->Transmit Bytes                     : 50325954
   -->Drop Packets                       : 0
   <--Transmit Packets                   : 0
   <--Transmit Bytes                     : 0
   <--Drop Packets                       : 0
   --------------------------------------------------------------
   ```
   
   # Verify that user session table information on the master and slave service boards is correct.
   
   ```
   [NAT64_CGN] display nat session table slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break
   Slot: 1
   Current total sessions:3.
   icmp: [2001:db8:2068::0002]:200(198.51.100.0:200)--> *:32768
   udp: [2001:db8:2068::0002]:-( 198.51.100.0:-)-->[2001:db8:2091::]:-(0.0.0.0:-), frag_ID:100
   udp: [2001:db8:2068::0002]:1024(198.51.100.0:1024)--> *:*
   ```
   
   # Run the **display nat statistics** command to view the number of sent and received packets on the master service board.
   
   ```
   [NAT64_CGN] display nat statistics received slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break
   Slot: 1 
   ------------------------------------------------------------------------
   Packets received from interface :632014772
   Packets received from mainboard :29450
   Packets received by nat entry :255587842
   -------------------------------------------------------------------------
   ```
   ```
   [NAT64_CGN] display nat statistics transmitted slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break
   Slot: 1
   --------------------------------------------------------------
   Packets transmitted to interface :159142427
   Packets transmitted to mainboard :22219
   Seclog packets transmitted :0
   SYSLOG packets transmitted :0
   Userinfo log msg transmitted to cp :0
   Transparent packet with nat :65080312
   Transparent packet without nat :0
   ---------------------------------------------------------------
   ```

#### Configuration Files

* NAT64 CGN device configuration file
  
  ```
  #
  sysname NAT64_CGN
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 16 slot  
   active nat session-table size 16 slot  
   active nat bandwidth-enhance 40 slot 1
   active nat bandwidth-enhance 40 slot 2
   active nat64 vsuf slot 1
   active nat64 vsuf slot 2
  #
  acl ipv6 number 3003
   rule 5 permit ipv6 source 2001:db8::1:1112 126 destination 64:FF9B::C0A8:85 96
  #
  traffic classifier c1 operator or
   if-match ipv6 acl 3003 precedence 1
  #
  traffic behavior b1
   nat64 bind instance nat64-1
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  interface GigabitEthernet 0/1/1
   ipv6 enable
   ipv6 address 2001:db8::1:110e 126
   traffic-policy p1 inbound
  #
  service-ha hot-backup enable
  service-ha delay-time 10
  #
  service-location 1
   location slot 1 backup slot 2
  #
  service-instance-group group1
   service-location 1
  #
  nat64 instance nat64-1 id 1
   service-instance-group group1
   port-range 4096
   nat64 alg ftp
   nat64 alg http
   nat64 address-group nat64-group1 group-id 1
    section 0 11.1.1.0 mask 24
   nat64 log host 1.1.1.1 514 source 2.2.2.2 514 name loghost
   nat64 log user enable
   nat64 filter mode full-cone
   nat64 filter mode full-cone
   nat64 prefix 64:FF9B:: prefix-length 96 1
  #
  return
  ```