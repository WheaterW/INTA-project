Example for Configuring ARP Security
====================================

Example for Configuring ARP Security

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130622092__fig_dc_vrp_arp-sec_cfg_001901), Device is connected to the server through 100GE 1/0/3, to HostA and HostB in VLAN 10 through 100GE 1/0/1, and to HostC and HostD in VLAN 20 through 100GE 1/0/2. In this scenario, the following ARP attacks may occur:

* If the server is attacked, it may send a large number of packets with unreachable destination IP addresses.
* If HostA is attacked, it may send a large number of bogus ARP messages with different source IP addresses.
* If HostC is attacked, it may send a large number of ARP messages with fixed source IP addresses.
* If HostD is attacked, it may send a large number of ARP messages with unreachable destination IP addresses.

To prevent these attacks, configure ARP security on Device.

**Figure 1** Network diagram of configuring ARP security![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130781926.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure strict ARP learning globally so that the device learns only address information carried in the ARP reply messages in response to the ARP request messages that the device itself sends.
2. Configure ARP entry limiting on an interface to enable the device to limit the number of ARP entries that the interface can learn, preventing an ARP entry overflow.
3. Configure fixed ARP to prevent attackers from sending bogus ARP messages to modify ARP entries.
4. Configure rate limiting on ARP messages to limit the number of ARP messages processed per second, reducing system overheads.
5. Configure rate limiting on ARP Miss messages to limit the number of ARP Miss messages processed per second, reducing system overheads. In addition, ensure that the device can process a large number of ARP Miss messages from the server.

#### Data Preparation

To complete the configuration, you need the following data:

* Limit on the number of ARP entries that an interface can learn: 20
* Mode of fixed ARP: fixed-mac
* Rate limit for ARP messages: 15
* Rate limit for ARP Miss messages: 30 for HostD; 20 for other hosts; 50 for the server

#### Procedure

1. Configure IP addresses and routing protocols for the interfaces. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001130622092__p2087070106214100).
2. Configure strict ARP learning.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*Device] arp learning strict
   [*Device] commit
   ```
3. Configure an ARP entry limit for an interface.
   
   
   
   # Set an ARP entry limit to 20 for VLAN 10 on 100GE1/0/1.
   
   ```
   [~Device] interface 100ge1/0/1
   [~Device-100GE1/0/1] portswitch
   [*Device-100GE1/0/1] arp limit vlan 10 20
   [*Device-100GE1/0/1] quit
   [*Device] commit
   ```
   
   # Configure an ARP entry limit for 100GE 1/0/2 and 100GE 1/0/3. For configuration details, see the configuration of 100GE 1/0/1.
4. Configure fixed ARP.
   
   
   ```
   [~Device] arp anti-attack entry-check fixed-mac enable
   [*Device] commit
   ```
5. Configure rate limiting on ARP messages.
   
   
   ```
   [~Device] arp anti-attack rate-limit source-ip maximum 15
   [*Device] commit
   ```
6. Configure rate limiting on ARP Miss messages.
   
   
   ```
   [~Device] arp miss anti-attack rate-limit source-ip 10.10.10.10 maximum 30
   [*Device] arp miss anti-attack rate-limit source-ip maximum 20
   [*Device] arp miss anti-attack rate-limit source-ip 10.20.20.20 maximum 50
   [*Device] commit
   ```

#### Verifying the Configuration

# Run the **display arp learning strict** command to check the configuration of strict ARP learning.

```
<HUAWEI> display arp learning strict
 The global arp learning strict state:enable
------------------------------------------------------------
 Interface                           LearningStrictState
------------------------------------------------------------
------------------------------------------------------------
 Total:0     Force-enable:0     Force-disable:0
```

# Run the **display arp limit** command to check the ARP entry limit configured on 100GE 1/0/1.

```
<HUAWEI> display arp limit interface 100ge1/0/1
Interface                 VLAN     Limit        Learnt
---------------------------------------------------------------------------
 100GE1/0/1                 10       20            0
---------------------------------------------------------------------------
 Total:1 
```

# Run the **display arp miss anti-attack rate-limit** command to check the rate limits configured for ARP Miss messages.

```
<HUAWEI> display arp miss anti-attack rate-limit
Global ARP miss rate-limit  :  500 (0 means no limit)

VLAN ID          Suppress Rate(pps)(0 means no limit)
-------------------------------------------------------------------------------
All                 0
-------------------------------------------------------------------------------
Total: 0, spec of rate-limit configuration for VLAN is 1024.

Source IP        Suppress Rate(pps)(0 means no limit)
-------------------------------------------------------------------------------
10.10.10.10/32          30
10.20.20.20/32          50
Other                   20
-------------------------------------------------------------------------------
Total: 2, spec of rate-limit configuration for Source IP is 1024.
```

# Run the **display arp packet statistics** command to check ARP message statistics.

```
<HUAWEI> display arp packet statistics
ARP Packets Received
  Total:                      154333
  Learnt Count:                    8
  Discard For Entry Limit:         5
  Discard For Speed Limit:         0
  Discard For Proxy Suppress:      0
  Discard For Other:          151597
ARP Packets Sent 
  Total:                           0
  Request:                         0
  Reply:                           0
  Gratuitous ARP:                  0
ARP-Miss Message Received:  
  Total:                           0
  Discard For Speed Limit:         0
  Discard For Other:               3
```
#### Configuration Scripts

Device

```
#
sysname Device
#
vlan batch 10 20 30
#
arp learning strict
arp anti-attack entry-check fixed-mac enable
arp anti-attack rate-limit source-ip maximum 15
arp miss anti-attack rate-limit source-ip 10.10.10.10 maximum 30
arp miss anti-attack rate-limit source-ip maximum 20
arp miss anti-attack rate-limit source-ip 10.20.20.20 maximum 50
#
interface Vlanif10
 ip address 10.9.9.1 255.255.255.0
#
interface Vlanif20
 ip address 10.10.10.1 255.255.255.0
#
interface Vlanif30
 ip address 10.20.20.1 255.255.255.0
#
interface 100GE1/0/1
 arp limit vlan 10 20
#
interface 100GE1/0/2
 arp limit vlan 20 20
#
interface 100GE1/0/3
 arp limit vlan 30 20
#
return
```