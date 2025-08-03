Configuring an APN ID Instance
==============================

Configure an APN ID instance to set values for the fields in an APN ID template.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**apn**](cmdqueryname=apn)
   
   
   
   The APN view is created and displayed.
3. Run [**ipv6**](cmdqueryname=ipv6)
   
   
   
   The APN IPv6 view is created and displayed.
4. Run [**apn-id instance**](cmdqueryname=apn-id+instance) *instance-name*
   
   
   
   An APN ID instance is created, and its view is displayed.
5. Run [**template**](cmdqueryname=template) *template-name*
   
   
   
   An APN ID template is applied to the instance. The applied template must have been configured in the APN IPv6 view.
6. Run [**apn-field**](cmdqueryname=apn-field) *field-name* *field-value*
   
   
   
   A value is set for the app group or user group field.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.