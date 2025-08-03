Enabling the Statistics Collection Function on a Sub-interface
==============================================================

After enabling the statistics collection function on a sub-interface, you can view the statistics about the received or sent packets on the sub-interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of the Ethernet sub-interface that requires the statistics collection function is displayed.
3. Run [**statistic enable**](cmdqueryname=statistic+enable)
   
   
   
   The statistics collection function is enabled on the Ethernet sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) In addition to running the [**statistic enable**](cmdqueryname=statistic+enable) command on a sub-interface to enable the statistics collection function, you can run the [**subinterface traffic-statistics enable**](cmdqueryname=subinterface+traffic-statistics+enable) command in the system view or Ethernet interface view to enable the statistics collection function in batches. Running the [**subinterface traffic-statistics enable**](cmdqueryname=subinterface+traffic-statistics+enable) command consumes a large number of system resources. Exercise caution when running this command. In addition, note the following points:
   * If this command is run in the system view, the traffic statistics collection function is enabled on all sub-interface of the device.
   * If this command is run in the view of a physical interface, the traffic statistics collection function is enabled on all sub-interfaces of the interface.