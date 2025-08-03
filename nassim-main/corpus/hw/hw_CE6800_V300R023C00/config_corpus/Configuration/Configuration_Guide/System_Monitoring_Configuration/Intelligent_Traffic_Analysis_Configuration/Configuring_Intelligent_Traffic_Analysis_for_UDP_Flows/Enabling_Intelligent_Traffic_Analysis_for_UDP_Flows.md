Enabling Intelligent Traffic Analysis for UDP Flows
===================================================

Enabling Intelligent Traffic Analysis for UDP Flows

#### Prerequisites

An ACL has been created by running the [**acl**](cmdqueryname=acl) command in the system view. Currently, only the following advanced ACL rules are supported. The ACL rules that are not supported cannot be delivered, preventing the TAP from receiving corresponding service flows.

* UDP + destination IPv4 address + source IPv4 address + destination UDP port number

![](public_sys-resources/note_3.0-en-us.png) 

In intelligent traffic analysis for UDP flows, the **deny** or **permit** action specified in an ACL rule does not take effect. Service flows are sent to the TAP for processing as long as they match the preceding advanced ACL rules.




#### Context

After intelligent traffic analysis for UDP flows is enabled, the device can perform in-depth analysis on specified UDP flows and send analysis results to the analyzer for further analysis and graphical display.

Intelligent traffic analysis for UDP flows is performed on a per-block basis. Therefore, after enabling this function, configure the number of blocks in a UDP flow to be intelligently analyzed.

You can use MQC to implement intelligent traffic analysis for UDP flows by defining the [**traffic-analysis enable**](cmdqueryname=traffic-analysis+enable) action in an MQC traffic behavior.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure PTP clock synchronization, that is, the 1588v2 function.
   
   
   
   For details, see "Configuring Basic 1588v2 Functions" in Configuration Guide > 1588v2 (PTP) Configuration.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If 1588v2 has been configured on the device and takes effect, IPv4 UDP flow analysis supports nanosecond-level delay measurement. Otherwise, IPv4 UDP flow analysis supports microsecond-level delay measurement.
3. Configure a traffic classifier.
   
   
   
   For details, see "Configuring a Traffic Classifier" in Configuration Guide > QoS Configuration.
4. Create a traffic behavior and enter the traffic behavior view.
   
   
   ```
   [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
   ```
   
   By default, no traffic behavior is created.
5. Enable intelligent traffic analysis for UDP flows globally.
   
   
   ```
   [traffic-analysis enable](cmdqueryname=traffic-analysis+enable)
   ```
   
   By default, intelligent traffic analysis for UDP flows is disabled globally.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Configure a traffic policy.
   
   
   
   For details, see "Configuring a Traffic Policy" in Configuration Guide > QoS Configuration > MQC Configuration.
8. Apply the traffic policy globally.
   
   
   
   For details, see "Applying a Traffic Policy" in Configuration Guide > QoS Configuration.
9. Configure the number of blocks in a UDP flow to be intelligently analyzed.
   
   
   ```
   [traffic-analysis udp identification block](cmdqueryname=traffic-analysis+udp+identification+block) number
   ```
   
   By default, a UDP flow is divided into 256 blocks for intelligent traffic analysis.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```