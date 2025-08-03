Example for Configuring SBFD for IS-IS SRv6 BE
==============================================

This section describes how to configure SBFD to detect SRv6 BE faults to improve network reliability.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001199471075__fig_dc_vrp_sr_all_cfg_005001), SRv6 BE is deployed between devices on a public network. To improve network reliability, SBFD needs to be deployed, and BGP auto FRR needs to be configured on DeviceA. In this way, when SBFD detects a fault on the primary SRv6 BE path, BGP auto FRR can be triggered to quickly switch traffic to the backup path, minimizing the impact on services.

**Figure 1** SBFD for SRv6 BE networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](figure/en-us_image_0000001172314284.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure IS-IS to implement IPv6 interworking between devices.
3. Configure DeviceB as an RR and establish IBGP peer relationships with DeviceA, DeviceC, and DeviceD for it.
4. Configure basic SRv6 BE functions on each device.
5. Enable BGP auto FRR on DeviceA.
6. Configure SBFD between the initiator and reflector to detect the peer locator reachability, speeding up BGP auto FRR switching.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 address of each interface
* IS-IS process ID and level of each device
* BGP AS number

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface LoopBack 1
   ```
   ```
   [*DeviceA-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceA-LoopBack1] ipv6 address 2001:DB8:11::11 128
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::1 96
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface LoopBack 1
   ```
   ```
   [*DeviceB-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceB-LoopBack1] ipv6 address 2001:DB8:22::22 128
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:DB8:1::2 96
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 address 2001:DB8:2::1 96
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] ipv6 address 2001:DB8:3::1 96
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface LoopBack 1
   ```
   ```
   [*DeviceC-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceC-LoopBack1] ipv6 address 2001:DB8:33::33 128
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 address 2001:DB8:2::2 96
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceD] interface LoopBack 1
   ```
   ```
   [*DeviceD-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceD-LoopBack1] ipv6 address 2001:DB8:44::44 128
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 address 2001:DB8:3::2 96
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] commit
   ```
2. Configure IS-IS on the devices for them to communicate.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] cost-style wide
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface LoopBack 1
   ```
   ```
   [*DeviceA-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*DeviceA-LoopBack1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-1
   ```
   ```
   [*DeviceB-isis-1] cost-style wide
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface LoopBack 1
   ```
   ```
   [*DeviceB-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-LoopBack1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet0/3/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] is-level level-1
   ```
   ```
   [*DeviceC-isis-1] cost-style wide
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface LoopBack 1
   ```
   ```
   [*DeviceC-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] ipv6 route-static 2001:DB8:1::100 128 NULL 0
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-1
   ```
   ```
   [*DeviceD-isis-1] cost-style wide
   ```
   ```
   [*DeviceD-isis-1] network-entity 10.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] ipv6 enable topology ipv6
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface LoopBack 1
   ```
   ```
   [*DeviceD-LoopBack1] isis ipv6 enable 1
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] isis ipv6 enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] ipv6 route-static 2001:DB8:1::100 128 NULL 0
   ```
   ```
   [*DeviceD] commit
   ```
