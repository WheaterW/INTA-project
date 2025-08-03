Configuring VLAN-based VLAN Mapping
===================================

Configuring VLAN-based VLAN Mapping

#### Context

When an interface configured with VLAN-based VLAN mapping receives a single-tagged or double-tagged packet, the interface replaces the VLAN tag of the single-tagged packet or the outer VLAN tag of the double-tagged packet with a VLAN tag on the public network, or replaces both VLAN tags of the double-tagged packet with VLAN tags on the public network based on the configured VLAN mapping mode.

![](public_sys-resources/note_3.0-en-us.png) 

VLAN-based VLAN mapping can be configured only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Change the interface working mode from Layer 3 to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the link type of the interface and the VLAN allowed by the interface. Use either of the following methods based on requirements:
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * VLAN mapping can be configured only on a trunk or hybrid interface. The interface must be added to the translated VLAN in tagged mode.
   * If 2 to 1 or 2 to 2 mapping mode is configured, the VLAN ID allowed by the VLAN mapping-enabled interface must be the outer VLAN ID.
   * Set the link type of the interface to trunk and configure the VLAN allowed by the VLAN mapping-enabled interface. The VLAN is the translated VLAN.
     ```
     [port link-type trunk](cmdqueryname=port+link-type+trunk)
     [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { vlan-id1 [ to vlan-id2 ] } &<1-40>
     ```
   * Set the link type of the interface to hybrid and configure the VLAN allowed by the VLAN mapping-enabled interface. The VLAN is the translated VLAN.
     ```
     [port link-type hybrid](cmdqueryname=port+link-type+hybrid)
     [port hybrid tagged vlan](cmdqueryname=port+hybrid+tagged+vlan) { vlan-id1 [ to vlan-id2 ] } &<1-10>
     ```
5. Configure the VLAN mapping function. Use either of the following methods based on requirements:
   
   
   * Configure 1 to 1 VLAN mapping to map the single tag in a packet to a specified tag.
     ```
     [port vlan-mapping vlan](cmdqueryname=port+vlan-mapping+vlan) vlan-id1  map-vlan vlan-id3 [ remark-8021p 8021p-value ]
     ```
   * Configure 2 to 1 VLAN mapping to map the double tags in a packet to a specified tag.
     ```
     port vlan-mapping vlan vlan-id1 inner-vlan vlan-id5 map-single-vlan vlan-id3
     ```
   * Configure 2 to 2 VLAN mapping to map the outer tag of double tags in a packet to a specified tag and transparently transmit the inner tag as data.
     ```
     [port vlan-mapping vlan](cmdqueryname=port+vlan-mapping+vlan) vlan-id1 inner-vlan vlan-id5 to vlan-id6 map-vlan vlan-id3 [ remark-8021p 8021p-value ]
     ```
   * Configure 2 to 2 VLAN mapping to map the double tags in a packet to two specified tags.
     ```
     [port vlan-mapping vlan](cmdqueryname=port+vlan-mapping+vlan) vlan-id1 inner-vlan vlan-id5 map-vlan vlan-id3 map-inner-vlan vlan-id4 [ remark-8021p 8021p-value ]
     ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the interface view to check the VLAN mapping configuration on the interface.