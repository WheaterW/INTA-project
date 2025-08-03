Applying a QoS Profile
======================

You can define a QoS profile and apply it to interfaces to implement unified scheduling of traffic on these interfaces.

#### Context

To achieve uniform scheduling of incoming traffic flows on multiple interfaces, you need to implement traffic management by user levels. Interface-based HQoS only supports classifying traffic flows on one interface into an SQ for scheduling. It does not support uniform scheduling of traffic flows on multiple interfaces. Profile-based HQoS, by comparison, supports classifying traffic flows on multiple interfaces into an SQ for scheduling. It implements uniform scheduling of traffic flows on multiple interfaces by defining QoS profiles and applying the profiles to different interfaces.


#### Procedure

* Apply a QoS profile.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run any of the following commands to apply a QoS profile to a specific type of interface:
     
     
     + To apply a QoS profile to an IP-Trunk interface or a dot1q interface, run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } [ **identifier** **none** ] [ **group** *group-name* ] command.
     + To apply a QoS profile to a Layer 2 interface or dot1q VLAN tag termination sub-interface, run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **vlan** *vlan-id-begin* [ **to** *vlan-id-end* ] [ **identifier** { **vlan-id** | **none** } ] [ **group** *group-name* ] command.
     + To apply a QoS profile to a QinQ VLAN tag termination sub-interface, run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **pe-vid** *pe-vlan-id* { **ce-vid** *ce-vlan-id-begin* [ **to** *ce-vlan-id-end* ] } [ **identifier** { **pe-vid** | **ce-vid** | **pe-ce-vid** | **none** } ] [ **group** *group-name* ] command.
     + To apply a QoS profile to an EVC Layer 2 sub-interface, run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } [ **identifier** { **none** | **vid** | **ce-vid** | **vid-ce-vid** } ] [ **group** *group-name* ] command.
     + To apply a QoS profile to an NVE interface, run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **vni** *vni-id* **source** *sourceip* **peer** *peerip* command.
  4. (Optional) Run [**user-queue shaping bgp-local-ifnet-traffic outbound**](cmdqueryname=user-queue+shaping+bgp-local-ifnet-traffic+outbound)
     
     
     
     HQoS is enabled for traffic carried by a BGP local IFNET tunnel on the interface.
     
     
     
     After HQoS is configured on an outbound interface of a BGP local IFNET tunnel, if the outbound interface resides on a downstream board equipped with a non-eTM subcard, you need to perform this step to allow HQoS to take effect.
  5. (Optional) Run [**qos user-queue member-link-scheduler distribute**](cmdqueryname=qos+user-queue+member-link-scheduler+distribute) 
     
     
     
     Weight-based bandwidth distribution among trunk member interfaces is configured when the QoS profile's user-queue is applied to the trunk interface.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* (Optional) Apply the channel profile.
  1. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  2. Run [**qos channel-profile**](cmdqueryname=qos+channel-profile) *channel-profile-name*
     
     
     
     The channel profile is applied to the board.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Restart the board for this command to take effect.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the user view.
  6. Run [**reset**](cmdqueryname=reset) **slot** *slot-id*
     
     
     
     The board is restarted.