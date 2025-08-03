Defining Traffic Policies
=========================

After defining traffic classifiers and traffic behaviors,
you need to configure traffic policies by associating traffic classifiers
with traffic behaviors.

#### Context

Perform the following
steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and the policy view is displayed.
3. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
   
   
   
   A traffic behavior is
   associated with a specified traffic classifier in the traffic policy.