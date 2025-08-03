Verifying the Configuration
===========================

After traffic policing based on MF classification is successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, and configured queues and their application.

#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check traffic information on interfaces.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check bindings between all traffic classifiers and traffic behaviors or between a specified traffic classifier and a traffic behavior in a traffic policy.
* Run the [**display car resource**](cmdqueryname=display+car+resource) **slot** *slot-id* command to check the allocation of CAR resources.
* Run the [**display qos resource rule**](cmdqueryname=display+qos+resource+rule) { **aclv4** | **aclv6** | **l2acl** | **mpls** } **slot** *slot-id* command to check the ACL rule usage on each board.
* Run the [**display qos resource traffic-policy application**](cmdqueryname=display+qos+resource+traffic-policy+application) [ **slot** *slot-id* ] command to check the number of interfaces that have traffic policies bound and the number of interfaces to which traffic policies can still be bound.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) [ [ **name** ] *policy-name* ] **statistics** **interface** { *interface-name* | *interface-type* *interface-number* } [ [**vlan**](cmdqueryname=vlan) *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vid** *vid* | **ce-vid** *ce-vid* | **vid** *vid* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To check CAR statistics, you must specify the **classifier-based** parameter.