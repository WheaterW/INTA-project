Configuring User Testing
========================

User testing is used to locate a fault by checking whether a user can pass the authentication of a RADIUS server group when the AAA server does not function properly.

#### Context

In the following RADIUS attribute configuration, Step 3 and Step 4 can be configured based on service requirements.

Perform the following steps on the Router:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The password must be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
* For security purposes, you are advised to specify the ciphertext mode. To improve the device security, periodically change the password.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-test-group**](cmdqueryname=radius-test-group) *radius-test-group-name*
   
   
   
   The RADIUS server test template is configured.
3. Run **include** [ **authentication** | **accounting** ] { *radius-attr-name* **auto** | *radius-attr-name* *radius-attribute-value* | **user-password** *user-password* | **chap-password** *chap-password* }
   
   
   
   The RADIUS attributes to be sent are added to the RADIUS server test template.
4. Run [**exclude**](cmdqueryname=exclude) [ **authentication** | **accounting** ] **radius-attribute-name**
   
   
   
   The RADIUS attributes that are excluded from the RADIUS server test template are configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

Run the [**test-aaa**](cmdqueryname=test-aaa) *user-name* *password* [ **password random** [ *random1* *random2* ] **timestamp** [ *timestamp1* *timestamp2* ] ] **radius-group** *group-name* [ **radius-server** { *ip-address* | *ipv6-address* } [ **vpn-instance** *vpn-instancename* ] *port-number* ] [ **nas-ip-address** *nas-ip-address* ] [ **chap** | **pap** ] [ **test-group** *test-group-name* ] [ **trace** ] command in any view to check whether a user can pass the authentication of the RADIUS server group.