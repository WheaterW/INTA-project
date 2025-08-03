Configuring User Queues Based on a QoS Profile
==============================================

A QoS profile is the aggregate of QoS scheduling parameters. Configurable scheduling parameters for SQs include CIR, PIR, Flow Queue (FQ) profiles, and lengths for packet loss compensation of service profiles.

#### Context

In user access scenarios, the RADIUS attribute HW-QOS-Profile-Name (31) carried in received authentication packets can be used to dynamically specify a QoS rate limit profile for users. The prerequisite is that a QoS profile and scheduling parameters have been configured on the device. For details about the HW-QOS-Profile-Name (31) attribute, see the RADIUS attribute list in the product documentation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name*
   
   
   
   A QoS profile is defined and its view is displayed.
3. Run [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] | **cir** **cir-percentage** *cir-percentage-value* [ **pir** **pir-percentage** *pir-percentage-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } ]\* [ **inbound** | **outbound** ] [ **color-aware** ]
   
   
   
   CAR is configured to guarantee user traffic.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.