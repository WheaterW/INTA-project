Setting an MLD Snooping Version
===============================

Setting an MLD Snooping Version

#### Context

MLD manages group memberships and runs on the network segment between Layer 3 multicast devices and member hosts. MLD has two versions: MLDv1 and MLDv2. After an MLD snooping version is configured on a Layer 2 device, the device can process MLD messages accordingly. Generally, the same version used on the upstream Layer 3 multicast device is configured on a Layer 2 device. If MLD is not enabled on the Layer 3 multicast device, the version used on the Layer 2 device should be later than or the same as that on member hosts.

In most cases, you are advised to use the same MLD version for all hosts in the same VLAN. If user hosts in a VLAN support different versions, the highest MLD snooping version among them needs to be configured on the device so that it can process the messages from all the hosts.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Set an MLD snooping version.
   
   
   ```
   [mld snooping version](cmdqueryname=mld+snooping+version) number
   ```
   
   By default, the device can process both MLDv1 and MLDv2 messages.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```