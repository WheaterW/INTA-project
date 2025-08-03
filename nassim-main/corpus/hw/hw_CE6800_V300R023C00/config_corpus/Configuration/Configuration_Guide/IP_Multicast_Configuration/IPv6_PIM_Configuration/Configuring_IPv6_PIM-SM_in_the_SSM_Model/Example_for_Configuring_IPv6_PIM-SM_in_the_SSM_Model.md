Example for Configuring IPv6 PIM-SM in the SSM Model
====================================================

Example for Configuring IPv6 PIM-SM in the SSM Model

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001589190289__fig_dc_vrp_multicast_cfg_004101), multicast services are deployed. An IGP has been deployed on this network, and unicast traffic forwarding is normal. It is required that hosts on the network join source-specific multicast groups.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


**Figure 1** Network diagram of configuring IPv6 PIM-SM in the SSM model  
![](figure/en-us_image_0000001589190393.png)

#### Configuration Precautions

During the configuration, ensure that the SSM group address ranges on all devices are the same.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses and an IPv6 unicast routing protocol for interfaces on each device.
2. Enable the IPv6 multicast function on all devices that need to provide multicast services and enable IPv6 PIM-SM on all the involved interfaces.
3. Enable MLD on the interfaces that directly connect devices to hosts.
4. Set the same SSM group address range on all devices.

#### Procedure

1. Assign an IPv6 address to each device interface and configure a unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the IPv6 multicast function on all devices and enable IPv6 PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] multicast ipv6 routing-enable
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] pim ipv6 sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] pim ipv6 sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Enable MLD on the interfaces connected to user hosts.
   
   
   
   # Enable MLD on the interface connecting DeviceC to hosts.
   
   ```
   [~DeviceC] interface 100GE 1/0/2
   [*DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] mld enable
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
4. Set an SSM group address range.
   
   
   
   # Set the SSM group address range to FF3E::1/64 on all devices. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] acl ipv6 number 2000
   [*DeviceA-acl6-basic-2000] rule permit source ff3e::1 64
   [*DeviceA-acl6-basic-2000] quit
   [*DeviceA] pim ipv6
   [*DeviceA-pim6] ssm-policy 2000
   [*DeviceA-pim6] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display pim ipv6 routing-table** command on devices to check their IPv6 PIM routing tables. The command outputs help determine whether HostA can receive data sent from the multicast source (2001:db8:3001::2/64) to the multicast group (FF3E::1/64). The command outputs on DeviceA and DeviceB are as follows:

```
<DeviceA> display pim ipv6 routing-table
VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (2001:db8:3001::2, FF3E::1)
     Protocol: pim-ssm, Flag: LOC
     UpTime: 00:02:13
     Upstream interface: 100GE1/0/2, Refresh time: 00:02:13
         Upstream neighbor: 2001:db8:3001::2
         RPF prime neighbor: 2001:db8:3001::2
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1
             Protocol:  mld, UpTime: 00:02:13, Expires: 00:03:17

<DeviceB> display pim ipv6 routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (2001:db8:3001::2, FF3E::1)
     Protocol: pim-ssm, Flag:
     UpTime: 00:09:15
     Upstream interface: 100GE1/0/1, Refresh time: 00:09:15
         Upstream neighbor: 2001:db8:2001::1
         RPF prime neighbor: 2001:db8:2001::1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol:  mld, UpTime: 00:09:15, Expires: 00:03:13
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast ipv6 routing-enable
  #
  acl ipv6 number 2000
   rule 5 permit source FF3E::1 64
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2001::1 64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3001::1 64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6
   ssm-policy 2000
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
  acl ipv6 number 2000
   rule 5 permit source FF3E::1 64
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2001::2 64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1001::1 64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  pim ipv6
   ssm-policy 2000
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
  acl ipv6 number 2000
   rule 5 permit source FF3E::1 64
  #
  isis 1
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1001::2 64
   pim ipv6 sm
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4001::1 64
   pim ipv6 sm
   mld enable
   isis ipv6 enable 1
  #
  pim ipv6
   ssm-policy 2000
  #
  return
  ```