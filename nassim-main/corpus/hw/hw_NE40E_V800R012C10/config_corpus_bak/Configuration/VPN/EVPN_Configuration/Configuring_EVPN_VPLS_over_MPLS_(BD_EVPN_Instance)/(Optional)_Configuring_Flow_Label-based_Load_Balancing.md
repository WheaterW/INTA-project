(Optional) Configuring Flow Label-based Load Balancing
======================================================

After flow label-based load balancing is configured, EVPN VPLS services can select forwarding paths based on flow labels, improving forwarding efficiency.

#### Context

On a network with EVPN VPLS service traffic, if multiple links exist between Ps, flow label-based load balancing can be configured on PEs to improve traffic forwarding efficiency and reduce the forwarding pressure on Ps. After this function is configured, PEs can calculate flow labels for different types of data traffic and add flow labels to them. When a P receives packets carrying flow labels, it selects paths based on flow labels to forward these packets, achieving load balancing.


#### Procedure

* Perform the following steps on the PEs at both ends of an EVPN instance.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**flow-label hash-fields**](cmdqueryname=flow-label+hash-fields) { **l2** | **l3** | **l4** } command to configure hash factors for flow label-based load balancing.
     
     
     
     This command is supported only by the admin VS.
  3. Run the [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode** command to enter the BD EVPN instance view.
  4. Run the [**flow-label static**](cmdqueryname=flow-label+static) command to enable static flow label-based load balancing for EVPN VPLS.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the static flow label-based load balancing configuration does not match on both ends, the device discards packets carrying flow labels, causing packet loss.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Perform the following steps on Ps.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**slot**](cmdqueryname=slot) *slot-id* command to enter the slot view.
  3. Run the [**load-balance hash-fields mpls**](cmdqueryname=load-balance+hash-fields+mpls) **label** command to configure a hash factor for per-flow load balancing of MPLS packets on an interface board.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.