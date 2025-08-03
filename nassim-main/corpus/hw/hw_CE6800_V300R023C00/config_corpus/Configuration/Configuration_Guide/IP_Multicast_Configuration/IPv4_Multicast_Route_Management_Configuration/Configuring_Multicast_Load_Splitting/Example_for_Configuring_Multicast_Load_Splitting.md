Example for Configuring Multicast Load Splitting
================================================

Example for Configuring Multicast Load Splitting

#### Networking Requirements

On a PIM-SM network where multicast services are stable, configure the stable-preferred multicast load splitting policy so that multicast traffic can be distributed among multiple equal-cost routes for transmission. As shown in [Figure 1](#EN-US_TASK_0000001176662523__fig_dc_vrp_multicast_cfg_009701), there are three equal-cost routes from the device connected with HostA to the multicast source (Source). HostA needs to stably receive multicast data for an extended period of time from the source. To evenly distribute entries to equal-cost routes, a multicast load splitting policy is required so that load balancing among the equal-cost routes can be implemented.

**Figure 1** Network diagram of configuring multicast load splitting![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001216407038.png "Click to enlarge")
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces.
2. Configure IS-IS to implement interworking among all the devices and ensure that route costs are the same.
3. Enable the multicast function on all the devices, enable PIM-SM on all the involved interfaces, and configure the loopback interface of DeviceA as an RP.
4. Configure stable-preferred multicast load splitting on DeviceE.
5. Configure the host-facing interface of DeviceF to statically join the multicast groups.


#### Procedure

1. Assign IP addresses to interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface 100GE 1/0/1
   [~DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.110.1.2 255.255.255.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 192.168.1.1 255.255.255.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 192.168.2.1 255.255.255.0
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] undo portswitch
   [*DeviceA-100GE1/0/4] ip address 192.168.3.1 255.255.255.0
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
2. Configure IS-IS to implement interworking among all the devices and ensure that route costs are the same.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   [*DeviceA-isis-1] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] isis enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] isis enable 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] isis enable 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] isis enable 1
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] isis enable 1
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
3. Enable the multicast function on all the devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] pim sm
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface Loopback 0
   [*DeviceA-LoopBack0] pim sm
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
   
   The configurations of DeviceB, DeviceC, DeviceD, DeviceE, and DeviceF are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
4. Enable IGMP on the interface connecting to the host.
   
   
   
   # Enable IGMP on the interface connecting DeviceF to the host.
   
   ```
   [~DeviceF] interface 100GE 1/0/1
   [*DeviceF-100GE1/0/1] igmp enable
   [*DeviceF-100GE1/0/1] quit
   [*DeviceF] commit
   ```
5. Configure DeviceA as an RP.
   
   # Configure Loopback0's address on DeviceA as the RP address.
   ```
   [~DeviceA] pim
   [*DeviceA-pim] c-bsr loopback 0
   [*DeviceA-pim] c-rp loopback 0
   [*DeviceA-pim] commit
   ```
6. Configure stable-preferred multicast load splitting on DeviceE.
   
   
   ```
   [~DeviceE] multicast load-splitting stable-preferred
   [*DeviceE] commit
   ```
7. Configure host-facing interfaces to statically join multicast groups.
   
   
   
   # Configure 100GE1/0/1 that connects DeviceF to the host to statically join multicast groups 225.1.1.1 to 225.1.1.3.
   
   ```
   [~DeviceF] interface 100GE 1/0/1
   [*DeviceF-100GE1/0/1] igmp static-group 225.1.1.1 inc-step-mask 32 number 3
   [*DeviceF-100GE1/0/1] quit
   [*DeviceF] commit
   ```

#### Verifying the Configuration

# Check the PIM routing table on DeviceE. Source (10.110.1.1/24) sends multicast data to multicast groups 225.1.1.1 to 225.1.1.3. HostA can receive the multicast data from the multicast source.

```
[~DeviceE] display pim routing-table brief
 VPN-Instance: public net
 Total 3 (*, G) entries; 3 (S, G) entries

 Entries                                Upstream interface       NDwnstrms
 (*, 225.1.1.1)                         100GE1/0/3                 1
 (10.110.1.1, 225.1.1.1)                100GE1/0/3                 1
 (*, 225.1.1.2)                         100GE1/0/2                 1
 (10.110.1.1, 225.1.1.2)                100GE1/0/2                 1
 (*, 225.1.1.3)                         100GE1/0/1                 1
 (10.110.1.1, 225.1.1.3)                100GE1/0/1                 1

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
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.110.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface Loopback0
   ip address 1.1.1.1 255.255.255.255
   pim sm
   isis enable 1
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.5.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.6.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  multicast routing-enable
  multicast load-splitting stable-preferred
  #
  isis 1
   network-entity 10.0000.0000.0005.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   isis enable 1
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.5.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.6.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 192.168.7.1 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  multicast routing-enable
  #
  isis 1
   network-entity 10.0000.0000.0006.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.110.2.2 255.255.255.0
   pim sm
   igmp enable
   igmp static-group 225.1.1.1 inc-step-mask 32 number 3
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.7.2 255.255.255.0
   pim sm
   isis enable 1
  #
  return
  ```