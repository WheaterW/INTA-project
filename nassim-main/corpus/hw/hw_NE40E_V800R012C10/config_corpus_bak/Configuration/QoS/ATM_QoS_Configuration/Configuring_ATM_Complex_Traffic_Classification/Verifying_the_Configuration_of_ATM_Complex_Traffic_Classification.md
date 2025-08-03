Verifying the Configuration of ATM Complex Traffic Classification
=================================================================

After ATM complex traffic classification is configured, you can view information about the configured traffic classifiers, traffic behaviors, traffic policies in which the specified classifiers and behaviors are associated, and traffic statistics on interfaces.

#### Context

Run the following commands to check the previous configurations.


#### Procedure

* Use the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined** | **user-defined** } [ *behavior-name* ] command to check the configuration of a traffic behavior.
* Use the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the configuration of a traffic classifier.
* Use the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check information about the associations of all traffic classifiers with traffic behaviors, or information about the association of a particular traffic classifier with a traffic behavior.
* Use the [**display traffic policy statistics**](cmdqueryname=display+traffic+policy+statistics) **interface** *interface-type* *interface-number* [ .*sub-interface* ] { **inbound** | **outbound** } [ **verbose** { **classifier-based** | **rule-based** } [ **class** *class-name* ] ] command to check information about the traffic policy statistics on an interface.