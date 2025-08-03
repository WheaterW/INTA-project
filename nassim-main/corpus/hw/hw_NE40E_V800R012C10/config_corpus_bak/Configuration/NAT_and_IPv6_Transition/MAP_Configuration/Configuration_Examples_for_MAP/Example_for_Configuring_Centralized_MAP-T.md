Example for Configuring Centralized MAP-T
=========================================

This section provides an example for configuring the centralized MAP-T function on a device functioning as a MAP-BR.

#### Networking Requirements

In a centralized scenario shown in [Figure 1](#EN-US_TASK_0172374847__fig_dc_ne_map_cfg_0030), the MAP-BR and BRAS reside on different devices. The BRAS delivers MAP addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. (In this example, only key BRAS configurations are provided. For details about IPv6 address assignment configuration, see HUAWEI NE40E-M2 seriesUniversal Service Router Configuration Guide - User Access - IPv6 Address Management Configuration.) RouterA (MAP BR) resides on the edge of a MAP domain and allows MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. The MAP-CEs can also communicate with each other through the MAP-BR based on each other's public IPv4 address.

**Figure 1** MAP-T networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 are GE 0/2/0 and GE 0/2/1, respectively.


  
![](images/fig_dc_ne_map_cfg_0030.png)

#### Prerequisites

* The MAP license has been loaded to the MAP-BR, and the MAP function has been activated.
* The MAP-BR has at least one interface board that supports the MAP function.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BMR.
2. Configure a DMR prefix address and a prefix length.
3. Configure an IPv6 prefix pool and address pool on the BRAS.
4. Configure a MAP-T instance and bind the DMR and BMR rules to the MAP-T instance.

#### Data Preparation

To complete the configuration, you need the following data:

* BMR name (bmr\_name), IPv6 address (2001:db8:1::1), prefix length (48 bits), IPv4 address (1.1.1.0), mask (24), EA length (16 bits), and PSID offset (4)
* DMR name (dmr\_name), IPv6 address (2001:db8:3::1), and prefix length (96 bits)
* MAP-T instance name (1) and ID (1)
* Interface1's IPv6 address (2001:db8:2::1) and mask length (64 bits).
* Interface2's IPv4 address (11.1.1.1) and mask length (24 bits)


#### Procedure

1. Configure a BMR on the BRAS to instruct the BRAS to assign IPv6 and IPv4 addresses to the MAP-CEs. In this example, the IPv6 prefix address assigned to the MAP-CE is **2001:db8:1::1**, the prefix length is **48**, and the length of the EA-bits is **16**. The public IPv4 prefix address allocated to the MAP-CE is **1.1.1.0** and the prefix length is **24**. The offset length of the PSID field is **4**, which means that ports **0** to **4096** are reserved.
   
   
   ```
   <BRAS> system-view
   [~BRAS] map rule bmr_name
   [*BRAS-map-rule-bmr_name] rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
   [*BRAS-map-rule-bmr_name] commit
   [~BRAS-map-rule-bmr_name] quit
   ```
2. Configure a DMR rule on the BRAS and combine the IPv6 prefix configured in the DMR rule with the destination IPv4 address on a MAP-CE to form a destination IPv6 address.
   
   
   ```
   [~BRAS] dmr-prefix dmr_name ipv6-prefix 2001:db8:3::1 prefix-length 96
   [*BRAS] commit
   ```
3. Configure an IPv6 prefix pool and an address pool on the BRAS.
   
   
   * Configure an IPv6 prefix pool named **pre1**, bind it to the MAP rule named **bmr\_name**, and assign IPv4 and IPv6 addresses that comply with BMR rules to MAP-CEs.
     ```
     [~BRAS] ipv6 prefix pre1 delegationf
     [*BRAS-ipv6-prefix-pre1] map-rule bmr_name
     [*BRAS-ipv6-prefix-pre1] commit
     [~BRAS-ipv6-prefix-pre1] quit
     ```
   * Configure an IPv6 address pool named **pool1** and bind it to the prefix pool named **pre1**. Bind the prefix **dmr\_name** to the IPv6 address pool so that the BRAS encapsulates the IPv6 prefix as Option 91 information (OPTION\_S46\_DMR) into the DHCPv6 Response message sent to MAP-CEs.
     ```
     [~BRAS] ipv6 pool pool1 bas delegation
     [*BRAS-ipv6-pool-pool1] prefix pre1
     [*BRAS-ipv6-pool-pool1] option-s46 dmr-prefix dmr_name
     [*BRAS-ipv6-pool-pool1] commit
     [~BRAS-ipv6-pool-pool1] quit
     ```
4. Configure BMRs on the MAP-BR. Configure the BMR to remove the user-side IPv4 address from the IPv6 address and encapsulate IPv6 information into the IPv4 address and port number of the network-side traffic.
   
   
   ```
   <RouterA> system-view
   [~RouterA] map rule bmr_name
   [*RouterA-map-rule-bmr_name] rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
   [*RouterA-map-rule-bmr_name] commit
   [~RouterA-map-rule-bmr_name] quit
   ```
5. Configure a DMR on the MAP-BR.
   
   
   ```
   [~RouterA] dmr-prefix dmr_name ipv6-prefix 2001:db8:3::1 prefix-length 96
   [*RouterA] commit
   ```
6. Configure a MAP-T instance on the MAP-BR and bind the configured DMR and BMR rules to the MAP-T instance. The DMR rule is used to translate the IPv6 packets imported from the MAP-CE to the MAP-T instance for address translation and bind the BMR rules to encapsulate and verify the packets in the instance.
   
   
   ```
   [~RouterA] map-t instance 1 id 1
   [*RouterA-map-t-instance-1] dmr-prefix dmr_name
   [*RouterA-map-t-instance-1] map-rule bmr_name
   [*RouterA-map-t-instance-1] commit
   [~RouterA-map-t-instance-1] quit
   ```
7. Configure IP addresses of the user- and network-side interfaces on the MAP-BR.
   
   
   ```
   [~RouterA] interface GigabitEthernet0/2/0
   [~RouterA-GigabitEthernet0/2/0] ipv6 enable
   [*RouterA-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::1 64
   [*RouterA-GigabitEthernet0/2/0] commit
   [~RouterA-GigabitEthernet0/2/0] quit
   [~RouterA] interface GigabitEthernet0/2/1
   [~RouterA-GigabitEthernet0/2/1] ip address 11.1.1.1 24
   [*RouterA-GigabitEthernet0/2/1] commit
   [~RouterA-GigabitEthernet0/2/1] quit
   [~RouterA] ipv6 route-static 2001:db8:1::1 48 2001:db8:2::2
   [*RouterA] commit
   ```
8. Configure an address for the interface connecting the BRAS to the MAP-BR device.
   
   
   ```
   [~BRAS] interface GigabitEthernet0/2/0
   [*BRAS-GigabitEthernet0/2/0] ipv6 enable
   [*BRAS-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::2 64
   [*BRAS-GigabitEthernet0/2/0] undo shutdown
   [*BRAS-GigabitEthernet0/2/0] commit
   [~BRAS-GigabitEthernet0/2/0] quit
   [~BRAS] ipv6 route-static 2001:db8:3::1 48 2001:db8:2::1
   [*BRAS] commit
   ```

#### Router A Configuration File (MAP-BR)

```
#
dmr-prefix dmr_name ipv6-prefix 2001:db8:3::1 prefix-length 96
#
map rule bmr_name
 rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
#
map-t instance 1 id 1
 dmr-prefix dmr_name
 map-rule bmr_name
#
interface GigabitEthernet0/2/0
 undo negotiation auto
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:2::1/64
#
interface GigabitEthernet0/2/1
 undo negotiation auto
 undo shutdown
 control-flap
 ip address 11.1.1.1 255.255.255.0
#
ipv6 route-static 2001:db8:1::1 48 2001:db8:2::2
#
```
#### BRAS Configuration File

```
#
dmr-prefix dmr_name ipv6-prefix 2001:db8:3::1 prefix-length 96
#
map rule bmr_name
 rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
#
ipv6 prefix pre1 delegation
 map rule bmr_name
ipv6 pool pool1 bas delegation
 prefix pre1
 option-s46 dmr-prefix dmr_name
#
interface GigabitEthernet0/2/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:2::2/64
#
ipv6 route-static 2001:db8:3::1 48 2001:db8:2::1
#
```