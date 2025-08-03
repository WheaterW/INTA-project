Example for Configuring IPv6 DNS
================================

This section provides an example for configuring IPv6 DNS.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364827__fig_dc_vrp_ipv6_dns_cfg_000801), DeviceA functions as an IPv6 DNS client. To allow DeviceA to use the domain name **huawei.com** to access the host with the IPv6 address 2001:db8:2::1/64 through an IPv6 DNS server, configure dynamic DNS.

In addition, to allow DeviceA to use the domain name to manage DeviceB and DeviceC, configure static IPv6 DNS entries for DeviceB and DeviceC on DeviceA.

**Figure 1** IPv6 DNS networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_ipv6_dns_cfg_000801.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure static IPv6 DNS entries.
2. Enable dynamic DNS.
3. Specify a DNS server IPv6 address.
4. Configure a domain name suffix.

#### Data Preparation

To complete the configuration, you need the following data:

* Domain names of DeviceB and DeviceC
* DNS server IPv6 address
* Domain name suffix

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure static IPv6 DNS entries.
   
   ```
   <DeviceA> system-view
   ```
   ```
   [~DeviceA] ipv6 host DeviceB 2001:db8:1::2
   ```
   ```
   [*DeviceA] ipv6 host DeviceC 2001:db8:2::3
   ```
   
   # Enable dynamic DNS.
   
   ```
   [*DeviceA] dns resolve
   ```
   
   # Specify a DNS server IPv6 address.
   
   ```
   [*DeviceA] dns server ipv6 2001:db8:3::2
   ```
   
   # Configure the domain name suffix **net**.
   
   ```
   [*DeviceA] dns domain net
   ```
   
   # Configure the domain name suffix **com**.
   
   ```
   [*DeviceA] dns domain com
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To implement DNS, a route from Device A to the IPv6 DNS server is also required. For details on how to configure routes, see *Configuration Guide - IP Routing*.
2. Verify the configuration.
   
   
   
   # Run the **ping ipv6 huawei.com** command on DeviceA. The ping operation is successful, and the resolved destination IPv6 address is 2001:db8:2::1.
   
   ```
   <DeviceA> ping ipv6 huawei.com
   ```
   ```
     Resolved Host ( huawei.com -> 2001:db8:2::1)
   ```
   ```
     PING huawei.com : 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 2001:db8:2::1: bytes=56 Sequence=1 ttl=126 time=6 ms
   ```
   ```
       Reply from 2001:db8:2::1: bytes=56 Sequence=2 ttl=126 time=4 ms
   ```
   ```
       Reply from 2001:db8:2::1: bytes=56 Sequence=3 ttl=126 time=4 ms
   ```
   ```
       Reply from 2001:db8:2::1: bytes=56 Sequence=4 ttl=126 time=4 ms
   ```
   ```
       Reply from 2001:db8:2::1: bytes=56 Sequence=5 ttl=126 time=4 ms
   
   ```
   ```
     --- huawei.com ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 4/4/6 ms
   ```
   
   # Run the **display ipv6 host** command on DeviceA. The command output shows the mapping between the host name and IPv6 address in static IPv6 DNS entries.
   
   ```
   <DeviceA> display ipv6 host
   ```
   ```
   Host                 Age        Flags  Address
   ```
   ```
   DeviceB              0          static 2001:db8:1::2
   ```
   ```
   DeviceC              0          static 2001:db8:2::3
   ```
   
   # Run the **display dns ipv6 dynamic-host** command on DeviceA. The command output shows dynamic IPv6 DNS entries in the domain name cache.
   
   ```
   <DeviceA> display dns ipv6 dynamic-host
   ```
   ```
   No   Domain Name           Ipv6address                              TTL          Alias
   ```
   ```
   1    huawei.com            2001:db8:2::1                            3579  
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The TTL field in the command output shows the lifetime of a dynamic IPv6 DNS entry, expressed in seconds.

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
   ipv6 host DeviceB 2001:db8:1::2
   ipv6 host DeviceC 2001:db8:2::3
  #
   dns resolve
   dns server ipv6 2001:db8:3::2
   dns domain net
   dns domain com
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ripng 1 enable
  #
  ripng 1
  #
  return
  
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ripng 1 enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ripng 1 enable
  #
  ripng 1
  #
  return
  
  ```
* DeviceC configuration file
  
  ```
  #
   sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 address 2001:db8:2::3/64
   ripng 1 enable
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 address 2001:db8:3::1/64
   ripng 1 enable
  #
  ripng 1
  #
  return
  
  ```