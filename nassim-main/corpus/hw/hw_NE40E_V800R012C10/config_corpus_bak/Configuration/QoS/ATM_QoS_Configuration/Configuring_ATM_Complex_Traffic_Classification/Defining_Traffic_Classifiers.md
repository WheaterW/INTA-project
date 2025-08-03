Defining Traffic Classifiers
============================

Before configuring complex traffic classification, you need to define a traffic classifier.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Configure an ACL rule.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For details about ACLs, see [ACL Configuration](../vrp/dc_vrp_acl4_cfg_0040.html) or [ACL6 Configuration](../vrp/dc_vrp_acl6_cfg_0040.html).
3. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is defined and the traffic classifier view is displayed.
4. Run the following command as required to define a traffic classifier.
   
   
   * To define an ACL matching rule, run:
     
     ```
     [if-match acl](cmdqueryname=if-match+acl) acl-number
     ```
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Only ACLs that match packets based on the Layer 3 or Layer 4 information are supported.
   * To define a DSCP matching rule, run:
     
     ```
     [if-match dscp](cmdqueryname=if-match+dscp) dscp-value
     ```
   * To define a TCP flag matching rule, run:
     
     ```
     [if-match tcp syn-flag](cmdqueryname=if-match+tcp+syn-flag) tcpflag-value
     ```
   * To define a matching rule based on IP precedence, run:
     
     ```
     [if-match](cmdqueryname=if-match) [ ipv6 ]  ip-precedence ip-precedence
     ```
   * To define a rule for matching all packets, run:
     
     ```
     [if-match any](cmdqueryname=if-match+any) 
     ```
   * To define a rule for matching packets based on the MPLS EXP value, run:
     
     ```
     [if-match mpls-exp](cmdqueryname=if-match+mpls-exp) exp-value
     ```