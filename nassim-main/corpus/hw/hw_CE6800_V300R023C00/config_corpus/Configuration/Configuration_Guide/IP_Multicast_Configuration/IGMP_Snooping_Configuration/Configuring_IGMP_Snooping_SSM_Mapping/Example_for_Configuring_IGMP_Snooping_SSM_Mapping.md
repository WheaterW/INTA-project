Example for Configuring IGMP Snooping SSM Mapping
=================================================

Example for Configuring IGMP Snooping SSM Mapping

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0000001176741567__fig_dc_cfg_vxlan_cfgcase_000401), a router (Router) connects to the user network through a Layer 2 device (Device). Router runs IGMPv3 and uses both the ASM and SSM models to provide multicast services. UserA, UserB, and UserC run IGMPv2 and do not support IGMPv3. Multicast sources Source1 and Source2 simultaneously send multicast data to multicast group 225.1.1.1. However, hosts want to receive multicast data from only Source1. To meet this requirement, configure IGMP snooping SSM mapping on Device.

**Figure 1** Network diagram of Layer 2 multicast SSM mapping![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface3 represent 100GE1/0/1 and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001130781922.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on Device and add related interfaces to the VLAN.
2. Enable IGMP snooping globally and in the VLAN so that users can receive multicast data.
3. Configure an IGMP snooping SSM group policy to add the ASM group address to the SSM group address range.
4. Configure IGMP snooping SSM mapping so that users receive only the multicast data from a specified multicast source.

#### Procedure

1. Create a VLAN and add related interfaces to the VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Device
   [*HUAWEI] commit
   [~Device] vlan 10
   [*Device-vlan10] quit
   [*Device] interface 100ge 1/0/1
   [*Device-100GE1/0/1] port link-type access
   [*Device-100GE1/0/1] port default vlan 10
   [*Device-100GE1/0/1] quit
   [*Device] interface 100ge 1/0/3
   [*Device-100GE1/0/3] port link-type trunk
   [*Device-100GE1/0/3] port trunk allow-pass vlan 10
   [*Device-100GE1/0/3] commit
   [~Device-100GE1/0/3] quit
   ```
2. Enable IGMP snooping.
   
   
   
   # Enable IGMP snooping globally.
   
   ```
   [~Device] igmp snooping enable
   ```
   
   # Enable IGMP snooping in VLAN10.
   
   ```
   [*Device] vlan 10
   [*Device-vlan10] igmp snooping enable
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
3. Configure an IGMP snooping SSM group policy.
   
   
   
   # Create an ACL, and configure a rule that allows hosts to receive data of multicast group 225.1.1.1.
   
   ```
   [~Device] acl number 2008
   [*Device-acl4-basic-2008] rule 5 permit source 225.1.1.1 0
   [*Device-acl4-basic-2008] commit
   [~Device-acl4-basic-2008] quit
   ```
   
   # Configure an SSM mapping policy in the VLAN to include group 225.1.1.1 in the SSM group range.
   
   ```
   [~Device] vlan 10 
   [*Device-vlan10] igmp snooping ssm-policy 2008
   [*Device-vlan10] commit
   ```
4. Configure the SSM mapping function.
   
   
   
   # Specify IGMPv3 on Device, enable SSM mapping, and configure a mapping between group address 225.1.1.1 and source address 10.10.1.1.
   
   ```
   [~Device-vlan10] igmp snooping version 3
   [*Device-vlan10] igmp snooping ssm-mapping enable 
   [*Device-vlan10] igmp snooping ssm-mapping 225.1.1.1 32 10.10.1.1
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```

#### Verifying the Configuration

# Check the IGMP snooping configuration in the VLAN.

```
[~Device] display igmp snooping vlan configuration
 IGMP Snooping Configuration for VLAN 10
     igmp snooping enable
     igmp snooping version 3
     igmp snooping ssm-policy 2008
     igmp snooping ssm-mapping enable
     igmp snooping ssm-mapping 225.1.1.1 255.255.255.255 10.10.1.1
```

An SSM mapping policy has been configured in VLAN10.


#### Configuration Scripts

* Device
  ```
  #
  sysname Device
  #
  vlan batch 10
  #
  igmp snooping enable
  #
  acl number 2008
   rule 5 permit source 225.1.1.1 0
  #
  vlan 10
   igmp snooping enable
   igmp snooping version 3
   igmp snooping ssm-policy 2008
   igmp snooping ssm-mapping enable
   igmp snooping ssm-mapping 225.1.1.1 255.255.255.255 10.10.1.1
  #
  interface 100GE1/0/1
   port default vlan 10
  #
  interface 100GE1/0/3
   port link-type trunk
   port trunk allow-pass vlan 10 
  #
  return 
  ```