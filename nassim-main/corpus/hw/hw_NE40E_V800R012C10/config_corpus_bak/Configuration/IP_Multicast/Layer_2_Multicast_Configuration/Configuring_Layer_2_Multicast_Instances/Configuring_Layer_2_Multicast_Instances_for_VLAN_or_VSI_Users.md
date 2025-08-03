Configuring Layer 2 Multicast Instances for VLAN or VSI Users
=============================================================

If users in different VLANs or VSIs request for the same group's data from the same source, configure a Layer 2 multicast instance on a device, allowing the device to request for only one copy of each multicast data flow for such users from the upstream device.

#### Context

To implement inter-VLAN or inter-VSI multicast traffic replication, configure a Layer 2 multicast instance, and then associate a multicast instance with one or more user instances in Layer 2 multicast instance view.

For the same Layer 2 multicast instance, the multicast and user instances can be VLANs, VSIs, or a combination of them.

* For VLAN users, the multicast and user instances must be VLANs.
* For VSI users, the multicast instance must be a VSI, and the user instances can be either VSIs or VLANs.

To facilitate service management, multicast content providers generally operate different types of channels in different Layer 2 multicast instances. If this is the case, channels need to be specified for Layer 2 multicast instances.


#### Procedure

* Configure a Layer 2 multicast instance for VLAN users.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
     
     
     
     IGMP snooping is enabled for the VLAN.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Enable IGMP snooping only for the VLAN to be configured as the multicast instance.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  5. Run [**l2-multicast instance**](cmdqueryname=l2-multicast+instance) *instance-id*
     
     
     
     A Layer 2 multicast instance is created, and the instance view is displayed.
  6. Run [**import-channel**](cmdqueryname=import-channel) *group-address* { *mask* | *mask-length* }
     
     
     
     A multicast channel is specified for the Layer 2 multicast instance.
     
     
     
     After this step is performed, the instance forwards multicast data only for this channel.
  7. Run [**multicast-instance**](cmdqueryname=multicast-instance) **vlan** *vlan-id*
     
     
     
     A VLAN is configured as the multicast instance for the Layer 2 multicast instance.
  8. Run [**user-instance**](cmdqueryname=user-instance) **vlan** { *vlan-id* [ **to** *vlan-id* ] } &<1-10>
     
     
     
     VLANs are configured as user instances for the Layer 2 multicast instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Multiple user VLANs can be configured for a Layer 2 multicast instance, but a VLAN cannot be configured as both a multicast instance and a user instance.
* Configure a Layer 2 multicast instance for VPLS users.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
     
     
     
     IGMP snooping is enabled globally.
  3. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  4. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
     
     
     
     IGMP snooping is enabled for the VSI.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Enable IGMP snooping only for the VSI to be configured as the multicast instance.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  6. Run [**l2-multicast instance**](cmdqueryname=l2-multicast+instance) *instance-id*
     
     
     
     A Layer 2 multicast instance is created, and the instance view is displayed.
  7. Run [**import-channel**](cmdqueryname=import-channel) *group-address* { *mask* | *mask-length* }
     
     
     
     A multicast channel is specified for the Layer 2 multicast instance.
     
     
     
     After this step is performed, the instance forwards multicast data only for this channel.
  8. Run [**multicast-instance**](cmdqueryname=multicast-instance) **vsi** *vsi-name*
     
     
     
     A VSI is configured as the multicast instance for the Layer 2 multicast instance.
  9. Run [**user-instance**](cmdqueryname=user-instance) { **vsi** *vsi-name* | **vlan** { *vlan-id* [ **to** *vlan-id* ] } &<1-10> }
     
     
     
     VLANs or VSIs are configured as user instances for the Layer 2 multicast instance.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Multiple VLANs or VSIs can be configured as user instances for a Layer 2 multicast instance, but a VLAN or VSI cannot be configured as both a multicast instance and a user instance.