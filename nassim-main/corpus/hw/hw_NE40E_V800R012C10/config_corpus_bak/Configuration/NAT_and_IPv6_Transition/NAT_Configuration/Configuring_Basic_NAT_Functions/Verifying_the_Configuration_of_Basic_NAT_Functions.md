Verifying the Configuration of Basic NAT Functions
==================================================

After configuring basic NAT functions, verify the configuration.

#### Prerequisites

Basic NAT functions have been configured.


#### Procedure

* Run the [**display nat instance**](cmdqueryname=display+nat+instance) [ *instance-name* ] command to check the configuration of a NAT instance.
* Run the [**display nat address-usage**](cmdqueryname=display+nat+address-usage) [ **by-session** ] **instance** *instance-name* **address-group** *address-group-name* [ **slot** *slot-id* ] [ **verbose** ] command to check the public port usage of a NAT address pool.
* Run the [**display nat-policy template**](cmdqueryname=display+nat-policy+template) [ *template-name* ] command to check information about a NAT template.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**display nat address-usage**](cmdqueryname=display+nat+address-usage) and [**display nat-policy template**](cmdqueryname=display+nat-policy+template) commands are supported only on the NE40E-M2K and NE40E-M2K-B.