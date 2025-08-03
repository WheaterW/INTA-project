Example for Configuring Distributed MAP-E
=========================================

This section provides an example for configuring the distributed MAP-E function on a device that functions as the MAP-BR and BRAS.

#### Networking Requirements

In a distributed scenario shown in [Figure 1](#EN-US_TASK_0172374850__fig_dc_ne_map_cfg_0030), both the MAP-BR and BRAS reside on Router A. The BRAS functions as a DHCPv6 server to deliver MAP IPv6 addresses and mapping rules to MAP-CEs in DHCPv6 IA\_PD mode. Router A also functions as a MAP-BR and resides on the edge of a MAP domain. Router A allows the MAP-CEs to access the public IPv4 network through the IPv6 network that is within the MAP domain. In addition, the MAP-CEs can use each other's public IPv4 address to communicate through the MAP-BR.

**Figure 1** Networking diagram for configuring MAP-E![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 are GE 0/2/0 and GE 0/2/1, respectively. Interface 1 is used in this example.


  
![](images/fig_dc_ne_map_cfg_0036.png)

#### Prerequisites

* The MAP license has been loaded to the MAP-BR, and the MAP function has been activated.
* The MAP-BR has at least one interface board that supports the MAP function.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a BR.
2. Configure BMR rules.
3. Configure an IPv6 prefix pool and an IPv6 address pool.
4. Configure a MAP-E instance and bind the BMR and BR rules to the MAP-E instance.
5. Configure user access and RADIUS authentication on the BRAS.

#### Data Preparation

To complete the configuration, you need the following data:

* BR name (br\_name), IPv6 address (2001:db8:1124::1), and prefix length (96 bits)
* BMR name (bmr\_name), IPv6 address (2001:db8:1::1), prefix length (48), IPv4 address (1.1.1.0), mask length (24), EA-length (16), and PSID-offset length (4)
* MAP-E instance name (2) and ID (2)
* Interface1's IPv6 address (2001:db8:2::1), IPv6 mask length (64 bits), IPv4 address (10.1.1.1), and IPv4 mask length (24 bits)
* Interface2's IPv4 address (11.1.1.1) and mask length (24 bits)


#### Procedure

1. On the MAP-BR, configure the BR that is the local IPv6 address as the destination address of IPv6 packets sent by MAP-CEs. Set the BR name to **br\_name**, the IPv6 address to **2001:db8:1124::1**, and the prefix length to **96**.
   
   
   ```
   <RouterA> system-view
   [~RouterA] br-ipv6-address br_name ipv6-address 2001:db8:1124::1 prefix-length 96
   [*RouterA] commit
   ```
2. Configure a BMR rule on the MAP-BR to instruct the BRAS to assign IPv6 and IPv4 addresses to MAP-CEs. Configure the BMR to remove the user-side IPv4 address from the IPv6 address and encapsulate IPv6 information into the IPv4 address and port number of the network-side traffic.
   
   
   ```
   [~RouterA] map rule bmr_name
   [*RouterA-map-rule-bmr_name] rule-prefix 2001:db8:1::1 prefix-length 48 ipv4-prefix 1.1.1.0 prefix-length 24 ea-length 16 psid-offset 4
   [*RouterA-map-rule-bmr_name] commit
   [~RouterA-map-rule-bmr_name] quit
   ```
3. Configure an IPv6 prefix pool and an address pool on the BRAS.
   
   
   * Configure an IPv6 prefix pool named **pre1** and bind it to the BMR rule named **bmr\_name** to allocate PD prefixes to MAP-CEs.
     ```
     [~RouterA] ipv6 prefix pre1 delegation
     [*RouterA-ipv6-prefix-pre1] map-rule bmr_name
     [*RouterA-ipv6-prefix-pre1] commit
     [~RouterA-ipv6-prefix-pre1] quit
     ```
   * Configure an IPv6 address pool named **pool1** and bind it to the prefix pool named **pre1**. Bind the BR name **br\_name** to the IPv6 address pool. Then, the BRAS encapsulates the IPv6 prefix as Option 90 information (OPTION\_S46\_BR) into the DHCPv6 Response message sent to the MAP-E users.
     ```
     [~RouterA] ipv6 pool pool1 bas delegation
     [*RouterA-ipv6-pool-pool1] prefix pre1
     [*RouterA-ipv6-pool-pool1] option-s46 br-ipv6-address br_name
     [*RouterA-ipv6-pool-pool1] commit
     [~RouterA-ipv6-pool-pool1] quit
     ```
4. Configure a MAP-E instance on the device and bind the configured BR and BMR rules to the MAP-E instance. The BR is used to import the encapsulated traffic of MAP-CEs to an interface board, select the MAP-E instance for conversion, and bind the BMR rule to encapsulate and verify the packets in the instance.
   
   
   ```
   [~RouterA] map-e instance 2 id 2
   [*RouterA-map-e-instance-2] br-ipv6-address br_name
   [*RouterA-map-e-instance-2] map-rule bmr_name
   [*RouterA-map-e-instance-2] commit
   [~RouterA-map-e-instance-2] quit
   ```
5. Configure IP addresses of the user- and network-side interfaces on the device.
   
   
   ```
   [~RouterA] interface GigabitEthernet0/2/0
   [~RouterA-GigabitEthernet0/2/0] ipv6 enable
   [*RouterA-GigabitEthernet0/2/0] ipv6 address auto link-local
   [*RouterA-GigabitEthernet0/2/0] commit
   [~RouterA-GigabitEthernet0/2/0] quit
   [~RouterA] interface GigabitEthernet0/2/1
   [~RouterA-GigabitEthernet0/2/1] ip address 11.1.1.1 24
   [*RouterA-GigabitEthernet0/2/1] commit
   [~RouterA-GigabitEthernet0/2/1] quit
   [~RouterA] quit
   ```
6. Configure a user access domain.
   
   
   ```
   [~RouterA] radius-server group rd1
   [*RouterA-radius-rd1] radius-server authentication 192.168.7.249 1645 weight 0
   [*RouterA-radius-rd1] radius-server accounting 192.168.7.249 1646 weight 0
   [*RouterA-radius-rd1] radius-server shared-key YsHsjx_202206
   [*RouterA-radius-rd1] commit
   [~RouterA-radius-rd1] radius-server type plus11
   [~RouterA-radius-rd1] radius-server traffic-unit kbyte
   [~RouterA-radius-rd1] quit
   [~RouterA] aaa
   [~RouterA-aaa] authentication-scheme auth1
   [*RouterA-aaa-authen-auth1] authentication-mode radius
   [*RouterA-aaa-authen-auth1] commit
   [~RouterA-aaa-authen-auth1] quit
   [~RouterA-aaa] accounting-scheme acct1
   [*RouterA-aaa-accounting-acct1] accounting-mode radius
   [~RouterA-aaa-accounting-acct1] commit
   [~RouterA-aaa-accounting-acct1] quit
   [~RouterA] aaa
   [*RouterA-aaa] domain map-e
   [*RouterA-aaa-map-e] authentication-scheme auth1
   [*RouterA-aaa-map-e] accounting-scheme acct1
   [*RouterA-aaa-map-e] radius-server group rd1
   [*RouterA-aaa-map-e] commit
   [~RouterA-aaa-map-e] ipv6-pool pool1
   [~RouterA-aaa-map-e] quit
   [~RouterA-aaa] quit
   ```
7. Configure a DUID for the DHCPv6 server.
   
   
   ```
   [~RouterA] dhcpv6 duid llt
   [*RouterA] commit
   ```
8. Configure IPoEv6 access.
   
   
   ```
   [~RouterA] interface GigabitEthernet0/2/0
   [*RouterA-GigabitEthernet0/2/0] bas
   [*RouterA-GigabitEthernet0/2/0-bas] access-type layer2-subscriber default-domain authentication map-e
   [~RouterA-GigabitEthernet0/2/0-bas] authentication-method-ipv6 bind
   [*RouterA-GigabitEthernet0/2/0-bas] commit
   ```

#### Router A Configuration File

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
ipv6 prefix pre1 delegation
 map-rule bmr_name
ipv6 pool pool1 bas delegation
 prefix pre1
 option-s46 br-ipv6-address br_name
#
radius-server group rd1
 radius-server authentication 192.168.7.249 1645 weight 0
 radius-server accounting 192.168.7.249 1646 weight 0
 radius-server shared-key %^%#x*CgITP4C~;q,*+DEW'JBWe#)"Q&|7bX]b:Y<{w'%^%#
 radius-server type plus11
 radius-server traffic-unit kbyte
#
aaa
 authentication-scheme auth1
  authentication-mode radius
 accounting-scheme acct1
  accounting-mode radius
 domain map-e
  authentication-scheme auth1
  accounting-scheme acct1
  radius-server group rd1
  ipv6-pool pool1
#
dhcpv6 duid 0001000125a7625df063f9761497
#
interface GigabitEthernet0/2/0
 undo negotiation auto
 undo shutdown
 ipv6 enable
 ipv6 address auto link-local
 bas
  access-type layer2-subscriber default-domain authentication map-e
  authentication-method-ipv6 bind
#
interface GigabitEthernet0/2/1
 undo negotiation auto
 undo shutdown
 control-flap
 ip address 11.1.1.1 255.255.255.0
#
ipv6 route-static 2001:db8:1::1 48 2001:db8:2::1
#

```