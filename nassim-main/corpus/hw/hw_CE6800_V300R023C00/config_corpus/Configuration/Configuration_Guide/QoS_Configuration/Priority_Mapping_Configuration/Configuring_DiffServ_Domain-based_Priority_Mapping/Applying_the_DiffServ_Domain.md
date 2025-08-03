Applying the DiffServ Domain
============================

Applying the DiffServ Domain

#### Context

You can bind a DiffServ domain to an inbound or outbound interface of packets so that the device can implement mapping between external priorities and internal priorities/colors according to the mappings defined in the DiffServ domain.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
   
   To enter the Layer 2 sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command.
3. Apply a DiffServ domain.
   
   
   ```
   [trust upstream](cmdqueryname=trust+upstream) { ds-domain-name | none }
   ```
   
   
   
   By default, the domain **default** is applied to an interface.
   
   If [**trust upstream**](cmdqueryname=trust+upstream) **none** is configured on an interface, the device performs no priority mapping on incoming packets.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The [**trust upstream**](cmdqueryname=trust+upstream) **none** command cannot be configured together with the [**qos phb marking 8021p disable**](cmdqueryname=qos+phb+marking+8021p+disable) and [**qos phb marking dscp enable**](cmdqueryname=qos+phb+marking+dscp+enable) commands on the device.
4. (Optional) Enable the mapping between PHBs and DSCP values for outgoing packets.
   
   
   ```
   [qos phb marking dscp enable](cmdqueryname=qos+phb+marking+dscp+enable)
   ```
5. (Optional) Disable the mapping between PHBs and 802.1p values for outgoing packets.
   
   
   ```
   [qos phb marking 8021p disable](cmdqueryname=qos+phb+marking+8021p+disable)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```