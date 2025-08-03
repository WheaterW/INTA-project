Example for Configuring Prefix-based BGP ORF
============================================

Prefix-based BGP ORF is used to implement on-demand BGP route advertisement.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172366382__fig_dc_vrp_bgp_cfg_407801), Devices A and B are in AS 100. Devices C, D, and E are in AS 200. Device A requires Device C to send only routing information matching the import policy of Device A, but Device C does not want to maintain a separate export policy for Device A. Prefix-based BGP ORF can be configured in such a situation.

**Figure 1** Networking diagram for configuring prefix-based BGP ORF![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/0, GE 0/2/0, GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_407801.png)  


#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish an EBGP peer relationship between Devices A and C, and establish IBGP peer relationships between Devices A and B, between Devices C and D, and between Devices C and E.
2. Configure a prefix-based import policy on Device A, and enable prefix-based BGP ORF on Devices A and C.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs 1.1.1.1 and 2.2.2.2 and AS number 100 of Devices A and B respectively
* Router IDs 3.3.3.3, 4.4.4.4, and 5.5.5.5 and AS number 200 of Devices C, D, and E respectively

#### Procedure

1. Configure an IP address for each interface.
   
   
   
   Configure an IP address for each interface, as shown in [Figure 1](#EN-US_TASK_0172366382__fig_dc_vrp_bgp_cfg_407801). For details on configuration procedures, see corresponding configuration files.
2. Establish BGP peer relationships.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 1.1.1.1
   [*DeviceA-bgp] peer 10.2.1.1 as-number 100
   [*DeviceA-bgp] peer 10.1.1.2 as-number 200
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] import-route direct
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] commit
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 100
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] peer 10.2.1.2 as-number 100
   [*DeviceB-bgp] commit
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 200
   [*DeviceC-bgp] router-id 3.3.3.3
   [*DeviceC-bgp] peer 10.1.1.1 as-number 100
   [*DeviceC-bgp] peer 10.3.1.1 as-number 200
   [*DeviceC-bgp] peer 10.4.1.1 as-number 200
   [*DeviceC-bgp] ipv4-family unicast
   [*DeviceC-bgp-af-ipv4] import-route direct
   [*DeviceC-bgp-af-ipv4] quit
   [*DeviceC-bgp] commit
   [~DeviceC-bgp] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] bgp 200
   [*DeviceD-bgp] router-id 4.4.4.4
   [*DeviceD-bgp] peer 10.3.1.2 as-number 200
   [*DeviceD-bgp] commit
   [~DeviceD-bgp] quit
   ```
   
   # Configure Device E.
   
   ```
   [~DeviceE] bgp 200
   [*DeviceE-bgp] router-id 5.5.5.5
   [*DeviceE-bgp] peer 10.4.1.2 as-number 200
   [*DeviceE-bgp] commit
   [~DeviceE-bgp] quit
   ```
3. Configure a prefix-based import policy on Device A.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] ip ip-prefix 1 index 10 permit 10.3.1.0 24 greater-equal 24 less-equal 32
   [*DeviceA] bgp 100
   [*DeviceA-bgp] peer 10.1.1.2 ip-prefix 1 import
   [*DeviceA-bgp] commit
   [~DeviceA-bgp] quit
   ```
   
   # View routing information sent by Device C.
   
   ```
   [~DeviceC] display bgp routing-table peer 10.1.1.1 advertised-routes
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 7
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   3.3.3.3/32         10.1.1.2        0                     0      200?
    *>   10.1.1.0/30        10.1.1.2        0                     0      200?
    *>   10.1.1.1/32        10.1.1.2        0                     0      200?
    *>   10.3.1.0/30        10.1.1.2        0                     0      200?
    *>   10.3.1.1/32        10.1.1.2        0                     0      200?
    *>   10.4.1.0/30        10.1.1.2        0                     0      200?
    *>   10.4.1.1/32        10.1.1.2        0                     0      200?
   ```
   
   # View routing information accepted by Device A.
   
   ```
   [~DeviceA] display bgp routing-table peer 10.1.1.2 received-routes
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.3.1.0/30        10.1.1.2        0                     0      200?
    *>   10.3.1.1/32        10.1.1.2        0                     0      200?
   ```
   
   When prefix-based BGP ORF is not enabled, Device C sends seven routes, but Device A accepts only two routes because Device A applies the prefix-based import policy to the seven routes.
