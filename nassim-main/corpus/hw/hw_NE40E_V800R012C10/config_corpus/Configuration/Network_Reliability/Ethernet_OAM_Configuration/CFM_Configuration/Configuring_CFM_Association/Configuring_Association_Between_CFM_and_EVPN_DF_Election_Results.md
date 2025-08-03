Configuring Association Between CFM and EVPN DF Election Results
================================================================

In dual-homing single-active EVPN networking where the designated forwarder (DF) election result is used to determine the active/standby state of PEs, association between CFM and EVPN DF election can be configured to improve device- and link-level reliability.

#### Context

Association between CFM and EVPN DF election result is unidirectional. With this function enabled, the result of electing a PE as the backup DF is reported to CFM, which then notifies the CE of the fault, triggering the CE to clear corresponding MAC entries of the corresponding VLAN.


#### Pre-configuration Tasks

Before associating CFM with EVPN DF election results, complete the following tasks:

* Configure basic CFM functions.
* Configure basic EVPN functions.
* Configure a CFM association on the CE to trigger deletion of MAC address entries.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   The OAM management view is displayed.
3. Run [**oam-bind ingress evpn df interface**](cmdqueryname=oam-bind+ingress+evpn+df+interface) *interface-type* *interface-number* **egress** **cfm** **md** *md-name* **ma** *ma-name*
   
   EVPN is configured to report DF election results to CFM.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.