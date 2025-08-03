Example for Configuring IPv6 PIM-SM in the ASM Model
====================================================

Example for Configuring IPv6 PIM-SM in the ASM Model

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001538445434__fig_dc_vrp_multicast_cfg_003701), multicast services are deployed. An IGP has been deployed on the network, unicast services are running properly, and the network has been connected to the Internet. It is required that hosts receive VOD information in multicast mode. You can configure a static RP, dynamic RP election, or both. If both a static RP and dynamic RP election are configured, dynamic RP election is preferentially used, with the static RP as a backup.

**Figure 1** Network diagram of configuring IPv6 PIM-SM in the ASM model![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, and 100GE 1/0/4, respectively.

![](figure/en-us_image_0000001538286086.png)


| Device | Interface | IPv6 Address |
| --- | --- | --- |
| DeviceA | 100GE1/0/1 | 2001:db8:1:2001::1/64 |
| 100GE1/0/2 | 2001:db8:1:3001::1/64 |
| 100GE1/0/3 | 2001:db8:1:2002::1/64 |
| DeviceB | 100GE1/0/1 | 2001:db8:1:2003::1/64 |
| 100GE1/0/2 | 2001:db8:1:4001::1/64 |
| DeviceC | 100GE1/0/1 | 2001:db8:1:2004::1/64 |
| 100GE1/0/2 | 2001:db8:1:4001::2/64 |
| DeviceD | 100GE1/0/1 | 2001:db8:1:2005::1/64 |
| 100GE1/0/2 | 2001:db8:1:2002::2/64 |
| 100GE1/0/3 | 2001:db8:1:5001::1/64 |
| 100GE1/0/4 | 2001:db8:1:6001::1/64 |
| DeviceE | 100GE1/0/1 | 2001:db8:1:2004::2/64 |
| 100GE1/0/2 | 2001:db8:1:2003::2/64 |
| 100GE1/0/3 | 2001:db8:1:2001::2/64 |
| 100GE1/0/4 | 2001:db8:1:2005::2/64 |



#### Configuration Precautions

During the configuration, note the following:

* To use a static RP, configure the same RP address on all devices.
* If users need to receive data from a specified multicast source, configure IPv6 PIM-SM in the SSM model. Ensure that all devices have the same SSM group address range.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses and an IPv6 unicast routing protocol for interfaces on each device.
2. Enable the IPv6 multicast function on all devices that need to provide multicast services and enable IPv6 PIM-SM on all the involved interfaces.
3. Enable MLD on the interfaces that directly connect devices to hosts.
4. Configure RPs. On an IPv6 PIM-SM network, an RP is the core of providing ASM services and a transit device for forwarding multicast data. Using a device that has a large number of multicast traffic branches, DeviceE in [Figure 1](#EN-US_TASK_0000001538445434__fig_dc_vrp_multicast_cfg_003701) for example, as an RP is recommended.
5. (Optional) Configure a BSR boundary on the interface that connects DeviceD to the Internet.

#### Procedure

1. Assign an IPv6 address to each device interface and configure an IPv6 unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the IPv6 multicast function on all devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Enable IPv6 PIM-SM, using DeviceE as an example. The configurations of other devices are similar to those shown in this example. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceE] multicast ipv6 routing-enable
   [*DeviceE] interface 100GE 1/0/1
   [*DeviceE-100GE1/0/1] undo portswitch
   [*DeviceE-100GE1/0/1] pim ipv6 sm
   [*DeviceE-100GE1/0/1] quit
   [*DeviceE] interface 100GE 1/0/2
   [*DeviceE-100GE1/0/2] undo portswitch
   [*DeviceE-100GE1/0/2] pim ipv6 sm
   [*DeviceE-100GE1/0/2] quit
   [*DeviceE] interface 100GE 1/0/3
   [*DeviceE-100GE1/0/3] undo portswitch
   [*DeviceE-100GE1/0/3] pim ipv6 sm
   [*DeviceE-100GE1/0/3] quit
   [*DeviceE] interface 100GE 1/0/4
   [*DeviceE-100GE1/0/4] undo portswitch
   [*DeviceE-100GE1/0/4] pim ipv6 sm
   [*DeviceE-100GE1/0/4] quit
   [*DeviceE] commit
   ```
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD, using DeviceA as an example.
   
   ```
   [~DeviceA] interface 100GE 1/0/2
   [~DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] mld enable
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
4. Configure RPs.
   
   
   
   # To use dynamic RP election, perform the following configurations on one or more devices in the PIM-SM domain. For example, on DeviceE, set the range of groups served by the RP and configure an interface as a C-BSR and C-RP.
   
   ```
   [~DeviceE] acl ipv6 number 2000
   [*DeviceE-acl6-basic-2000] rule permit source ff1e::1/64
   [*DeviceE-acl6-basic-2000] quit
   [*DeviceE] pim ipv6
   [*DeviceE-pim6] c-bsr 2001:db8:1:2003::2
   [*DeviceE-pim6] c-rp 2001:db8:1:2003::2 group-policy 2000 priority 0
   [*DeviceE-pim6] quit
   [*DeviceE] commit
   ```
   
   # Configure a static RP on DeviceE. The configurations of DeviceA, DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceE. For detailed configurations, see Configuration Scripts. You can specify **preferred** in the **static-rp** *rp-address* command to enable the static RP to be preferentially selected.
   
   ```
   [~DeviceE] pim ipv6
   [*DeviceE-pim6] static-rp 2001:db8:1:2005::2
   [*DeviceE-pim6] quit
   [*DeviceE] commit
   ```
5. (Optional) Configure a BSR boundary on the interface that connects DeviceD to the Internet.
   
   
   ```
   [~DeviceD] interface 100GE 1/0/4
   [~DeviceD-100GE1/0/4] undo portswitch
   [*DeviceD-100GE1/0/4] pim ipv6 bsr-boundary
   [*DeviceD-100GE1/0/4] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Run the **display pim ipv6 interface** command to view information about IPv6 PIM interfaces on each device. The following example shows the IPv6 PIM interface information on DeviceE.

```
<DeviceE> display pim ipv6 interface
VPN-Instance: public net
Interface  State NbrCnt HelloInt   DR-Pri     DR-Address
100GE1/0/1   up     1       30         1        2001:db8:1:2004::2
100GE1/0/2   up     1       30         1        2001:db8:1:2003::2
100GE1/0/3   up     1       30         1        2001:db8:1:2001::2
100GE1/0/4   up     1       30         1        2001:db8:1:2005::1
```

# Run the **display pim ipv6 bsr-info** command to check BSR information on each device. For example, BSR information on DeviceD and DeviceE is as follows (C-BSR information is also displayed on DeviceE):

```
<DeviceD> display pim ipv6 bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 2001:db8:1:2003::2
     Priority: 0
     Hash mask length: 126
     State: Accept Preferred
     Uptime: 02:08:57
     Expires: 00:01:15
     Next BSR message scheduled at: 00:01:42
     C-RP Count: 1
```
```
<DeviceE> display pim ipv6 bsr-info
 VPN-Instance: public net
 Elected AdminScope BSR Count: 0
 Elected BSR Address: 2001:db8:1:2003::2
     Priority: 0
     Hash mask length: 126
     State: Elected
     Uptime: 02:25:03
     Next BSR message scheduled at: 00:00:57
     C-RP Count: 1
 Candidate AdminScope BSR Count: 0
 Candidate BSR Address: 2001:db8:1:2003::2
     Priority: 0
     Hash mask length: 30
     State: Elected
     Wait to be BSR: 0
```

# Run the **display pim ipv6 rp-info** command to check RP information on each device. The RP information on DeviceD and DeviceE is as follows:

```
<DeviceD> display pim ipv6 rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: FF0E::1/64
     RP: 2001:db8:1:2003::2
     Priority: 0
     Uptime: 02:27:17
     Expires: 00:02:15
 PIM SM static RP Number:1
     Static RP: 2001:db8:1:2005::2
```
```
<DeviceE> display pim ipv6 rp-info
 VPN-Instance: public net
 PIM-SM BSR RP Number:1
 Group/MaskLen: FF0E::1/64
     RP: 2001:db8:1:2003::2 (local)
     Priority: 0
     Uptime: 02:27:27
     Expires: 00:02:03
 PIM SM static RP Number:1
     Static RP: 2001:db8:1:2005::2 (local)
```

# Run the **display pim ipv6 routing-table** command to view the IPv6 PIM routing table on each device. For example, the IPv6 PIM routing information on DeviceD and DeviceE is as follows:

```
<DeviceD> display pim ipv6 routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 2 (S, G) entries

 (2001:db8:1:6001::11, FF0E::1)
     RP: 2001:db8:1:2003::2
     Protocol: pim-sm, Flag: SPT ACT
     UpTime: 00:57:20
     Upstream interface: 100GE1/0/3, Refresh time: 00:57:20
         Upstream neighbor: NULL
         RPF prime neighbor: 2001:db8:1:6001::11
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol:  pim-sm, UpTime: 00:57:20, Expires: 00:03:02
```
```
<DeviceE> display pim ipv6 routing-table
 VPN-Instance: public net
 Total 1 (*, G) entry; 1 (S, G) entry

 (*, FF0E::)
     RP: 2001:db8:1:2003::2 (local)
     Protocol: pim-sm, Flag: WC
     UpTime: 00:21:40
     Upstream interface: register, Refresh time: 00:21:40
         Upstream neighbor: 2001:db8:1:2005::1
         RPF prime neighbor: 2001:db8:1:2005::1
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
  multicast ipv6 routing-enable
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2001::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:3001::1/64
   pim ipv6 sm
   mld enable
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2002::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6
   static-rp 2001:db8:1:2005::2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  multicast ipv6 routing-enable
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2003::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:4001::1/64
   pim ipv6 sm
   mld enable
   isis ipv6 enable 1
  #
  pim ipv6 
   static-rp 2001:db8:1:2005::2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  multicast ipv6 routing-enable
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2004::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:4001::2/64
   pim ipv6 sm
   mld enable
   isis ipv6 enable 1
  #
  #
  pim ipv6 
   static-rp 2001:db8:1:2005::2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  multicast ipv6 routing-enable
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0004.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2005::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2002::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:5001::1/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:6001::1/64
   pim ipv6 bsr-boundary
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6
   static-rp 2001:db8:1:2005::2
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule 5 permit source FF0E::1/64
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0005.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2004::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2003::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2001::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
   interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1:2005::2/64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6 
   static-rp 2001:db8:1:2005::2
   c-bsr 2001:db8:2003::2
   c-rp 2001:db8:2003::2 group-policy 2000
  #
  return
  ```