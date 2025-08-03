Configuring a QoS Profile
=========================

A QoS profile can be configured on an NE40E that functions as an LNS. A QoS profile contains user queue parameters and scheduling parameters. Different QoS applications can use the same QoS profile.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name*
   
   
   
   A QoS profile is created, and its view is displayed.
3. Run [**user-queue**](cmdqueryname=user-queue) **cir** *cir-value* [ [ **pir** *pir-value* ] [ **pbs** *pbs-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **flow-mapping** *mapping-name* ]  | [ **user-group-queue** *group-name* ] | [ **service-template** *service-template-name* ] ] \*[ **inbound** | **outbound** ]
   
   
   
   Queue scheduling parameters are set for user queues.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.