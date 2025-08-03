(Optional) Configuring Cost Values for SR-MPLS TE Policies
==========================================================

Configure cost values for SR-MPLS TE Policies so that the ingress can select the optimal SR-MPLS TE Policy based on the values.

#### Context

By default, the cost (or metric) values of SR-MPLS TE Policies are irrelevant to IGP cost values â the cost values of the IGP routes on which the SR-MPLS TE Policies depend. The default cost value of an SR-MPLS TE Policy is 0. As a result, the ingress cannot perform cost-based SR-MPLS TE Policy selection. To avoid this problem, you can either configure SR-MPLS TE Policies to inherit IGP cost values or directly configure absolute cost values for the SR-MPLS TE Policies.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   SR is enabled globally, and the SR view is displayed.
3. Run [**sr-te policy**](cmdqueryname=sr-te+policy) *policy-name*[ **endpoint** *ipv4-address* **color** *color-value* ]
   
   
   
   An SR-MPLS TE Policy with the specified endpoint and color is created, and the SR-MPLS TE Policy view is displayed.
4. Run [**metric inherit-igp**](cmdqueryname=metric+inherit-igp)
   
   
   
   The SR-MPLS TE Policy is configured to inherit the IGP cost.
5. Run [**igp metric absolute**](cmdqueryname=igp+metric+absolute) *absoluteValue*
   
   
   
   An absolute cost is configured for the SR-MPLS TE Policy.
   
   
   
   When an SR-MPLS TE Policy is configured to inherit the IGP cost, the cost of the SR-MPLS TE Policy is reported to the tunnel management module according to the following rules:
   
   * If the [**igp metric absolute**](cmdqueryname=igp+metric+absolute) command is run to configure an absolute IGP cost, the configured cost is reported as the cost of the SR-MPLS TE Policy.
   * If the [**igp metric absolute**](cmdqueryname=igp+metric+absolute) command is not run, the cost of the route that has a 32-bit mask and is destined for the endpoint of the SR-MPLS TE Policy is subscribed to and reported as the cost of the SR-MPLS TE Policy. In this case, the route cost may be different from the actual path cost of the SR-MPLS TE Policy.
   * If the [**metric inherit-igp**](cmdqueryname=metric+inherit-igp) command is not run, the cost of the SR-MPLS TE Policy reported to the tunnel management module is 0.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.