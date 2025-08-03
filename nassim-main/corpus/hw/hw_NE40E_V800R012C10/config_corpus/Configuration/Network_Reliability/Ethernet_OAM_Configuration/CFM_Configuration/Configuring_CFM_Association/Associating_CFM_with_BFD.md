Associating CFM with BFD
========================

This section describes how to associate connectivity fault management (CFM) with Bidirectional Forwarding Detection (BFD).

#### Context

CFM on the user side can be associated with BFD on the network side to detect faults, ensuring service reliability. With this association, when CFM or BFD detects a link fault, it instructs the Manager (MGR) module to notify the other mechanism of the fault. The association can be unidirectional or bidirectional. For details about the association, see [Overview of CFM](dc_vrp_cfm_cfg_000002.html).

Association between CFM and BFD is bidirectional.

* When CFM detects a link fault, it notifies BFD of the fault.
* When BFD detects a link fault, it notifies CFM of the fault.

BFD supports the following types of sessions:

* Static BFD for LSP (LDP, TE, TE-LSP, static-LSP, and VLL PW) sessions (a PST is required)
* BFD for IP sessions: No PST needs to be configured.

Perform the following steps on each device with CFM or BFD deployed.


#### Pre-configuration Tasks

Before associating CFM with BFD, complete the following tasks:

* [Configure basic CFM functions.](dc_vrp_cfm_cfg_000004.html)
* Configure basic BFD functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Configure the association depending on the usage scenario.
   
   
   
   **Table 1** CFM and BFD association configuration
   | Scenario | Configuration Solution 1 | Configuration Solution 2 |
   | --- | --- | --- |
   | Bidirectional association between CFM and BFD | Run the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **bfd-session** *bfd-session-id* command to configure the bidirectional association between CFM and BFD.  NOTE: If you have run the [**oam-bind cfm md**](cmdqueryname=oam-bind+cfm+md) *md-name* **ma** *ma-name* **bfd-session** *bfd-session-id* command, the configuration file contains the following commands: * [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **cfm** **md** *md-name* **ma** *ma-name* * [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **bfd-session** *bfd-session-id* | Perform the following operations: * Run the [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **cfm** **md** *md-name* **ma** *ma-name* command to enable BFD to instruct the MGR module to notify CFM of a fault. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **bfd-session** *bfd-session-id* command to enable CFM to instruct the MGR module to notify BFD of a fault. |
   | Unidirectional association between CFM and BFD | Perform either of the following operations: * Run the [**oam-bind ingress bfd**](cmdqueryname=oam-bind+ingress+bfd) **session** *bfd-session-id* **egress** **cfm** **md** *md-name* **ma** *ma-name* command to enable BFD to instruct the MGR module to notify CFM of a fault. * Run the [**oam-bind ingress cfm md**](cmdqueryname=oam-bind+ingress+cfm+md) *md-name* **ma** *ma-name* **egress** **bfd-session** *bfd-session-id* command to enable CFM to instruct the MGR module to notify BFD of a fault. | None |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.