Example for Configuring OSPFv3 Route Summarization on an ASBR
=============================================================

This section provides an example showing how to configure OSPFv3 route summarization on an ASBR.

#### Networking Requirements

Routes with the same IPv6 prefix can be summarized into one route. On a large-scale OSPFv3 network, route lookup may slow down because of the large size of the routing table. To reduce the routing table size and simplify management, configure route summarization. With route summarization, if a link connected to a device within the IPv6 address range that has been summarized alternates between up and down, the link status change is not advertised to the devices beyond the IPv6 address range. This prevents route flapping and improves network stability.

In [Figure 1](#EN-US_TASK_0172365813__fig_dc_vrp_ospfv3_cfg_209001), both the ASBR and Device A run OSPFv3. The ASBR imports three static routes with the same prefix: 2001:DB8:2::1/128, 2001:DB8:3::1/128, and 2001:DB8:4::1/128. After the three static routes with the same prefix are summarized into route 2001:DB8::/32 on the ASBR, the ASBR advertises only this route to area 0. This reduces the size of the routing table, simplifies route management, and improves network stability.

**Figure 1** Example for configuring OSPFv3 route summarization on an ASBR![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ospfv3_cfg_209001.png)

#### Precautions

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication". OSPFv3 IPsec is used as an example. For details, see "Example for Configuring IPsec for OSPFv3."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each interface to ensure that devices on the network can communicate with each other.
2. Configure basic OSPFv3 functions on the ASBR and Device A.
3. Configure three static routes (2001:DB8:2::1/128, 2001:DB8:3::1/128, and 2001:DB8:4::1/128) on the ASBR and import them into OSPFv3.
4. Configure OSPFv3 route summarization on the ASBR.

#### Data Preparation

To complete the configuration, you need the following data:

* Area 0
* Router ID (1.1.1.1) of Device A
* Router ID (2.2.2.2) of the ASBR

#### Procedure

1. Configure IP addresses for interfaces. For detailed configurations, see Configuration Files.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure the ASBR.
   
   ```
   [~ASBR] ospfv3 1
   ```
   ```
   [*ASBR-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*ASBR-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*ASBR-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*ASBR-ospfv3-1] quit
   ```
   ```
   [*ASBR] commit
   ```
   ```
   [~ASBR] interface gigabitethernet0/1/0
   ```
   ```
   [~ASBR-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*ASBR-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR] commit
   ```
   
   # After the configuration is complete, run the [**display ospfv3 peer**](cmdqueryname=display+ospfv3+peer) command. The command output shows that a neighbor relationship has been established between DeviceA and the ASBR. The following example uses the command output on the ASBR:
   
   ```
   [~ASBR] display ospfv3 peer
   
   OSPFv3 Process (1)
   Total number of peer(s): 1
    Peer(s) in full state: 1
   OSPFv3 Area (0.0.0.0)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   1.1.1.1            1 Full/DR          00:00:37   GE0/1/0               0    
   ```
3. Configure three static routes with the same prefix on the ASBR and import them into OSPFv3.
   
   
   ```
   [~ASBR] ipv6 route-static 2001:DB8:2::1 128 NULL0
   ```
   ```
   [*ASBR] ipv6 route-static 2001:DB8:3::1 128 NULL0
   ```
   ```
   [*ASBR] ipv6 route-static 2001:DB8:4::1 128 NULL0
   ```
   ```
   [*ASBR] commit
   ```
   ```
   [~ASBR] ospfv3 1
   ```
   ```
   [*ASBR-ospfv3-1] import-route static
   ```
   ```
   [*ASBR-ospfv3-1] quit
   ```
   ```
   [~ASBR] commit
   ```
   
   # After the configuration is complete, run the [**display ospfv3 lsdb**](cmdqueryname=display+ospfv3+lsdb) command on the ASBR to check OSPFv3 LSDB information. There are three AS-external LSAs in the LSDB, and the prefixes of corresponding routes are 2001:DB8:2::/128, 2001:DB8:3::/128, and 2001:DB8:4::/128, indicating that route summarization is not performed.
   
   ```
   [~ASBR] display ospfv3 lsdb
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Link-LSA (Interface GE0/1/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.18        1.1.1.1          172   0x80000002 0xa78d          1
   0.0.0.18        2.2.2.2          117   0x80000002 0xde3b          1
   
                  Router-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         1.1.1.1          115   0x80000002 0xd020      1
   0.0.0.1         2.2.2.2          80    0x80000003 0xb633      1
   
                  Network-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.18        1.1.1.1          115   0x80000001 0xd333
   
                  Intra-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         1.1.1.1          115   0x80000001 0x279b       1 Network-LSA    
   
                  AS-External-LSA
   Link State ID   Origin Router    Age   Seq#       CkSum  Type  
   0.0.0.1         2.2.2.2          76    0x80000001 0xade0 E2    
   0.0.0.2         2.2.2.2          76    0x80000001 0xb3d8 E2    
   0.0.0.3         2.2.2.2          76    0x80000001 0xb9d0 E2 
   ```
   ```
   [~ASBR] display ospfv3 lsdb external
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  AS-External-LSA
   
     LS Age: 116
     LS Type: AS-External-LSA
     Link State ID: 0.0.0.1
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0xade0
     Length: 48
     Flags: (E|-|T)
      Metric Type: 2 (Larger than any link state path)
         Metric: 1
      Prefix: 2001:DB8:2::1/128
       Prefix Options: 0 (-|-|-|-|-)
       Tag: 1
   
     LS Age: 116
     LS Type: AS-External-LSA
     Link State ID: 0.0.0.2
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0xb3d8
     Length: 48    
     Flags: (E|-|T)
      Metric Type: 2 (Larger than any link state path)
         Metric: 1 
      Prefix: 2001:DB8:3::1/128
       Prefix Options: 0 (-|-|-|-|-)
       Tag: 1      
                   
     LS Age: 116   
     LS Type: AS-External-LSA
     Link State ID: 0.0.0.3
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0xb9d0
     Length: 48    
     Flags: (E|-|T)
      Metric Type: 2 (Larger than any link state path)
         Metric: 1 
      Prefix: 2001:DB8:4::1/128
       Prefix Options: 0 (-|-|-|-|-)
       Tag: 1      
   ```
4. Configure route summarization on the ASBR.
   
   
   
   # On the ASBR, summarize three static routes 2001:DB8:2::1/128, 2001:DB8:3::1/128, and 2001:DB8:4::1/128 into route 2001:DB8::/32.
   
   ```
   [~ASBR] ospfv3 1
   ```
   ```
   [*ASBR-ospfv3-1] asbr-summary 2001:DB8:: 32
   ```
   ```
   [*ASBR-ospfv3-1] quit
   ```
   ```
   [*ASBR] commit
   ```
5. Verify the configuration.
   
   
   
   # After route summarization is configured, run the [**display ospfv3 lsdb**](cmdqueryname=display+ospfv3+lsdb) command on the ASBR. The command output shows that the three static routes 2001:DB8:2::1/128, 2001:DB8:3::1/128, and 2001:DB8:4::1/128 have been summarized into route 2001:DB8::/32.
   
   ```
   [~ASBR] display ospfv3 lsdb
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  Link-LSA (Interface GE0/1/0)
   Link State ID   Origin Router    Age   Seq#       CkSum      Prefix
   0.0.0.18        1.1.1.1          643   0x80000002 0xa78d          1
   0.0.0.18        2.2.2.2          588   0x80000002 0xde3b          1
   
                  Router-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum    Link
   0.0.0.1         1.1.1.1          586   0x80000002 0xd020      1
   0.0.0.1         2.2.2.2          551   0x80000003 0xb633      1
   
                  Network-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum 
   0.0.0.18        1.1.1.1          586   0x80000001 0xd333
   
                  Intra-Area-Prefix-LSA (Area 0.0.0.0)
   Link State ID   Origin Router    Age   Seq#       CkSum   Prefix Reference      
   0.0.0.1         1.1.1.1          586   0x80000001 0x279b       1 Network-LSA    
   
                  AS-External-LSA
   Link State ID   Origin Router    Age   Seq#       CkSum  Type  
   0.0.0.4         2.2.2.2          123   0x80000001 0x606f E2    
   ```
   ```
   [~ASBR] display ospfv3 lsdb external
   
              OSPFv3 Router with ID (2.2.2.2) (Process 1)
   
                  AS-External-LSA
   
     LS Age: 133
     LS Type: AS-External-LSA
     Link State ID: 0.0.0.4
     Originating Router: 2.2.2.2
     LS Seq Number: 0x80000001
     Retransmit Count: 0
     Checksum: 0x606f
     Length: 36
     Flags: (E|-|T)
      Metric Type: 2 (Larger than any link state path)
         Metric: 2
      Prefix: 2001:DB8::/32
       Prefix Options: 0 (-|-|-|-|-)
       Tag: 1
   ```
   
   # Run the [**display ospfv3 asbr-summary**](cmdqueryname=display+ospfv3+asbr-summary) command on the ASBR. The command output shows information about the summary route of the static routes imported by OSPFv3.
   
   ```
   [~ASBR] display ospfv3 asbr-summary
   
   OSPFv3 Process (1)
    Prefix                                 Prefix-Len   Matched          Status        
    2001:DB8::                              32           3 [Active]       Advertised    
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
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
* ASBR configuration file
  
  ```
  #
  sysname ASBR
  #               
  ospfv3 1        
   router-id 2.2.2.2
   import-route static
   asbr-summary 2001:DB8:: 32
   area 0.0.0.0   
  #               
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #               
  ipv6 route-static 2001:DB8:2::1 128 NULL0
  ipv6 route-static 2001:DB8:3::1 128 NULL0
  ipv6 route-static 2001:DB8:4::1 128 NULL0
  #               
  return      
  ```