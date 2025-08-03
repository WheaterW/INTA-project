Checking the Configurations
===========================

After configuring the MCP, DCPs, and TLPs, check the IP FPM hop-by-hop performance statistics collection function.

#### Prerequisites

The IP FPM hop-by-hop performance statistics collection function has been configured.


#### Procedure

* Run the [**display ipfpm mcp**](cmdqueryname=display+ipfpm+mcp) command to check MCP configurations.
* Run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) command to check DCP configurations.
* Run the [**display ipfpm statistic-type**](cmdqueryname=display+ipfpm+statistic-type) { **loss** | **oneway-delay** | **twoway-delay** } **instance** *instance-id* **ach** *ach-id* [ **verbose** ] command to check the hop-by-hop performance statistics for a specified ACH.