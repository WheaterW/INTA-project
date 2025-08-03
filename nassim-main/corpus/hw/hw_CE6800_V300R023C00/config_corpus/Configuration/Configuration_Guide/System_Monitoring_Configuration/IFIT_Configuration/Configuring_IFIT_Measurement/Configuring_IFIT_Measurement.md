Configuring IFIT Measurement
============================

Configuring IFIT Measurement

#### Prerequisites

Before configuring IFIT to implement network packet loss and delay measurement, you have completed the following tasks:

* Configure static routes or dynamic routing protocols to ensure network connectivity between devices.
* Configure an ACL rule to be bound to an IFIT traffic classifier.
* Configure a clock synchronization protocol, such as 1588v2, NTP, or high-precision NTP.

#### Context

Users want to use the NMS to monitor network traffic in real time to quickly detect abnormal traffic and locate faults. You can configure IFIT measurement on physical devices so that the devices can periodically send packet loss and delay measurement information to the NMS for summary, analysis, and display.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable IFIT measurement, create an IFIT view and enter the view, or enter an existing IFIT view.
   
   
   ```
   [ifit](cmdqueryname=ifit)
   ```
   
   By default, no IFIT view is created.
3. Create an IFIT DCN instance and enter the view, or enter the view of an existing IFIT DCN instance.
   
   
   ```
   [dcn-instance](cmdqueryname=dcn-instance)
   ```
   
   By default, no DCN instance is created.
4. Configure the IFIT NE ID.
   
   
   ```
   [node-id](cmdqueryname=node-id) node-id-value
   ```
   
   By default, no IFIT NE ID is configured.
5. Configure the interface role in the outbound direction.
   
   
   
   You can configure the interface role in the outbound direction globally or on an interface.
   
   * Configure the IFIT NE role globally.
     ```
     [role](cmdqueryname=role) { ingress-egress | transit }
     ```
     
     By default, an IFIT NE is configured as a transit node.
     
     If an NE is configured as both ingress and egress nodes, the IFIT packet header is removed from all outgoing packets on the NE. If an NE is configured as a transit node, the IFIT packet header is retained in all outgoing packets on the NE.
   * Configure the role on an interface.
     ```
     { [edge-port](cmdqueryname=edge-port) | [transit-port](cmdqueryname=transit-port) } { [interface](cmdqueryname=interface) { interface-type interface-number | interface-name } } &<1-8>
     ```
     
     By default, the role on an interface is determined by the globally configured IFIT NE role.
     
     If an interface is configured as an edge port, the IFIT packet header is removed from outgoing packets on the interface. If an interface is configured as a transit port, the IFIT packet header is retained in outgoing packets on the interface.
   
   
   
   When the interface role in the outbound direction is configured both globally and on an interface, the configuration on the interface takes precedence.
6. Configure the IFIT measurement interval.
   
   
   ```
   [interval](cmdqueryname=interval) interval-value
   ```
   
   By default, the IFIT measurement interval is 60s.
7. Configure the aging time of measurement flows.
   
   
   ```
   [aging-time](cmdqueryname=aging-time) time-value
   ```
   
   By default, the aging time of measurement flows is 120s.
   
   The aging time of measurement flows must be greater than the IFIT measurement interval.
8. Configure an IFIT traffic classifier.
   
   
   1. Create an IFIT traffic classifier and enter the view, or enter the view of an existing IFIT traffic classifier.
      ```
      [traffic classifier](cmdqueryname=traffic+classifier) classifier-name
      ```
   2. Define ACL rules in the IFIT traffic classifier.
      ```
      [if-match](cmdqueryname=if-match) [ ipv6 ] acl { acl-number | name acl-name }
      ```
      
      By default, no ACL rule is configured in an IFIT traffic classifier.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      * Only advanced ACLs (3000 to 3999) can be bound to an IFIT traffic classifier.
      * The ACL rules can contain only 5-tuple information. An ACL rule containing unsupported information will not be delivered. As a result, the IFIT function cannot be enabled for the corresponding traffic. The supported 5-tuple information is as follows:
        + Protocol (TCP or UDP)
        + Source IPv4 or IPv6 address and mask
        + Destination IPv4 or IPv6 address and mask
        + TCP or UDP source port number (The value must be the same as the specified port number.)
        + TCP or UDP destination port number (The value must be the same as the specified port number.)
   3. Return to the IFIT DCN instance view.
      ```
      [quit](cmdqueryname=quit)
      ```
