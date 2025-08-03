Example for Configuring SA Message Filtering
============================================

Example for Configuring SA Message Filtering

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130623922__fig9472039125916), service data is transmitted in multicast mode on a network that is divided into three PIM-SM domains. Multicast source Source1 sends multicast data to multicast groups 225.1.1.0/30 and 226.1.1.0/30, and multicast source Source2 sends multicast data to the multicast group 227.1.1.0/30. HostA and HostB receive only multicast data sent to multicast groups 225.1.1.0/30 and 226.1.1.0/30, and HostC receives only multicast data sent to multicast groups 226.1.1.0/30 and 227.1.1.0/30.

**Figure 1** Network diagram of configuring SA message filtering![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001130783730.png)

#### Configuration Roadmap

Configure MSDP to implement multicast source information sharing across domains. Then, configure SA message filtering to ensure that receivers can only receive the corresponding multicast data.

1. Enable the multicast function and configure interface IP addresses on devices, and configure OSPF in each PIM-SM domain for intra-domain interconnection.
2. Enable PIM-SM on each interface, configure BSR boundaries to form PIM-SM domains, and enable IGMP on interfaces connected to hosts.
3. Configure Loopback0 interfaces on DeviceA, DeviceC, and DeviceD as the C-BSR and C-RP of their respective PIM-SM domains.
4. Set up MSDP peer relationships between RPs in PIM-SM domains. Establish peer relationships between DeviceA and DeviceC, and between DeviceC and DeviceD.
5. Configure the rules for filtering SA messages. Specifically, configure DeviceC not to forward SA messages related to Source1 (225.1.1.0/30) to DeviceD, and configure DeviceD not to create SA messages related to Source2.

#### Procedure

1. Enable the multicast function. Based on [Figure 1](#EN-US_TASK_0000001130623922__fig9472039125916), assign an IP address to each interface, and configure OSPF as a unicast routing protocol for interworking in each PIM-SM domain.
   
   
   
   # Enable the multicast function on DeviceA and configure interface IP addresses and masks. The configurations of other devices are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.1.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] ip address 10.1.2.1 24
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo portswitch
   [*DeviceA-100GE1/0/3] ip address 192.168.1.1 24
   [*DeviceA-100GE1/0/3] quit
   [~DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] ip address 1.1.1.1 255.255.255.255
   [*DeviceA-LoopBack0] quit
   [*DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 1.1.1.1 0.0.0.0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.2.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
2. Configure PIM-SM.
   
   
   
   # Enable PIM-SM on each interface. The following uses the configuration of DeviceA as an example. The configurations of other devices are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/1 
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] pim sm
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface loopback 0
   [*DeviceA-LoopBack0] pim sm
   [*DeviceA-LoopBack0] quit
   [*DeviceA] commit
   ```
3. Enable IGMP on the host-side interface. The following uses DeviceA as an example. The configurations of DeviceC and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1 
   [*DeviceA-100GE1/0/1] igmp enable
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA-100GE1/0/1] commit
   ```
4. Configure BSR boundaries and divide the PIM-SM domains.
   
   
   
   # Configure BSR boundaries on DeviceC. The configurations of DeviceA, DeviceB, and DeviceD are similar to the configuration of DeviceC. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] pim bsr-boundary
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/4
   [*DeviceC-100GE1/0/4] pim bsr-boundary
   [*DeviceC-100GE1/0/4] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] pim bsr-boundary
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
5. Configure C-BSRs and C-RPs.
   
   
   
   # Configure Loopback0 on DeviceA as a C-BSR and C-RP. The configurations of DeviceC and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA-pim] pim
   [*DeviceA-pim] c-bsr loopback0
   [*DeviceA-pim] c-rp loopback0
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```
6. Configure MSDP peers.
   
   
   
   # Configure an MSDP peer on DeviceA.
   
   ```
   [~DeviceA] msdp
   [*DeviceA-msdp] peer 192.168.1.2 connect-interface 100ge 1/0/1
   [*DeviceA-msdp] quit
   [*DeviceA] commit
   ```
   
   # Configure an MSDP peer on DeviceC.
   
   ```
   [~DeviceC] msdp
   [*DeviceC-msdp] peer 192.168.1.1 connect-interface 100ge 1/0/1
   [*DeviceC-msdp] peer 10.1.5.2 connect-interface 100ge 1/0/2
   [*DeviceC-msdp] quit
   [*DeviceC] commit
   ```
   
   # Configure an MSDP peer on DeviceD.
   
   ```
   [~DeviceD] msdp
   [*DeviceD-msdp] peer 10.1.5.1 connect-interface 100ge 1/0/2
   [*DeviceD-msdp] quit
   [*DeviceD] commit
   ```
7. Configure the rules for filtering SA messages.
   
   
   
   # Configure DeviceC not to forward SA messages related to Source1 (225.1.1.0/30) to DeviceD.
   
   ```
   [~DeviceC] acl number 3001
   [*DeviceC-acl4-advance-3001] rule deny ip source 10.1.3.100 0 destination 225.1.1.0 0.0.0.3
   [*DeviceC-acl4-advance-3001] rule permit ip source any destination any
   [*DeviceC-acl4-advance-3001] quit
   [*DeviceC] msdp
   [*DeviceC-msdp] peer 10.1.5.2 sa-policy export 3001
   [*DeviceC-msdp] quit
   [*DeviceC] commit
   ```
   
   # Configure DeviceD not to create SA messages related to Source2.
   
   ```
   [~DeviceD] acl number 2001
   [*DeviceD-acl4-basic-2001] rule deny source 10.1.6.100 0
   [*DeviceD-acl4-basic-2001] quit
   [*DeviceD] msdp
   [*DeviceD-msdp] import-source acl 2001
   [*DeviceD-msdp] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display msdp sa-cache** command to view information about (S, G) entries in the SA cache. The following example uses the command output on DeviceC and DeviceD.

