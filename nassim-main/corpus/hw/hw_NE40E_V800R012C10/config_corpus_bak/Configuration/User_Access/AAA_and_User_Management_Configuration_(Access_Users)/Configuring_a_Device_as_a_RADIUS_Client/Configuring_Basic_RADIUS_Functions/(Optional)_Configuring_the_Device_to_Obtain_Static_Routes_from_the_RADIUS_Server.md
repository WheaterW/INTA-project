(Optional) Configuring the Device to Obtain Static Routes from the RADIUS Server
================================================================================

(Optional)_Configuring_the_Device_to_Obtain_Static_Routes_from_the_RADIUS_Server

#### Context

The device can periodically or immediately synchronize static routes with those delivered by the RADIUS server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa route-download**](cmdqueryname=aaa+route-download) **server-group** *group-name* **base-user-name** *user-name* **password** { **simple** | **cipher** } *password* [ **download-interval** *interval-value* | **retry-interval** *retry-interval-value* | **retry-max-count** *retry-count* | **tag** *tag-value* | **cost** *cost-value* | **synchronization** *synchronization* ]
   
   
   
   The device is configured to periodically synchronize static routes with those delivered by the RADIUS server.
3. (Optional) Run [**aaa route-download**](cmdqueryname=aaa+route-download) **recover-delay** *delay-time*
   
   
   
   The device is configured to delay advertising static routes downloaded from a RADIUS server after the device is restarted and configurations are restored.
   
   
   
   In multi-device backup scenarios, if the [**aaa route-download**](cmdqueryname=aaa+route-download) command is run to configure a device to periodically synchronize static routes with those delivered by the RADIUS server, the [**aaa route-download recover-delay**](cmdqueryname=aaa+route-download+recover-delay) command must also be run. After the [**aaa route-download recover-delay**](cmdqueryname=aaa+route-download+recover-delay) command is run, static routes downloaded from a RADIUS server are advertised after a delay following a device restart and successful backup of user information. In this case, when the master device is restarted, the network-side traffic is switched to the new master device, preventing a traffic detour.
4. (Optional) Run [**clear ip routes aaa-download**](cmdqueryname=clear+ip+routes+aaa-download) [ [ **vpn-instance** *vpn-name* ] [ *ip-address* *mask-len* | *ipv6-address* *prefix-length* ] | **all** ]
   
   
   
   The static routes delivered by the RADIUS server are cleared.
5. (Optional) Run [**aaa route-download now force**](cmdqueryname=aaa+route-download+now+force)
   
   
   
   The device is configured to immediately synchronize static routes with those delivered by the RADIUS server.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.