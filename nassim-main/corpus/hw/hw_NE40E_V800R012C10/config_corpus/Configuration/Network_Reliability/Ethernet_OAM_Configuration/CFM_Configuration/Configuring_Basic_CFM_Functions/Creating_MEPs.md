Creating MEPs
=============

This section describes how to create maintenance association end points (MEPs).

#### Context

Create MEPs to implement continuity check (CC).

MEPs can be either local MEP or remote maintenance association end points (RMEPs).

MEPs are also classified by direction: inward and outward. [Table 1](#EN-US_TASK_0172361944__tab_dc_vrp_cfm_cfg_00000901) describes MEP or RMEP type configurations in different networking scenarios and interfaces.

**Table 1** MEP configurations in different networking scenarios
| Networking Environment | | Description | | | |
| --- | --- | --- | --- | --- | --- |
| Direct link | | Both interfaces of a direct link must be physical interfaces, Eth-Trunk interfaces, or Trunk member interfaces. These interfaces support outward MEPs. | | | |
| End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | This device supports only common sub-interfaces, L3VE interfaces, and outward MEPs. | | | |
| End-to-end link | Layer 2 device | MEPs have different types in different networking scenarios:  * In an MA, VLAN- and interface-based MEPs are mutually exclusive. Common inward- and outward-facing MEPs are mutually exclusive. A single VLAN-based MEP can be created. * In virtual local area network (VLAN) scenarios, this device supports Layer 2 interfaces and inward and outward MEPs. * In virtual private LAN service (VPLS) scenarios, this device supports common sub-interfaces, L2VE interfaces, common Trunk sub-interfaces, sub-interfaces for dot1q and QinQ VLAN tag termination, QinQ stacking sub-interfaces, VLAN member interfaces (VSI access using VLANs), and 1 to 1 QinQ mapping sub-interfaces. Inward and outward MEPs can be configured for interfaces except L2VE interfaces which support only inward MEPs. * In virtual leased line (VLL) scenarios, this device supports common sub-interfaces, sub-interfaces for QinQ VLAN tag termination, L2VE interfaces, QinQ stacking sub-interfaces, VLAN member interfaces (VLL access using VLANs), and 1 to 1 QinQ mapping sub-interfaces. Inward and outward MEPs can be configured for interfaces except L2VE interfaces which support only inward MEPs. * In L2TPv3 scenarios, this device supports EVC sub-interfaces. CC test support outward MEPs, LB/LT test support outward and inward MEPs. * PW-based MEPs can be configured in PBB VPLS, VPLS and HVPLS scenarios. | | | |

Perform the following steps on each device on which MEPs need to be configured:


#### Procedure

1. Create a local MEP.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      
      
      The MA view is displayed.
   4. [Table 2](#EN-US_TASK_0172361944__tab_dc_vrp_cfm_cfg_00000902) lists MEP configurations in different networking scenarios.
      
      
      
      **Table 2** MEP configurations in different networking scenarios
      | Networking Environment | | | | Configuration | | | |
      | --- | --- | --- | --- | --- | --- | --- | --- |
      | Direct link | | | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type* *interface-number* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | Common sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* *interface-type interface-number.subnumber* **vlan** *vlan-id* **outward** command to create a local MEP.  NOTE:  The value of the **vlan** *vlan-id* parameter is the ID of the VLAN that the sub-interface specified by the **interface** *interface-type interface-number.subnumber* parameter joins. When you create a local MEP, you can specify a VLAN in this command to associate with services. | | | |
      | End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | QinQ stacking and 1 to 1 QinQ mapping sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* **vlan-id** *vlan-id* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | VLANIF interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* *interface-type interface-number* **vlan** *vlan-id* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | Dot1q VLAN tag termination sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* [ **vlan-id** *vlan-id* ] { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Device that connects a Layer 2 network to a Layer 3 network | QinQ VLAN tag termination sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* **pe-vid** *pe-vid* **ce-vid** *ce-vid* { **outward** | **inward** } command to create a local MEP.  NOTE:  Only qinq protocol 0x8100, 0x9100, 0x88a8, and 0x9200 can be configured on the port. | | | |
      | End-to-end link | Layer 2 device | Layer 2 interfaces in VLAN scenarios | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | Common sub-interfaces in VPLS or VLL scenarios | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* [ **vlan-id** *vlan-id* ] { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | QinQ stacking and 1 to 1 QinQ mapping sub-interfaces in VPLS or VLL scenarios | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* **vlan-id** *vlan-id* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | VLAN member interfaces in VPLS or VLL scenarios | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* *interface-type interface-number* **vlan** *vlan-id* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | Dot1q VLAN tag termination sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* [ **vlan-id** *vlan-id* ] { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | QinQ VLAN tag termination sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* **pe-vid** *pe-vid* **ce-vid** *ce-vid* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | EVC sub-interfaces | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **interface** *interface-type interface-number.subnumber* **vlan** *vlan-id* **pe-vid** *pe-vid* **ce-vid** *ce-vid* { **outward** | **inward** } command to create a local MEP. | | | |
      | End-to-end link | Layer 2 device | PWs in VPLS, HVPLS, or PBB VPLS scenarios | | Run the [**mep mep-id**](cmdqueryname=mep+mep-id) *mep-id* **peer-ip** *peer-ip* [ **vc-id** *vc-id* ] [ **mac** *mac-address* ] { **outward** | **inward** } command to create a local MEP. | | | |
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Create an RMEP.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      
      
      The MD view is displayed.
   3. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      
      
      The MA view is displayed.
   4. Run [**remote-mep**](cmdqueryname=remote-mep) **mep-id** *mep-id* [ **mac** *mac-address* ]
      
      
      
      An RMEP is created.
   5. (Optional) Run [**active time**](cmdqueryname=active+time) *time*
      
      
      
      An activation time is set for the RMEP.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Follow-up Procedure

* To create multiple local MEPs in an MA, repeat Step 1.d.
* To create multiple RMEPs in an MA, repeat Step 2.d.
* To create MEPs in multiple MAs, repeat Step 1.c and Step 1.d.
* To create RMEPs in multiple MAs, repeat Step 2.c and Step 2.d.