```
[~DeviceC] display msdp sa-cache
MSDP Source-Active Cache Information of VPN instance: public net
 MSDP Total Source-Active Cache - 8 entries
 MSDP matched 8 entries

(10.1.3.100, 225.1.1.0)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ? 
 Uptime: 00:03:32, Expires: 00:05:28 

(10.1.3.100, 225.1.1.1)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ?
 Uptime: 00:03:32, Expires: 00:05:28

(10.1.3.100, 225.1.1.2)
 Origin RP: 10.1.1.1 
 Pro: BGP, AS: ?
 Uptime: 00:03:32, Expires: 00:05:28 

(10.1.3.100, 225.1.1.3)
 Origin RP: 10.1.1.1 
 Pro: BGP, AS: ?
 Uptime: 00:03:32, Expires: 00:05:28

(10.1.3.100, 226.1.1.0)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ? 
 Uptime: 00:03:32, Expires: 00:05:28

(10.1.3.100, 226.1.1.1)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ?
 Uptime: 00:03:32, Expires: 00:05:28

(10.1.3.100, 226.1.1.2)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ? 
 Uptime: 00:03:32, Expires: 00:05:28

(10.1.3.100, 226.1.1.3)
 Origin RP: 10.1.1.1 
 Pro: BGP, AS: ?
 Uptime: 00:03:32, Expires: 00:05:28

[~DeviceD] display msdp sa-cache
MSDP Source-Active Cache Information of VPN instance: public net
 MSDP Total Source-Active Cache - 4 entries
 MSDP matched 4 entries

(10.1.3.100, 226.1.1.0)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ?
 Uptime: 00:24:53, Expires: 00:05:06

(10.1.3.100, 226.1.1.1)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ? 
 Uptime: 00:24:53, Expires: 00:05:06

(10.1.3.100, 226.1.1.2)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ?
 Uptime: 00:24:53, Expires: 00:05:06

(10.1.3.100, 226.1.1.3)
 Origin RP: 10.1.1.1
 Pro: BGP, AS: ? 
 Uptime: 00:24:53, Expires: 00:05:06
```

The command output shows that the SA cache on DeviceC contains only multicast data of groups 225.1.1.0/30 and 226.1.1.0/30. The SA cache of DeviceD contains only multicast data of the group 226.1.1.0/30.


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.1.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  msdp
   peer 192.168.1.2 connect-interface 100GE1/0/3
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
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.2.2 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
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
  acl number 3001
   rule 5 deny ip source 10.1.3.100 0 destination 225.1.1.0 0.0.0.3 
   rule 10 permit ip 
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface  100GE1/0/4
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.5.1 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.4.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.4.0 0.0.0.255
    network 10.1.5.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.2.2.0 0.0.0.255
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  msdp
   peer 192.168.1.1 connect-interface 100GE1/0/3
   peer 10.1.5.2 connect-interface 100GE1/0/2
   peer 10.1.5.2 sa-policy export 3001
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
  acl number 2001
   rule 5 deny source 10.1.6.100 0 
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.1.5.2 255.255.255.0
   pim bsr-boundary 
   pim sm
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.1.6.1 255.255.255.0
   pim sm
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.1.7.1 255.255.255.0
   pim sm
   igmp enable
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   pim sm
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.5.0 0.0.0.255
    network 10.1.6.0 0.0.0.255
    network 10.1.7.0 0.0.0.255
  #
  pim
   c-bsr LoopBack0
   c-rp LoopBack0
  #
  msdp
   import-source acl 2001
   peer 10.1.5.1 connect-interface 100GE1/0/2
  #
  return
  ```