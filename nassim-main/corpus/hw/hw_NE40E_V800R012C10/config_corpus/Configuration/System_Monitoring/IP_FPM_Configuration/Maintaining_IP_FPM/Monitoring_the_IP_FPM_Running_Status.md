Monitoring the IP FPM Running Status
====================================

This section describes how to monitor the IP FPM running status.

#### Context

In routine maintenance, you can run the following display commands in any view to check IP FPM performance statistics and learn the IP FPM running status.


#### Procedure

* Run the [**display ipfpm statistic-type**](cmdqueryname=display+ipfpm+statistic-type) { **loss** | **oneway-delay** | **twoway-delay** } **instance** *instance-id* [ **verbose** ] command to check the performance statistics for a specified IP FPM instance.
* Run the [**display ipfpm statistic-type**](cmdqueryname=display+ipfpm+statistic-type) { **loss** | **oneway-delay** | **twoway-delay** } **instance** *instance-id* **ach** *ach-id* [ **verbose** ] command to check the hop-by-hop performance statistics for a specified ACH.