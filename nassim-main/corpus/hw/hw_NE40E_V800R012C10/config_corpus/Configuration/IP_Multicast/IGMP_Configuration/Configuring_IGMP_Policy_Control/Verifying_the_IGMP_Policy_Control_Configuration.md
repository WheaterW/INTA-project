Verifying the IGMP Policy Control Configuration
===============================================

After configuring IGMP Policy Control, verify the IGMP configuration and IGMP operating status.

#### Prerequisites

IGMP policy control has been configured.


#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of IGMP on an interface.
* Run the [**display cp-rate-limit**](cmdqueryname=display+cp-rate-limit) [ **slot** *slot-id* ] [ **verbose** ] command to check the information about all the users who use IGMP messages to launch attacks.
* Run the [**display cp-rate-limit**](cmdqueryname=display+cp-rate-limit) **interface** *interface-type* *interface-number* [ **vlan** *vlan-id* ] [ **verbose** ] command to check the information about the attackers on a specified interface.
* Run the [**display cp-rate-limit**](cmdqueryname=display+cp-rate-limit) **interface** *interface-type* *interface-number* **pe-vid** *pe-vid* **ce-vid** *ce-vid* [ **verbose** ] command to check the information about the attackers on a QinQ interface.