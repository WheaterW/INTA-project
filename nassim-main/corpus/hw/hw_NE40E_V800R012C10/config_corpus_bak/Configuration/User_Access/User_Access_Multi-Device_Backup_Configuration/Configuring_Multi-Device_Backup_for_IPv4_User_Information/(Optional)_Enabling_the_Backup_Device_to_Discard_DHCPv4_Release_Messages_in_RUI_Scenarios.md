(Optional) Enabling the Backup Device to Discard DHCPv4 Release Messages in RUI Scenarios
=========================================================================================

This section describes how to enable the backup device to discard DHCPv4 Release messages sent by users, so that the logout reasons recorded on the master and backup devices are the same.

#### Context

In RUI scenarios, if both the master and backup devices receive DHCPv4 Release messages, the logout reason recorded on the master and backup devices may be different due to a time sequence problem. To resolve this problem, you can enable the backup device to directly discard DHCPv4 Release messages without processing.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**access packet dhcp release rui-slave discard**](cmdqueryname=access+packet+dhcp+release+rui-slave+discard)
   
   
   
   The backup device is enabled to discard DHCPv4 Release messages in RUI scenarios.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.