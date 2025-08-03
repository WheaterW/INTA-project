Example for Configuring PIM Anycast-RP (IPv6)
=============================================

In the scenario where multiple multicast sources and receivers are located in a PIM-SM domain, you can configure Anycast-RP peer relationships so that IP routing will automatically select the topologically closest Rendezvous Point (RP) for each source and receiver. This alleviates burdens on RPs, implements RP backup, and optimizes multicast forwarding paths.

#### Networking Requirements

In a traditional PIM-SM domain, all multicast groups map to one RP. When the network is overloaded or traffic congests on an RP, the RP may be overburdened. If the RP fails, routes converge slowly or multicast packets are forwarded over non-optimal paths. Configuring the PIM Anycast-RP can address these problems. IP routing will automatically select the topologically closest RP for each source and receiver. This feature can accelerate data transmission to receivers.

On the network shown in [Figure 1](#EN-US_TASK_0172367528__fig_dc_vrp_multicast_cfg_216301), there are multiple multicast sources and receivers in the PIM-SM domain. Receiver 2 requests multicast data from the source. Configure Anycast-RP peer relationships between Device C and Device D so that Receiver 2 can send a Join message to the closest RP, that is, Device D. After receiving multicast data from the source, Device A encapsulates the multicast data into a Register message and sends it to Device C. Upon receipt, Device C forwards the Register message to Device D and Receiver 2 can receive the multicast data from the source.

**Figure 1** Configuring PIM Anycast-RP  
![](images/fig_dc_vrp_multicast_cfg_216301.png)

| Device | Interface | IPv6 Address  Link-local Address |
| --- | --- | --- |
| Device A | interface1, GE 0/1/0 | 2001:db8:1::1/64  FE80::1 |
| interface2, GE 0/2/0 | 2001:db8:2::1/64  FE80::2 |
| Device B | interface1, GE 0/1/0 | 2001:db8:3::1/64  FE80::3 |
| Device C | interface1, GE 0/1/0 | 2001:db8:4::1/64  FE80::4 |
| interface2, GE 0/2/0 | 2001:db8:2::2/64  FE80::5 |
| interface3, GE 0/3/0 | 2001:db8:5::1/64  FE80::6 |
| Loopback0 | 2001:db8:7::7/128  FE80::7 |
| Loopback1 | 2001:db8:8::8/128  FE80::8 |
| Device D | interface1, GE 0/1/0 | 2001:db8:3::2/64  FE80::9 |
| interface2, GE 0/2/0 | 2001:db8:6::1/64  FE80::10 |
| interface3, GE 0/3/0 | 2001:db8:4::2/64  FE80::11 |
| Loopback0 | 2001:db8:7::7/128  FE80::12 |
| Loopback1 | 2001:db8:9::9/128  FE80::13 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each Router interface and configure Open Shortest Path First version 3 (OSPFv3) to implement IP interworking.
2. Enable multicast routing on each Router and PIM-SM on each Router interface.
3. Enable Multicast Listener Discovery (MLD) on interfaces connecting Routers to hosts.
4. On Device C and Device D, configure the Loopback 0 interfaces as both Candidate-Rendezvous Points (C-RPs) and Candidate-BootStrap Routers (C-BSRs).
5. Configure the address of the Loopback 0 interfaces on Device C and Device D as the Anycast-RP address.
6. On Device C and Device D, configure the addresses of the Loopback 1 interfaces as the local addresses of Anycast-RPs.
7. Configure Anycast-RP peer relationships between Device C and Device D.

#### Data Preparation

To complete the configuration, you need the following data:

* Multicast group address: FF5E::6/64
* RP address
* Local RP address of the Anycast-RP

#### Procedure

1. Assign an IPv6 address to each Router interface and configure OSPFv3 to implement IP interworking. For configuration details, see [Configuration Files](#EN-US_TASK_0172367528__sectiondc_vrp_multicast_cfg_216305) in this section.
   
   
   
   # Enable global IPv6 on Device A.
   
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
   [~DeviceA] ipv6
   ```
   
   # Enable global IPv6 on Device B.
   
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
   [~DeviceB] ipv6
   ```
   
   # Enable global IPv6 on Device C.
   
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
   [~DeviceC] ipv6
   ```
   
   # Enable global IPv6 on Device D.
   
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
   [~DeviceD] ipv6
   ```
   
   # Assign an IPv6 address and a link-local address for each Router interface based on [Figure 1](#EN-US_TASK_0172367528__fig_dc_vrp_multicast_cfg_216301).
   
   # Configure Device A.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address fe80::1 link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ipv6 address fe80::2 link-local
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:3::1 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address fe80::3 link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 address 2001:db8:4::1 64
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 address fe80::4 link-local
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::2 64
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address fe80::5 link-local
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ipv6 address 2001:db8:5::1 64
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ipv6 address fe80::6 link-local
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] ipv6 enable
   ```
   ```
   [*DeviceC-LoopBack0] ipv6 address 2001:db8:7::7 128
   ```
   ```
   [*DeviceC-LoopBack0] ipv6 address fe80::7 link-local
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceC-LoopBack1] ipv6 address 2001:db8:8::8 128
   ```
   ```
   [*DeviceC-LoopBack1] ipv6 address fe80::8 link-local
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 address 2001:db8:3::2 64
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 address fe80::9 link-local
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ipv6 address 2001:db8:6::1 64
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ipv6 address fe80::10 link-local
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ipv6 address 2001:db8:4::2 64
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ipv6 address fe80::11 link-local
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] interface loopback 0
   ```
   ```
   [*DeviceD-LoopBack0] ipv6 enable
   ```
   ```
   [*DeviceD-LoopBack0] ipv6 address 2001:db8:7::7 128
   ```
   ```
   [*DeviceD-LoopBack0] ipv6 address fe80::12 link-local
   ```
   ```
   [*DeviceD-LoopBack0] quit
   ```
   ```
   [*DeviceD] interface loopback 1
   ```
   ```
   [*DeviceD-LoopBack1] ipv6 enable
   ```
   ```
   [*DeviceD-LoopBack1] ipv6 address 2001:db8:9::9 128
   ```
   ```
   [*DeviceD-LoopBack1] ipv6 address fe80::13 link-local
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
   
   # Configure OSPFv3 between Routers to implement IP interworking.
   
   # Configure Device A.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 10.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0
   ```
   ```
   [*DeviceA-ospfv3-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 10.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0
   ```
   ```
   [*DeviceB-ospfv3-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 10.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] area 0
   ```
   ```
   [*DeviceC-ospfv3-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] ospfv3 1 area 0
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] ospfv3 1
   ```
   ```
   [*DeviceD-ospfv3-1] router-id 10.4.4.4
   ```
   ```
   [*DeviceD-ospfv3-1] area 0
   ```
   ```
   [*DeviceD-ospfv3-area-0.0.0.0] quit
   ```
   ```
   [*DeviceD-ospfv3-1] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] interface loopback0
   ```
   ```
   [*DeviceD-LoopBack0] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-LoopBack0] quit
   ```
   ```
   [*DeviceD] interface loopback1
   ```
   ```
   [*DeviceD-LoopBack1] ospfv3 1 area 0
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
2. Enable IPv6 multicast routing. Enable IPv6 PIM-SM on each Router interface and enable multicast listener discovery (MLD) on the interfaces connecting Routers to user hosts.
   
   
   
   # Enable IPv6 multicast routing on all Routers. Enable IPv6 PIM-SM on each Router interface and enable MLD on the interfaces connecting Device C and Device D to user hosts.
   
   # Configure Device A.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] pim ipv6 sm
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] pim ipv6 sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] pim ipv6 sm
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] mld enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceC] interface loopback 0
   ```
   ```
   [*DeviceC-LoopBack0] pim ipv6 sm
   ```
   ```
   [*DeviceC-LoopBack0] quit
   ```
   ```
   [*DeviceC] interface loopback 1
   ```
   ```
   [*DeviceC-LoopBack1] pim ipv6 sm
   ```
   ```
   [*DeviceC-LoopBack1] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] multicast ipv6 routing-enable
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] mld enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceD] interface GigabitEthernet 0/3/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] pim ipv6 sm
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] mld enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceD] interface loopback 0
   ```
   ```
   [*DeviceD-LoopBack0] pim ipv6 sm
   ```
   ```
   [*DeviceD-LoopBack0] quit
   ```
   ```
   [*DeviceD] interface loopback 1
   ```
   ```
   [*DeviceD-LoopBack1] pim ipv6 sm
   ```
   ```
   [*DeviceD-LoopBack1] quit
   ```
3. On Device C and Device D, configure the Loopback 0 interfaces as both C-RPs and C-BSRs.
   
   
   
   # Configure Device C.
   
   ```
   [~DeviceC] pim-ipv6
   ```
   ```
   [*DeviceC-pim6] c-bsr 2001:db8:7::7
   ```
   ```
   [*DeviceC-pim6] c-rp 2001:db8:7::7
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] pim-ipv6
   ```
   ```
   [*DeviceD-pim6] c-bsr 2001:db8:7::7
   ```
   ```
   [*DeviceD-pim6] c-rp 2001:db8:7::7
   ```
4. Configure the address of the Loopback 0 interfaces on Device C and Device D as the Anycast-RP address.
   
   
   
   # Configure Device C.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceC-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
   
   # Configure Device D.
   
   ```
   [*DeviceD-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceD-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
5. On Device C and Device D, configure the addresses of the Loopback 1 interfaces as the local addresses of Anycast-RPs.
   
   
   
   # Configure Device C.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceC-pim6-anycast-rp-2001:DB8:7::7] local-address 2001:DB8:8::8
   ```
   ```
   [*DeviceC-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
   
   # Configure Device D.
   
   ```
   [*DeviceD-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceD-pim6-anycast-rp-2001:DB8:7::7] local-address 2001:db8:9::9
   ```
   ```
   [*DeviceD-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
6. Configure Anycast-RP peer relationships between Device C and Device D.
   
   
   
   # Configure Device C.
   
   ```
   [*DeviceC-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceC-pim6-anycast-rp-2001:DB8:7::7] peer 2001:db8:9::9
   ```
   ```
   [*DeviceC-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
   ```
   [*DeviceC-pim6] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Configure Device D.
   
   ```
   [*DeviceD-pim6] anycast-rp 2001:db8:7::7
   ```
   ```
   [*DeviceD-pim6-anycast-rp-2001:DB8:7::7] peer 2001:db8:8::8
   ```
   ```
   [*DeviceD-pim6-anycast-rp-2001:DB8:7::7] quit
   ```
   ```
   [*DeviceD-pim6] quit
   ```
   ```
   [*DeviceD] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display pim ipv6 rp-info** command on Device C and Device D to check RP information.
   
   ```
   <DeviceC> display pim ipv6 rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: FF00::/8
        RP: 2001:DB8:7::7 (local)
        Priority: 192
        Uptime: 00:17:45
        Expires: 00:01:45
   ```
   ```
   <DeviceD> display pim ipv6 rp-info
   ```
   ```
    VPN-Instance: public net
    PIM-SM BSR RP Number:1
    Group/MaskLen: FF00::/8
        RP: 2001:DB8:7::7 (local)
        Priority: 192
        Uptime: 00:16:26
        Expires: 00:02:04
   ```
   
   The preceding command output shows that Device C and Device D both serve as an RP and can forward Register messages from the multicast source to each other.
   
   # Have Source (2001:db8:1::2/64) send multicast data to group G (ff5e::6). Have Source send a Register message to Device C and have Receiver 2 send a Join message to Device D. Then, run the **display pim ipv6 routing-table** command to check PIM entries on each Router.
   
   ```
   <DeviceC> display pim ipv6 routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (2001:DB8:1::2, FF5E::6)
        RP: 2001:DB8:7::7 (local)
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:01:40
        Upstream interface: GigabitEthernet0/2/0, Refresh time: 00:01:40
            Upstream neighbor: FE80::2
            RPF prime neighbor: FE80::2
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/1/0
                Protocol: pim-sm, UpTime: 00:00:45, Expires: 00:02:45
   
   ```
   ```
   <DeviceD> display pim ipv6 routing-table
   ```
   ```
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, FF5E::6)
        RP: 2001:DB8:7::7 (local)
        Protocol: pim-sm, Flag: WC
        UpTime: 00:01:14
        Upstream interface: Register, Refresh time: 00:01:14
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/2/0
                Protocol: mld, UpTime: 00:01:14, Expires: -
   
    (2001:DB8:1::2, FF5E::6)
        RP: 2001:DB8:7::7 (local)
        Protocol: pim-sm, Flag: SWT ACT
        UpTime: 00:00:17
        Upstream interface: Register, Refresh time: 00:00:17
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
            1: GigabitEthernet0/2/0
                Protocol: pim-sm, UpTime: 00:00:17, Expires: -
   
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
   sysname DeviceA
  #
   multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 10.1.1.1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ipv6 address FE80::1 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ipv6 address FE80::2 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  return
  
  ```
* Device B configuration file
  
  ```
  #
   sysname DeviceB
  #
   multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 10.2.2.2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   ipv6 address FE80::3 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  return
  
  ```
* Device C configuration file
  
  ```
  #
   sysname DeviceC
  #
   multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 10.3.3.3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   ipv6 address FE80::4 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ipv6 address FE80::5 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:5::1/64
   ipv6 address FE80::6 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
   mld enable
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:7::7/128
   ipv6 address FE80::7 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:8::8/128
   ipv6 address FE80::8 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  pim-ipv6
   c-bsr 2001:DB8:7::7
   c-rp 2001:DB8:7::7
   anycast-rp 2001:DB8:7::7
    local-address 2001:DB8:8::8
    peer 2001:DB8:9::9
  #
  return
  ```
* Device D configuration file
  
  ```
  #
   sysname DeviceD
  #
   multicast ipv6 routing-enable
  #
  ospfv3 1
   router-id 10.4.4.4
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   ipv6 address FE80::9 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:6::1/64
   ipv6 address FE80::10 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   ipv6 address FE80::11 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
   mld enable
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:7::7/128
   ipv6 address FE80::12 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:9::9/128
   ipv6 address FE80::13 link-local
   ospfv3 1 area 0.0.0.0
   pim ipv6 sm
  #
  pim-ipv6
   c-bsr 2001:DB8:7::7
   c-rp 2001:DB8:7::7
   anycast-rp 2001:DB8:7::7
    local-address 2001:DB8:9::9
    peer 2001:DB8:8::8
  #
  return
  ```