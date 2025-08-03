Defining a Traffic Policy
=========================

After traffic classifiers and traffic behaviors are defined, traffic classifiers and traffic behaviors need to be associated to form traffic policies.

#### Context

Do as follows on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and the traffic policy view is displayed.
3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ]
   
   
   
   A traffic behavior is associated with a specified traffic class in the traffic policy.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.