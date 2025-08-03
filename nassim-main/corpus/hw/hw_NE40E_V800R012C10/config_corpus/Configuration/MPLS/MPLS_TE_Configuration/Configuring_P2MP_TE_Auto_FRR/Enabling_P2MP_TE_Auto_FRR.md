Enabling P2MP TE Auto FRR
=========================

Enabling P2MP TE Auto FRR on the ingress or a transit node of the primary tunnel is the prerequisite of configuring TE Auto FRR.

#### Context

Perform either of the following operations to enable P2MP TE Auto FRR on the NE40E:

* Configure the entire device and its interface when Auto FRR needs to be configured on most interfaces.
* Only configure a specified interface when Auto FRR needs to be configured only on a few interfaces.


#### Procedure

* Configure the entire device and its interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) **self-adapting**
     
     
     
     MPLS TE Auto FRR is enabled globally.
     
     
     
     P2MP TE FRR only supports link protection, while a bypass tunnel that the ingress establishes supports node protection by default. As a result, the bypass tunnel fails to be established. To prevent the establishment failure, configure the **self-adapting** parameter in this command, which enables the ingress to automatically switch from node protection to link protection.
  4. Run [**mpls te p2mp-te auto-frr enable**](cmdqueryname=mpls+te+p2mp-te+auto-frr+enable)
     
     
     
     P2MP TE Auto FRR is enabled globally.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the outbound interface on the primary tunnel is displayed.
  7. (Optional) Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) { **block** | **default** }
     
     
     
     TE auto FRR is enabled.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a specified interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te p2mp-te auto-frr enable**](cmdqueryname=mpls+te+p2mp-te+auto-frr+enable)
     
     
     
     P2MP TE Auto FRR is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the outbound interface on the primary tunnel is displayed.
  6. Run [**mpls te auto-frr**](cmdqueryname=mpls+te+auto-frr) { **default** | **link** | **self-adapting** }
     
     
     
     TE auto FRR is enabled.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.