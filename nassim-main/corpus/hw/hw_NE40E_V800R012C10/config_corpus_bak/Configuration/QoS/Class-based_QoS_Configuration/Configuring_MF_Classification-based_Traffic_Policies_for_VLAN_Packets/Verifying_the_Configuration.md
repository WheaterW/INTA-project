Verifying the Configuration
===========================

After VLAN QoS is successfully configured, you can view the traffic classifiers, traffic behaviors, binding between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, and configured queues and their application.

#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check traffic information about an interface.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check bindings between all traffic classifiers and traffic behaviors or between a specified traffic classifier and a traffic behavior in a traffic policy.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) **statistics** **interface** *interface-type* *interface-number* [ .*sub-interface* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics on an interface.
* Run the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) **interface** *interface-type* *interface-number* [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics on an interface.
* Run the [**display traffic policy not-support policy**](cmdqueryname=display+traffic+policy+not-support+policy) *policy-name* **interface** *interface-type* *interface-number* **outbound** command to check rules that are not supported by a specified traffic policy in the downstream direction of a specified interface.
* Run the [**display traffic policy not-support**](cmdqueryname=display+traffic+policy+not-support) **policy** *policy-name* **slot** *slot-num* { **inbound** | **outbound** } **vsi-acl** **ac-mode** command to check rules and actions that are not supported by a specified traffic policy on a specified board.