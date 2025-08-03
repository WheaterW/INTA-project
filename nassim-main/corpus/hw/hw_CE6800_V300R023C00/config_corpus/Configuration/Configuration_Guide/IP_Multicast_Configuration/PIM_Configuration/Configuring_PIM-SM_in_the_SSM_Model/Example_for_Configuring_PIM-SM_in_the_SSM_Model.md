Example for Configuring PIM-SM in the SSM Model
===============================================

Example for Configuring PIM-SM in the SSM Model

#### Networking Requirements

On the ISP network shown in [Figure 1](#EN-US_TASK_0000001176743303__fig_dc_vrp_multicast_cfg_004101), multicast services are deployed. An IGP has been deployed on this network, and unicast traffic forwarding is normal. It is required that hosts on the network join source-specific multicast groups.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


**Figure 1** Network diagram of configuring PIM-SM in the SSM model  
![](figure/en-us_image_0000001130623944.png)

#### Precautions

During the configuration, ensure that the SSM group address ranges on all devices are the same.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses and a unicast routing protocol for interfaces on each device.
2. Enable the multicast function on all devices that need to provide multicast services and enable PIM-SM on all the involved interfaces.
3. Enable IGMP on the interfaces that directly connect devices to hosts.
4. Set the same SSM group address range on all devices.

#### Procedure

1. Assign an IP address to each device interface and configure a unicast routing protocol. For detailed configurations, see Configuration Scripts.
2. Enable the multicast function on all devices and enable PIM-SM on all the involved interfaces.
   
   
   
   # Configure DeviceA. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA, and are not mentioned here.
   
   ```
   [~DeviceA] multicast routing-enable
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] undo portswitch
   [*DeviceA-100GE1/0/2] pim sm
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] pim sm
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
3. Enable IGMP on the interfaces directly connected to hosts.
   
   
   
   # Enable IGMP on the interface connecting DeviceC to a host and set the IGMP version to 3.
   
   ```
   [~DeviceC] interface 100GE 1/0/2
   [~DeviceC-100GE1/0/2] undo portswitch
   [*DeviceC-100GE1/0/2] igmp enable
   [*DeviceC-100GE1/0/2] igmp version 3
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
4. Set an SSM group address range.
   
   
   
   # Set the SSM group address range to 232.1.1.0/24 on all devices. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA, and are not mentioned here.
   
   ```
   [~DeviceA] acl number 2000
   [*DeviceA-acl4-basic-2000] rule permit source 232.1.1.0 0.0.0.255
   [*DeviceA-acl4-basic-2000] quit
   [*DeviceA] pim
   [*DeviceA-pim] ssm-policy 2000
   [*DeviceA-pim] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display pim routing-table** command to view the PIM routing table on devices and check whether HostA can receive information sent from the multicast source 10.110.1.1/24 to the multicast group 232.1.1.1/24. The command output on DeviceA and DeviceB is as follows:

```
<DeviceA> display pim routing-table
VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.110.1.1, 232.1.1.1)
     Protocol: pim-ssm, Flag: LOC
     UpTime: 00:02:13
     Upstream interface: 100GE1/0/2, Refresh time: 00:02:13
         Upstream neighbor: 10.110.1.1
         RPF prime neighbor: 10.110.1.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/1
             Protocol:  pim-ssm, UpTime: 00:02:13, Expires: 00:03:17

<DeviceB> display pim routing-table
 VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (10.110.1.1, 232.1.1.1)
     Protocol: pim-ssm, Flag:
     UpTime: 00:09:15
     Upstream interface: 100GE1/0/1, Refresh time: 00:09:15
         Upstream neighbor: 192.168.2.1
         RPF prime neighbor: 192.168.2.1
     Downstream interface(s) information:
     Total number of downstreams: 1
        1: 100GE1/0/2
             Protocol:  pim-ssm, UpTime: 00:09:15, Expires: 00:03:13
```
#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  multicast routing-enable
  #
  acl number 2000
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0001.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.1 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.1.2 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
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
  acl number 2000
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.2.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 192.168.4.1 255.255.255.0
   pim sm
   isis enable 1
  #
  pim
   ssm-policy 2000
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
  acl number 2000
   rule 5 permit source 232.1.1.0 0.0.0.255
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 192.168.4.2 255.255.255.0
   pim sm
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.110.2.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   isis enable 1
  #
  pim
   ssm-policy 2000
  #
  return
  ```