Verifying the Configuration
===========================

After MF classification-based traffic policies for VXLAN packets are successfully configured, you can check the traffic classifiers, traffic behaviors, bindings between traffic classifiers and behaviors in the specified traffic policy, configured traffic policies and their application, as well as configured queues and their application.

#### Procedure

* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check bindings between all traffic classifiers and traffic behaviors or between a specified traffic classifier and a traffic behavior in a traffic policy.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) **statistics** { **bridge-domain** *bdid* **vxlan-mode** | **vpn-instance** *vpn-name* **vxlan-mode** } { **inbound** | **outbound** } [ **verbose** { **classifier-based** [ **class** *class-name* ] | **rule-based** [ **class** *class-name* ] [ **filter** ] } ] command to check traffic policy statistics on interfaces.
  
  
  
  In VS mode, this command is supported only by the admin VS.