Configuring MQC-based VLAN Mapping
==================================

Configuring MQC-based VLAN Mapping

#### Context

Modular QoS command line interface (MQC) can be used to implement VLAN mapping for classified packets. Packets can be classified based on matching rules in a traffic classifier. To re-mark the VLAN IDs in classified packets, configure a traffic policy to associate a traffic classifier with a traffic behavior defining VLAN mapping.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a traffic classifier. For details, see "Configuring a Traffic Classifier" under "MQC Configuration" in *Configuration Guide > QoS Configuration*.
3. Configure a traffic behavior.
   1. Create a traffic behavior and enter the traffic behavior view, or enter the view of an existing traffic behavior.
      
      
      ```
      [traffic behavior](cmdqueryname=traffic+behavior) behavior-name
      ```
   2. Re-mark the outer VLAN tag of packets.
      
      
      ```
      [vlan-mapping vlan](cmdqueryname=vlan-mapping+vlan) vlan-id
      ```
   3. (Optional) Re-mark the inner VLAN tag of packets.
      
      
      ```
      [vlan-mapping inner-vlan](cmdqueryname=vlan-mapping+inner-vlan) inner-vlan-id
      ```
   4. Exit the traffic behavior view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Configure a traffic policy. For details, see "Configuring a Traffic Policy" under "MQC Configuration" in *Configuration Guide > QoS Configuration*.
5. Apply the traffic policy. For details, see "Applying a Traffic Policy" under "MQC Configuration" in *Configuration Guide > QoS Configuration*.

#### Verifying the Configuration

* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] command to check the traffic policy configuration.
* Run the [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) command to check records of applied traffic policies.