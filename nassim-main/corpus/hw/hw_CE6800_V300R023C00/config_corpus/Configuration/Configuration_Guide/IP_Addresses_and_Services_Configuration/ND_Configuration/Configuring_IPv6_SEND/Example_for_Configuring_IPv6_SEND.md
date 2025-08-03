Example for Configuring IPv6 SEND
=================================

Example for Configuring IPv6 SEND

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130782292__fig_dc_vrp_ipv6_cfg_003601), DeviceA and DeviceB communicate using IPv6. Assume that DeviceB is an attacker. To enable DeviceA to discard messages received from DeviceB, configure IPv6 SEND on DeviceA.

**Figure 1** Network diagram of configuring IPv6 SEND![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001176742101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a CGA IPv6 address and a common IPv6 address for DeviceA's interface 1.
2. Enable the strict security mode on DeviceA's interface 1.
3. Configure IPv6 addresses for DeviceB's interface 1.

#### Procedure

1. Configure a CGA IPv6 address and a common IPv6 address for DeviceA's interface 1.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] rsa key-pair label huawei
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 security rsakey-pair huawei
   [*DeviceA-100GE1/0/1] ipv6 security modifier sec-level 1
   [*DeviceA-100GE1/0/1] ipv6 address fe80::3 link-local cga
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:2::/64 cga
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1/64
   [*DeviceA-100GE1/0/1] [commit](cmdqueryname=commit)
   ```
2. Enable the strict security mode on DeviceA's interface 1.
   
   
   ```
   [*DeviceA-100GE1/0/1] ipv6 nd security strict
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Configure IPv6 addresses for DeviceB's interface 1.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceB] interface 100ge 1/0/1
   [~DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address auto link-local
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:2::2/64
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1::2/64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

If the configuration is successful, you can check that the IPv6 addresses and IPv6 SEND have been configured and the interface status and IPv6 protocol status are up.

# Check information about DeviceA's 100ge 1/0/1.

```
[*DeviceA] interface 100ge 1/0/1
[~DeviceA-100ge1/0/1] display this ipv6 interface
100ge1/0/1 current state : UP
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
  ND RAs are halted 
  ND Proxy is disabled
```

# Check the IPv6 SEND configuration on DeviceA's 100ge 1/0/1.

```
[~DeviceA-1/0/1] display ipv6 security interface 100ge 1/0/1
 (L) : Link local address
 SEND: Security ND
 SEND information for the interface : 100ge1/0/1
----------------------------------------------------------------------------
 IPv6 address                                   PrefixLength Collision Count
----------------------------------------------------------------------------
 FE80::3057:B5D6:6BD6:6CA8 (L)                  10           0
 2001:db8:2::2092:84CE:827B:D5A4                64           0
----------------------------------------------------------------------------
 SEND sec value                     : 1
 SEND security modifier value       : 2001:db8:3::1
 SEND RSA key label bound           : huawei
 SEND ND minimum key length value   : 512
 SEND ND maximum key length value   : 2048
 SEND ND Timestamp delta value      : 300
 SEND ND Timestamp fuzz value       : 1
 SEND ND Timestamp drift value      : 1
 SEND ND fully secured mode         : enabled
```

# Check information about DeviceB's 100ge 1/0/1.

```
[*DeviceB] interface 100ge 1/0/1
[~DeviceB-100ge1/0/1] display this ipv6 interface
100GE1/0/1 current state : UP
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
  ND RAs are halted 
  ND Proxy is disabled
```

# Ping the CGA link-local address of DeviceA from DeviceB. The ping fails because IPv6 SEND is configured on DeviceA.

```
[~DeviceB-1/0/1] ping ipv6 FE80::3057:B5D6:6BD6:6CA8 -i 100ge 1/0/1
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
[~DeviceB-100GE1/0/1 ] ping ipv6 2001:db8:2::2092:84CE:827B:D5A4
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
[~DeviceB-100GE1/0/1 ] ping ipv6 2001:db8:1::1
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

# Disable the strict security mode on DeviceA, and ping DeviceA's IPv6 address from DeviceB. The ping is successful. The following provides an example of pinging the CGA global unicast address of DeviceA.

```
[~DeviceA-100GE1/0/1 ] undo ipv6 nd security strict
[*DeviceB-100GE1/0/1 ] [commit](cmdqueryname=commit)
```
```
[*DeviceB-100GE1/0/1 ] ping ipv6 2001:db8:2::2092:84CE:827B:D5A4
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
#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  rsa key-pair label huawei
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 security rsakey-pair huawei
   ipv6 security modifier sec-level 1
   ipv6 address 2001:db8:2::/64 cga
   ipv6 address 2001:db8:1::1/64
   ipv6 address fe80::3 link-local cga
   ipv6 nd security strict
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ipv6 address 2001:db8:1::2/64
   ipv6 address auto link-local
  #
  return
  ```