Enabling Last-Mile QoS
======================

You must enable last-mile QoS before configuring it.

#### Context

The NE40E allows you to configure last-mile QoS in the AAA domain view. The configuration in the AAA domain view takes effect for only the L2TP service.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**qos link-adjustment remote enable**](cmdqueryname=qos+link-adjustment+remote+enable)
   
   
   
   Last-mile QoS is enabled in the AAA domain view.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.