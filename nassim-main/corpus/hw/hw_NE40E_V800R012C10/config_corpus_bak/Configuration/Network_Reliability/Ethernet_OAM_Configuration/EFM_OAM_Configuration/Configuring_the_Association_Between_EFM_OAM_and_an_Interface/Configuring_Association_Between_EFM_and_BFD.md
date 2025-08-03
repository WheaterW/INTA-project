Configuring Association Between EFM and BFD
===========================================

If EFM is deployed at the user side and BFD is deployed at the network side of a device, association between EFM and CFM can be configured. This allows EFM and CFM to notify each other of faults and ensures reliable service transmission.

#### Context

For details on the principles and usage scenarios of association between EFM and BFD, see [Overview of EFM OAM](dc_vrp_efm_cfg_2001.html).

Association between EFM and BFD is bidirectional. The details are as follows:

* When EFM detects a link fault, it will notify BFD of the fault.
* When BFD detects a link fault, it will notify EFM of the fault.

The following BFD sessions support association between EFM and BFD:

* Static BFD for LSP (LDP, TE, TE-LSP, static-LSP, and VLL PW) sessions (a PST is required)
* BFD for IP sessions (no PST is required)

Perform the following steps on each device with EFM or BFD deployed:


#### Pre-configuration Tasks

Before configuring association between EFM and BFD, complete the following tasks:

* [Configure basic EFM functions.](dc_vrp_efm_cfg_2003.html)
* Configure basic BFD functions.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**oam-mgr**](cmdqueryname=oam-mgr)
   
   
   
   The OAM management view is displayed.
3. Perform either of the following configurations as required.
   
   
   
   **Table 1** Association between EFM and BFD Scenario
   | Scenario | Configuration Scheme 1 | Configuration Scheme 2 |
   | --- | --- | --- |
   | Bidirectional fault notification between EFM and BFD | Run the [**oam-bind efm interface**](cmdqueryname=oam-bind+efm+interface) *interface-type* *interface-number* **bfd-session** *bfd-session-id* command to configure EFM and BFD to notify each other of faults.  NOTE:  If the [**oam-bind efm interface**](cmdqueryname=oam-bind+efm+interface) *interface-type* *interface-number* **bfd-session** *bfd-session-id* command is run, the [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **efm** **interface** *interface-type* *interface-number* and [**oam-bind ingress efm interface**](cmdqueryname=oam-bind+ingress+efm+interface) *interface-type* *interface-number* **egress** **bfd-session** *bfd-session-id* commands will be displayed in the configuration file. | Perform the following operations: Run the following commands for unidirectional notification to implement bidirectional notification: * Run the [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **efm** **interface** *interface-type* *interface-number* command to configure BFD to notify EFM of faults. * Run the [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **efm** **interface** *interface-type* *interface-number* command to configure EFM to notify BFD of faults. |
   | Unidirectional fault notification between EFM and BFD | * Run the [**oam-bind ingress efm interface**](cmdqueryname=oam-bind+ingress+efm+interface) *interface-type* *interface-number* **egress** **bfd-session** *bfd-session-id* command to configure EFM to notify BFD of faults. * Run the [**oam-bind ingress bfd-session**](cmdqueryname=oam-bind+ingress+bfd-session) *bfd-session-id* **egress** **efm** **interface** *interface-type* *interface-number* command to configure BFD to notify EFM of faults. | N/A |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.