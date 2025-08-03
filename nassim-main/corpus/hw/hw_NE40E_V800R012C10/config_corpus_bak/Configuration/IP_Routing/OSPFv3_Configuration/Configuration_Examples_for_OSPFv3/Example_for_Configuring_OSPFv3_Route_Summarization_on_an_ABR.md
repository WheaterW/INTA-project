Example for Configuring OSPFv3 Route Summarization on an ABR
============================================================

This section provides an example showing how to configure OSPFv3 route summarization on an ABR.

#### Networking Requirements

Routes with the same IPv6 prefix can be summarized into one route. On a large-scale OSPFv3 network, route lookup may slow down because of the large size of the routing table. To reduce the routing table size and simplify management, configure route summarization. With route summarization, if a link connected to a device within an IPv6 address range that has been summarized alternates between up and down, the link status change is not advertised to the devices beyond the IPv6 address range. This prevents route flapping and improves network stability.

In [Figure 1](#EN-US_TASK_0172365816__fig_dc_vrp_ospfv3_cfg_209101), all devices run OSPFv3. To reduce the routing table size, simplify route management, and improve network stability, it is required that the ABR be configured to summarize area 1's routes with the same prefix (2001:DB8::) into route 2001:DB8::/32 and advertise only the summary route to area 0.

**Figure 1** Configuring OSPFv3 route summarization on an ABR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_ospfv3_cfg_209101.png)  


#### Precautions

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication". OSPFv3 IPsec is used as an example. For details, see "Example for Configuring IPsec for OSPFv3."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure that devices on the network can communicate with each other.
2. Configure basic OSPFv3 functions on all devices.
3. Configure OSPFv3 route summarization on the ABR.

#### Data Preparation

To complete the configuration, you need the following data:

* Areas 0 and 1
* Router ID (1.1.1.1) of Device B
* Router ID (2.2.2.2) of the ABR
* Router ID (3.3.3.3) of Device A
* Router ID (4.4.4.4) of Device C

