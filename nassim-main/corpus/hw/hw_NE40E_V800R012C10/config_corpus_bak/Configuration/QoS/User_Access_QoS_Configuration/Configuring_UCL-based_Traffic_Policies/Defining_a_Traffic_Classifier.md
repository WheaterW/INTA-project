Defining a Traffic Classifier
=============================

Before configuring class-based QoS for the traffic on the network, you need to define a traffic classifier.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is defined and the traffic classifier view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When a traffic classifier is defined for UCL, the logical relationship "and" between matching rules does not take effect.
3. Run [**if-match**](cmdqueryname=if-match) [ **ipv6** ] **acl** *acl-number* [ **precedence** *precedence-value* ]
   
   
   
   A UCL-based complex traffic classification rule is configured.
   
   In this configuration, the value of *acl-number* ranges from 6000 to 9999.
   
   To configure multiple UCL-based complex traffic classification rules, you can repeat this step.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.