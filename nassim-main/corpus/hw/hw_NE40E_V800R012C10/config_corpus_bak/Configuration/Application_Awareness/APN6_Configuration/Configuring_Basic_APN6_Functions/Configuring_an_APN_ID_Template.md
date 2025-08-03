Configuring an APN ID Template
==============================

An APN ID template defines a hierarchical structure of APN IDs. An APN ID is composed of three fields â APP-Group-ID, USER-Group-ID, and Reserved. You can configure an APN ID template to determine the total length of an APN ID, total length of application groups, total length of user groups, and length of a specific application or user group. After you apply the template to an APN ID instance, the system can generate APN IDs for this instance based on the template.

#### Pre-configuration Tasks

Before configuring APN6, apply for the APN6 license and run the [**license active**](cmdqueryname=license+active) command to activate the license file that contains APN6 resources.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**apn**](cmdqueryname=apn)
   
   
   
   The APN view is created and displayed.
3. Run [**ipv6**](cmdqueryname=ipv6)
   
   
   
   The APN IPv6 view is created and displayed.
4. (Optional) Run [**apn-id inherit**](cmdqueryname=apn-id+inherit) {**enable** | **disable** }
   
   
   
   The APN ID inheritance function is configured.
5. Run [**apn-id template**](cmdqueryname=apn-id+template) *template-name*[**length** *total-length* { [ **app-group** *app-group-length* ] | [ **user-group** *user-group-length* ] }*\** ]
   
   
   
   A template is created, and its view is displayed.
6. Perform the following operations as required.
   
   
   * Run the [**app-group index**](cmdqueryname=app-group+index) *index-value* *field-name* [**length**](cmdqueryname=length) *field-length* command to configure a name and length for the application group field.
   * Run the [**user-group index**](cmdqueryname=user-group+index) *index-value* *field-name* [**length**](cmdqueryname=length) *field-length* command to configure a name and length for the user group field.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.