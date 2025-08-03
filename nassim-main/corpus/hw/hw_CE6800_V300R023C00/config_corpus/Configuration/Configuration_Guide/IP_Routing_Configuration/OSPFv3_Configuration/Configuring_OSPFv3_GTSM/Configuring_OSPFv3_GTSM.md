Configuring OSPFv3 GTSM
=======================

Configuring OSPFv3 GTSM

#### Prerequisites

Before configuring OSPFv3 GTSM, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable OSPFv3 GTSM.
   
   
   ```
   [ospfv3 valid-ttl-hops](cmdqueryname=ospfv3+valid-ttl-hops) ttl [ vpn-instance vpn-instance-name ]
   ```
   
   After this step is performed, only the packets that match the specified OSPFv3 GTSM policy are sent to the control plane for processing. Note the following:
   
   * The [**ospfv3 valid-ttl-hops**](cmdqueryname=ospfv3+valid-ttl-hops) command has two functions: enabling OSPFv3 GTSM and specifying a TTL value for check. The **vpn-instance** parameter is valid only for the latter function.
   * Valid TTL values are within the range [255 â *ttl* + 1, 255].
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```