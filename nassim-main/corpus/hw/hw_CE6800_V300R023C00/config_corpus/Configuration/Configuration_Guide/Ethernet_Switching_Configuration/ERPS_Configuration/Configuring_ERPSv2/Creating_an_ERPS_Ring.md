Creating an ERPS Ring
=====================

Creating an ERPS Ring

#### Context

ERPS works for ERPS rings. An ERPS ring consists of connected Layer 2 switching devices that are configured with the same control VLAN and data VLAN. Before configuring other ERPS functions, create an ERPS ring.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an ERPS ring and enter the ERPS ring view.
   
   
   ```
   [erps ring](cmdqueryname=erps+ring) ring-id
   ```
   
   
   
   By default, an ERPS ring created using the [**erps ring**](cmdqueryname=erps+ring) *ring-id* command is a major ring.
3. Configure the device to run ERPSv2.
   
   
   ```
   [version](cmdqueryname=version) v2 
   ```
   
   
   
   By default, the device runs ERPSv1.
   
   Before changing ERPSv2 to ERPSv1, delete ERPS configurations that are not supported in ERPSv1.
4. (Optional) Configure the ERPS ring as a sub-ring.
   
   
   ```
   [sub-ring](cmdqueryname=sub-ring)
   ```
   
   By default, an ERPS ring is a major ring. The difference between a major ring and a sub-ring is that the major ring is a closed ring but the sub-ring is not. If the ERPS ring needs to be configured as a major ring, skip this step.
   
   Ensure that no port is added to the ERPS ring to be configured as a sub-ring. If a port is added to the ERPS ring, you must run the [**undo erps ring**](cmdqueryname=undo+erps+ring) command in the interface view or the [**undo port**](cmdqueryname=undo+port) command in the ERPS ring view to remove the port from the ERPS ring.
5. (Optional) Configure the R-APS PDU transmission mode in a sub-ring.
   
   
   ```
   [virtual-channel](cmdqueryname=virtual-channel) { enable | disable }
   ```
   
   By default, nodes in a sub-ring transmit R-APS PDUs in NVC mode. The default transmission mode is recommended. When the sub-ring links are discontinuous, the VC transmission mode is required. If the ERPS ring is a major ring, skip this step.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To use a virtual channel, configure the VC transmission mode on all nodes of the sub-ring and the interconnected nodes of the sub-ring and major ring.
6. (Optional) Enable the function of encapsulating an ERPS ring ID into the destination MAC address of R-APS PDUs.
   
   
   ```
   [encapsulate-ring-id enable](cmdqueryname=encapsulate-ring-id+enable)
   ```
   
   By default, the function of encapsulating an ERPS ring ID into the destination MAC address of R-APS PDUs is disabled.
7. (Optional) Configure a description.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   By default, the description of an ERPS ring is the ERPS ring name, for example, Ring 1.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```