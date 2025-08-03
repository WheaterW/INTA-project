Enabling Intelligent Traffic Analysis for TCP Flows
===================================================

Enabling Intelligent Traffic Analysis for TCP Flows

#### Prerequisites

An ACL has been created by running the [**acl**](cmdqueryname=acl) command in the system view. Currently, only the following advanced ACL rules are supported. The ACL rules that are not supported cannot be delivered, preventing the TAP from receiving corresponding service flows.

* Rule 1: TCP + destination IPv4 or IPv6 address
* Rule 2: TCP + destination IPv4 or IPv6 address + destination TCP port number
* Rule 3: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address
* Rule 4: TCP + source IPv4 or IPv6 address + destination IPv4 or IPv6 address + destination TCP port number

![](public_sys-resources/note_3.0-en-us.png) 

In intelligent traffic analysis for TCP flows, the **deny** or **permit** action specified in an ACL rule does not take effect. Service flows are sent to the TAP for processing as long as they match the preceding advanced ACL rules.




#### Context

You can configure intelligent traffic analysis for TCP flows on the device. The device then matches service flows based on ACL rules, and sends the matched service flows to the TAP for in-depth analysis. In this way, precise data of performance indicators is obtained, which helps you monitor specified service flows in real time and locate faults quickly and accurately.

You can use MQC to implement intelligent traffic analysis for TCP flows by configuring [**traffic-analysis enable**](cmdqueryname=traffic-analysis+enable) in an MQC traffic behavior.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a traffic classifier.
   
   
   
   For details, see "Configuring a Traffic Classifier" in Configuration Guide > QoS Configuration.
3. Create a traffic behavior and enter the traffic behavior view.
   
   
   ```
   [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
   ```
   
   By default, no traffic behavior is created.
4. Enable intelligent traffic analysis for TCP flows globally.
   
   
   ```
   [traffic-analysis enable](cmdqueryname=traffic-analysis+enable)
   ```
   
   By default, intelligent traffic analysis for TCP flows is disabled globally.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Configure a traffic policy.
   
   
   
   For details, see "Configuring a Traffic Policy" in Configuration Guide > QoS Configuration > MQC Configuration.
7. Apply the traffic policy globally.
   
   
   
   For details, see "Applying a Traffic Policy" in Configuration Guide > QoS Configuration.
8. (Optional) Enable intelligent traffic analysis for unidirectional TCP flows.
   
   
   ```
   [traffic-analysis tcp one-way](cmdqueryname=traffic-analysis+tcp+one-way) sequence sequence-value sequence-mask
   ```
   
   
   
   By default, intelligent traffic analysis for unidirectional TCP flows is disabled.
   
   When packets of a specified TCP flow traverse the same path in both directions, you can enable intelligent traffic analysis for the TCP flow to obtain information about this flow. In scenarios such as M-LAG and ECMP, however, packets of a specified TCP flow may traverse a different path for each direction. In this case, you can enable intelligent traffic analysis for unidirectional TCP flows.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```