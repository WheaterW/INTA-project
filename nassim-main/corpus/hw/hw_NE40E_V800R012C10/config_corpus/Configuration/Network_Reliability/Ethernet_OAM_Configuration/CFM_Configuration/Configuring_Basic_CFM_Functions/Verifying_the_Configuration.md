Verifying the Configuration
===========================

After configuring basic Ethernet CFM functions, verify the configurations.

#### Prerequisites

The configurations of basic Ethernet CFM functions are complete.


#### Procedure

* Run the [**display cfm md**](cmdqueryname=display+cfm+md) [ *md-name* ] command to check the information about a maintenance domain (MD).
* Run the [**display cfm ma**](cmdqueryname=display+cfm+ma) [ **md** *md-name* [ **ma** *ma-name* ] ] command to check the information about a maintenance association (MA).
* Run the [**display cfm mep**](cmdqueryname=display+cfm+mep) [ **md** *md-name* [ **ma** *ma-name* [ mep-id *mep-id* ] ] ] command to check the information about a local maintenance association end point (MEP).
* Run the [**display cfm remote-mep**](cmdqueryname=display+cfm+remote-mep) [ [ **md** *md-name* [ **ma** *ma-name* [ **mep-id** *mep-id* ] ] ] | [ **md** *md-name* [ **ma** *ma-name* ] ] **cfm-state** { **disable** | **down** | **up** } ] command to check the information about a remote maintenance association end point (RMEP).
* Run the [**display cfm mip**](cmdqueryname=display+cfm+mip) [ **interface** *interface-type* *interface-number* | **level** *level* ] command to check the information about a maintenance association intermediate point (MIP).
* Run the [**display cfm default md**](cmdqueryname=display+cfm+default+md) command to check information about the default MD.
* Run the [**display oam global configuration**](cmdqueryname=display+oam+global+configuration) command to check the MAC address model for maintenance points (MPs).