#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ospfv3 1 area 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceB-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 4.4.4.4
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*DeviceC-ospfv3-1-area-0.0.0.1] quit
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] interface gigabitethernet0/3/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/3/0] ospfv3 1 area 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure the ABR.
   
   ```
   [~ABR] ospfv3 1
   ```
   ```
   [*ABR-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*ABR-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*ABR-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*ABR-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*ABR-ospfv3-1-area-0.0.0.1] quit
   ```
   ```
   [*ABR-ospfv3-1] quit
   ```
   ```
   [*ABR] commit
   ```
   ```
   [~ABR] interface gigabitethernet0/1/0
   ```
   ```
   [~ABR-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*ABR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ABR] interface gigabitethernet0/2/0
   ```
   ```
   [*ABR-GigabitEthernet0/2/0] ospfv3 1 area 1
   ```
   ```
   [*ABR-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ABR] interface gigabitethernet0/3/0
   ```
   ```
   [*ABR-GigabitEthernet0/3/0] ospfv3 1 area 1
   ```
   ```
   [*ABR-GigabitEthernet0/3/0] quit
   ```
   ```
   [*ABR] commit
   ```
   
   # Run the [**display ospfv3 peer**](cmdqueryname=display+ospfv3+peer) command to check whether the ABR establishes a neighbor relationship with Device A, Device B, and Device C. The following example uses the command output on the ABR:
   
   ```
   [~ABR] display ospfv3 peer
   
   OSPFv3 Process (1)
   Total number of peer(s): 3
    Peer(s) in full state: 3
   OSPFv3 Area (0.0.0.0)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   1.1.1.1            1 Full/DR          00:00:35   GE0/1/0               0       
   OSPFv3 Area (0.0.0.1)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   4.4.4.4            1 Full/Backup      00:00:40   GE0/3/0               0       
   3.3.3.3            1 Full/Backup      00:00:31   GE0/2/0               0       
   ```
   
   # Run the [**display ospfv3 lsdb**](cmdqueryname=display+ospfv3+lsdb) command on the ABR to check OSPFv3 LSDB information. The **Inter-area-prefix LSA** field in the LSDB of area 1 shows that no summarization is performed for the routes. Therefore, the routes advertised to area 0 are not summarized.
   
   ```
   [~ABR] display ospfv3 lsdb
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Link-LSA (Interface GE0/1/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.18        1.1.1.1          1740  0x80000010 0x8b9b          1
   0.0.0.18        2.2.2.2          1684  0x80000010 0xc249          1
   
                  Link-LSA (Interface GE0/3/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.19        2.2.2.2          154   0x80000002 0x33e2          1
   0.0.0.19        4.4.4.4          75    0x80000002 0xf927          1
   
                  Link-LSA (Interface GE0/2/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.20        2.2.2.2          383   0x8000000e 0x306           1
   0.0.0.11        3.3.3.3          232   0x8000000e 0xc146          1
   
                  Router-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         1.1.1.1          1682  0x80000010 0xb42e      1
   0.0.0.1         2.2.2.2          384   0x80000014 0x9148      1
   
                  Network-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.18        1.1.1.1          1682  0x8000000f 0xb741
                   
                  Inter-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.2         2.2.2.2          154   0x80000001 0x9071
   0.0.0.3         2.2.2.2          1726  0x8000000a 0xf315
                   
                  Intra-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         1.1.1.1          1682  0x8000000f 0xba9        1 Network-LSA    
                   
                  Router-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         2.2.2.2          70    0x8000000f 0xa0f4      2
   0.0.0.1         3.3.3.3          226   0x8000000e 0x904d      1
   0.0.0.1         4.4.4.4          71    0x80000002 0xe8f5      1
                   
                  Network-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.19        2.2.2.2          70    0x80000001 0x22d3
   0.0.0.20        2.2.2.2          225   0x8000000d 0xdd0f
                   
                  Inter-Area-Prefix-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.1         2.2.2.2          390   0x8000000d 0x6296
                   
                  Intra-Area-Prefix-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         2.2.2.2          231   0x8000000d 0x4f5c       1 Network-LSA    
   0.0.0.2         2.2.2.2          76    0x80000001 0x6b4b       1 Network-LSA    
   ```
   ```
   [~ABR] display ospfv3 lsdb inter-prefix
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Inter-Area-Prefix-LSA (Area 0.0.0.0)
   
     LS Age: 197
     LS Type: Inter-Area-Prefix-LSA
     Link State ID: 0.0.0.2
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0x9071
     Length: 36
   
      Metric: 1
      Prefix: 2001:DB8:3::/64
       Prefix Options: 0 (-|-|-|-|-)
   
     LS Age: 1769
     LS Type: Inter-Area-Prefix-LSA
     Link State ID: 0.0.0.3
     Originating Router: 2.2.2.2
     LS Seq Number: 0x8000000a
     Retransmit Count: 0
     Checksum: 0xf315
     Length: 36    
                   
      Metric: 1    
      Prefix: 2001:DB8:2::/48
       Prefix Options: 0 (-|-|-|-|-)
                   
                  Inter-Area-Prefix-LSA (Area 0.0.0.1)
                   
     LS Age: 427   
     LS Type: Inter-Area-Prefix-LSA
     Link State ID: 0.0.0.1
     Originating Router: 2.2.2.2
     LS Seq Number: 0x8000000d
     Retransmit Count: 0
     Checksum: 0x6296
     Length: 36    
                   
      Metric: 1    
      Prefix: 2001:DB8:1::/64
       Prefix Options: 0 (-|-|-|-|-)
   ```
3. Configure the ABR to summarize the routes with the same prefix in area 1 into route 2001:DB8::/32.
   
   
   ```
   [~ABR] ospfv3 1
   ```
   ```
   [*ABR-ospfv3-1] area 0.0.0.1
   ```
   ```
   [*ABR-ospfv3-1-area-0.0.0.1] abr-summary 2001:DB8:: 32
   ```
   ```
   [*ABR-ospfv3-1-area-0.0.0.1] quit
   ```
   ```
   [*ABR-ospfv3-1] quit
   ```
   ```
   [*ABR] commit
   ```
