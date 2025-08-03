Example for Configuring an OSPFv3 NSSA
======================================

Example for Configuring an OSPFv3 NSSA

#### Networking Requirements

An excessive number of entries in a routing table wastes network resources and leads to high CPU usage. To solve this problem, a non-backbone area on the border of an AS can be configured as an NSSA, which can import AS external routes and advertise them within the entire AS, without learning external routes from the other OSPFv3 areas in the AS. This reduces the consumption of bandwidth and storage resources on the device.

On the network shown in [Figure 1](#EN-US_TASK_0000001176662845__fig_dc_vrp_ospfv3_cfg_209301), OSPFv3 runs on all devices and the entire AS is divided into two areas. DeviceA and DeviceB function as ABRs to forward inter-area routes, and DeviceD functions as an ASBR and imports the external static route 2001:DB8:6::1/128. To import AS external routes, but reduce the number of LSAs advertised to area 1 without compromising route reachability, configure area 1 as an NSSA.

**Figure 1** Network diagram of configuring an OSPFv3 NSSA![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130783222.png)

#### Precautions

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication." OSPFv3 area authentication is used as an example. For details, see "Example for Configuring Basic OSPFv3 Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPFv3 functions on each device to ensure OSPFv3 interconnection.
2. Configure area 1 as an NSSA.
3. Configure DeviceC to import the static route 2001:DB8:7::1/128.
4. Configure DeviceD to import the static route 2001:DB8:6::1/128.

#### Procedure

1. Assign an IP address to each interface involved.
   
   
   
   Assign an IP address to each interface involved according to [Figure 1](#EN-US_TASK_0000001176662845__fig_dc_vrp_ospfv3_cfg_209301). For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176662845__postreq89901616133511).
2. Configure basic OSPFv3 functions.
   
   
   
   For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001176662845__postreq89901616133511).
3. Configure area 1 as an NSSA.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   [*DeviceA-ospfv3-1] area 1
   [*DeviceA-ospfv3-1-area-0.0.0.1] nssa
   [*DeviceA-ospfv3-1-area-0.0.0.1] quit
   [*DeviceA-ospfv3-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   [*DeviceB-ospfv3-1] area 1
   [*DeviceB-ospfv3-1-area-0.0.0.1] nssa
   [*DeviceB-ospfv3-1-area-0.0.0.1] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospfv3 1
   [*DeviceD-ospfv3-1] area 1
   [*DeviceD-ospfv3-1-area-0.0.0.1] nssa
   [*DeviceD-ospfv3-1-area-0.0.0.1] quit
   [*DeviceD-ospfv3-1] quit
   [*DeviceD] commit
   ```
4. Configure DeviceC to import the static route 2001:DB8:7::1/128.
   
   
   ```
   [~DeviceC] ipv6 route-static 2001:DB8:7::1 128 NULL0
   [*DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] import-route static
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   ```
5. Configure DeviceD to import the static route 2001:DB8:6::1/128.
   
   
   ```
   [~DeviceD] ipv6 route-static 2001:DB8:6::1 128 NULL0
   [*DeviceD] ospfv3 1
   [*DeviceD-ospfv3-1] import-route static
   [*DeviceD-ospfv3-1] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Check the OSPFv3 routing tables of DeviceC and DeviceD.

```
[~DeviceC] display ospfv3 routing
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6

OSPFv3 Process (1)
     Destination                                                         Metric
       Next-hop
     2001:DB8:1::/64                                                          1
       directly connected, 100GE1/0/1, Flags : A
IA   2001:DB8:2::/64                                                          2
       via FE80::3A6D:7CFF:FE21:1200, 100GE1/0/1, Flags : A
IA   2001:DB8:2::/64                                                          2
       via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
     2001:DB8:3::/64                                                          1
       directly connected, 100GE1/0/2, Flags : A
IA   2001:DB8:4::/64                                                          2
       via FE80::3A6D:7CFF:FE21:1200, 100GE1/0/1, Flags : A
IA   2001:DB8:5::/64                                                          2
       via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
E2   2001:DB8:6::1/128                                              1        
      via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
```
```
[DeviceD] display ospfv3 routing
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6

OSPFv3 Process (1)
     Destination                                                         Metric
       Next-hop
E2   ::/0                                                                     1
N      via FE80::3A6D:7CFF:FE21:1200, 100GE1/0/1, Flags : A
E2   ::/0                                                                     1
N      via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
IA   2001:DB8:1::/64                                                          2
       via FE80::3A6D:7CFF:FE21:1200, 100GE1/0/1, Flags : A
     2001:DB8:2::/64                                                          2
       via FE80::3A6D:7CFF:FE21:1200, 100GE1/0/1, Flags : A
     2001:DB8:2::/64                                                          2
       via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
IA   2001:DB8:3::/64                                                          2
       via FE80::3A6D:7CFF:FE41:1200, 100GE1/0/2, Flags : A
     2001:DB8:4::/64                                                          1
       directly connected, 100GE1/0/1, Flags : A
     2001:DB8:5::/64                                                          1
       directly connected, 100GE1/0/2, Flags : A
```

The command output shows that DeviceC has imported the AS external route (2001:DB8:6::1/128) and that the route was advertised by DeviceB. In addition, the NSSA does not learn the route 2001:DB8:7::1/128 from area 0.

# Check routing information of the NSSA on each device involved. This example uses DeviceA.

```
[~DeviceA] display ospfv3 routing nssa-routes
Codes : E2 - Type 2 External, E1 - Type 1 External, IA - Inter-Area,
        N - NSSA
Flags : A - Added to URT6

OSPFv3 Process (1)
     Destination                                                         Metric
       Next-hop
E2   2001:DB8:6::1/128                                          1 N
      via FE80::3A6D:7CFF:FE11:1200, 100GE1/0/2, Flags : A
```

# Check NSSA-LSA information on each device involved. This example uses DeviceA.

```
[~DeviceA] display ospfv3 lsdb nssa
           OSPFv3 Router with ID (1.1.1.1) (Process 1)

               NSSA-external-LSA (Area 0.0.0.1)

  LS Age: 391
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.0
  Originating Router: 1.1.1.1
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0x6ebe
  Length: 32
  Flags: (E|-|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1
   Prefix: ::/0
    Prefix Options: 0 (-|-|-|-|-)
    Tag: 0

  LS Age: 378
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.0
  Originating Router: 2.2.2.2
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0x50d8
  Length: 32    
  Flags: (E|-|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1
   Prefix: ::/0
    Prefix Options: 0 (-|-|-|-|-)
    Tag: 0      
                
  LS Age: 429   
  LS Type: NSSA-external-LSA
  Link State ID: 0.0.0.1
  Originating Router: 4.4.4.4
  LS Seq Number: 0x80000001
  Retransmit Count: 0
  Checksum: 0xb7e0
  Length: 48    
  Flags: (E|-|T)
   Metric Type: 2 (Larger than any link state path)
      Metric: 1 
   Prefix: 2001:DB8:6::1/128
    Prefix Options: 8 (-|P|-|-|-)
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0
  #               
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:4::1/64
   ospfv3 1 area 0.0.0.1
  #               
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.1
  #               
  ospfv3 1        
   router-id 1.1.1.1
   area 0.0.0.0   
   area 0.0.0.1   
    nssa            
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.1
  #               
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:3::1/64
   ospfv3 1 area 0.0.0.0
  #               
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:5::2/64
   ospfv3 1 area 0.0.0.1
  #               
  ospfv3 1        
   router-id 2.2.2.2
   area 0.0.0.0   
   area 0.0.0.1   
    nssa            
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #   
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
  #               
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:3::2/64
   ospfv3 1 area 0.0.0.0
  #               
  ospfv3 1        
   router-id 3.3.3.3
   import-route static
   area 0.0.0.0   
  #               
  ipv6 route-static 2001:DB8:7::1 128 NULL0 
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:4::2/64
   ospfv3 1 area 0.0.0.1
  #               
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable    
   ipv6 address 2001:DB8:5::1/64
   ospfv3 1 area 0.0.0.1
  #              
  ospfv3 1        
   router-id 4.4.4.4
   import-route static
   area 0.0.0.1   
    nssa          
  #
  ipv6 route-static 2001:DB8:6::1 128 NULL0 
  #
  return
  ```