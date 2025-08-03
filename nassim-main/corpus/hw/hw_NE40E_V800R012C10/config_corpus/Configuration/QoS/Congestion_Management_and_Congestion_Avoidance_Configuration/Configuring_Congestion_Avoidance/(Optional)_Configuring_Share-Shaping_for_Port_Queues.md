(Optional) Configuring Share-Shaping for Port Queues
====================================================

When the outbound interfaces of port queues with different priorities are the same main interface, you can perform share-shaping for the port queues using the same scheduling mode.

#### Context

Perform the following steps on a main interface:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**port share-shaping**](cmdqueryname=port+share-shaping) { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } \* [ **pq** | **wfq** **weight** *weight-value* | **lpq** ] { *shaping-value* | **shaping-percentage** *shaping-percentage-value* } [ **pbs** *pbs-value* ]
   
   
   
   Share shaping is configured for PQs.
   
   
   
   If this command is run more than once on an interface, the latest configuration overrides the previous one.
   
   The [**port share-shaping**](cmdqueryname=port+share-shaping) and [**share-shaping (port queue view)**](cmdqueryname=share-shaping+%28port+queue+view%29) commands are mutually exclusive on an interface.
   
   This command cannot be
   configured on a trunk member interface, and the interface on which
   this command is configured cannot be added to a trunk interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.