4. Verify the configuration.
   
   
   
   # After route summarization is configured, run the [**display ospfv3 lsdb**](cmdqueryname=display+ospfv3+lsdb) command on the ABR. The command output shows that the routes with the same prefix in area 1 are summarized into route 2001:DB8::/32 and advertised to area 0.
   
   ```
   [~ABR] display ospfv3 lsdb
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Link-LSA (Interface GE0/1/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.18        1.1.1.1          108   0x80000011 0x899c          1
   0.0.0.18        2.2.2.2          52    0x80000011 0xc04a          1
   
                  Link-LSA (Interface GE0/3/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.19        2.2.2.2          322   0x80000002 0x33e2          1
   0.0.0.19        4.4.4.4          243   0x80000002 0xf927          1
   
                  Link-LSA (Interface GE0/2/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.20        2.2.2.2          551   0x8000000e 0x306           1
   0.0.0.11        3.3.3.3          400   0x8000000e 0xc146          1
   
                  Router-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         1.1.1.1          50    0x80000011 0xb22f      1
   0.0.0.1         2.2.2.2          552   0x80000014 0x9148      1
   
                  Network-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.18        1.1.1.1          50    0x80000010 0xb542
                   
                  Inter-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.3         2.2.2.2          30    0x80000001 0x6dba
                   
                  Intra-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         1.1.1.1          50    0x80000010 0x9aa        1 Network-LSA    
                   
                  Router-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         2.2.2.2          238   0x8000000f 0xa0f4      2
   0.0.0.1         3.3.3.3          394   0x8000000e 0x904d      1
   0.0.0.1         4.4.4.4          239   0x80000002 0xe8f5      1
                   
                  Network-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.19        2.2.2.2          238   0x80000001 0x22d3
   0.0.0.20        2.2.2.2          393   0x8000000d 0xdd0f
                   
                  Inter-Area-Prefix-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.1         2.2.2.2          552   0x8000000d 0x6296
                   
                  Intra-Area-Prefix-LSA (Area 0.0.0.1)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         2.2.2.2          399   0x8000000d 0x4f5c       1 Network-LSA    
   0.0.0.2         2.2.2.2          244   0x80000001 0x6b4b       1 Network-LSA    
   ```
   ```
   [~ABR] display ospfv3 lsdb inter-prefix
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Inter-Area-Prefix-LSA (Area 0.0.0.0)
   
     LS Age: 40
     LS Type: Inter-Area-Prefix-LSA
     Link State ID: 0.0.0.3
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0x6dba
     Length: 32
   
      Metric: 1
      Prefix: 2001:DB8::/32
       Prefix Options: 0 (-|-|-|-|-)
   
                  Inter-Area-Prefix-LSA (Area 0.0.0.1)
   
     LS Age: 562
     LS Type: Inter-Area-Prefix-LSA
     Link State ID: 0.0.0.1
     Originating Router: 2.2.2.2
     LS Seq Number: 0x8000000d
     Retransmit Count: 0
     Checksum: 0x6296
     Length: 36    
                   
      Metric: 1    
      Prefix: 2001:DB8:1::/64
       Prefix Options: 0 (-|-|-|-|-) 
   ```
   
   # Run the [**display ospfv3 abr-summary-list**](cmdqueryname=display+ospfv3+abr-summary-list) command on the ABR. The command output shows information about route summarization in area 1.
   
   ```
   [~ABR] display ospfv3 abr-summary-list
   
   OSPFv3 Process (1)
   Area ID  :  0.0.0.1
    Prefix                                 Prefix-Len   Matched          Status        
    2001:DB8::                             32           1 [Active]       Advertised   
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #               
  ospfv3 1        
   router-id 3.3.3.3
   area 0.0.0.1   
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.1
  #               
  return  
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #               
  ospfv3 1        
   router-id 1.1.1.1
   area 0.0.0.0   
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0
  #               
  return 
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #               
  ospfv3 1        
   router-id 4.4.4.4
   area 0.0.0.1   
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::1/64
   ospfv3 1 area 0.0.0.1
  #               
  return 
  ```
* ABR configuration file
  
  ```
  #
  sysname ABR
  #               
  ospfv3 1        
   router-id 2.2.2.2
   area 0.0.0.0   
   area 0.0.0.1   
    abr-summary 2001:DB8:: 32
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #               
  interface GigabitEthernet0/2/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.1
  #               
  interface GigabitEthernet0/3/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.1
  #               
  return 
  ```