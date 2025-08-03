Checking the Configurations
===========================

After configuring the MCP, DCPs, and TLPs, check the IP FPM end-to-end performance statistics collection function.

#### Prerequisites

The IP FPM end-to-end performance statistics collection function has been configured.


#### Procedure

* Run the [**display ipfpm mcp**](cmdqueryname=display+ipfpm+mcp) command to check MCP configurations.
* Run the [**display ipfpm dcp**](cmdqueryname=display+ipfpm+dcp) command to check DCP configurations.
* Run the [**display ipfpm statistic-type**](cmdqueryname=display+ipfpm+statistic-type) { **loss** | **oneway-delay** | **twoway-delay** } **instance** *instance-id* [ **verbose** ] command to check the performance statistics for a specified IP FPM instance.