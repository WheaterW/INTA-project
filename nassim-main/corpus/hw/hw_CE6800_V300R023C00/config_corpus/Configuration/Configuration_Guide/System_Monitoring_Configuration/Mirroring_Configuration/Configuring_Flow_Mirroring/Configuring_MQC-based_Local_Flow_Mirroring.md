Configuring MQC-based Local Flow Mirroring
==========================================

Configuring MQC-based Local Flow Mirroring

#### Prerequisites

The task of [Configuring an Observing Port](galaxy_mirror_cfg_0031.html) has been completed.


#### Context

In flow mirroring, packets of a specified service flow that passes through a mirrored port are copied to an observing port, which then sends the packets to a monitoring device. MQC-based flow mirroring filters specific service flows using various matching rules in traffic classifiers. To configure MQC-based flow mirroring, apply a traffic policy containing flow mirroring behaviors to the system, a VLAN, an interface, or a VPN instance. Local MQC-based flow mirroring is used when an observing port is directly connected to a monitoring device.

![](public_sys-resources/note_3.0-en-us.png) 

* During the configuration of flow mirroring, the action defined in an ACL rule must be set to permit.
* When the logging function is configured for packets matching a traffic classifier (the **logging** parameter is specified in the [**rule**](cmdqueryname=rule) command) and the mirroring function is configured on the device, the mirroring function does not take effect for the packets matching the traffic classifier. To mirror such packets, delete the **logging** parameter in the [**rule**](cmdqueryname=rule) command.
* For fragments, flow mirroring mirrors the reassembled packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a traffic classifier. For details, see "Configuring a Traffic Classifier" under "MQC Configuration" in Configuration Guide > QoS Configuration.
3. Configure a traffic behavior.
   1. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Mirror traffic to an observing port or an observing port group.
      
      
      ```
      [mirroring observe-port](cmdqueryname=mirroring+observe-port) { observe-port-index | group group-id }
      ```
   3. Exit the traffic behavior view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Configure a traffic policy. For details, see "Configuring a Traffic Policy" under "MQC Configuration" in Configuration Guide > QoS Configuration.
5. Apply the traffic policy. For details, see "Applying a Traffic Policy" under "MQC Configuration" in Configuration Guide > QoS Configuration.

#### Verifying the Configuration

* Run the [**display port-mirroring**](cmdqueryname=display+port-mirroring) command to check the mirroring configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] command to check the traffic policy configuration.
* Run the [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) command to check records of applied traffic policies.