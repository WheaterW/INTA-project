Example for Configuring IPv6 Addresses for Interfaces
=====================================================

This example shows how to configure IPv6 addresses for interfaces.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365142__fig_dc_vrp_ipv6_cfg_003101), DeviceA and DeviceB are connected through GE interfaces. To check the connectivity between the two interfaces, configure global unicast IPv6 addresses 2001:db8::1/32 and 2001:db8::2/32 for the GE interfaces.

**Figure 1** Configuring IPv6 addresses for interfaces![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ipv6_cfg_003101.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| DeviceA | GE 0/1/0 | 2001:db8::1/32 |
| DeviceB | GE 0/1/0 | 2001:db8::2/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable IPv6 on interfaces.
2. Configure global unicast IPv6 addresses for interfaces.

#### Data Preparation

To complete the configuration, you need global unicast IPv6 addresses of the interfaces.


#### Procedure

1. Configure global unicast IPv6 addresses for interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface GigabitEthernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8::1 32
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface GigabitEthernet 0/1/0
   [~DeviceB-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8::2 32
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   [*DeviceB-GigabitEthernet0/1/0] commit
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
2. Verify the configuration.
   
   
   
   If you can view the configured unicast global addresses and that the interfaces and the IPv6 protocol are in the Up state, it indicates that the configuration is successful.
   
   # Display the interface information of DeviceA.
   
   ```
   [~DeviceA] display ipv6 interface GigabitEthernet 0/1/0
   GigabitEthernet0/1/0 current state : UP
   IPv6 protocol current state : UP
   link-local address is FE80::C964:0:B8B6:1
     Global unicast address(es):
       2001:db8::1, subnet is 2001:db8::/32
     Joined group address(es):
       FF02::1:FF00:1
       FF02::1:FFB6:1
       FF02::2
       FF02::1
     MTU is 4470 bytes
     ND DAD is enabled, number of DAD attempts: 1
     ND reachable time is 1200000 milliseconds
     ND retransmit interval is 1000 milliseconds
     Hosts use stateless autoconfig for addresses
   ```
   
   # Display the interface information of DeviceB.
   
   ```
   [~DeviceB] display ipv6 interface GigabitEthernet 0/1/0
   GigabitEthernet0/1/0 current state : UP
   IPv6 protocol current state : UP
   link-local address is FE80::2D6F:0:7AF3:1
     Global unicast address(es):
       2001:db8::2, subnet is 2001:db8::/32
     Joined group address(es):
       FF02::1:FF00:2
       FF02::1:FFF3:1
       FF02::2
       FF02::1
     MTU is 4470 bytes
     ND DAD is enabled, number of DAD attempts: 1
     ND reachable time is 1200000 milliseconds
     ND retransmit interval is 1000 milliseconds
     Hosts use stateless autoconfig for addresses
   ```
   
   # Ping the link-local address of DeviceB from DeviceA. Note that you need to use the parameter **-i** to specify the interface corresponding to the link-local address.
   
   ```
   [~DeviceA] ping ipv6 fe80::2d6f:0:7af3:1 -i GigabitEthernet 0/1/0
     PING FE80::2D6F:0:7AF3:1 : 56  data bytes, press CTRL_C to break
       Reply from FE80::2D6F:0:7AF3:1
       bytes=56 Sequence=1 hop limit=64  time = 60 ms
       Reply from FE80::2D6F:0:7AF3:1
       bytes=56 Sequence=2 hop limit=64  time = 50 ms
       Reply from FE80::2D6F:0:7AF3:1
       bytes=56 Sequence=3 hop limit=64  time = 50 ms
       Reply from FE80::2D6F:0:7AF3:1
       bytes=56 Sequence=4 hop limit=64  time = 30 ms
       Reply from FE80::2D6F:0:7AF3:1
       bytes=56 Sequence=5 hop limit=64  time = 1 ms
   
     --- FE80::2D6F:0:7AF3:1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/38/60 ms
   ```
   
   # Ping the global unicast IPv6 address of DeviceB from DeviceA.
   
   ```
   [~DeviceA] ping ipv6 2001:db8::2
     PING 2001:db8::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8::2
       bytes=56 Sequence=1 hop limit=64  time = 30 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=2 hop limit=64  time = 50 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=3 hop limit=64  time = 50 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=4 hop limit=64  time = 20 ms
       Reply from 2001:db8::2
       bytes=56 Sequence=5 hop limit=64  time = 40 ms
   
     --- 2001:db8::2 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 20/38/50 ms
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  interface GigabitEthernet0/1/0
  undo shutdown
  ipv6 enable
  ipv6 address 2001:db8::1/32
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  interface GigabitEthernet0/1/0
  undo shutdown
  ipv6 enable
  ipv6 address 2001:db8::2/32
  #
  return
  ```