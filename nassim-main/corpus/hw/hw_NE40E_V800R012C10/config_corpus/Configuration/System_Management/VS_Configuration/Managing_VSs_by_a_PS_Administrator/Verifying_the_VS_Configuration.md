Verifying the VS Configuration
==============================

Verify the VS configuration as a PS administrator.

#### Prerequisites

All VS configurations are complete.


#### Procedure

* Run the [**display virtual-system**](cmdqueryname=display+virtual-system) [ **name** *vs-name* ] [ **verbose** ] command to check basic VS information.
* Run the [**display virtual-system**](cmdqueryname=display+virtual-system) [ **name** *vs-name* ] **resource** command to check resource information about a specified VS or all VSs of a PS.
  
  
  
  The parameter **name** is supported only on the Admin-VS.
* Run the [**display virtual-system resource-template**](cmdqueryname=display+virtual-system+resource-template) command to check resource template information about a specified VS or all VSs of a PS.
* Run the [**display virtual-system configuration state**](cmdqueryname=display+virtual-system+configuration+state) command to check the VS configuration status.