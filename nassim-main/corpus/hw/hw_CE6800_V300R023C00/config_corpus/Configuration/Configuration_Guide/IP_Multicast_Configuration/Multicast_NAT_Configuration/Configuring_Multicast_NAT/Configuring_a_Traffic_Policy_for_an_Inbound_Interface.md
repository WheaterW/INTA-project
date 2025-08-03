Configuring a Traffic Policy for an Inbound Interface
=====================================================

Configuring a Traffic Policy for an Inbound Interface

#### Context

In multicast NAT, traffic policies need to be configured for the inbound interface of multicast streams to match input multicast streams.

In multicast NAT, input and output multicast streams are associated through a multicast NAT instance. To associate input multicast streams with a multicast NAT instance, traffic policies need to be applied on the inbound interface of multicast streams.

![](public_sys-resources/note_3.0-en-us.png) 

This function is only supported by the following: CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.



#### Procedure

1. Configure a traffic classifier.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a traffic classifier and enter the traffic classifier view, or enter the view of an existing traffic classifier.
      
      
      ```
      [traffic classifier](cmdqueryname=traffic+classifier) classifier-name [ type { and | or } ]
      ```
   3. Define matching rules in the traffic classifier.
      
      
      
      You can configure multiple matching rules in a traffic classifier. For details, see "Configuring a Traffic Classifier" in the *Configuration Guide > QoS > MQC Configuration*.
   4. Exit the traffic classifier view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Configure a traffic behavior.
   1. Create a traffic behavior and enter the traffic behavior view.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Bind streams to a multicast NAT instance.
      
      
      ```
      [multicast-nat bind instance](cmdqueryname=multicast-nat+bind+instance) id instance-id [ name instance-name ]
      ```
   3. Exit the traffic behavior view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
3. Configure a traffic policy.
   1. Create a traffic policy and enter the traffic policy view, or enter the view of an existing traffic policy.
      
      
      ```
      [traffic policy](cmdqueryname=traffic+policy) policy-name
      ```
   2. Associate the traffic behavior with the traffic classifier in the traffic policy.
      
      
      ```
      [classifier](cmdqueryname=classifier) classifier-name behavior behavior-name [ precedence precedence-value ]
      ```
   3. Exit the traffic policy view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Apply the traffic policy.
   1. Enter the interface view.
      
      
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Switch the interface working mode from Layer 2 to Layer 3. Determine whether to perform this step based on the current interface working mode.
      
      
      ```
      [undo portswitch](cmdqueryname=undo+portswitch)
      ```
   3. Apply the traffic policy on the interface.
      
      
      ```
      [traffic-policy](cmdqueryname=traffic-policy) policy-name inbound
      ```
   4. Enable multicast NAT on the inbound interface of multicast streams.
      
      
      ```
      [multicast-nat inbound enable](cmdqueryname=multicast-nat+inbound+enable)
      ```
   5. Exit the interface view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   6. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```