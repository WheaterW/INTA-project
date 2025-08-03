Verifying the CPOS-Trunk Interface Configuration
================================================

After configuring a CPOS-Trunk interface, check the configurations and status of the CPOS-Trunk interface.

#### Prerequisites

A CPOS-Trunk interface has been configured.


#### Procedure

* Run the [**display cpos-trunk**](cmdqueryname=display+cpos-trunk) *trunk-id* command to check the configurations of a CPOS-Trunk interface.
* Run the [**display interface**](cmdqueryname=display+interface) **trunk-serial** [ *trunk-serial-id* ] command to check the status and packet statistics of a specified or all trunk serial interfaces.
* Run the [**display ppp mp-global**](cmdqueryname=display+ppp+mp-global) [ **interface** *global-mp-group* *interface-number* ] command to check the configurations of a global MP-group interface.
* Run the [**display interface global-ima-group**](cmdqueryname=display+interface+global-ima-group) [ *global-ima-group-number* ] command to check configurations and status of a global IMA-group interface.