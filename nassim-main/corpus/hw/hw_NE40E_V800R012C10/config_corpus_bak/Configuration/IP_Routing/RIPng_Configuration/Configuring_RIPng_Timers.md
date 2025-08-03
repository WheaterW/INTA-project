Configuring RIPng Timers
========================

There are four RIPng timers: Update, Age, Suppress, and Garbage-collect timers. You can adjust the RIPng convergence speed by changing the values of the RIPng timers.

#### Usage Scenario

The value of *update* is less than that of *age*, and the value of *suppress* is less than that of *garbage-collect*. Setting improper values for the timers affects RIP convergence speed and even causes route flapping on the network. For example, if the value of *update* is greater than that of *age*, a device cannot inform its neighbors of the change of RIP routes immediately. Configuring Suppression timers can prevent routing loops. For details, see [Configuring Suppression Timers](dc_vrp_ripng_cfg_0012.html).


#### Pre-configuration Tasks

Before configuring RIPng timers, complete the following tasks:

* Configure IPv6 addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIPng Functions](dc_vrp_ripng_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ripng**](cmdqueryname=ripng) [ *process-id* ]
   
   
   
   A RIPng process is created, and the RIPng view is displayed.
3. Run [**timers ripng**](cmdqueryname=timers+ripng) *update* *age* *suppress* *garbage-collect*
   
   
   
   RIPng timers are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is submitted.

#### Checking the Configurations

Run the following commands to check the previous configuration.

* Run the [**display ripng**](cmdqueryname=display+ripng) command to view the values of RIPng timers.