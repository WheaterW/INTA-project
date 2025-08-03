Example for Configuring Centralized DS-Lite Inter-Board Hot Backup
==================================================================

Example for Configuring Centralized DS-Lite Inter-Board Hot Backup

#### Networking Requirements

In the centralized deployment scenario shown in [Figure 1](#EN-US_TASK_0172362467__fig_01), a CGN device is deployed close to the CR on the MAN core as a standalone device and equipped with two CGN boards to implement 1:1 inter-board backup. A terminal user assigned a private IPv4 address accesses an IPv6 metropolitan area network (MAN) through the customer premises equipment (CPE). The CPE establishes a Dual-Stack Lite (DS-Lite) tunnel to the CGN device. The CPE transmits traffic with the private IPv4 address along the DS-Lite tunnel to the CGN device. The CGN device decapsulates traffic, uses a Network Address Translation (NAT) technique to translate the private IPv4 address to a public IPv4 address, and forwards traffic to the IPv4 Internet.**Figure 1** Centralized DS-Lite networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/1.


  
![](images/fig_dc_ne_ds-lite_0005.png)


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Apply for NAT session resources and configure DS-Lite session resources and the DS-Lite GTL license.
2. Enable HA hot backup.
3. Add the CPU of the master service board to a DS-Lite instance.
4. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
5. Configure a traffic policy for the DS-Lite tunnel.
6. Configure basic DS-Lite functions.
7. Enable the CGN device to advertise routes.

#### Procedure

1. Apply for NAT session resources and configure DS-Lite session resources and the DS-Lite GTL license.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CGN
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CGN] vsm on-board-mode disable
   ```
   ```
   [*CGN] commit
   ```
   ```
   [~HUAWEI] display license
   ```
   ```
    Item name          Item type  Value    Description 
    -------------------------------------------------------------                        
   LCR5NATDS00        Resource   256      2M NAT Session    
                
   ```
   ```
   [~CGN] License
   ```
   ```
   [*CGN-license] active nat session-table size 16 slot 1 
   ```
   ```
   [*CGN-license] active nat session-table size 16 slot 2 
   ```
   ```
   [*CGN-license] active nat bandwidth-enhance 40 slot 1
   ```
   ```
   [*CGN-license] active nat bandwidth-enhance 40 slot 2
   ```
   ```
   [*CGN-license] active ds-lite vsuf slot 1
   ```
   ```
   [*CGN-license] active ds-lite vsuf slot 2
   ```
   ```
   [*CGN-license] commit
   ```
   ```
   [~CGN-license] quit
   ```
2. Enable HA hot backup.
   
   
   ```
   [~CGN] service-ha hot-backup enable
   ```
   ```
   [*CGN] commit
   ```
3. Add the CPU of the master service board to a DS-Lite instance.
   
   
   ```
   [~CGN] service-location 1
   ```
   ```
   [*CGN-service-location-1] location slot 1 backup slot 2 
   ```
   ```
   [*CGN-service-location-1] commit
   ```
   ```
   [~CGN-service-location-1] quit
   ```
   ```
   [~CGN] service-instance-group group1
   ```
   ```
   [*CGN-instance-group-group1] service-location 1
   ```
   ```
   [*CGN-instance-group-group1] commit
   ```
   ```
   [~CGN-instance-group-group1] quit
   ```
   ```
   [~CGN] ds-lite instance ds-lite-1 id 1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] service-instance-group group1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] commit
   ```
   ```
   [~CGN-ds-lite-instance-ds-lite-1] quit
   ```
4. Configure a local IPv6 address and a remote IPv6 address for a DS-Lite tunnel.
   
   
   ```
   [~CGN] ds-lite instance ds-lite-1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] local-ipv6 2001:dB8:2::12 prefix-length 128
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] remote-ipv6 2001:db8:1:: prefix-length 41
   ```
   ```
   [~CGN-ds-lite-instance-ds-lite-1] commit
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] quit
   ```
5. Configure a traffic policy for the DS-Lite tunnel.
   
   
   ```
   [~CGN] acl ipv6 3500
   ```
   ```
   [*CGN-acl6-basic-3500] rule permit ipv6 source 2001:db8:1:: 41 destination 2001:dB8:2::12 128
   ```
   ```
   [*CGN-acl6-basic-3500] commit
   ```
   ```
   [~CGN-acl6-basic-3500] quit
   ```
   ```
   [~CGN] traffic classifier c1
   ```
   ```
   [*CGN-classifier-c1] if-match ipv6 acl 3500
   ```
   ```
   [~CGN-classifier-c1] commit
   ```
   ```
   [*CGN-classifier-c1] quit
   ```
   ```
   [~CGN] traffic behavior b1
   ```
   ```
   [*CGN-behavior-b1] ds-lite bind instance ds-lite-1
   ```
   ```
   [~CGN-behavior-b1] commit
   ```
   ```
   [*CGN-behavior-b1] quit
   ```
   ```
   [~CGN] traffic policy p1
   ```
   ```
   [*CGN-trafficpolicy-p1] classifier c1 behavior b1
   ```
   ```
   [*CGN-trafficpolicy-p1] commit
   ```
   ```
   [~CGN-trafficpolicy-p1] quit
   ```
   ```
   [~CGN] interface gigabitethernet 0/1/1
   ```
   ```
   [~CGN-GigabitEthernet0/1/1] traffic-policy p1 inbound
   ```
   ```
   [*CGN-GigabitEthernet0/1/1] commit
   ```
   ```
   [~CGN-GigabitEthernet0/1/1] quit
   ```
6. Configure basic DS-Lite functions.
   
   
   ```
   [~CGN] ds-lite instance ds-lite-1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] port-range 4096
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] ds-lite address-group group1 group-id 1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1-ds-lite-address-group-group1] section 0 11.1.1.1 mask 24
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1-ds-lite-address-group-group1] quit
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] ds-lite outbound 3500 address-group group1
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] ds-lite alg all
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] ds-lite filter mode full-cone
   ```
   ```
   [*CGN-ds-lite-instance-ds-lite-1] commit
   ```
   ```
   [~CGN-ds-lite-instance-ds-lite-1] quit
   ```
7. Enable the CGN device to advertise routes.
   
   
   
   Advertise public routing information based on the live network status. If a public address pool is configured using a mask, run the **network** command to advertise a route. Do not configure a black-hole summary route, which prevents a failure to forward reverse traffic.
8. Verify the configuration.
   
   
   
   # Run the **display device** command to view the status of the master and slave service boards.
   
   ```
   <CGN> display device
   ```
   ```
   NE40E's Device status:
   Slot #    Type       Online    Register      Status      Primary 
   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
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
   <CGN> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib
   ---------------------------------------------------------------
   Routing Table: Public                                        
            Destinations : 21813    Routes : 21814  
   Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface
        11.1.1.0/24  Unr     64   10          D   127.0.0.1       InLoopBack0
   
   ```
   ```
   <CGN> display ipv6 routing-table 2001:dB8:2::12
   ```
   ```
   Routing Table :      
   Summary Count : 1    
                        
    Destination  : 2001:dB8:2::12                  PrefixLength : 128
    NextHop      : ::1                             Preference   : 64
    Cost         : 10                              Protocol     : Unr
    RelayNextHop : ::                              TunnelID     : 0x0 
    Interface    : InLoopBack0                     Flags        : D     
   ```
   
   # Verify that the master/backup status in the service-location is correct.
   
   ```
   <CGN> display service-location 1
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
   <CGN> display nat user-information slot 1 verbose
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break ... 
   Slot: 1 
   Total number:  2. 
     --------------------------------------------------------------------------- 
     User Type                             :  Ds-Lite 
     IPv6Address                           :  2001:db8:1::0221:0:0200:0001/128 
     User ID                               :  -
     VPN Instance                          :  -   
     Address Group                         :  group1 
     DS-Lite Instance                      :  ds-lite-1 
     Public IP                             :  11.1.1.2 
     Start Port                            :  1024 
     Port Range                            :  4096 
     Port Total                            :  4096 
     Total/TCP/UDP/ICMP Session Limit      :  8192/10240/10240/512
     Total/TCP/UDP/ICMP Session Current    :  26/0/26/0
     Total/TCP/UDP/ICMP Port Limit         :  20992/10240/10240/512
     Total/TCP/UDP/ICMP Port Current       :  8192/0/8192/0
     Nat ALG Enable                        :  ALL
     Rbp Index/Rbp Status                  :  0/0/0
     Token/TB/TP                           :  0/0/0
     Port Forwarding Flag                  :  Non Port Forwarding
     Port Forwarding Ports                 :  0 0 0 0 0
     Aging Time(s)                         :  -
     Left Time(s)                          :  -
     Port Limit Discard Count              :  0
     Session Limit Discard Count           :  0
     Fib Miss Discard Count                :  0
     -->Transmit Packets                   :  8192
     -->Transmit Bytes                     :  19252
     -->Drop Packets                       :  0
     <--Transmit Packets                   :  0
     ------------------------------------------------------------
   ```
   
   # Verify that user session table information on the master and slave service boards is correct.
   
   ```
   <CGN> display nat session table slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break 
   Slot: 1     
   Current total sessions: 8192.                                 
     udp: 192.168.1.2:28195[11.1.1.2:1723]--> *:*   
     udp: 192.168.1.2:20069[11.1.1.2:1727]--> *:*    
     udp: 192.168.1.2:59556[11.1.1.2:1085]--> *:*   
   ```
   ```
   <CGN> display nat session table slot 2
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break 
   Slot: 2     
   Current total sessions: 8192.                                 
     udp: 192.168.1.2:28195[11.1.1.2:1723]--> *:*   
     udp: 192.168.1.2:20069[11.1.1.2:1727]--> *:*    
     udp: 192.168.1.2:59556[11.1.1.2:1085]--> *:*   
   ```
   
   # Run the **display nat statistics** command to view the number of sent and received packets on the master service board.
   
   ```
   <CGN> display nat statistics received slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break 
   Slot: 1     
   ---------------------------------------------------------------------
    Packets received from interface                :632014772    
    Packets received from mainboard                :29450        
    Packets received by nat entry                  :255587842    
    receive hrp packets from peer device           :0            
    receive boardhrp packets from peer board       :0            
   -----------------------------------------------------------------------
   ```
   ```
   <CGN> display nat statistics transmitted slot 1
   ```
   ```
   This operation will take a few minutes. Press 'Ctrl+C' to break 
   Slot: 1     
   -----------------------------------------------------------------------
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
   ------------------------------------------------------------------------
   ```

#### Configuration Files

* CGN configuration file
  
  ```
  #
  sysname CGN
  #
  vsm on-board-mode disable
  #
  license
   active nat session-table size 16 slot 1 
   active nat session-table size 16 slot 2 
   active nat bandwidth-enhance 40 slot 2
   active nat bandwidth-enhance 40 slot 2
   active ds-lite vsuf slot 1
   active ds-lite vsuf slot 2
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
  ds-lite instance ds-lite-1 id 1
   port-range 4096
   local-ipv6 2001:dB8:2::12 prefix-length 128
   remote-ipv6 2001:db8:1:: prefix-length 41
   ds-lite address-group group1 group-id 1
     section 0 11.1.1.1 mask 24
   ds-lite outbound 3500 address-group group1
   ds-lite alg all
   ds-lite filter mode full-cone
  #
  acl ipv6 3500
   rule permit ipv6 source 2001:db8:1:: 41 destination 2001:dB8:2::12 128
  #
  traffic classifier c1 operator or
   if-match ipv6 acl 3500 precedence 1
  #
  traffic behavior b1
   ds-lite bind instance ds-lite-1
  #
  traffic policy p1
   classifier c1 behavior b1 precedence 1
  #
  interface gigabitethernet 0/1/1
   ip address 10.1.1.1 24
   traffic-policy p1 inbound
  #
  return
  ```