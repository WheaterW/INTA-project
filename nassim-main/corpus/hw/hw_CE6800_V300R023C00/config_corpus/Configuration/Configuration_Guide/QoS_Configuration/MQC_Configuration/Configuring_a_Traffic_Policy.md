Configuring a Traffic Policy
============================

Configuring a Traffic Policy

#### Prerequisites

Before configuring a traffic policy, complete the following tasks:

* [Configure a traffic classifier.](galaxy_mqc_cfg_0005.html)
* [Configure a traffic behavior.](galaxy_mqc_cfg_0006.html)


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a traffic policy and enter the traffic policy view, or enter the view of an existing traffic policy.
   
   
   ```
   [traffic policy](cmdqueryname=traffic+policy) policy-name
   ```
   
   The device supports a maximum of 2048 traffic policies.
3. Bind a traffic behavior and a traffic classifier to the traffic policy.
   
   
   ```
   [classifier](cmdqueryname=classifier) classifier-name behavior behavior-name [ precedence precedence-value ]
   ```
   
   A maximum of 2048 traffic classifiers can be bound to a traffic policy.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```