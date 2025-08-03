Verifying the Configuration
===========================

After class-based QoS is successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, as well as configured queues and their application.

#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check traffic information about an interface.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check bindings between all traffic classifiers and traffic behaviors or between a specified traffic classifier and a traffic behavior in a traffic policy.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) **statistics** **interface** *interface-type* *interface-number* [ .*sub-interface* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics on an interface.
* Run the [**display flow-car**](cmdqueryname=display+flow-car) [ **ipv6** ] **statistics** { **source-ip** | **destination-ip** } [ *ip-address* ] **slot** *slot-id* { **inbound** | **outbound** } command to check flow CAR statistics in a specified direction on the board in a specified slot based on the source or destination IP address.
* Run the [**display traffic policy vpn-instance**](cmdqueryname=display+traffic+policy+vpn-instance) **brief** command to check the bindings between VPN instances and traffic policies.