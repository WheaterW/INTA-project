(Optional) Configuring a Session ID Range for PPPoE Users
=========================================================

This section describes how to configure a range of session IDs that can be assigned to PPPoE users. This configuration prevents hot backup failures caused by session ID conflicts in an RUI scenario where one MAC address is mapped to multiple sessions.

#### Context

In an RUI scenario where one MAC address is mapped to multiple sessions, users with the same MAC address may go online from different devices and be assigned the same session ID. In this case, if the master device backs up user data to the backup device, certain users may fail to go online due to a session ID conflict. Therefore, you can configure different session ID ranges on the master and backup devices to prevent the devices from assigning the same session ID to users.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pppoe-server rui remote-mac session-id**](cmdqueryname=pppoe-server+rui+remote-mac+session-id) **start-session-id** *start-session-id* **end-session-id** *end-session-id*
   
   
   
   A session ID range is configured for PPPoE users.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.