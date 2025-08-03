(Optional) Configuring RADIUS Attributes
========================================

To enable attributes delivered by a RADIUS server through
CoA packets or RADIUS to take effect, you must configure these attributes on the NE40E.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**value-added-service edsg modify-synchronous**](cmdqueryname=value-added-service+edsg+modify-synchronous) *attribute-name*
   
   
   
   A specified attribute is enabled to take effect upon activation
   or deactivation of EDSG services.
4. Run [**value-added-service edsg accounting interim send-update
   user-ip enable**](cmdqueryname=value-added-service+edsg+accounting+interim+send-update+user-ip+enable) 
   
   
   
   The device is enabled to send a real-time accounting packet
   carrying the HW-Acct-Update-Address (26-159) attribute with a value
   of 1 for EDSG services when the user address changes.