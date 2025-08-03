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
3. (Optional) Enable the function of encapsulating an ERPS ring ID into the destination MAC address of R-APS PDUs.
   
   
   ```
   [encapsulate-ring-id enable](cmdqueryname=encapsulate-ring-id+enable)   
   ```
   
   
   
   By default, the function of encapsulating an ERPS ring ID into the destination MAC address of R-APS PDUs is disabled.
4. (Optional) Configure a description.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   By default, the description of an ERPS ring is the ERPS ring name, for example, Ring 1.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```