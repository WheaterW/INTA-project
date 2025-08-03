Configuring ECN Overlay
=======================

Configuring ECN Overlay

#### Prerequisites

Before configuring the ECN Overlay function, you have configured either of the following ECN functions based on actual requirements:

* [Static ECN function](galaxy_congestion_avoid_cfg_0013.html)
* [AI ECN function](galaxy_ai_aiecn_cfg_0005.html)

#### Context

To apply the ECN function on a VXLAN network, you need to configure the ECN Overlay function.

* For a network overlay, you only need to enable the function for mapping the ECN field in the outer IP header of the VXLAN packet to the IP header of the original packet on the egress NVE, that is, the function for mapping the outer ECN field to the inner ECN field during VXLAN decapsulation.
* For a host/hybrid overlay, in addition to the function for mapping the outer ECN field to the inner ECN field during VXLAN decapsulation, you also need to enable the inner ECN marking function on the transit node, so that the ECN field in the outer IP header of the VXLAN packet can be mapped to the IP header of the original packet on the transit node.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the function for mapping the outer ECN field to the inner ECN field during VXLAN decapsulation.
   
   
   ```
   [assign forward nvo3 egress mark-ecn enable](cmdqueryname=assign+forward+nvo3+egress+mark-ecn+enable)
   ```
   
   By default, the function for mapping the outer ECN field to the inner ECN field during VXLAN decapsulation is disabled.
3. (Optional) Enable the inner ECN marking function on a transit node on a VXLAN network.
   
   
   ```
   [assign forward nvo3 transit mark inner-ecn enable](cmdqueryname=assign+forward+nvo3+transit+mark+inner-ecn+enable)
   ```
   
   By default, the inner ECN marking function is disabled on transit nodes on a VXLAN network.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display nvo3 ecn configuration**](cmdqueryname=display+nvo3+ecn+configuration) command to check whether the ECN Overlay function is enabled.