9. Configure an IFIT traffic behavior.
   
   
   1. Create an IFIT traffic behavior and enter the view, or enter the view of an existing IFIT traffic behavior.
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Configure the format of the inserted IFIT packet headers and IFIT working mode.
      ```
      [action insert header](cmdqueryname=action+insert+header) [ header-mode dcn ] [ measure-mode { e2e | trace } ]
      ```
      
      By default, the IFIT packet headers in DCN format are inserted and the IFIT working mode is E2E.
   3. Configure the type of IFIT flows.
      ```
      [flow-type](cmdqueryname=flow-type) { dynamic | static flow-id flow-id  }
      ```
      
      By default, dynamic IFIT flows are used for analysis.
   4. (Optional) Configure a flow table aggregation policy for dynamic IFIT flows.
      ```
      [aggregation](cmdqueryname=aggregation) { source-port | destination-port | none }
      ```
      
      By default, the aggregation source or destination port is not specified.
      
      Static flows are created and analyzed based on specified flow characteristics, which are not affected by the flow table aggregation policy. Therefore, this step is not required for such flows.
   5. (Optional) Enable IFIT delay measurement using one of the following methods:
      * Enable IFIT delay measurement to measure the delay of the first packet in each measurement flow within an interval.
        ```
        [delay-measure enable](cmdqueryname=delay-measure+enable)
        ```
        
        By default, IFIT delay measurement is disabled.
      * Enable IFIT packet-by-packet delay measurement to measure the delay of each packet in each measurement flow within an interval.
        ```
        [delay-measure per-packet enable](cmdqueryname=delay-measure+per-packet+enable)
        ```
        
        By default, IFIT packet-by-packet delay measurement is disabled.![](public_sys-resources/note_3.0-en-us.png) 
      * To enable IFIT delay measurement, you must configure 1588v2 to implement clock synchronization between devices.
   6. Return to the IFIT DCN instance view.
      ```
      [quit](cmdqueryname=quit)
      ```
10. Configure an IFIT traffic policy.
    
    
    1. Create an IFIT traffic policy and enter the view, or enter the view of an existing IFIT traffic policy.
       ```
       [traffic policy](cmdqueryname=traffic+policy) policy-name
       ```
    2. Bind a traffic behavior and a traffic classifier to the IFIT traffic policy.
       ```
       [classifier](cmdqueryname=classifier) classifier-name [behavior](cmdqueryname=behavior) behavior-name [ precedence precedence-value | cache-number cache-number ] *
       ```
    3. Return to the IFIT DCN instance view.
       ```
       [quit](cmdqueryname=quit)
       ```
    4. Return to the IFIT view.
       ```
       [quit](cmdqueryname=quit)
       ```
    5. Return to the system view.
       ```
       [quit](cmdqueryname=quit)
       ```
11. Apply the IFIT traffic policy.
    
    
    
    You can apply the IFIT traffic policy globally or to an interface.
    
    * Apply the IFIT traffic policy globally.
      ```
      [ifit traffic-policy](cmdqueryname=ifit+traffic-policy) policy-name global
      ```
    * Apply the IFIT traffic policy to an interface.
      1. Enter the interface view.
         ```
         [interface](cmdqueryname=interface) interface-type interface-number
         ```
      2. Apply the IFIT traffic policy to the interface.
         ```
         [ifit traffic-policy](cmdqueryname=ifit+traffic-policy) policy-name
         ```
      3. Return to the system view.
         ```
         [quit](cmdqueryname=quit)
         ```![](public_sys-resources/note_3.0-en-us.png) 
    
    An IFIT traffic policy cannot be applied both globally and to an interface.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```