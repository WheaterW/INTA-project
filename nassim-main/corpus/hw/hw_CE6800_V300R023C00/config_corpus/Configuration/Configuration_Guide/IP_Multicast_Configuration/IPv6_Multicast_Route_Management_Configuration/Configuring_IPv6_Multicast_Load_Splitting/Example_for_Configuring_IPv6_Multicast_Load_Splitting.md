Example for Configuring IPv6 Multicast Load Splitting
=====================================================

Example for Configuring IPv6 Multicast Load Splitting

#### Networking Requirements

On an IPv6 PIM-SM network where multicast services are stable, configure the stable-preferred multicast load splitting policy so that multicast traffic can be distributed among multiple equal-cost routes for transmission. As shown in [Figure 1](#EN-US_TASK_0000001583800477__fig_dc_vrp_multicast_cfg_009701), there are three equal-cost routes from the device connected with HostA to the multicast source (Source). HostA needs to stably receive multicast data for an extended period of time from the source. An IPv6 load splitting policy needs to be configured to evenly distribute entries to equal-cost routes to implement load splitting among the equal-cost routes.

**Figure 1** Network diagram of configuring multicast load splitting![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.


  
![](figure/en-us_image_0000001583640765.png)

| Device | Interface | IP Address |
| --- | --- | --- |
| DeviceA | interface1 | 2001:db8:2001::2/64 |
| interface2 | 2001:db8:2002::1/64 |
| interface3 | 2001:db8:2003::1/64 |
| interface4 | 2001:db8:2004::1/64 |
| LoopBack0 | 2001:db8:2000::1/64 |
| DeviceB | interface1 | 2001:db8:2002::2/64 |
| interface2 | 2001:db8:2005::1/64 |
| DeviceC | interface1 | 2001:db8:2003::2/64 |
| interface2 | 2001:db8:2006::1/64 |
| DeviceD | interface1 | 2001:db8:2004::2/64 |
| interface2 | 2001:db8:2007::1/64 |
| DeviceE | interface1 | 2001:db8:2005::2/64 |
| interface2 | 2001:db8:2006::2/64 |
| interface3 | 2001:db8:2007::2/64 |
| interface4 | 2001:db8:3001::1/64 |

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IPv6 address to each interface involved.
2. Configure IPv6 IS-IS to implement interworking among all the devices and ensure that route costs are the same.
3. Enable the multicast function on all the devices, enable IPv6 PIM-SM on all the involved interfaces, and configure the loopback interface of DeviceA as an RP.
4. Configure stable-preferred multicast load splitting on DeviceE.
5. Configure static multicast groups on DeviceE's interface connected to the host.


#### Procedure

1. Assign an IPv6 address to each interface.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [~DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:2001::2/64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:2002::1/64
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ipv6 enable
   [*DeviceA-100GE1/0/3] ipv6 address 2001:db8:2003::1/64
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] undo portswitch
   [*DeviceA-100GE1/0/4] ipv6 enable
   [*DeviceA-100GE1/0/4] ipv6 address 2001:db8:2004::1/64
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] ipv6 enable
   [*DeviceA-LoopBack0] ipv6 address 2001:db8:2000::1/128
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, and DeviceE are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure IPv6 IS-IS to implement interworking among all the devices and ensure that route costs are the same.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [~DeviceA-isis-1] ipv6 enable
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] isis ipv6 enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] isis ipv6 enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] isis ipv6 enable 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] isis ipv6 enable 1
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] isis ipv6 enable 1
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, and DeviceE are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable the IPv6 multicast function on all the devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] pim ipv6 sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] pim ipv6 sm
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] pim ipv6 sm
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, and DeviceE are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
4. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceE to the host.
   
   ```
   [~DeviceE] interface 100ge 1/0/4
   [*DeviceE-100GE1/0/4] mld enable
   [*DeviceE-100GE1/0/4] quit
   [*DeviceE] commit
   ```
5. Configure DeviceA as an RP.
   
   # Configure Loopback0's address on DeviceA as the RP address.
   ```
   [~DeviceA] pim ipv6
   [*DeviceA-pim6] c-bsr 2001:db8:2000::1
   [*DeviceA-pim6] c-rp 2001:db8:2000::1
   [*DeviceA-pim6] commit
   ```
6. Configure stable-preferred multicast load splitting on DeviceE.
   
   
   ```
   [~DeviceE] multicast ipv6 load-splitting stable-preferred
   [*DeviceE] commit
   ```
7. Configure static multicast groups on the interface connected to the host.
   
   
   
   # Configure static multicast groups FF13::1 to FF13::3 on interface4 of DeviceE, which is connected to the host.
   
   ```
   [~DeviceE] interface 100ge 1/0/4
   [*DeviceE-100GE1/0/4] mld static-group ff13::1 inc-step-mask 128 number 3
   [*DeviceE-100GE1/0/4] quit
   [*DeviceE] commit
   ```

#### Verifying the Configuration

# Check the IPv6 PIM routing table on DeviceE. Source (2001:db8:2001::1/64) sends multicast data to multicast groups FF13::1 to FF13::3. HostA can receive the multicast data from the multicast source.

```
[~DeviceE] display pim ipv6 routing-table brief
 VPN-Instance: public net
 Total 3 (*, G) entries; 3 (S, G) entries

  00001.(*, FF13::1)
       Upstream interface:100GE1/0/3 
       Number of downstream:1
  00002.(FC00:0:0:1::2, FF13::1)
       Upstream interface:100GE1/0/3 
       Number of downstream:1
  00003.(*, FF13::2)
       Upstream interface: 100GE1/0/2 
       Number of downstream:1
  00004.(FC00:0:0:1::2, FF13::2)
       Upstream interface: 100GE1/0/2 
       Number of downstream:1
  00005.(*, FF13::3)
       Upstream interface: 100GE1/0/1
       Number of downstream:1
  00006.(FC00:0:0:1::2, FF13::3)
       Upstream interface: 100GE1/0/1
       Number of downstream:1
```

(\*, G) and (S, G) entries are evenly distributed to the three equal-cost routes, with the upstream interfaces of the routes being 100GE1/0/3, 100GE1/0/2, and 100GE1/0/1.

![](public_sys-resources/note_3.0-en-us.png) 

The load splitting algorithm processes (\*, G) and (S, G) entries separately using the same rule.



#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:1::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:2::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:3::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:4::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface Loopback0
   ipv6 enable
   ipv6 address FC00:1:1:1::1/128
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6
   c-bsr FC00:1:1:1::1
   c-rp FC00:1:1:1::1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:2::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:5::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:3::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:6::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:4::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:7::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  multicast ipv6 routing-enable
  multicast ipv6 load-splitting stable-preferred
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0005.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:5::2/64
   isis ipv6 enable 1
   pim ipv6 sm
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:6::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:7::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address FC00:0:0:8::1/64
   mld static-group FF13::1 inc-step-mask 128 number 3
   pim ipv6 sm
   isis ipv6 enable 1
  #
  return
  ```