Verifying the Configuration
===========================

After configuring static PW FRR, verify configured static PW information.

#### Prerequisites

Static PW FRR has been configured.


#### Procedure

* Run the [**display mpls static-l2vc**](cmdqueryname=display+mpls+static-l2vc) [ *vc-id* | **interface** *interface-type* *interface-number* | **state** { **down** | **up** } | **brief** ] command to check information about a static PW on the PEs at both ends of the PW.
* Run the [**display mpls switch-l2vc**](cmdqueryname=display+mpls+switch-l2vc) [ **brief** | **state** { **up** | **down** } | *ip-address* *vc-id* **encapsulation** *encapsulation-type* ] command to check static PW switching information on the SPE.