4. Enable prefix-based BGP ORF.
   
   
   
   # Enable prefix-based BGP ORF on DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] peer 10.1.1.2 capability-advertise orf ip-prefix both
   [*DeviceA-bgp] commit
   [~DeviceA-bgp] quit
   ```
   
   # Enable prefix-based BGP ORF on DeviceC.
   
   ```
   [~DeviceC] bgp 200
   [*DeviceC-bgp] peer 10.1.1.1 capability-advertise orf ip-prefix both
   [*DeviceC-bgp] commit
   [~DeviceC-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   # View prefix-based BGP ORF negotiation information on Device A.
   
   ```
   [~DeviceA] display bgp peer 10.1.1.2 verbose
                                                                                   
            BGP Peer is 10.1.1.2,  remote AS 200                                   
            Type: EBGP link                                                        
            BGP version 4, Remote router ID 3.3.3.3                                
            Update-group ID: 1                                                     
            BGP current state: Established, Up for 00h00m01s                       
            BGP current event: RecvRouteRefresh                                    
            BGP last state: OpenConfirm                                            
            BGP Peer Up count: 2                                                   
            Received total routes: 0                                               
            Received active routes total: 0                                        
            Advertised total routes: 5                                             
            Port:  Local - 179      Remote - 54545                                 
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec          
            Received  : Active Hold Time: 180 sec                                  
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec          
            Peer optional capabilities:                                            
            Peer supports bgp multi-protocol extension                             
            Peer supports bgp route refresh capability                             
            Peer supports bgp outbound route filter capability                     
            Support Address-Prefix: IPv4-UNC address-family, rfc-compatible, both  
            Peer supports bgp 4-byte-as capability                                 
            Address family IPv4 Unicast: advertised and received                   
    Received: Total 3 messages                                                     
                     Update messages                1                              
                     Open messages                  1                              
                     KeepAlive messages             1                              
                     Notification messages          0                              
                     Refresh messages               1                              
    Sent: Total 9 messages                                                         
                     Update messages                5                              
                     Open messages                  2                              
                     KeepAlive messages             1                              
                     Notification messages          0                              
                     Refresh messages               1                              
    Authentication type configured: None                                           
    Last keepalive received: 2012-03-06 19:17:37 UTC-8:00
    Last keepalive sent    : 2012-03-06 19:17:37 UTC-8:00
    Last update    received: 2012-03-06 19:17:43 UTC-8:00
    Last update    sent    : 2012-03-06 19:17:37 UTC-8:00                         
    Minimum route advertisement interval is 30 seconds                             
    Optional capabilities:                                                         
    Route refresh capability has been enabled                                      
    Outbound route filter capability has been enabled                              
    Enable Address-Prefix: IPv4-UNC address-family, rfc-compatible, both           
    4-byte-as capability has been enabled                                          
    Multi-hop ebgp has been enabled                                                
    Peer Preferred Value: 0                                                        
    Routing policy configured:                                                     
    No import update filter list                                                   
    No export update filter list                                                   
    Import prefix list is: 1                                                       
    No export prefix list                                                          
    No import route policy                                                         
    No export route policy                                                         
    No import distribute policy                                                    
    No export distribute policy  
   ```
   
   # View routing information sent by Device C.
   
   ```
   [~DeviceC] display bgp routing-table peer 10.1.1.1 advertised-routes
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.3.1.0/30        10.1.1.2        0                     0      200?
    *>   10.3.1.1/32        10.1.1.2        0                     0      200?
   ```
   
   # View routing information accepted by Device A.
   
   ```
   [~DeviceA] display bgp routing-table peer 10.1.1.2 received-routes
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   10.3.1.0/30        10.1.1.2        0                     0      200?
    *>   10.3.1.1/32        10.1.1.2        0                     0      200?
   ```
   
   After BGP ORF is enabled, Device C sends only two routes based on the prefix-based import policy provided by Device A, and Device A accepts only the two routes.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #                                                                               
  sysname DeviceA                                                                
  #                                                                               
  interface GigabitEthernet0/2/0                                                              
   ip address 10.2.1.2 255.255.255.252                                            
  #                                                                               
  interface GigabitEthernet0/1/0                                                                                              
   ip address 10.1.1.1 255.255.255.252                                            
  #                                                                               
  interface LoopBack1                                                             
   ip address 1.1.1.1 255.255.255.255                                             
  #                                                                               
  bgp 100                                                                         
   router-id 1.1.1.1                                                              
   peer 10.1.1.2 as-number 200                                                    
   peer 10.2.1.1 as-number 100                                                    
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
    import-route direct                                                           
    peer 10.1.1.2 enable                                                          
    peer 10.1.1.2 ip-prefix 1 import                                              
    peer 10.1.1.2 capability-advertise orf ip-prefix both                         
    peer 10.2.1.1 enable                                                          
  #                                                                               
   ip ip-prefix 1 index 10 permit 10.3.1.0 24 greater-equal 24 less-equal 32      
  #                                                                               
  return                                                                          
  ```
* DeviceB configuration file
  
  ```
  #                                                                               
  sysname DeviceB                                                                
  #                                                                               
  interface GigabitEthernet0/1/0                                                                                              
   ip address 10.2.1.1 255.255.255.252                                            
  #                                                                               
  interface LoopBack1                                                             
   ip address 2.2.2.2 255.255.255.255                                             
  #                                                                               
  bgp 100                                                                         
   router-id 2.2.2.2                                                              
   peer 10.2.1.2 as-number 100                                                    
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                        
    peer 10.2.1.2 enable                                                          
  #                                                                               
  return                                                                          
  ```
* DeviceC configuration file
  
  ```
  #                                                                               
  sysname DeviceC                                                                
  #                                                                               
  interface GigabitEthernet0/2/0                                                              
   ip address 10.3.1.2 255.255.255.252                                            
  #                                                                               
  interface GigabitEthernet0/1/0                                                              
   ip address 10.1.1.2 255.255.255.252                                            
  #                                                                               
  interface GigabitEthernet0/3/0                                                              
   ip address 10.4.1.2 255.255.255.252                                            
  #                                                                               
  interface LoopBack1                                                             
   ip address 3.3.3.3 255.255.255.255                                             
  #                                                                               
  bgp 200                                                                         
   router-id 3.3.3.3                                                              
   peer 10.1.1.1 as-number 100                                                    
   peer 10.3.1.1 as-number 200                                                    
   peer 10.4.1.1 as-number 200                                                    
   #                                                                              
   ipv4-family unicast
    undo synchronization                                                                                                                      
    import-route direct                                                           
    peer 10.1.1.1 enable                                                          
    peer 10.1.1.1 capability-advertise orf ip-prefix both                         
    peer 10.3.1.1 enable                                                          
    peer 10.4.1.1 enable                                                          
  #                                                                               
  return                                                                          
  ```
* DeviceD configuration file
  
  ```
  #                                                                               
  sysname DeviceD                                                                
  #                                                                               
  interface GigabitEthernet0/1/0                                                              
   ip address 10.3.1.1 255.255.255.252                                            
  #                                                                               
  interface LoopBack1                                                             
   ip address 4.4.4.4 255.255.255.255                                             
  #                                                                               
  bgp 200                                                                         
   router-id 4.4.4.4                                                              
   peer 10.3.1.2 as-number 200                                                    
   #                                                                              
   ipv4-family unicast
    undo synchronization                                                                                                                      
    peer 10.3.1.2 enable                                                          
  #                                                                               
  return                                                                          
  ```
* DeviceE configuration file
  
  ```
  #                                                                               
  sysname DeviceE                                                                
  #                                                                               
  interface GigabitEthernet0/1/1                                                              
   ip address 10.4.1.1 255.255.255.252                                            
  #                                                                               
  interface LoopBack1                                                             
   ip address 5.5.5.5 255.255.255.255                                             
  #                                                                               
  bgp 200                                                                         
   router-id 5.5.5.5                                                              
   peer 10.4.1.2 as-number 200                                                    
   #                                                                              
   ipv4-family unicast                                                            
    undo synchronization                                                          
    peer 10.4.1.2 enable                                                          
  #                                                                               
  return                                                                          
  ```