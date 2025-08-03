Example for Configuring Dynamic ND
==================================

Example for Configuring Dynamic ND

#### Prerequisites

The link-local address and global EUI-64 unicast address of the PC have been obtained.

* Link-local address of the PC: fe80::2e0:4cff:fe77:a1b6
* Global EUI-64 unicast address of the PC: 2001:db8::78b3:4397:c0c4:f078

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176662043__fig_dc_vrp_ipv6_cfg_200701), DeviceA is connected to the PC through the interface 100GE 1/0/1. To implement interworking, configure dynamic ND with a link-local unicast address and global EUI-64 unicast address specified.

**Figure 1** Configuring dynamic ND  
![](figure/en-us_image_0000001176662097.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a link-local unicast address and global EUI-64 unicast address on the interface 100GE 1/0/1.
2. Configure a prefix to be carried in RA messages on the interface 100GE 1/0/1 and enable RA message advertisement.

#### Procedure

1. Configure a link-local unicast address on an interface. After the [**ipv6 enable**](cmdqueryname=ipv6+enable) command is run on the interface, the system automatically generates a link-local address for the interface.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] undo shutdown
   [*DeviceA-100GE1/0/1] ipv6 enable
   ```
2. Configure a global EUI-64 unicast address and a prefix to be carried in RA messages on the interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The PC can automatically obtain the prefix in RA messages from DeviceA only after the prefix is configured and RA message advertisement is enabled on DeviceA.
   
   ```
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8::/32 eui-64
   [*DeviceA-100GE1/0/1] ipv6 nd ra prefix 2001:db8::/32 1000 1000
   [*DeviceA-100GE1/0/1] ipv6 nd ra halt disable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

If configurations are successful, you can view the configured link-local unicast address and global EUI-64 unicast address and find that the interface and IPv6 are both up.

# Check the interface information of DeviceA.

```
[*DeviceA] interface 100ge 1/0/1
[~DeviceA-100GE1/0/1] display this ipv6 interface
100GE1/0/1 current state : UP
IPv6 protocol current state : UP
IPv6 is enabled, link-local address is FE80::2E0:FCFF:FE7D:A497
  Global unicast address(es):
    2001:db8::2E0:FCFF:FE7D:A497, subnet is 2001:db8::/32
  Joined group address(es):
    FF02::1:FF7D:A497
    FF02::2
    FF02::1
  MTU is 1500 bytes
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 1200000 milliseconds
  ND retransmit interval is 1000 milliseconds
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND router advertisement max interval 600 seconds, min interval 200 seconds
  ND router advertisements live for 1800 seconds
  Hosts use stateless autoconfig for addresses    
```

# Ping the link-local address of the PC from DeviceA. The **-i** parameter specifies the interface corresponding to the link-local address.

```
[~DeviceA-100GE1/0/1] ping ipv6 fe80::2e0:4cff:fe77:a1b6 -i 100ge 1/0/1
PING FE80::2E0:4CFF:FE77:A1B6: 56 data bytes, press CTRL_C to break
  Reply from FE80::2E0:4CFF:FE77:A1B6
  bytes=56 Sequence=1 hop limit=64 time = 60 ms
  Reply from FE80::2E0:4CFF:FE77:A1B6
  bytes=56 Sequence=2 hop limit=64 time = 50 ms
  Reply from FE80::2E0:4CFF:FE77:A1B6
  bytes=56 Sequence=3 hop limit=64 time = 50 ms
  Reply from FE80::2E0:4CFF:FE77:A1B6
  bytes=56 Sequence=4 hop limit=64 time = 30 ms
  Reply from FE80::2E0:4CFF:FE77:A1B6
  bytes=56 Sequence=5 hop limit=64 time = 1 ms
--- FE80::2E0:4CFF:FE77:A1B6 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 1/38/60 ms
```

# Ping the global EUI-64 unicast address of the PC from DeviceA.

```
[~DeviceA-100GE1/0/1] ping ipv6 2001:db8::78b3:4397:c0c4:f078
PING 2001:db8::78B3:4397:C0C4:F078 : 56 data bytes, press CTRL_C to break
  Reply from 2001:db8::78B3:4397:C0C4:F078
  bytes=56 Sequence=1 hop limit=64 time = 30 ms
  Reply from 2001:db8::78B3:4397:C0C4:F078
  bytes=56 Sequence=2 hop limit=64 time = 50 ms
  Reply from 2001:db8::78B3:4397:C0C4:F078
  bytes=56 Sequence=3 hop limit=64 time = 50 ms
  Reply from 2001:db8::78B3:4397:C0C4:F078
  bytes=56 Sequence=4 hop limit=64 time = 20 ms
  Reply from 2001:db8::78B3:4397:C0C4:F078
  bytes=56 Sequence=5 hop limit=64 time = 40 ms
--- 2001:db8::78B3:4397:C0C4:F078 ping statistics ---
  5 packet(s) transmitted
  5 packet(s) received
  0.00% packet loss
  round-trip min/avg/max = 20/38/50 ms
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 nd ra prefix 2001:db8::/32 1000 1000
   ipv6 address 2001:db8::/32 eui-64
   ipv6 nd ra halt disable
  #
  return
  ```