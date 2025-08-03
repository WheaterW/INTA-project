Configuring VPLS Decoupling
===========================

In a scenario where a VPLS service recurses to a public network, to prevent public network changes from affecting the convergence performance of the VPLS service, configure VPLS decoupling.

#### Usage Scenario

In a scenario where a VPLS service recurses to a public network, if the public network flaps, the VPLS service will change, and forwarding entries will be updated on devices, affecting the convergence performance of the VPLS service. To prevent the impact of public network changes on the VPLS service, configure VPLS decoupling.


#### Pre-configuration Tasks

Before configuring VPLS decoupling, complete the following tasks:

* Configure basic VPLS functions.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls l2vpn**](cmdqueryname=mpls+l2vpn)
   
   
   
   MPLS L2VPN is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   A VSI is configured, and its view is displayed.
6. Run [**mpls vpls convergence separate enable**](cmdqueryname=mpls+vpls+convergence+separate+enable)
   
   
   
   VPLS decoupling is configured.
   
   
   
   Enabling VPLS decoupling in the system view takes effect for all VSIs. Enabling VPLS decoupling in the VSI view takes effect only for the specified VSI. VPLS decoupling cannot be configured in both views.
7. (Optional) Run [**reserve-interface fast-switch enable**](cmdqueryname=reserve-interface+fast-switch+enable)
   
   
   
   Reserve-interface fast switching is enabled.
   
   
   
   To quickly switch broadcast traffic to the standby interface board when the active interface board fails, perform this step to enable reserve-interface fast switching.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.