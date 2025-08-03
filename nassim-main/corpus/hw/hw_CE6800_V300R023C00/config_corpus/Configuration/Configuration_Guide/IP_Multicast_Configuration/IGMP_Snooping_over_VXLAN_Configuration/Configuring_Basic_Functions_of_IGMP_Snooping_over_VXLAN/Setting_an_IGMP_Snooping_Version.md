Setting an IGMP Snooping Version
================================

Setting an IGMP Snooping Version

#### Context

IGMP manages multicast group member relationships and runs on the network segment between Layer 3 multicast devices and member hosts. IGMP has three versions: IGMPv1, IGMPv2, and IGMPv3. You can configure an IGMP snooping version as required on a Layer 2 device so that the device processes IGMP messages accordingly. Generally, the same version used on the upstream Layer 3 multicast device is configured on a Layer 2 device. If IGMP is not enabled on the Layer 3 multicast device, the version used on the Layer 2 device should be later than or the same as that on member hosts. Devices in the same BD must run the same IGMP version. If user hosts in a BD support different versions, the highest IGMP snooping version among them needs to be configured on the device so that it can process the messages from all the hosts.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Set an IGMP snooping version.
   
   
   ```
   [igmp snooping version](cmdqueryname=igmp+snooping+version) number
   ```
   
   
   
   By default, IGMP snooping over VXLAN can process IGMPv1 and IGMPv2 messages but cannot process IGMPv3 messages.
   
   If IGMP snooping over VXLAN is required to process IGMPv3 messages, perform this step to set the version number to 3. The version is backward compatible. For example, if the version is set to 3, IGMP snooping can process IGMPv1, IGMPv2, and IGMPv3 messages.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```