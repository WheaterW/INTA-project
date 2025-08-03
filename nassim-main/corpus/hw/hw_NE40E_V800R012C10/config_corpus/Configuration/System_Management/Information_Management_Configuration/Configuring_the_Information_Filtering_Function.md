Configuring the Information Filtering Function
==============================================

To reduce redundant and unnecessary information on the device, configure the information filtering function.

#### Usage Scenario

Some services, such as ARP or VRRP, generate a large amount of information within a short period of time. The information filtering function can be used to filter out redundant and unnecessary information on the device.


#### Pre-configuration Tasks

Before enabling the information filtering function, ensure that the device is powered on correctly and the self-test is successful.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following command to configure the information filtering function.
   
   
   * To filter out a specified log or trap, run the [**info-center filter-id**](cmdqueryname=info-center+filter-id) { *filter-id* | **bymodule-alias** *modname* *alias* } command.
     
     The specified log or trap is not generated or output to any direction.
   * To suppress the output of statistics about consecutive repeated logs, run the [**info-center statistic-suppress enable**](cmdqueryname=info-center+statistic-suppress+enable) command.
     
     If this function is enabled, only one of the repeated logs will be recorded.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Consecutive repeated logs have the same log ID and parameters, and no other logs exist between them.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display logbuffer**](cmdqueryname=display+logbuffer) command to check whether the log filtering function is effective.
  
  If the protocol status of the interface alternates between Up and Down after the [**info-center filter-id**](cmdqueryname=info-center+filter-id) **bymodule-alias** *modname* *alias* command is run to filter out the *alias* log of the *modname* module, the log information cannot be displayed after the [**display logbuffer**](cmdqueryname=display+logbuffer) command is run.