Defining a Traffic Behavior and Configuring Traffic Policing Actions
====================================================================

This section describes how to configure traffic policing actions for different traffic classifiers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is configured and its view is displayed.
3. Run [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } ] \* [ **summary** ] [ **color-aware** ] or [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } ] \* [ **summary** ] [ **color-aware** ] [ **limit-type pps** ] or [**car**](cmdqueryname=car) { **cir** **cir-percentage** *cir-percentage-value* [ **pir** **pir-percentage** *pir-percentage-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **remark dscp** *dscp* | **service-class** class **color** *color* ] } ] \* [ **color-aware** ]
   
   
   
   A traffic policing action is configured.
   
   
   
   You can specify different parameters as required.
   
   * To configure traffic policing with a single token bucket, specify **cir** and **cbs** and set **pbs** to 0.
   * To configure traffic policing with a single rate and two token buckets, specify **cir**, **cbs**, and **pbs**.
   * To configure traffic policing with two rates and two token buckets, specify **cir**, **pir**, **cbs**, and **pbs**.
   * **cir** and **pir** are expressed in kbit/s, and **cbs** and **pbs** are expressed in bytes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After CAR is configured and applied, you can run the [**display traffic policy statistics interface**](cmdqueryname=display+traffic+policy+statistics+interface) command to check CAR statistics.
   
   Applying a traffic policy configured with traffic policing to an interface affects the original [**qos car**](cmdqueryname=qos+car) command.
4. Run [**user-queue**](cmdqueryname=user-queue) **cir** *cir-value* [ [ **pir** *pir-value* ] | [ **flow-queue** *flow-queue-name* ] | [ **flow-mapping** *mapping-name* ] | [ **user-group-queue** *group-name* ] | [ **service-template** *service-template-name* ] ] \*
   
   
   
   Class-based HQoS scheduling is configured for the traffic behavior.
5. (Optional) Run [**flow-car**](cmdqueryname=flow-car) { **ipv6** | **ipv4-ipv6** } **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] **identifier** { **source-ip** | **destination-ip** }
   
   
   
   Independent rate limiting is performed for flows matching ACL rules based only on source or destination IPv6 addresses, or based on both source or destination IPv4 and IPv6 addresses.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

The NE40E supports the re-marking of the priority and color of packets after traffic policing. If the CoS of a packet is re-marked as EF, BE, CS6, or CS7, the packet can be re-marked only in green.