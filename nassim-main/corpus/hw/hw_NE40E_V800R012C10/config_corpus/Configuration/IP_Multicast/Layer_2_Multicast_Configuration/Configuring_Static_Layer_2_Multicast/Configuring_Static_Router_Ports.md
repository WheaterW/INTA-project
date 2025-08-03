Configuring Static Router Ports
===============================

Static router ports can be configured to enable users to regularly receive multicast data packets because static router ports do not age.

#### Context

Router ports receive multicast data packets from an upstream device, and are enabled as dynamic by default. However, static router ports can be configured to allow users to regularly receive multicast data packets. Since static router ports do not age, multicast services are not interrupted.

On a stable network, PW interfaces and sub-interfaces in a VPLS or interfaces in a VLAN can be configured as static router ports.

Static router ports do not age, and can only be deleted using relevant commands.


#### Procedure

* Static router ports can be configured at different positions on a network to ensure regular multicast traffic reception. The steps listed in [Table 1](#EN-US_TASK_0172367854__tab_dc_vrp_l2mc_cfg_001201) can be performed in any order. Complete one or more steps as required to configure static router ports.
  
  
  
  **Table 1** Configuring static router ports
  | Usage Scenario | Position | Configuration Procedure | Description |
  | --- | --- | --- | --- |
  | VLAN | Interface | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**interface**](cmdqueryname=interface) *interface-typeinterface-number* command to enter the Ethernet interface view. 3. Run the [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **vlan** *vlan-id* command to configure the interfaces in a specified VLAN as static router ports. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. | Before configuring the interface as a static router port, ensure that the interface has been added to a specific VLAN. Otherwise, the configuration will not take effect. |
  | VPLS | Sub-interface | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subnumber* command to enter the sub-interface view. 3. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the sub-interface to a VSI. 4. Run the [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **vsi** *vsi-name* command to configure the sub-interface as a static router port in the VSI. 5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. | + A sub-interface that is not bound to a VSI cannot be configured as a static router port. + If a sub-interface configured as a static router port is unbound from a VSI, all static router port configurations will be deleted from the sub-interface. The sub-interface can be a common sub-interface or a Dot1q termination sub-interface. Only one Dot1q termination sub-interface in a VSI can be configured as a static router port. |
  | PW | 1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view. 2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command to enter the VSI view. 3. Run the [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **remote-peer** *ip-address* [ **negotiation-vc-id** *vc-id* | **bgp-ad** ] command to configure a PW interface as a static router port in the VSI. 4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration. | Perform the following configurations as required according to the PW signaling negotiation mode: + If LDP is used as the signaling negotiation protocol, run the [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **remote-peer** *ip-address* [ **negotiation-vc-id** *vc-id* ] command. + If BGP-AD is used as the signaling negotiation protocol, run the [**igmp-snooping static-router-port**](cmdqueryname=igmp-snooping+static-router-port) **remote-peer** *ip-address* **bgp-ad** command. If no IP address is set for the remote peer, the PW interface can still be configured as a static router port in the VSI, but the configuration will not take effect. It will only take effect after an IP address is set for the remote peer. |