Creating an iNOF Customized Zone
================================

Creating an iNOF Customized Zone

#### Context

A device in an iNOF system can manage hosts connected to the system through zones. By default, the device has a default zone that cannot be deleted; however, you can also configure a customized zone. After the configuration is complete, if the IP address of a newly connected SNSD-enabled host has been added to a customized zone, the host is automatically added to this zone. The iNOF system can then monitor and manage the host.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Create an iNOF customized zone and enter the zone view. If the customized zone has been configured, directly enter the zone view.
   
   
   ```
   [zone](cmdqueryname=zone) zone-name
   ```
   
   By default, no iNOF customized zone is created, and a default zone exists on the device.
5. Add the IP addresses of zone members to the iNOF customized zone.
   
   
   * On an IPv4 network:
     ```
     [host](cmdqueryname=host) { ip-address | ip-address1 to ip-address2 }
     ```
   * On an IPv6 network:
     ```
     [host](cmdqueryname=host) { ipv6-address | ipv6-address1 to ipv6-address2 }
     ```
   
   By default, the IP addresses of zone members are not added to an iNOF customized zone.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * A member can be added to multiple zones.
   * You can run the [**host**](cmdqueryname=host) command to manually add members to a customized zone, but cannot manually add them to the default zone using this command. For details on how to add members to the default zone, see [(Optional) Configuring the Function of Automatically Adding Hosts to the iNOF Default Zone](galaxy_ai_inof_cfg_0011.html).
6. Exit the iNOF customized zone view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```