Configuring Bandwidth Information Flooding for MPLS TE
======================================================

If the link bandwidth changes slightly, the threshold for flooding bandwidth information is set on the ingress or a transit node of a CR-LSP, which reduces flooding attempts and saves network resources.

#### Usage Scenario

To synchronize data between TEDBs in an IGP area, OSPF TE or IS-IS TE is configured to update TEDB information and flood bandwidth information if the remaining bandwidth changes on an MPLS interface.

The NE40E supports the following methods of controlling bandwidth information flooding:

* Configure flooding commands to enable immediate bandwidth information flooding on a device.
* Configure a flooding interval to enable periodic bandwidth information flooding on a device.
* Configure a flooding threshold to prevent frequent flooding.
  + When the percentage of the bandwidth reserved for the MPLS TE tunnel on a link to the remaining link bandwidth in the TEDB is greater than or equal to the configured threshold (flooding threshold), OSPF TE and IS-IS TE flood link bandwidth information to all devices in this area and update TEDB information.
  + When the percentage of the bandwidth released by the MPLS TE tunnel to the remaining link bandwidth in the TEDB is greater than or equal to the configured threshold, OSPF TE and IS-IS TE flood link bandwidth information to all devices in this area and update TEDB information.


#### Pre-configuration Tasks

Before adjusting the flooding threshold, [configure an RSVP-TE tunnel](dc_vrp_te-p2p_cfg_0003.html).


#### Procedure

* Configure forcible bandwidth information flooding.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te manual-flooding**](cmdqueryname=mpls+te+manual-flooding)
     
     
     
     A device on the MPLS TE tunnel is configured to immediately flood the bandwidth change to the network.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure periodic bandwidth information flooding.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te periodic-flooding**](cmdqueryname=mpls+te+periodic-flooding) [ **interval** *time-value* ]
     
     
     
     Periodic bandwidth information flooding is enabled on a device.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a flooding threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls te bandwidth change thresholds**](cmdqueryname=mpls+te+bandwidth+change+thresholds) { **down** *percent-down* | **up** *percent-up* }
     
     
     
     The bandwidth flooding threshold is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.