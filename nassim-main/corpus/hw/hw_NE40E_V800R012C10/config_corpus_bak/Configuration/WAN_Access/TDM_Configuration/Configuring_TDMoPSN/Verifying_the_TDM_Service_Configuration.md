Verifying the TDM Service Configuration
=======================================

After a TDM service is configured, you cannot only view configurations and statuses of E1/CE1 interfaces, but also view information about the static PW and dynamic PW.

#### Context

Run the following commands to check the previous configuration.


#### Procedure

* Run the [**display controller e1**](cmdqueryname=display+controller+e1) *controller-number* command to check the configuration and status of the E1/CE1 interface.
* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) [ *vc-id* |**interface** *interface-type* *interface-number* |**state** { **down** | **up** } ] or [**display mpls static-l2vc brief**](cmdqueryname=display+mpls+static-l2vc+brief) command to check information about the static PW.
* Run the [**display mpls l2vc**](cmdqueryname=display+mpls+l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* ] or [**display mpls l2vc brief**](cmdqueryname=display+mpls+l2vc+brief) command to check information about the dynamic PW.