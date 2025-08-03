Configuring MQC-based Selective QinQ
====================================

Configuring MQC-based Selective QinQ

#### Context

MQC-based selective QinQ filters specified service flows using diverse matching rules configured in traffic classifiers and adds outer VLAN tags to packets matching those rules. This function is equivalent to a global, VLAN-based, or interface-based traffic policy associated with the traffic behavior of VLAN stacking.

![](public_sys-resources/note_3.0-en-us.png) 

* An interface learns the MAC address in the VLAN specified by the outer VLAN tag of QinQ packets.
* If single-tagged packets from a VLAN need to be transparently transmitted, do not specify the VLAN as the inner VLAN for selective QinQ.


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
   2. Configure the outer VLAN tag to be added to packets.
      
      
      ```
      [vlan-stacking vlan](cmdqueryname=vlan-stacking+vlan) vlan-id
      ```
   3. Exit the traffic behavior view and return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
4. Configure a traffic policy. For details, see "Configuring a Traffic Policy" under "MQC Configuration" in *Configuration Guide > QoS Configuration*.
5. Apply the traffic policy. For details, see "Applying a Traffic Policy" under "MQC Configuration" in *Configuration Guide > QoS Configuration*.
   
   
   
   A traffic policy can be applied globally, in a VLAN, or on an interface. A traffic policy defining VLAN stacking can be applied only to the inbound direction.

#### Verifying the Configuration

* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] command to check the traffic policy configuration.
* Run the [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) command to check records of applied traffic policies.