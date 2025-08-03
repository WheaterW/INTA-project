Example for Configuring IPv6 Neighbor Discovery
===============================================

This section provides an example for configuring IPv6 neighbor discovery.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172365182__fig_dc_vrp_ipv6_cfg_200701), DeviceA is directly connected to the PC by GE 0/1/0.

**Figure 1** Configuring IPv6 neighbor discovery  
![](images/fig_dc_vrp_ipv6_cfg_200701.png)

#### Precautions

None

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a link-local unicast address and global EUI-64 unicast addresses on GE 0/1/0.
2. Configure a prefix to be carried in RA messages on GE 0/1/0 and enable RA message advertisement.


#### Data Preparation

To complete the configuration, you need the following data:

* Local unicast addresses of the link and global EUI-64 on GE 0/1/0
* RA prefix message to be advertised

#### Procedure

1. Configure a link-local unicast address on GE 0/1/0. After the [**ipv6 enable**](cmdqueryname=ipv6+enable) command is run on the interface, the system automatically generates a link-local address for the interface.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address auto link-local
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
2. Configure a global EUI-64 unicast address and a prefix to be carried in RA messages on GE 0/1/0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The PC can automatically obtain the prefix in RA messages only after the prefix is configured and RA message advertisement is enabled on DeviceA.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8::/32 eui-64
   [*DeviceA-GigabitEthernet0/1/0] ipv6 nd ra prefix 2001:db8::/32 1000 1000
   [*DeviceA-GigabitEthernet0/1/0] undo ipv6 nd ra halt
   [*DeviceA-GigabitEthernet0/1/0] commit
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
3. Verify the configuration.
   
   
   
   If configurations are successful, you can view the configured link-local unicast address and global EUI-64 unicast address and find that GE 0/1/0 and IPv6 are both up.
   
   # Display information about DeviceA's interface.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] display this ipv6 interface
   GigabitEthernet0/1/0 current state : UP
   IPv6 protocol current state : UP
   IPv6 is enabled, link-local address is FE80::2E0:FCFF:FE7D:A497
     Global unicast address(es):
       2001:db8::2E0:FCFF:FE7D:A497, subnet is 2001:db8::/64
     Joined group address(es):
       FF02::1:FF7D:A497
       FF02::2
       FF02::1
     MTU is 1500 bytes
     ND DAD is enabled, number of DAD attempts: 1
     ND NUD is enabled, number of NUD attempts: 3
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
   
   # Display the PC information.
   
   ```
   GigabitEthernet adapter 1:
   
           Connection-specific DNS Suffix  . :
           Description . . . . . . . . . . . : Realtek RTL8139 Family PCI Fast Ethernet NIC #2
           Physical Address. . . . . . . . . : 00-E0-FC-77-A1-B6
           Dhcp Enabled. . . . . . . . . . . : No
           IP Address. . . . . . . . . . . . : 10.1.1.33
           Subnet Mask . . . . . . . . . . . : 255.0.0.0
           IP Address. . . . . . . . . . . . : 2001:db8::78b3:4397:c0c4:f078
           IP Address. . . . . . . . . . . . : 2001:db8::2e0:4cff:fe77:a1b6
           IP Address. . . . . . . . . . . . : fe80::2e0:4cff:fe77:a1b6%6
           Default Gateway . . . . . . . . . : fe80::288:ff:fe10:b%6
           DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                               fec0:0:0:ffff::2%1
                                               fec0:0:0:ffff::3%1
   ```
   
   # Ping the link-local address of the PC from DeviceA. The **-i** parameter specifies the interface corresponding to the link-local address.
   
   ```
   [~DeviceA-GigabitEthernet0/1/0] ping ipv6 fe80::2e0:4cff:fe77:a1b6 -i gigabitethernet0/1/0
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
   [~DeviceA-GigabitEthernet0/1/0] ping ipv6 2001:db8::78b3:4397:c0c4:f078
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

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address auto link-local
   ipv6 nd ra prefix 2001:db8::/32 1000 1000
   ipv6 address 2001:db8::/32 eui-64
   undo ipv6 nd ra halt
  #
  return
  ```