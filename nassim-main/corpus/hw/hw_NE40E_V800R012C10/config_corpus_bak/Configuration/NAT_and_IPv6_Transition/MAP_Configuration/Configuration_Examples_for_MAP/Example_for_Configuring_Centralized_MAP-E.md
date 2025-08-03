Example for Configuring Centralized MAP-E
=========================================

This section provides an example for configuring the centralized MAP-E function on the device that functions as a MAP BR.

#### Networking Requirements

In a centralized scenario shown in [Figure 1](#EN-US_TASK_0172374849__fig_dc_ne_map_cfg_0030), the MAP-BR (Router A) and BRAS reside on different devices. The BRAS delivers MAP IPv6 addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. Router A resides on the edge of a MAP domain and allows MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. The MAP-CEs use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Networking diagram for configuring MAP-E![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 are GE 0/2/0 and GE 0/2/1, respectively.


  
![](images/fig_dc_ne_map_cfg_0030.png)

#### Prerequisites

* The MAP license has been loaded to the MAP-BR, and the MAP function has been activated.
* The MAP-BR has at least one interface board that supports the MAP function.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BR.
2. Configure BMR rules.
3. Configure a MAP-E instance and bind the BMR and BR rules to the MAP-E instance.
4. Configure an IPv6 prefix pool and address pool on the BRAS.
5. Configure the IP address for each interface and a static route.

#### Data Preparation

To complete the configuration, you need the following data:

* BR name (br\_name), IPv6 address (2001:db8:1124::1), and prefix length (96 bits)
* BMR name (bmr\_name), IPv6 address (2001:db8:1::1), prefix length (48), IPv4 address (1.1.1.0), mask length (24), EA-length (16), and PSID-offset length (4)
* MAP-E instance name (2) and ID (2)
* Interface1's IPv6 address (2001:db8:2::1) and mask length (64 bits).
* Interface2's IPv4 address (11.1.1.1) and mask length (24 bits)


#### Procedure

1. Configure the BR function on a BRAS named **br\_name** and set the IPv6 address to **2001:db8:1124::1** and the prefix length to **96**. Use the BR's IPv6 address as the destination address carried in packets sent by MAP-CEs.
   
   
   ```
   <BRAS> system-view
   [~BRAS] br-ipv6-address br_name ipv6-address 2001:db8:1124::1 prefix-length 96
   [*BRAS] commit
   ```
2. Configure a BMR on the BRAS to instruct the BRAS to assign IPv6 and IPv4 addresses to the MAP-CEs. In this example, the IPv6 prefix address assigned to the MAP-CE is **2001:db8:1::1**, the prefix length is **48**, and the length of the EA-bits is **16**. The public IPv4 prefix address allocated to the MAP-CE is **1.1.1.0** and the prefix length is **24**. The offset length of the PSID field is **4**, which means that ports **0** to **4096** are reserved.
   
   
   ```
   [~BRAS] map rule bmr_name
   [*BRAS-map-rule-bmr_name] rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
   [*BRAS-map-rule-bmr_name] commit
   [~BRAS-map-rule-bmr_name] quit
   ```
3. Configure an IPv6 prefix pool and an address pool on the BRAS.
   
   
   * Configure an IPv6 prefix pool named **pre1** and bind it to the BMR rule named **bmr\_name** to allocate PD prefixes to MAP-CEs.
     ```
     [~BRAS] ipv6 prefix pre1 delegation
     [*BRAS-ipv6-prefix-pre1] map-rule bmr_name
     [*BRAS-ipv6-prefix-pre1] commit
     [~BRAS-ipv6-prefix-pre1] quit
     ```
   * Configure an IPv6 address pool named **pool1** and bind it to the prefix pool named **pre1**. Bind the BR name **br\_name** to the IPv6 address pool. Then, the BRAS encapsulates the IPv6 prefix as Option 90 information (OPTION\_S46\_BR) into the DHCPv6 Response message sent to the MAP-E users.
     ```
     <BRAS> system-view
     [~BRAS] ipv6 pool pool1 bas delegation
     [*BRAS-ipv6-pool-pool1] prefix pre1
     [*BRAS-ipv6-pool-pool1] option-s46 br-ipv6-address br_name
     [*BRAS-ipv6-pool-pool1] commit
     [~BRAS-ipv6-pool-pool1] quit
     ```
4. On the MAP-BR, configure the BR that is the local IPv6 address as the destination address of IPv6 packets sent by MAP-CEs. Set the BR name to **br\_name**, the IPv6 address to **2001:db8:1124::1**, and the prefix length to **96**.
   
   
   ```
   <RouterA> system-view
   [~RouterA] br-ipv6-address br_name ipv6-address 2001:db8:1124::1 prefix-length 96
   [*RouterA] commit
   ```
5. Configure BMRs on the MAP-BR. Configure the BMR to remove the user-side IPv4 address from the IPv6 address and encapsulate IPv6 information into the IPv4 address and port number of the network-side traffic.
   
   
   ```
   [~RouterA] map rule bmr_name
   [*RouterA-map-rule-bmr_name] rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
   [*RouterA-map-rule-bmr_name] commit
   [~RouterA-map-rule-bmr_name] quit
   ```
6. Configure a MAP-E instance on the MAP-BR and bind the configured BR and BMR rules to the MAP-E instance. The BR is used to import the encapsulated traffic of MAP-CEs to an interface board, select the MAP-E instance for conversion, and bind the BMR rule to encapsulate and verify the packets in the instance.
   
   
   ```
   [~RouterA] map-e instance 2 id 2
   [*RouterA-map-e-instance-2] br-ipv6-address br_name
   [*RouterA-map-e-instance-2] map-rule bmr_name
   [*RouterA-map-e-instance-2] commit
   [~RouterA-map-e-instance-2] quit
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
   [~BRAS] ipv6 route-static 2001:db8:1124::1 64 2001:db8:2::1
   [*BRAS] commit
   ```

#### Router A Configuration File (MAP-BR)

```
#
br-ipv6-address br_name ipv6-address 2001:db8:1124::1 prefix-length 96
#
map rule bmr_name
 rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
#
map-e instance 2 id 2
 br-ipv6-address br_name
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
br-ipv6-address br_name ipv6-address 2001:db8:1124::1 prefix-length 96
#
map rule bmr_name
 rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
#
ipv6 prefix pre1 delegation
 map-rule bmr_name
ipv6 pool pool1 bas delegation
 prefix pre1
 option-s46 br-ipv6-address br_name
#
interface GigabitEthernet0/2/0
 undo shutdown
 ipv6 enable
 ipv6 address 2001:db8:2::2/64
#
ipv6 route-static 2001:db8:1124::1 64 2001:db8:2::1
#
```