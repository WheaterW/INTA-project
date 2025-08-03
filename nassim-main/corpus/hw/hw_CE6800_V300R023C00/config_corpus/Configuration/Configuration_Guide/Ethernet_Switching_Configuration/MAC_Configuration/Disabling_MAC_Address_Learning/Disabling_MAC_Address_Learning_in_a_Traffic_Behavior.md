Disabling MAC Address Learning in a Traffic Behavior
====================================================

Disabling MAC Address Learning in a Traffic Behavior

#### Context

You can disable MAC address learning in a traffic behavior in the following scenarios:

* A device learns the MAC address from the first received packet. If the address is fixed and the network is stable, the device does not need to relearn the address. To save MAC addresses and improve device running efficiency, apply a traffic policy and disable MAC address learning in all the traffic classifiers bound to the traffic policy.
* Some unauthorized users may send a large number of packets with frequently changed MAC addresses to attack network devices. To prevent MAC address overflow and deterioration in device performance, apply a traffic policy and disable MAC address learning in all the traffic classifiers bound to the traffic policy.


#### Procedure

1. Configure a traffic classifier.
   
   
   
   | Step | Command |
   | --- | --- |
   | Enter the system view. | [**system-view**](cmdqueryname=system-view) |
   | Create a traffic classifier and enter the traffic classifier view, or enter the view of an existing traffic classifier. | [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **type** { **and** | **or** } ] |
   | Define matching rules in the traffic classifier.  Multiple types of matching rules can be defined for a traffic classifier. For details, see "MQC Configuration" in CLI Configuration Guide > QoS Configuration. | [**if-match**](cmdqueryname=if-match) |
   | Exit from the traffic classifier view. | [**quit**](cmdqueryname=quit) |
   | Commit the configurations. | [**commit**](cmdqueryname=commit) |
2. Configure a traffic behavior.
   
   
   
   | Step | Command |
   | --- | --- |
   | Create a traffic behavior and enter the traffic behavior view. | [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name* |
   | Disable MAC address learning in the traffic behavior view. | [**mac-address learning disable**](cmdqueryname=mac-address+learning+disable) |
   | Exit from the traffic behavior view. | [**quit**](cmdqueryname=quit) |
   | Commit the configurations. | [**commit**](cmdqueryname=commit) |
3. Configure a traffic policy.
   
   
   
   | Step | Command |
   | --- | --- |
   | Create a traffic policy and enter the traffic policy view, or enter the view of an existing traffic policy. | [**traffic policy**](cmdqueryname=traffic+policy) *policy-name* |
   | Bind the traffic behavior and traffic classifier in the traffic policy. | [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name* [ **precedence** *precedence-value* ] |
   | Exit from the traffic policy view. | [**quit**](cmdqueryname=quit) |
   | Commit the configurations. | [**commit**](cmdqueryname=commit) |
4. Apply the traffic policy. Specify a mode in which the traffic policy takes effect as needed.
   
   
   
   | Step | | Command |
   | --- | --- | --- |
   | Apply the traffic policy to an interface. | Enter the Layer 2 interface view. | [**interface**](cmdqueryname=interface) *interface-type* *interface-number* |
   | Apply the traffic policy to the interface. | [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** |
   | Apply the traffic policy to a VLAN. | Enter the VLAN view. | [**vlan**](cmdqueryname=vlan) *vlan-id* |
   | Apply the traffic policy to the VLAN. | [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound** |
   | Apply the traffic policy globally. | | [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **global** [ **slot** *slot-id* ] **inbound** |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] command to check whether MAC address learning is successfully disabled in a traffic behavior.