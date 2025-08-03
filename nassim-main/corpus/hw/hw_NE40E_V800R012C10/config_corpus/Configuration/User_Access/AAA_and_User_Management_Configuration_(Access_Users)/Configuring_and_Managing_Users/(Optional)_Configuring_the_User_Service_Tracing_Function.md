(Optional) Configuring the User Service Tracing Function
========================================================

(Optional) Configuring the User Service Tracing Function

#### Context

You can configure this function during fault diagnosis. Using the service tracing function decreases the performance of the NE40E to some extent. Therefore, you are recommended to use this function only when you need to locate faults. This function is not enabled in normal cases.

Step 3 and Step 4 can be performed as required. If this function is enabled when the status of a large number of users changes, you need to configure the objects to be traced as accurately as possible to avoid consumption of too many device resources. Otherwise, normal user services will be affected.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**trace enable**](cmdqueryname=trace+enable) command to enable the service tracing function.
3. Run the [**trace access-user object**](cmdqueryname=trace+access-user+object) *id* { **interface** { *interface-name* | *interface-type* *interface-number* } | **ip-address** *ip-address* | **mac-address** *mac-address* | **ce-vlan** *ce-vid* | **pe-vlan** *pe-vid* | **ipv6-address** *prefix-address/prefix-length* | **user-name** *username* | **tunnel-id** *tunnel-id* | **access-mode** { **pppoe** | **ipoe** } }\* [ **output** { **file** *file-name* [ **anonymize** **personal-data** ] | **syslog-server** *ip-address* [ **bind** **ssl-policy** *ssl-policy-name* ] [ **anonymize** **personal-data** ] | **vty** } | [ **-t** *time-value* ] | [ **mode** **packet** ] | [ **flow-report** ]]\*
   
   
   
   or [**trace access-user**](cmdqueryname=trace+access-user) **object** *object-id* **calling-number** [ **output** { **file** *file-name* | **syslog-server** *ip-address* | **vty** }] [ **mode** **packet** ] [ **-t** *time* ] [| **include** ] **calling-number-content** *text*
   
   or [**trace access-user**](cmdqueryname=trace+access-user) **object** *object-id* { **circuit-id** *text* | **remote-id** *text* }\* { **exact-match** | **partial-match** } [ **output** { **file** *file-name* | **syslog-server** *ip-address*[ **bind** **ssl-policy** *ssl-policy-name* ] | **vty** } | **-t** *time* | **mode** **packet** | **flow-report** ]\* command to create a service tracing object and configure the information output position, SSL policy to be bound to the tracing object, and aging time.
4. Run the [**trace access-user object online-fail top**](cmdqueryname=trace+access-user+object+online-fail+top) *topnum* [ **-t** *time-value* ] command to configure the device to sort the causes of user login failures in descending order by how many times a user login failure occurs within 20 minutes. For the top *topNum* user login failure causes, the device identifies the last user who failed to log in successfully among the login failure records based on each failure cause and automatically traces the user based on the MAC address.
   
   
   
   The device can trace the top 5 login failure causes at a time to locate the last users who failed to log in successfully. That is, the device can concurrently trace a maximum of five users who experienced a login failure.