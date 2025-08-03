Associating CFM with VRRP
=========================

This section describes how to associate connectivity fault management (CFM) with Virtual Router Redundancy Protocol (VRRP).

#### Context

The association can be unidirectional or bidirectional. For details about the association, see [Overview of CFM](dc_vrp_cfm_cfg_000002.html).

Perform the following steps on each device with CFM or VRRP deployed:


#### Pre-configuration Tasks

Before associating CFM with VRRP, complete the following tasks:

* Configure basic CFM functions.
* Configure basic VRRP functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Configure the association depending on the usage scenario:
   
   
   
   **Table 1** CFM and VRRP association configuration
   | Scenario | Configuration Solution 1 | Configuration Solution 2 |
   | --- | --- | --- |
   | Bidirectional association between CFM and VRRP | Run the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **vrrp** **vrid** *vrid* **interface** *interface-type* *interface-number* command to configure the bidirectional association between CFM and VRRP.  NOTE: If the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **vrrp** **vrid** *vrid* **interface** *interface-type* *interface-number* command is run, the configuration file contains the following commands: * [**oam-bind ingress vrrp**](cmdqueryname=oam-bind+ingress+vrrp) **vrid** *vrid* **interface** *interface-type* *interface-number* *md-name* **egress** **cfm md** *md-name* **ma** *ma-name* * [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **vrrp** **vrid** *vrid* **interface** *interface-type* *interface-number* | The following commands can be used together to configure EFM and CFM to notify each other of faults and can be used in any order: * Run the [**oam-bind ingress vrrp**](cmdqueryname=oam-bind+ingress+vrrp) **vrid** *vrid* **interface** *interface-type* *interface-number* **egress** **cfm md** *md-name* **ma** *ma-name* command to enable VRRP to notify CFM of a fault. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **vrrp** **vrid** *vrid* **interface** *interface-type* *interface-number* command to enable CFM to notify VRRP of a fault. |
   | Unidirectional association between CFM and VRRP | Perform either of the following operations: * Run the [**oam-bind ingress vrrp vrid**](cmdqueryname=oam-bind+ingress+vrrp+vrid) *vrrp-id* **interface** { *interface-name* | *interface-type* *interface-number* } **egress** **cfm** **md** *md-name* **ma** *ma-name* command to enable VRRP to notify CFM of a fault. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **vrrp** **vrid** *vrrp-id* **interface** { *interface-name* | *interface-type* *interface-number* } command to enable CFM to notify VRRP of a fault. | None |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.