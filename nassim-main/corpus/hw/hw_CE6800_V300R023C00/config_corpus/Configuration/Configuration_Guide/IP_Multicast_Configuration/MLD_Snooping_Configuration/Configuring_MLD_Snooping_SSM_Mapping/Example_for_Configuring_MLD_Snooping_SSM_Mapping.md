Example for Configuring MLD Snooping SSM Mapping
================================================

Example for Configuring MLD Snooping SSM Mapping

#### Networking Requirements

On the multicast network shown in [Figure 1](#EN-US_TASK_0000001372550981__fig_dc_cfg_vxlan_cfgcase_000401), a router (Router) connects to the user network through a Layer 2 device (Device). Router runs MLDv2 and uses both the ASM and SSM models to provide multicast services. UserA, UserB, and UserC run MLDv1, which cannot be upgraded to MLDv2. Multicast sources Source1 and Source2 simultaneously send multicast data to multicast group FF13::3. However, hosts want to receive multicast data from only Source1. To meet this requirement, configure MLD snooping SSM mapping on Device.

**Figure 1** Network diagram of Layer 2 multicast SSM mapping![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent 100GE1/0/1 and 100GE1/0/3, respectively.

![](figure/en-us_image_0000001444662086.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN on Device and add related interfaces to the VLAN.
2. Enable MLD snooping globally and in the VLAN so that users can receive multicast data.
3. Configure an MLD snooping SSM group policy to add the ASM group address to the SSM group address range.
4. Configure MLD snooping SSM mapping so that users receive only the multicast data from a specified multicast source.

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
2. Enable MLD snooping.
   
   
   
   # Enable MLD snooping globally.
   
   ```
   [~Device] mld snooping enable
   ```
   
   # Enable MLD snooping in VLAN 10.
   
   ```
   [*Device] vlan 10
   [*Device-vlan10] mld snooping enable
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```
3. Configure an MLD snooping SSM group policy.
   
   
   
   # Create an ACL6 and configure a rule that permits data packets sent to multicast group FF13::3.
   
   ```
   [~Device] acl ipv6 number 2008
   [*Device-acl4-basic-2008] rule 5 permit source FF13::3 64
   [*Device-acl4-basic-2008] commit
   [~Device-acl4-basic-2008] quit
   ```
   
   # Configure an SSM mapping policy in the VLAN to include group address FF13::3 in the SSM group address range.
   
   ```
   [~Device] vlan 10 
   [*Device-vlan10] mld snooping ssm-policy 2008
   [*Device-vlan10] commit
   ```
4. Configure the SSM mapping function.
   
   
   
   # Configure Device to run MLDv2, enable SSM mapping, and map group FF13::3 to the source address FC00:0:0:3::3.
   
   ```
   [~Device-vlan10] mld snooping version 2
   [*Device-vlan10] mld snooping ssm-mapping enable 
   [*Device-vlan10] mld snooping ssm-mapping ff13::3 64 fc00:0:0:3::3
   [*Device-vlan10] commit
   [~Device-vlan10] quit
   ```

#### Verifying the Configuration

# Check the MLD snooping configuration in the VLAN.

```
[~Device] display mld snooping vlan configuration
 MLD Snooping Configuration for VLAN 10
    mld snooping enable
     mld snooping version 2
     mld snooping ssm-policy 2008
     mld snooping ssm-mapping enable
     mld snooping ssm-mapping FF13:: 64 FC00:0:0:3::3
```

The command output shows that an SSM mapping policy has been configured in VLAN 10.


#### Configuration Scripts

```
#
sysname Device
#
vlan batch 10
#
mld snooping enable
#
acl ipv6 number 2008
 rule 5 permit source FF13::/64
#
vlan 10
 mld snooping enable
 mld snooping version 2
 mld snooping ssm-policy 2008
 mld snooping ssm-mapping enable
 mld snooping ssm-mapping FF13:: 64 FC00:0:0:3::3
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