3. Configure the IBGP peer relationship between the devices.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2001:DB8:22::22 as-number 100
   ```
   ```
   [*DeviceA-bgp] peer 2001:DB8:22::22 connect-interface LoopBack1
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] bestroute add-path path-number 2
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:DB8:22::22 enable
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:DB8:22::22 capability-advertise add-path both
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:DB8:22::22 advertise add-path path-number 2
   ```
   ```
   [*DeviceA-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:11::11 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:11::11 connect-interface LoopBack1
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:33::33 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:33::33 connect-interface LoopBack1
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:44::44 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 2001:DB8:44::44 connect-interface LoopBack1
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] bestroute add-path path-number 2
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:11::11 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:11::11 reflect-client
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:11::11 capability-advertise add-path both
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:11::11 advertise add-path path-number 2
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:33::33 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:44::44 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceB-bgp] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 2001:DB8:22::22 as-number 100
   ```
   ```
   [*DeviceC-bgp] peer 2001:DB8:22::22 connect-interface LoopBack1
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] import-route static
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:DB8:22::22 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:DB8:22::22 next-hop-local
   ```
   ```
   [*DeviceC-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceC-bgp] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 100
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 2001:DB8:22::22 as-number 100
   ```
   ```
   [*DeviceD-bgp] peer 2001:DB8:22::22 connect-interface LoopBack1
   ```
   ```
   [*DeviceD-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceD-bgp-af-ipv6] import-route static
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:DB8:22::22 enable
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:DB8:22::22 next-hop-local
   ```
   ```
   [*DeviceD-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceD-bgp] quit
   ```
   ```
   [*DeviceD] commit
   ```
4. Configure SRv6 BE.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] segment-routing ipv6
   ```
   ```
   [*DeviceA-segment-routing-ipv6] encapsulation source-address 2001:DB8:11::11  
   ```
   ```
   [*DeviceA-segment-routing-ipv6] locator a1 ipv6-prefix 2001:DB8:10:: 64 static 32
   ```
   ```
   [*DeviceA-segment-routing-ipv6-locator] quit
   ```
   ```
   [*DeviceA-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] segment-routing ipv6 locator a1
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] segment-routing ipv6 locator a1
   ```
   ```
   [*DeviceA-bgp-af-ipv6] segment-routing ipv6 best-effort
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceA-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] segment-routing ipv6
   ```
   ```
   [*DeviceB-segment-routing-ipv6] encapsulation source-address 2001:DB8:22::22
   ```
   ```
   [*DeviceB-segment-routing-ipv6] locator b1 ipv6-prefix 2001:DB8:20:: 64 static 32
   ```
   ```
   [*DeviceB-segment-routing-ipv6-locator] quit
   ```
   ```
   [*DeviceB-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] segment-routing ipv6 locator b1
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] bgp 100
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] segment-routing ipv6 locator b1
   ```
   ```
   [*DeviceB-bgp-af-ipv6] segment-routing ipv6 best-effort
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:11::11 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:33::33 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:DB8:44::44 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceB-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceB-bgp] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] segment-routing ipv6
   ```
   ```
   [*DeviceC-segment-routing-ipv6] encapsulation source-address 2001:DB8:33::33
   ```
   ```
   [*DeviceC-segment-routing-ipv6] locator c1 ipv6-prefix 2001:DB8:30:: 64 static 32
   ```
   ```
   [*DeviceC-segment-routing-ipv6-locator] quit
   ```
   ```
   [*DeviceC-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] segment-routing ipv6 locator c1
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] segment-routing ipv6 locator c1
   ```
   ```
   [*DeviceC-bgp-af-ipv6] segment-routing ipv6 advertise sbfd-discriminator
   ```
   ```
   [*DeviceC-bgp-af-ipv6] segment-routing ipv6 best-effort
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceC-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceC-bgp] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] segment-routing ipv6
   ```
   ```
   [*DeviceD-segment-routing-ipv6] encapsulation source-address 2001:DB8:44::44
   ```
   ```
   [*DeviceD-segment-routing-ipv6] locator d1 ipv6-prefix 2001:DB8:40:: 64 static 32
   ```
   ```
   [*DeviceD-segment-routing-ipv6-locator] quit
   ```
   ```
   [*DeviceD-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] segment-routing ipv6 locator d1
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] bgp 100
   ```
   ```
   [*DeviceD-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceD-bgp-af-ipv6] segment-routing ipv6 locator d1
   ```
   ```
   [*DeviceD-bgp-af-ipv6] segment-routing ipv6 advertise sbfd-discriminator
   ```
   ```
   [*DeviceD-bgp-af-ipv6] segment-routing ipv6 best-effort
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
   ```
   ```
   [*DeviceD-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceD-bgp] quit
   ```
   ```
   [*DeviceD] commit
   ```
