Enabling MLD Snooping SSM Mapping
=================================

Enabling MLD Snooping SSM Mapping

#### Context

By configuring SSM mapping, you can create one-to-one mappings between multicast groups and multicast sources. SSM mapping can be used only in VLANs that run MLD snooping v2.

Although MLDv2 needs to be specified in the VLAN when SSM mapping is configured, the device does not convert MLDv1 messages to MLDv2 messages when forwarding them to router ports. If you want the device to convert MLDv1 messages to MLDv2 messages before sending them to the upstream device, configure MLD snooping proxy or MLD snooping Report suppression on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set the MLD snooping version to 2 for the VLAN.
   
   
   ```
   [mld snooping version](cmdqueryname=mld+snooping+version) 2
   ```
   
   By default, the version number of MLD snooping is 2, and MLDv2 messages can be processed.
4. Enable SSM mapping in the VLAN.
   
   
   ```
   [mld snooping ssm-mapping enable](cmdqueryname=mld+snooping+ssm-mapping+enable) [ policy policy-name ]
   ```
   
   By default, SSM mapping is disabled in a VLAN.
5. Configure policies for processing Option 82 information on a DHCP relay agent.
   
   
   
   The multicast group addresses specified in this step must be within the SSM group address range. For details about how to configure the SSM group address range, see [(Optional) Configuring an SSM Group Address Range](vrp_l2mc6_cfg_0046.html).
   
   * If the **policy** *policy-name* parameter is not specified in [4](#EN-US_TASK_0000001372710805__step1569134551124645), run the following command to configure mappings between multicast group addresses and multicast source addresses.
     ```
     [mld snooping ssm-mapping](cmdqueryname=mld+snooping+ssm-mapping) group-address mask-length source-address
     ```
   * If the **policy** *policy-name* parameter is specified in [4](#EN-US_TASK_0000001372710805__step1569134551124645), run the following commands to enter the SSM mapping policy view and configure mappings between multicast group addresses and multicast source addresses.
     ```
     [quit](cmdqueryname=quit)
     [ssm-mapping ipv6 policy](cmdqueryname=ssm-mapping+ipv6+policy) policy-name
     [group](cmdqueryname=group) group-ipv6-address mask-length source source-ipv6-address
     ```
   
   The two configuration methods differ as follows:
   
   The mappings configured in an SSM mapping policy view can be applied to multiple VLANs, whereas those configured in the VLAN view take effect only in the current VLAN. To apply the same mappings to multiple VLANs, you are advised to perform the configuration in the SSM mapping policy view.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```