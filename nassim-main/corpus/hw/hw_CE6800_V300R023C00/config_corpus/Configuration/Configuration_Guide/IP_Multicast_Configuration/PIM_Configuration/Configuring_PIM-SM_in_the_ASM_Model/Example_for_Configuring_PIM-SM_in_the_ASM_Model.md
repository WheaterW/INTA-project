Example for Configuring PIM-SM in the ASM Model
===============================================

Example for Configuring PIM-SM in the ASM Model

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001176743273__fig_dc_vrp_multicast_cfg_003701), multicast services are deployed. An IGP has been deployed on the network, unicast services are running properly, and the network has been connected to the Internet. It is required that hosts receive VOD information in multicast mode. You can configure a static RP, dynamic RP election, or both. If both a static RP and dynamic RP election are configured, dynamic RP election is preferentially used, with the static RP as a backup.

**Figure 1** Network diagram of configuring PIM-SM in the ASM model![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.

![](figure/en-us_image_0000001130623868.png)



#### Precautions

Note the following during the configuration:

* To use a static RP, configure the same RP address on all devices.
* If users need to receive data from a specified multicast source, configure PIM-SM in the SSM model, and ensure that all devices have the same SSM group address range.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device.
2. Enable the multicast function on all devices that need to provide multicast services and enable PIM-SM on all the involved interfaces.
3. Enable IGMP on the interfaces that directly connect devices to hosts.
4. Configure RPs. On a PIM-SM network, an RP is an RPT's root node. Using a device that has a large number of multicast traffic branches, DeviceE in [Figure 1](#EN-US_TASK_0000001176743273__fig_dc_vrp_multicast_cfg_003701) for example, as an RP is recommended.
5. (Optional) Configure a BSR boundary on the interface that connects DeviceD to the Internet.

#### Procedure

1. Assign an IP address to each device interface and configure a unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Enable PIM-SM, using DeviceE as an example. The configurations of other devices are similar to those shown in this example and are not mentioned here.
   
   ```
   [~DeviceE] multicast routing-enable
   [*DeviceE] interface 100GE 1/0/1
   [*DeviceE-100GE1/0/1] undo portswitch
   [*DeviceE-100GE1/0/1] pim sm
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100GE 1/0/2
   [*DeviceE-100GE1/0/2] undo portswitch
   [*DeviceE-100GE1/0/2] pim sm
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] interface 100GE 1/0/3
   [*DeviceE-100GE1/0/3] undo portswitch
   [*DeviceE-100GE1/0/3] pim sm
   [*DeviceE-100GE1/0/3] quit
   [*DeviceE] interface 100GE 1/0/4
   [*DeviceE-100GE1/0/4] undo portswitch
   [*DeviceE-100GE1/0/4] pim sm
   [*DeviceE-100GE1/0/4] quit
   [*DeviceE] commit
   ```
3. Enable IGMP on the interfaces connected to hosts.
   
   
   
   # Enable IGMP, using DeviceA as an example.
   
   ```
   [~DeviceA] interface 100GE 1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] igmp enable
   [*DeviceA-100GE1/0/2] igmp version 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
4. Configure RPs.
   
   
   
   # To use dynamic RP election, perform the following configurations on one or more devices in the PIM-SM domain. For example, on DeviceE, set the range of groups served by the RP and specify an interface for the C-BSR and C-RP.
   
   ```
   [~DeviceE] acl number 2000
   [*DeviceE-acl4-basic-2000] rule permit source 225.1.1.0 0.0.0.255
   [*DeviceE-acl4-basic-2000] quit
   [*DeviceE] pim
   [*DeviceE-pim] c-bsr 100GE 1/0/2
   [*DeviceE-pim] c-rp 100GE 1/0/2 group-policy 2000 priority 0
   [*DeviceE-pim] quit
   [*DeviceE] commit
   ```
   
   # Configure a static RP on DeviceE. The configurations of DeviceA, DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceE, and are not mentioned here. You can specify **preferred** in the **static-rp** *rp-address* command to enable the static RP to be preferentially selected.
   
   ```
   [~DeviceE] pim
   [*DeviceE-pim] static-rp 192.168.4.1
   [*DeviceE-pim] quit
   [*DeviceE] commit
   ```
5. (Optional) Configure a BSR boundary on the interface that connects DeviceD to the Internet.
   
   
   ```
   [~DeviceD] interface 100GE 1/0/4
   [~DeviceD-100GE1/0/4] undo portswitch
   [*DeviceD-100GE1/0/4] pim bsr-boundary
   [*DeviceD-100GE1/0/4] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display pim interface** command to view information about PIM interfaces on each device. The following example uses the PIM interface information on DeviceE.

```
<DeviceE> display pim interface
VPN-Instance: public net
Interface  State NbrCnt HelloInt   DR-Pri     DR-Address
100GE1/0/1   up     1       30         1        192.168.3.2
100GE1/0/2   up     1       30         1        192.168.2.2
100GE1/0/3   up     1       30         1        192.168.9.2
100GE1/0/4   up     1       30         1        192.168.4.2
```

# Run the **display pim bsr-info** command to check BSR information on each device. For example, BSR information on DeviceD and DeviceE is as follows (C-BSR information is also displayed on DeviceE):

```
<DeviceD> display pim bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 192.168.2.2
     Priority: 0
     Hash mask length: 30
     State: Accept Preferred
     Scope: Not scoped
     Uptime: 02:08:57
     Expires: 00:01:15
     C-RP Count: 1
```
```
<DeviceE> display pim bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 192.168.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: Not scoped
     Uptime: 02:25:03
     Next BSR message scheduled at: 00:00:57
     C-RP Count: 1
 Candidate AdminScope BSR Count: 0
 Candidate BSR Address: 192.168.2.2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Scope: Not scoped
     Wait to be BSR: 0
```

# Run the **display pim rp-info** command to check RP information on each device. The RP information on DeviceD and DeviceE is as follows:

```
<DeviceD> display pim rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 225.1.1.0/24
     RP: 192.168.2.2
     Priority: 0
     Uptime: 02:27:17
     Expires: 00:02:15
 PIM SM static RP Number:1
     Static RP: 192.168.4.1
```
```
<DeviceE> display pim rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: 225.1.1.0/24
     RP: 192.168.2.2 (local)
     Priority: 0
     Uptime: 02:27:27
     Expires: 00:02:03
 PIM SM static RP Number:1
     Static RP: 192.168.4.1 (local)
```

# Run the **display pim routing-table** command to view the PIM routing table on each device. For example, the PIM routing tables on DeviceD and DeviceE are as follows:

```
<DeviceD> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 2 (S, G) entries

 (10.110.5.100, 225.1.1.1)
     RP: 192.168.2.2
     Protocol: pim-sm, Flag: SPT LOC ACT
     UpTime: 00:57:20
     Upstream interface: 100GE1/0/3, Refresh time: 00:57:20
         Upstream neighbor: NULL
         RPF prime neighbor: 10.110.5.100
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol:  pim-sm, UpTime: 00:57:20, Expires: 00:03:02
```
```
<DeviceE> display pim routing-table
 VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entry

 (*, 225.1.1.1)
     RP: 192.168.2.2 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:21:40
     Upstream interface: register, Refresh time: 00:21:40
         Upstream neighbor: 192.168.4.2
         RPF prime neighbor: 192.168.4.2
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/3
             Protocol:  pim-sm, UpTime: 00:21:40, Expires: 00:02:43
```
#### Configuration Scripts

* DeviceA
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.9.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 2
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.110.1.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   static-rp 192.168.4.1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast routing-enable
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 2
   isis enable 1
  #
  pim
   static-rp 192.168.4.1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast routing-enable
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.2.2 255.255.255.0
   pim sm
   igmp enable
   igmp version 2
   isis enable 1
  #
  pim
   static-rp 192.168.4.1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast routing-enable
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.110.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ip address 10.110.5.1 255.255.255.0
   pim bsr-boundary
   pim sm
   isis enable 1
  #
  pim
   static-rp 192.168.4.1
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 225.1.1.0 0.0.0.255
  isis 1
   network-entity 10.0000.0000.0005.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.3.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 192.168.9.2 255.255.255.0
   pim sm
   isis enable 1
  #
   interface 100GE1/0/4
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   static-rp 192.168.4.1
   c-bsr 100GE 1/0/2
   c-rp 100GE 1/0/2 group-policy 2000
  #
  return
  ```