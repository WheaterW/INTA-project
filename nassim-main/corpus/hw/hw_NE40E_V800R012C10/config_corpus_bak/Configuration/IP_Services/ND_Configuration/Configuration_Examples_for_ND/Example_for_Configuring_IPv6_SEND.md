Example for Configuring IPv6 SEND
=================================

This section provides an example for configuring IPv6 SEND.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365185__fig_dc_vrp_ipv6_cfg_003601), IPv6 SEND is configured on DeviceA. Assume that DeviceB is an attacker. When DeviceB sends messages to DeviceA, DeviceA regards them invalid and discards them.

**Figure 1** Configuring IPv6 SEND![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](images/fig_dc_vrp_ipv6_cfg_003601.png)

#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a CGA IPv6 address and a common IPv6 address on DeviceA.
2. Enable the strict security mode on an interface of DeviceA.
3. Configure an IPv6 address for an interface on DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* RSA key pair name
* Modifier value and security level of a CGA address
* CGA IPv6 address
* IPv6 address of DeviceB

#### Procedure

1. Configure a CGA IPv6 address on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [*DeviceA] rsa key-pair label test
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 security rsakey-pair test
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 security modifier sec-level 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address fe80::3 link-local cga
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::/64 cga
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1/64
   ```
2. Enable the strict security mode on an interface of DeviceA.
   
   
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 nd security strict
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
3. Configure an IPv6 address of DeviceB.
   
   
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
   [*DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address auto link-local
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
4. Verify the configuration.
   
   
   
   If the configuration is successful, you can check that the IPv6 addresses and IPv6 SEND have been configured and the interface status and IPv6 protocol status are up.
   
   # View information about GE 0/1/0 on DeviceA.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] display this ipv6 interface
   ```
   ```
   GigabitEthernet0/1/0 current state : UP 
   IPv6 protocol current state : UP 
   IPv6 is enabled, link-local address is FE80::3057:B5D6:6BD6:6CA8 
     Global unicast address(es):
      2001:db8:2::2092:84CE:827B:D5A4, subnet is 2001:db8:2::/64
      2001:db8:1::1, subnet is 2001:db8:1::/64
     Joined group address(es):
       FF02::1:FF7B:D5A4
       FF02::2
       FF02::1
       FF02::1:FFD6:6CA8
     MTU is 1500 bytes 
     ND DAD is enabled, number of DAD attempts: 1
     ND NUD is enabled, number of NUD attempts: 3
     ND NUD interval is 1000 milliseconds
     ND reachable time is 1200000 milliseconds
     ND stale time is 1200 seconds
     ND retransmit interval is 1000 milliseconds
     ND advertised reachable time is 0 milliseconds
     ND advertised retransmit interval is 0 milliseconds
     ND router advertisement max interval 600 seconds, min interval 200 seconds
     ND router advertisements live for 1800 seconds
     ND router advertisements hop-limit 64
     ND default router preference medium
     Hosts use stateless autoconfig for addresses
     ND Proxy is disabled
   ```
   
   # View the IPv6 SEND configuration on GE 0/1/0 of DeviceA.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] display ipv6 security interface gigabitethernet 0/1/0
   ```
   ```
    (L) : Link local address
    SEND information for the interface : GigabitEthernet0/1/0
   ----------------------------------------------------------------------------
    IPv6 address                                   PrefixLength Collision Count
   ----------------------------------------------------------------------------
    FE80::3057:B5D6:6BD6:6CA8 (L)                  10           0
    2001:db8:2::2092:84CE:827B:D5A4                64           0
   ----------------------------------------------------------------------------
    SEND sec value : 1
    SEND security modifier value : 2001:db8:1::1
    SEND RSA key label bound : test
    SEND ND minimum key length value : 512
    SEND ND maximum key length value : 2048
    SEND ND Timestamp delta value : 300
    SEND ND Timestamp fuzz value : 1
    SEND ND Timestamp drift value : 1
    SEND ND fully secured mode : enabled
   ```
   
   # View information about GE 0/1/0 on DeviceB.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0] display this ipv6 interface
   ```
   ```
   GigabitEthernet0/1/0 current state : UP 
   IPv6 protocol current state : UP 
   IPv6 is enabled, link-local address is FE80::2E0:E6FF:FE13:8100 
     Global unicast address(es):
       2001:db8:2::2, subnet is 2001:db8:2::/64
       2001:db8:1::2, subnet is 2001:db8:1::/64
     Joined group address(es):
       FF02::1:FF00:2
       FF02::2
       FF02::1
       FF02::1:FF13:8100
     MTU is 1500 bytes 
     ND DAD is enabled, number of DAD attempts: 1
     ND NUD is enabled, number of NUD attempts: 3
     ND NUD interval is 1000 milliseconds
     ND reachable time is 1200000 milliseconds
     ND stale time is 1200 seconds
     ND retransmit interval is 1000 milliseconds
     ND advertised reachable time is 0 milliseconds
     ND advertised retransmit interval is 0 milliseconds
     ND router advertisement max interval 600 seconds, min interval 200 seconds
     ND router advertisements live for 1800 seconds
     ND router advertisements hop-limit 64
     ND default router preference medium
     Hosts use stateless autoconfig for addresses
     ND Proxy is disabled
   ```
   
   # Ping the CGA link-local address of DeviceA from DeviceB. The ping fails because IPv6 SEND is configured on DeviceA.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0] ping ipv6 FE80::3057:B5D6:6BD6:6CA8 -i gigabitethernet 0/1/0
   ```
   ```
     PING FE80::3057:B5D6:6BD6:6CA8 : 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- FE80::3057:B5D6:6BD6:6CA8 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
       round-trip min/avg/max = 0/0/0 ms
                               
   ```
   
   # Ping the CGA global unicast address of DeviceA from DeviceB. The ping fails because IPv6 SEND is configured on DeviceA.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0] ping ipv6 2001:db8:2::2092:84CE:827B:D5A4
   ```
   ```
     PING 2001:db8:2::2092:84CE:827B:D5A4 : 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 2001:db8:2::2092:84CE:827B:D5A4 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
       round-trip min/avg/max = 0/0/0 ms
                                 
   ```
   
   # Ping the common global unicast address of DeviceA from DeviceB. The ping fails because IPv6 SEND is configured on DeviceA.
   
   ```
   [~DeviceB-GigabitEthernet0/1/0] ping ipv6 2001:db8:1::1
   ```
   ```
     PING 2001:db8:1::1 : 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 2001:db8:2::2092:84CE:827B:D5A4 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss
       round-trip min/avg/max = 0/0/0 ms
                                 
   ```
   
   # Disable IPv6 SEND on DeviceA. The ping from DeviceB to DeviceA is successful. The following part provides an example of pinging the CGA global unicast address of DeviceA.
   
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo ipv6 nd security strict
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ping ipv6 2001:db8:2::2092:84CE:827B:D5A4
   ```
   ```
     PING 2001:db8:2::2092:84CE:827B:D5A4 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:2::2092:84CE:827B:D5A4
       bytes=56 Sequence=1 hop limit=64  time = 1 ms
       Reply from 2001:db8:2::2092:84CE:827B:D5A4
       bytes=56 Sequence=2 hop limit=64  time = 20 ms
       Reply from 2001:db8:2::2092:84CE:827B:D5A4
       bytes=56 Sequence=3 hop limit=64  time = 1 ms
       Reply from 2001:db8:2::2092:84CE:827B:D5A4
       bytes=56 Sequence=4 hop limit=64  time = 1 ms
       Reply from 2001:db8:2::2092:84CE:827B:D5A4
       bytes=56 Sequence=5 hop limit=64  time = 1 ms
   
     --- 2001:db8:2::2092:84CE:827B:D5A4 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 1/4/20 ms
                                   
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  rsa key-pair label test
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 security rsakey-pair test
   ipv6 security modifier sec-level 1
   ipv6 address 2001:db8:2::/64 cga
   ipv6 address 2001:db8:1::1/64
   ipv6 address fe80::3 link-local cga
   ipv6 nd security strict
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
   ipv6 address 2001:db8:2::2/64
   ipv6 address 2001:db8:1::2/64
   ipv6 address auto link-local
  #
  return
  ```