Verifying the Configuration
===========================

After configuring route attribute sets, verify the configuration.

#### Prerequisites

Route attribute sets have been configured.


#### Procedure

* Run the [**display xpl**](cmdqueryname=display+xpl) { **as-path-list** | **community-list** | **ext-community-list rt** | **ext-community-list soo** | **ip-prefix-list** | **ipv6-prefix-list** | **route-filter** | **rd-list** | **route-flow-group** | **interface-list** } [ **name** *xpl-name* **attachpoints** ] command to check the configurations of XPL route attribute sets or the detailed information about the set references by routing protocols.
* Run the [**display xpl**](cmdqueryname=display+xpl) { **as-path-list** | **community-list** | **ext-community-list rt** | **ext-community-list soo** | **ip-prefix-list** | **ipv6-prefix-list** | **rd-list** | **route-filter** | **route-flow-group** | **interface-list** } **state** [ **attached** | **unattached** ] command to check information about XPL route attribute set configurations and references.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  To check detailed XPL configurations, run the [**display current-configuration**](cmdqueryname=display+current-configuration) **configuration** **xpl** command.