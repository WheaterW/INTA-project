Enabling IGMP Snooping SSM Mapping
==================================

Enabling IGMP Snooping SSM Mapping

#### Context

By configuring SSM mapping, you can create one-to-one mappings between multicast groups and multicast sources. SSM mapping can be used only in VLANs that run IGMP snooping v3.

Although SSM mapping takes effect only for IGMPv3 messages in a VLAN, a device does not convert IGMPv2 messages into IGMPv3 messages before sending them to router ports. If you want the device to convert IGMPv2 messages into IGMPv3 messages before sending them to the upstream device, configure IGMP snooping proxy or IGMP snooping Report suppression on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set the IGMP snooping version to 3 for the VLAN.
   
   
   ```
   [igmp snooping version](cmdqueryname=igmp+snooping+version) 3
   ```
   
   The default IGMP snooping version number is 2. However, IGMPv2 does not support SSM mapping.
4. Enable SSM mapping in the VLAN.
   
   
   ```
   [igmp snooping ssm-mapping enable](cmdqueryname=igmp+snooping+ssm-mapping+enable) [ policy policy-name ]
   ```
   
   By default, SSM mapping is disabled in a VLAN.
5. Configure the mapping between a multicast group and a multicast source.
   
   
   
   The multicast group addresses specified in this step must be within the SSM group address range. For details about how to configure the SSM group address range, see [(Optional) Configuring an SSM Group Address Range](vrp_l2mc_cfg_0046.html).
   
   * If the **policy** *policy-name* parameter is not specified in [4](#EN-US_TASK_0000001130622108__step1569134551124645), run the following command to configure mappings between multicast group addresses and multicast source addresses.
     ```
     [igmp snooping ssm-mapping](cmdqueryname=igmp+snooping+ssm-mapping) group-address { group-mask | mask-length } source-address
     ```
   * If the **policy** *policy-name* parameter is specified in [4](#EN-US_TASK_0000001130622108__step1569134551124645), run the following commands to enter the SSM mapping policy view and configure mappings between multicast group addresses and multicast source addresses.
     ```
     [quit](cmdqueryname=quit)
     [ssm-mapping policy](cmdqueryname=ssm-mapping+policy) policy-name
     [group](cmdqueryname=group) group-address { group-mask-length | group-mask } source source-address
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     The two configuration methods differ as follows:
     
     The mappings configured in an SSM mapping policy view can be applied to multiple VLANs, whereas those configured in the VLAN view take effect only in the current VLAN. To apply the same mappings to multiple VLANs, you are advised to perform the configuration in the SSM mapping policy view.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```