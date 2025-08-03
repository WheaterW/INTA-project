Defining a Traffic Policy for Mirrored Traffic and Applying It Globally
=======================================================================

This section describes how to define a traffic policy for mirrored traffic and apply the policy globally. It covers configuring a traffic classifier to define the traffic to be mirrored, specifying a traffic behavior, enabling flow mirroring, defining a traffic policy to associate the traffic classifier with the traffic behavior, and applying the traffic policy globally.

#### Context

To analyze user traffic more accurately, configure a traffic policy for mirrored traffic and apply the policy globally. In this way, only the traffic that meets the specified conditions is copied to the observing port for analysis, and irrelevant user traffic is filtered out.


#### Procedure

1. Configure a user control list (UCL).
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**acl**](cmdqueryname=acl) **name** *ucl-acl-name* **ucl** [ **match-order** { **auto** | **config** } ]
      
      
      
      A user ACL is created and its view is displayed.
   3. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
      
      
      
      An advanced ACL rule is created in the advanced ACL view.
   4. Run [**return**](cmdqueryname=return)
      
      
      
      Return to the user view.
2. Define a traffic classifier.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
      
      
      
      A traffic classifier is defined and its view is displayed.
      
      
      
      The classifier name specified by the *classifier-name* parameter cannot be any predefined classifier name in the system. For details about traffic classifiers, see *HUAWEI NE40E-M2 series Universal Service Router Configuration Guide - QoS*.
   3. Run [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** { *acl-number* | **name** *acl-name* }
      
      
      
      An ACL rule is defined.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**return**](cmdqueryname=return)
      
      
      
      Return to the user view.
3. Define a traffic behavior and enable flow mirroring.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
      
      
      
      A traffic behavior is defined and its view is displayed.
   3. Run [**port-mirroring enable**](cmdqueryname=port-mirroring+enable)
      
      
      
      Flow mirroring is enabled.
   4. (Optional) Run [**port-mirroring car**](cmdqueryname=port-mirroring+car) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ]
      
      
      
      The CAR function is implemented for mirrored traffic.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   6. Run [**return**](cmdqueryname=return)
      
      
      
      Return to the user view.
4. Define a traffic policy to associate the traffic classifier with the traffic behavior.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
      
      
      
      A traffic policy is defined and its view is displayed.
   3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
      
      
      
      A traffic behavior is specified for the specified traffic classifier in the traffic policy.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**return**](cmdqueryname=return)
      
      
      
      Return to the user view.
5. Create a service policy of the mirroring type and specify a service group for the service policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**service-policy**](cmdqueryname=service-policy) **name** *policy-name* **mirror**
      
      
      
      A service policy of the mirroring type is created and its view is displayed.
   3. Run [**service-group**](cmdqueryname=service-group) *service-group-name* [ **inbound** | **outbound** ] [ **priority** *priority* ]
      
      
      
      A service group is specified for the service policy.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   5. Run [**return**](cmdqueryname=return)
      
      
      
      Return to the user view.
6. Configure the mapping between the Option 82 attribute and the service policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mirror**](cmdqueryname=mirror) **rule** [ *rule-number-name* ] **service-policy** *service-policy-name* [ **partial-match** ] { **circuit-id** | **remote-id** } *description-text*
      
      
      
      The mapping between the Option 82 attribute and the service policy is configured.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
7. Apply the traffic policy globally.
   1. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
      
      
      
      The traffic policy is applied globally, so that user access packets are matched against rules in the traffic policy.
      
      
      
      In VS mode, this command is supported only by the admin VS.
   2. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.