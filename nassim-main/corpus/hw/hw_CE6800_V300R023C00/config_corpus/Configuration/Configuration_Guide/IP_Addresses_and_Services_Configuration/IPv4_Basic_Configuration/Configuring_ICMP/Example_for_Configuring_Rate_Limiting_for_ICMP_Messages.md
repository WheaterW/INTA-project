Example for Configuring Rate Limiting for ICMP Messages
=======================================================

Example for Configuring Rate Limiting for ICMP Messages

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130783584__fig4984175812), DeviceA and DeviceB are connected to PC1 and PC2, respectively. Attackers often send a large number of ICMP messages to attack the network, increasing network traffic and degrading device performance. To reduce network traffic and improve device performance, configure rate limiting for ICMP messages on DeviceA.

**Figure 1** Network diagram of configuring rate limiting for ICMP messages![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001130623830.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable rate limiting for ICMP messages.
2. Configure a rate threshold for ICMP messages.


#### Procedure

1. Assign IP addresses 192.168.1.2/24 and 192.168.1.1/24 to the 100GE 1/0/1 interfaces on DeviceA and DeviceB, respectively.
2. # Configure rate limiting for ICMP messages on DeviceA.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] undo icmp rate-limit disable
   [~DeviceA] icmp rate-limit threshold 10
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **ping** command on DeviceB. The command output shows that some reply messages are discarded, indicating that rate limiting takes effect.

```
[~DeviceB] ping -m 1 -c 1000 192.168.1.2
PING 192.168.1.2: 56  data bytes, press CTRL_C to break
    Reply from 192.168.1.2: bytes=56 Sequence=1 ttl=255 time=2 ms
    Reply from 192.168.1.2: bytes=56 Sequence=2 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=3 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=4 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=5 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=6 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=7 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=8 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=9 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=10 ttl=255 time=2 ms
    Request time out
    Reply from 192.168.1.2: bytes=56 Sequence=12 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=13 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=14 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=15 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=16 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=17 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=18 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=19 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=20 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=21 ttl=255 time=1 ms
    Request time out
    Reply from 192.168.1.2: bytes=56 Sequence=23 ttl=255 time=2 ms
    Reply from 192.168.1.2: bytes=56 Sequence=24 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=25 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=26 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=27 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=28 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=29 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=30 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=31 ttl=255 time=1 ms
    Reply from 192.168.1.2: bytes=56 Sequence=32 ttl=255 time=1 ms

  --- 192.168.1.2 ping statistics ---
    32 packet(s) transmitted
    30 packet(s) received
    6.25% packet loss
    round-trip min/avg/max = 1/1/2 ms
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  undo icmp rate-limit disable
  icmp rate-limit threshold 10
  #
  return
  ```