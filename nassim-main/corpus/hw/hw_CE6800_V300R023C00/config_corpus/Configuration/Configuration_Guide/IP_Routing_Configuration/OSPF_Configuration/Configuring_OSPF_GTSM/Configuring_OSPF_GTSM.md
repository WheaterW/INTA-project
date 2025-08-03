Configuring OSPF GTSM
=====================

Configuring OSPF GTSM

#### Prerequisites

Before configuring OSPF GTSM, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure OSPF GTSM.
   
   
   ```
   [ospf valid-ttl-hops](cmdqueryname=ospf+valid-ttl-hops) ttl [ nonstandard-multicast ] 
   ```
   
   After this step is performed, only the packets matching the OSPF GTSM policy are sent to the control plane for processing. Note the following:
   
   * The [**ospf valid-ttl-hops**](cmdqueryname=ospf+valid-ttl-hops) command has two functions: enabling OSPF GTSM and specifying a TTL value for check. The **vpn-instance** parameter is valid only for the latter function.
   * Valid TTL values are within the range [255 â *ttl* + 1, 255].
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```