Verifying the Configuration of UCL-based Traffic Policies
=========================================================

After UCL-based traffic policies are configured, you can view the information about the traffic policies on a specified interface or all interfaces and statistics about UCL-based traffic policies.

#### Procedure

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] [ | { **begin** | **exclude** | **include** } *regular-expression* ] command to check information about the traffic on an interface.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) { **system-defined**| **user-defined** } [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) { **system-defined** | **user-defined** } [ *policy-name* [ **classifier** *classifier-name* ] ] command to check associations between all traffic classifiers and traffic behaviors or between a specified traffic classifier and a traffic behavior in a traffic policy.