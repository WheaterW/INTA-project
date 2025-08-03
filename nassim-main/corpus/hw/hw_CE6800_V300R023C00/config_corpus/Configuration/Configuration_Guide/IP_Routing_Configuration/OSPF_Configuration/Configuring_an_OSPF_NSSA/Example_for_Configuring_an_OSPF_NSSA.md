Example for Configuring an OSPF NSSA
====================================

Example for Configuring an OSPF NSSA

#### Networking Requirements

An excessive number of entries in a routing table wastes network resources and leads to high CPU usage. To solve this problem, a non-backbone area on the border of an AS can be configured as an NSSA, which does not transmit routes learned from other areas in the AS, and instead imports AS external routes. This reduces bandwidth and storage resource consumption.

On the network shown in [Figure 1](#EN-US_TASK_0000001130783272__fig_dc_vrp_ospf_cfg_201901), OSPF runs on all devices and the entire AS is divided into two areas. DeviceA and DeviceB function as ABRs to forward inter-area routes, and DeviceD functions as an ASBR and imports the external static route 10.0.0.0/8. To import AS-external routes, but reduce the number of LSAs advertised to area 1 without compromising route reachability, configure area 1 as an NSSA and DeviceA as an LSA translator in the NSSA.

**Figure 1** Network diagram of configuring an OSPF NSSA![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130783360.png)

#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable OSPF on each device and configure basic OSPF functions to ensure that the devices can communicate with each other using OSPF.
2. Configure area 1 as an NSSA.
3. Configure DeviceD to import the static route 10.0.0.0/8.
4. Configure DeviceA in the NSSA as an LSA translator.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   Assign an IP address to each interface as shown in [Figure 1](#EN-US_TASK_0000001130783272__fig_dc_vrp_ospf_cfg_201901). For detailed configurations, see the configuration scripts.
2. Configure basic OSPF functions.
   
   
   
   For detailed configurations, see the configuration scripts.
3. Configure area 1 as an NSSA.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf
   [*DeviceA-ospf-1] area 1
   [*DeviceA-ospf-1-area-0.0.0.1] nssa
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf
   [*DeviceB-ospf-1] area 1
   [*DeviceB-ospf-1-area-0.0.0.1] nssa
   [*DeviceB-ospf-1-area-0.0.0.1] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospf
   [*DeviceD-ospf-1] area 1
   [*DeviceD-ospf-1-area-0.0.0.1] nssa
   [*DeviceD-ospf-1-area-0.0.0.1] quit
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   All devices in the NSSA must have the [**nssa**](cmdqueryname=nssa) command configuration.
4. Configure static route 10.0.0.0/8 on DeviceD, and configure the device to import the route into the OSPF process.
   
   
   ```
   [~DeviceD] ip route-static 10.0.0.0 8 null 0
   [*DeviceD] ospf
   [*DeviceD-ospf-1] import-route static
   [*DeviceD-ospf-1] quit
   [*DeviceD] commit
   ```
   
   # Check information about the OSPF routing table on DeviceC.
   
   ```
   [~DeviceC] display ospf routing
             OSPF Process 1 with Router ID 3.3.3.3
                      Routing Tables
   
    Routing for Network
    Destination        Cost  Type       NextHop         AdvRouter       Area
    192.168.3.0/24     2     Inter-area 192.168.0.1     1.1.1.1       0.0.0.0
    192.168.4.0/24     2     Inter-area 192.168.2.1     2.2.2.2       0.0.0.0
    192.168.0.0/24     1     Stub       192.168.0.2     3.3.3.3       0.0.0.0
    192.168.1.0/24     2     Inter-area 192.168.0.1     1.1.1.1       0.0.0.0
    192.168.1.0/24     2     Inter-area 192.168.2.1     2.2.2.2       0.0.0.0
    192.168.2.0/24     1     Stub       192.168.2.2     3.3.3.3       0.0.0.0
   
    Routing for ASEs
    Destination      Cost      Type       Tag    NextHop         AdvRouter
    10.0.0.0/8       1         Type2      1      192.168.2.1     2.2.2.2
   
    Total Nets: 7
    Intra Area: 2  Inter Area: 4  ASE: 1  NSSA: 0
   ```
   
   The command output shows that the router ID of the AS external route imported into the NSSA is 2.2.2.2, meaning that DeviceB functions as an LSA translator. This is because OSPF selects the ABR with the larger router ID as an LSA translator.
5. Configure DeviceA as an LSA translator.
   
   
   ```
   [~DeviceA] ospf
   [~DeviceA-ospf-1] area 1
   [*DeviceA-ospf-1-area-0.0.0.1] nssa default-route-advertise no-summary translator-always
   [*DeviceA-ospf-1-area-0.0.0.1] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Check information about the OSPF routing table on DeviceC.

```
[~DeviceC] display ospf routing
          OSPF Process 1 with Router ID 3.3.3.3
                   Routing Tables

 Routing for Network
 Destination        Cost  Type       NextHop         AdvRouter       Area
 192.168.3.0/24     2     Inter-area 192.168.0.1     1.1.1.1       0.0.0.0
 192.168.4.0/24     2     Inter-area 192.168.2.1     2.2.2.2       0.0.0.0
 192.168.0.0/24     1     Stub       192.168.0.2     3.3.3.3       0.0.0.0
 192.168.1.0/24     2     Inter-area 192.168.2.1     2.2.2.2       0.0.0.0
 192.168.1.0/24     2     Inter-area 192.168.0.1     1.1.1.1       0.0.0.0
 192.168.2.0/24     1     Stub       192.168.2.2     3.3.3.3       0.0.0.0

 Routing for ASEs
 Destination      Cost      Type       Tag    NextHop         AdvRouter
 10.0.0.0/8       1         Type2      1      192.168.0.1     1.1.1.1

 Total Nets: 7
 Intra Area: 2  Inter Area: 4  ASE: 1  NSSA: 0
```

The command output shows that DeviceC has imported an AS external route, and that the router ID of the device that advertises this route is 1.1.1.1, indicating that DeviceA functions as an LSA translator.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  router id 1.1.1.1
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.1 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
    nssa default-route-advertise no-summary translator-always
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  router id 2.2.2.2
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
   area 0.0.0.1
    network 192.168.1.0 0.0.0.255
    network 192.168.4.0 0.0.0.255
    nssa
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  router id 3.3.3.3
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.0.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
  #
  ospf 1
   area 0.0.0.0
    network 192.168.0.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  router id 4.4.4.4
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
  #
  ospf 1
  import-route static
   area 0.0.0.1
    network 192.168.3.0 0.0.0.255
    network 192.168.4.0 0.0.0.255
    nssa
  #
  ip route-static 10.0.0.0 255.0.0.0 NULL0
  #
  return
  ```