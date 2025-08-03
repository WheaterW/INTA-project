Example for Configuring an IPv6 Address Selection Policy Table
==============================================================

This section provides an example for configuring an IPv6 address selection policy table.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365145__fig_dc_vrp_ipv6_cfg_200201), the domain name (**huawei.com**) of Server A maps multiple IPv6 addresses. When DeviceA, as an IPv6 DNS client, accesses Server A by using the domain name (**huawei.com**), the DNS Server sends all IPv6 addresses of Server A to DeviceA. Then DeviceA queries the IPv6 address selection policy table to select a proper IPv6 address as the destination address of Server A.

**Figure 1** Configuring an IPv6 address selection policy table![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ipv6_cfg_200201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 address selection policy entries.
2. Configure dynamic IPv6 DNS services.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses on the interface of DeviceA
* Addresses, *label* values, and *precedence* values of IPv6 address selection policy entries
* IPv6 addresses of the DNS server

#### Procedure

1. Configure IPv6 address selection policy entries.
   
   
   
   # Configure IPv6 addresses for the interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface gigabitethernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address fe80::1 link-local
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:fed0:1::2 64
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::2 64
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:abcd::77 64
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure destination address selection policies.
   
   ```
   [~DeviceA] ipv6 address-policy 2001:db8:fed0:1::2 128 100 100
   ```
   ```
   [*DeviceA] ipv6 address-policy 2001:db8:1::1 128 100 100
   ```
   ```
   [*DeviceA] commit
   ```
2. Configure dynamic IPv6 DNS services.
   
   
   ```
   [~DeviceA] dns resolve
   ```
   ```
   [*DeviceA] dns server ipv6 2001:db8:abcd::1234
   ```
   ```
   [*DeviceA] dns domain com
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] quit
   ```
3. Verify the configuration.
   
   
   
   # Run the [**ping ipv6 huawei.com**](cmdqueryname=ping+ipv6+huawei.com) command on DeviceA. The command output shows that Server A can be pinged, with the destination IP address **2001:db8:1::1**.
   
   ```
   <DeviceA> ping ipv6 huawei.com
     Resolved Host (huawei.com -> 2001:db8:1::1)
     PING huawei.com : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:1::1: bytes=56 Sequence=1 ttl=126 time=6 ms
       Reply from 2001:db8:1::1: bytes=56 Sequence=2 ttl=126 time=4 ms
       Reply from 2001:db8:1::1: bytes=56 Sequence=3 ttl=126 time=4 ms
       Reply from 2001:db8:1::1: bytes=56 Sequence=4 ttl=126 time=4 ms
       Reply from 2001:db8:1::1: bytes=56 Sequence=5 ttl=126 time=4 ms
   
     --- huawei.com ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 4/4/6 ms
   ```
   
   # Run the **[**display ipv6 interface**](cmdqueryname=display+ipv6+interface+gigabitethernet) **gigabitethernet** 0/1/0** command on DeviceA. The command output shows information about the IPv6 address of GE 0/1/0.
   
   ```
   <DeviceA> display ipv6 interface gigabitethernet 0/1/0
   GigabitEthernet0/1/0 current state : UP  
   IPv6 protocol current state : UP 
   IPv6 is enabled, link-local address is FE80::1
     Global unicast address(es):
       2001:db8:fed0:1::2, subnet is 2001:db8:fed0:1::/64
       2001:db8:2::2, subnet is 2001:db8:2::/64
       2001:db8:abcd::77, subnet is 2001:db8:abcd::/64
     Joined group address(es):
       FF02::1:FF00:77
       FF02::2 
       FF02::1
       FF02::1:FF00:2
       FF02::1:FF00:1
     MTU is 1500 bytes
     ND DAD is enabled, number of DAD attempts: 1
     ND reachable time is 1200000 milliseconds 
     ND retransmit interval is 1000 milliseconds
     Hosts use stateless autoconfig for addresses
   ```
   
   # Run the **[**display ipv6 address-policy**](cmdqueryname=display+ipv6+address-policy+all) **all**** command on DeviceA. The command output shows information about address selection policy entries.
   
   ```
   <DeviceA> display ipv6 address-policy all
   ```
   ```
   Policy Table :
                Total:7
   -------------------------------------------------------------------------------
    Prefix     : ::                                      PrefixLength  : 0
    Precedence : 40                                      Label         : 1
    Default    : Yes
   
    Prefix     : 2001:db8:2                              PrefixLength  : 128
    Precedence : 50                                      Label         : 0
    Default    : Yes
   
    Prefix     : ::FFFF:0.0.0.0                          PrefixLength  : 96
    Precedence : 10                                      Label         : 4
    Default    : Yes
   
    Prefix     : 2001:db8:1::1                           PrefixLength  : 128
    Precedence : 100                                     Label         : 100
    Default    : No
   
    Prefix     : 2001::                                  PrefixLength  : 16
    Precedence : 30                                      Label         : 2
    Default    : Yes
   
    Prefix     : FC00::                                  PrefixLength  : 7
    Precedence : 20                                      Label         : 3
    Default    : Yes
   
    Prefix     : 2001:db8:fed0:1::2                      PrefixLength  : 128
    Precedence : 100                                     Label         : 100
    Default    : No
   
   -------------------------------------------------------------------------------
   ```

#### Configuration Files

* DeviceA configuration file
  ```
  #
   sysname DeviceA
  #
   dns resolve
   dns server ipv6 2001:db8:abcd::1234
   dns domain com
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:abcd::77/64
   ipv6 address 2001:db8:2::2/64
   ipv6 address FE80::1 link-local 
   ipv6 address 2001:db8:fed0:1::2/64
  #
   ipv6 address-policy 2001:db8:1::1 128 100 100
   ipv6 address-policy 2001:db8:fed0:1::2 128 100 100
  #
  return
  
  ```