(Optional) Configuring the RADIUS Server to Control User QoS
============================================================

(Optional)_Configuring_the_RADIUS_Server_to_Control_User_QoS

#### Context

The HW-Access-Service attribute delivered by the RADIUS server takes effect only when there are corresponding configurations on the device. After an access service template is configured, the RADIUS server can deliver the service template name and control user traffic by time segment. When the authentication response message sent by the RADIUS server includes the No. 83 HW-Access-Service attribute, the traffic bandwidth of online users is restricted based on the QoS profile rule bound to the service template. If an access service template contains a QoS profile without a time segment and another QoS profile with a time segment, the QoS profile with a time segment has a higher priority. If the QoS profile in an access service template is modified when a user is online, the latest QoS profile takes effect in real time. If all QoS profiles in a service template are deleted, the QoS profile before deletion takes effect for users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access-service**](cmdqueryname=access-service) *service-name*
   
   
   
   An access service template is created, and its view is displayed.
3. Run [**qos-profile**](cmdqueryname=qos-profile) *profile-name*
   
   
   
   The default QoS profile bound to the access service template is configured.
4. Run [**qos-profile**](cmdqueryname=qos-profile) *profile-name* **time-range** *time-range-name*
   
   
   
   The QoS profile with a time segment bound to the access service template is configured.
   
   
   
   Each access service template can be bound with up to 16 different time segments.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.