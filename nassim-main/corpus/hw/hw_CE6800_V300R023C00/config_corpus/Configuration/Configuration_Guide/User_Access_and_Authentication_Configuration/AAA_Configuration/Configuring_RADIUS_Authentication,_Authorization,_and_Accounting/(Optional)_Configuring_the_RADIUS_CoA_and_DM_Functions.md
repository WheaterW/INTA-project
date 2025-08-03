(Optional) Configuring the RADIUS CoA and DM Functions
======================================================

(Optional) Configuring the RADIUS CoA and DM Functions

#### Context

The device supports the RADIUS CoA and DM functions. CoA provides a mechanism to dynamically change the rights of online users, and DM provides a mechanism to disconnect users.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IP address for a RADIUS authorization server.
   
   
   ```
   [radius-server authorization](cmdqueryname=radius-server+authorization) ip-address [ vpn-instance vpn-instance-name ] shared-key cipher key-string [ server-group group-name ] [ protect enable ]
   ```
   
   By default, no RADIUS authorization server is configured.
3. Configure a port number for the RADIUS authorization server.
   
   
   ```
   [radius-server authorization](cmdqueryname=radius-server+authorization) port port-id
   ```
   
   By default, the port number of a RADIUS authorization server is 3799.
4. Configure the local IP address of the socket whose local UDP port number ranges from 1024 to 55535.
   
   
   ```
   [radius local-ip](cmdqueryname=radius+local-ip) ip-address [ vpn-name ]
   ```
   
   Or:
   
   ```
   [radius local-ip](cmdqueryname=radius+local-ip) any
   ```
   
   By default, the local IP address of the socket whose local UDP port number ranges from 1024 to 55535 is not configured.
   
   The [**radius local-ip**](cmdqueryname=radius+local-ip) **any** command sets the local IP address of the socket whose local UDP port number ranges from 1024 to 55535 to any IP address. For security purposes, you are advised not to run the [**radius local-ip**](cmdqueryname=radius+local-ip) **any** command.
5. (Optional) Configure the device to match the RADIUS attributes in the received CoA or DM Request packets against user information on the device.
   
   
   ```
   [radius-server authorization match-type](cmdqueryname=radius-server+authorization+match-type) { any | all }
   ```
   
   By default, the device matches the RADIUS attributes in the received CoA or DM Request packets against user information on the device in **any** mode. That is, the device matches an attribute with a high priority in a CoA or DM Request packet against user information on the device.
6. (Optional) Determine whether the device allows users to go online after authorization information check fails.
   
   
   ```
   authorization-info check-fail policy { online | offline }
   ```
   
   By default, a device allows users to go online after authorization information check fails.
7. (Optional) In the AAA view, configure the update mode of user authorization information delivered by the authorization server.
   
   
   ```
   authorization-modify mode { modify | overlay }
   ```
   
   By default, the update mode of user authorization information delivered by an authorization server is **overlay**.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```