5. Enable BGP auto FRR on DeviceA and configure SBFD between the initiator and reflector.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] auto-frr
   ```
   ```
   [*DeviceA-bgp-af-ipv6] quit
   ```
   ```
   [*DeviceA-bgp] quit
   ```
   ```
   [~DeviceA] bfd
   ```
   ```
   [*DeviceA-bfd] quit
   ```
   ```
   [*DeviceA] sbfd
   ```
   ```
   [*DeviceA-sbfd] quit
   ```
   ```
   [*DeviceA] te ipv6-router-id 2001:DB8:11::11
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] segment-routing ipv6
   ```
   ```
   [*DeviceA-segment-routing-ipv6] locator-bfd seamless enable
   ```
   ```
   [*DeviceA-segment-routing-ipv6] locator-bfd min-tx-interval 50 min-rx-interval 50
   ```
   ```
   [*DeviceA-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bfd
   ```
   ```
   [*DeviceC-bfd] quit
   ```
   ```
   [*DeviceC] sbfd
   ```
   ```
   [*DeviceC-sbfd] reflector discriminator 3.3.3.3
   ```
   ```
   [*DeviceC-sbfd] quit
   ```
   ```
   [*DeviceC] te ipv6-router-id 2001:DB8:33::33 
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] segment-routing ipv6
   ```
   ```
   [*DeviceC-segment-routing-ipv6] locator-bfd seamless enable
   ```
   ```
   [*DeviceC-segment-routing-ipv6] locator-bfd min-tx-interval 50 min-rx-interval 50
   ```
   ```
   [*DeviceC-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bfd
   ```
   ```
   [*DeviceD-bfd] quit
   ```
   ```
   [*DeviceD] sbfd
   ```
   ```
   [*DeviceD-sbfd] reflector discriminator 4.4.4.4
   ```
   ```
   [*DeviceD-sbfd] quit
   ```
   ```
   [*DeviceD] te ipv6-router-id 2001:DB8:44::44 
   ```
   ```
   [*DeviceD] commit
   ```
   ```
   [~DeviceD] segment-routing ipv6
   ```
   ```
   [*DeviceD-segment-routing-ipv6] locator-bfd seamless enable
   ```
   ```
   [*DeviceD-segment-routing-ipv6] locator-bfd min-tx-interval 50 min-rx-interval 50
   ```
   ```
   [*DeviceD-segment-routing-ipv6] quit
   ```
   ```
   [*DeviceD] commit
   ```
6. Verify the configuration.
   
   
   
   Run the [**display bfd session all**](cmdqueryname=display+bfd+session+all) command on DeviceA to check SBFD for locator session information.
   
   ```
   [~DeviceA] display bfd session all
   ```
   ```
   (w): State in WTR
   (*): State is invalid
   --------------------------------------------------------------------------------
   Local      Remote     PeerIpAddr      State     Type        InterfaceName
   --------------------------------------------------------------------------------
   16387      33686018   2001:DB8:40::
                                         Up        D_IP_PEER         -
   16388      16843009   2001:DB8:30::
                                         Up        D_IP_PEER         -
   --------------------------------------------------------------------------------
       Total UP/DOWN Session Number : 2/0
   ```
   
   Run the **display bgp ipv6 routing-table** *ipv6-address* [ *mask* | *mask-length* ] **bfd-discriminator** command on DeviceA to check SBFD discriminator information.
   
   ```
   [~DeviceA] display bgp ipv6 routing-table 2001:DB8:1::100 bfd-discriminator
   ```
   ```
    BGP routing table entry information of 2001:DB8:1::100/128:
    From: 2001:DB8:22::22
    BFD Discriminator: Locator SBFD <3.3.3.3>, Source IP <2001:DB8:30::>
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  bfd
  #
  sbfd
  #
  te ipv6-router-id 2001:DB8:11::11                          
  #
  segment-routing ipv6                          
   encapsulation source-address 2001:DB8:11::11
   locator-bfd seamless enable
   locator-bfd min-tx-interval 50 min-rx-interval 50
   locator a1 ipv6-prefix 2001:DB8:10:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0001.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator a1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:11::11/128
   isis ipv6 enable 1
  #
  bgp 100                                    
   router-id 1.1.1.1
   peer 2001:DB8:22::22 as-number 100
   peer 2001:DB8:22::22 connect-interface LoopBack1                                
   #                                                 
   ipv6-family unicast
    auto-frr
    bestroute add-path path-number 2   
    segment-routing ipv6 locator a1
    segment-routing ipv6 best-effort
    peer 2001:DB8:22::22 enable
    peer 2001:DB8:22::22 capability-advertise add-path both  
    peer 2001:DB8:22::22 advertise add-path path-number 2        
    peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:22::22
   locator b1 ipv6-prefix 2001:DB8:20:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0002.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator b1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/96
   isis ipv6 enable 1
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:22::22/128
   isis ipv6 enable 1
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:DB8:11::11 as-number 100
   peer 2001:DB8:11::11 connect-interface LoopBack1
   peer 2001:DB8:33::33 as-number 100
   peer 2001:DB8:33::33 connect-interface LoopBack1
   peer 2001:DB8:44::44 as-number 100
   peer 2001:DB8:44::44 connect-interface LoopBack1
   #
   ipv6-family unicast
    bestroute add-path path-number 2
    segment-routing ipv6 locator b1
    segment-routing ipv6 best-effort
    peer 2001:DB8:11::11 enable
    peer 2001:DB8:11::11 reflect-client
    peer 2001:DB8:11::11 capability-advertise add-path both
    peer 2001:DB8:11::11 advertise add-path path-number 2
    peer 2001:DB8:11::11 prefix-sid advertise-srv6-locator
    peer 2001:DB8:33::33 enable
    peer 2001:DB8:33::33 prefix-sid advertise-srv6-locator
    peer 2001:DB8:44::44 enable
    peer 2001:DB8:44::44 prefix-sid advertise-srv6-locator
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  sbfd
   reflector discriminator 3.3.3.3
  #
  te ipv6-router-id 2001:DB8:33::33
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:33::33
   locator-bfd seamless enable
   locator-bfd min-tx-interval 50 min-rx-interval 50
   locator c1 ipv6-prefix 2001:DB8:30:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator c1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:33::33/128
   isis ipv6 enable 1
  #
  ipv6 route-static 2001:DB8:1::100 128 NULL 0 
  #
  bgp 100
   router-id 3.3.3.3
   peer 2001:DB8:22::22 as-number 100
   peer 2001:DB8:22::22 connect-interface LoopBack1
   #
   ipv6-family unicast
    import-route static
    segment-routing ipv6 locator c1
    segment-routing ipv6 advertise sbfd-discriminator
    segment-routing ipv6 best-effort
    peer 2001:DB8:22::22 enable
    peer 2001:DB8:22::22 next-hop-local
    peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  bfd
  #
  sbfd
   reflector discriminator 4.4.4.4
  #
  te ipv6-router-id 2001:DB8:44::44
  #
  segment-routing ipv6
   encapsulation source-address 2001:DB8:44::44
   locator-bfd seamless enable
   locator-bfd min-tx-interval 50 min-rx-interval 50
   locator d1 ipv6-prefix 2001:DB8:40:: 64 static 32
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology ipv6
   segment-routing ipv6 locator d1
   #
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::2/96
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:44::44/128
   isis ipv6 enable 1
  #
  ipv6 route-static 2001:DB8:1::100 128 NULL 0
  #
  bgp 100
   router-id 4.4.4.4
   peer 2001:DB8:22::22 as-number 100
   peer 2001:DB8:22::22 connect-interface LoopBack1
   #
   ipv6-family unicast
    import-route static
    segment-routing ipv6 locator d1
    segment-routing ipv6 advertise sbfd-discriminator
    segment-routing ipv6 best-effort
    peer 2001:DB8:22::22 enable
    peer 2001:DB8:22::22 next-hop-local
    peer 2001:DB8:22::22 prefix-sid advertise-srv6-locator
  #
  return
  ```