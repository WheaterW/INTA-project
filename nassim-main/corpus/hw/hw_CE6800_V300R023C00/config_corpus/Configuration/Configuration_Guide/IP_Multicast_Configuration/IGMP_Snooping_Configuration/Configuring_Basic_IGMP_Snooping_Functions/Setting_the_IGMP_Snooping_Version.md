Setting the IGMP Snooping Version
=================================

Setting the IGMP Snooping Version

#### Context

IGMP manages group member relationships and runs on the network segment between Layer 3 multicast devices and member hosts. IGMP has three versions: IGMPv1, IGMPv2, and IGMPv3. You can set the IGMP snooping version on a Layer 2 device so that it processes the IGMP messages of a specific version. Generally, set the same version on the Layer 2 device as that on the upstream Layer 3 multicast device. If IGMP is not enabled on the Layer 3 multicast device, the version used on the Layer 2 device should be later than or the same as that running on downstream hosts.

In most cases, you are advised to use the same IGMP version for all hosts in the same VLAN. If user hosts in a VLAN support different versions, the highest IGMP snooping version among them needs to be configured on the device so that it can process the messages from all the hosts.

By default, if IGMP snooping is enabled to process IGMPv3 messages, it complies with the lightweight version of IGMPv3 while processing such messages. The differences between the lightweight and full versions of IGMPv3 are as follows:

* For an incoming MODE\_IS\_INCLUDE, ALLOW\_NEW\_SOURCES, or BLOCK\_OLD\_SOURCES message that carries a group address in the ASM address range: The device discards the message if the lightweight version is used, but processes the message as normal if the full version is used.
* For an incoming MODE\_IS\_EXCLUDE, CHANGE\_TO\_EXCLUDE\_MODE, or CHANGE\_TO\_INCLUDE\_MODE message that carries a group address in the ASM address range: The device ignores the number of source addresses carried in the message and instead considers that it contains zero source addresses if the lightweight version is used, but processes the message as normal if the full version is used.
* For an incoming MODE\_IS\_EXCLUDE or CHANGE\_TO\_EXCLUDE\_MODE message that carries a group address in the SSM address range and a non-zero source address: The device performs multicast source-and-group mapping based on the SSM mapping configuration if the lightweight version is used. If the mapping fails, the device does not process the message. In contrast, if the full version is used, the device processes the message based on the multicast group-and-source mapping information carried in the IGMPv3 message.

The processing actions in the lightweight and full versions are the same for the following types of messages:

* Incoming MODE\_IS\_INCLUDE, CHANGE\_TO\_INCLUDE\_MODE, ALLOW\_NEW\_SOURCES, or BLOCK\_OLD\_SOURCES message that carries a group address in the SSM address range
* Incoming MODE\_IS\_EXCLUDE or CHANGE\_TO\_EXCLUDE\_MODE message that carries a group address in the SSM address range and zero source addresses
* Incoming MODE\_IS\_EXCLUDE, CHANGE\_TO\_EXCLUDE\_MODE, or CHANGE\_TO\_INCLUDE\_MODE message that carries a group address in the ASM address range and zero source addresses

You can run the [**igmp snooping version**](cmdqueryname=igmp+snooping+version) **3** **standard-full** command to configure IGMP snooping to comply with the full version of IGMPv3 during the processing of IGMPv3 messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set the version of IGMP messages that can be processed by IGMP snooping.
   
   
   ```
   [igmp snooping version](cmdqueryname=igmp+snooping+version) number
   ```
   
   By default, the device can process IGMPv1 and IGMPv2 messages but cannot process IGMPv3 messages.
   
   If IGMP snooping is required to process IGMPv3 messages, perform this step to set the version number to 3. The version is backward compatible. For example, if the version is set to 3, IGMP snooping can process IGMPv1, IGMPv2, and IGMPv3 messages.
4. (Optional) Configure IGMP snooping to comply with the full version of IGMPv3 during the processing of IGMPv3 messages.
   
   
   ```
   [igmp snooping version](cmdqueryname=igmp+snooping+version) 3 standard-full
   ```
   
   By default, if IGMP snooping is enabled to process IGMPv3 messages, it complies with the lightweight version of IGMPv3 during the processing of received IGMPv3 messages.
   
   Perform this step if the device is required to comply with the full version of IGMPv3 during the processing of such messages.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```