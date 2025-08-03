Binding Output Multicast Streams to a Multicast Instance
========================================================

This section describes how to bind output multicast streams to a multicast instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast-nat bind-list**](cmdqueryname=multicast-nat+bind-list)
   
   
   
   The multicast NAT binding view is displayed.
3. Run [**multicast-nat outbound**](cmdqueryname=multicast-nat+outbound)  **id**  *outbound-id*  [ **name**  *outbound-name* ] **bind instance**  **id**  *instance-id*  [ **name**  *instance-name* ] [ **switch-mode****clean-switch** [ **switch-field** { **first-field** | **second-field** } ] [ **fast-mode** ] ]
   
   
   
   Output multicast streams are bound to a multicast instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If **fast-mode** is specified, you can run the [**set multicast-nat outbound-id**](cmdqueryname=set+multicast-nat+outbound-id)*outbound-id-value* **bind** **instance-id** *instance-id-value* [ **clean-switch** [ **first-field** | **second-field** ] ] **fast-mode** command to enable fast binding switching.
4. (Optional) Run [**multicast-nat clean-switch interval**](cmdqueryname=multicast-nat+clean-switch+interval)*interval-value*
   
   
   
   The interval at which two adjacent multicast NAT clean switching commands are delivered is configured.
   
   
   
   If clean switching needs to be frequently performed on multicast streams through configuration scripts or other methods that support batch operations, the interval at which two adjacent multicast NAT clean switching commands are delivered needs to be limited. By default, the interval at which two adjacent multicast NAT clean switching commands are delivered is 500 ms. To set the interval as required, perform this step.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the interval at which two adjacent multicast NAT clean switching commands are delivered is less than 500 ms, artifacts may occur.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.