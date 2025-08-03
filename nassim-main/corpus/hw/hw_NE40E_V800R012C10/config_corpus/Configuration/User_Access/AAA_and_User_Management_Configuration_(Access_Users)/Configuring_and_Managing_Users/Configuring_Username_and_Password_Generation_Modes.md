Configuring Username and Password Generation Modes
==================================================

Users such as binding authentication users do not need to enter the username or password when going online. Username and password generation modes can be configured on the NE40E.

#### Procedure

* Configure a username generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run any of the following commands to configure a username generation mode:
     
     
     
     A username consists of a pure username and a domain name. Generally, there are two formats: pure username + domain name delimiter + domain name (for example, username@domainname); domain name + domain name delimiter + pure username (for example, domainname@username). The following commands are about the generation modes of pure usernames.
     
     
     
     + Run the [**default-user-name**](cmdqueryname=default-user-name) [ **template** *template-name* ] **include** { **sysname** [ *separator* ] | **gateway-address** *separator* [ *username-seperator* ] | **ip-address** *separator* [ *username-seperator* ] | **ipv6-address** { **compressed** | **preferred** *seperator* } [ *username-seperator* ] | **delegation-prefix** [ *username-seperator* ] | **mac-address** { *separator* | **noseparator** } [ *username-seperator* ] | { **option82** [ *username-seperator* | { **sub-option** *suboption-id1* [ **offset** *offset1* ] **parse-mode** { **auto-identify** [ *length* ] | **string** [ *length* ] | **binary** *length* | **hex** [ *length* ] { **class1** | **class2** | **class3** } } [ *username-seperator* ] } &<1-4> ] | **access-line-id** [ *separator* | { **circuit-id** [ **offset** *offset1* ] **parse-mode** { **auto-identify** [ *length* ] | **string** [ *length* ] | **binary** *length* | **hex** [ *length* ] { **class1** | **class2** | **class3** } } *username-seperator* | **remote-id** [ **offset** *offset1* ] **parse-mode** { **auto-identify** [ *length* ] | **string** [ *length* ] | **binary** *length* | **hex** [ *length* ] { **class1** | **class2** | **class3** } } [ *username-seperator* ] } \* ] } | { **option60** | **vendor-class** } [ **cn** | [ **offset** *offset2* ] { **length** *length2* | **sub-option** **suboption-id2** [ **sub-offset** *offset2* ] [ **sub-length** *length2* ] } ] [ *username-seperator* ] | { **option61** | **client-id** } [ *username-seperator* ] | **option12** [ *username-seperator* ] | **pevlan** [ *username-seperator* ] | **cevlan** [ *username-seperator* ] | **port** [ *username-seperator* ] | **slot** [ *username-seperator* ] | **subslot** [ *username-seperator* ] } \* command to configure the device to generate a pure username for an IPoE or PPPoE user based on the information carried in the user access request packet.
     + Run the [**vlanpvc-to-username**](cmdqueryname=vlanpvc-to-username) { **standard** | **turkey** | **version10** | **version20** } command to configure the format of the automatically generated pure usernames of IPoE users.
     + Run the [**vlanpvc-to-username**](cmdqueryname=vlanpvc-to-username) **standard** **trust** { **pevlan** | **cevlan** } [ **ignore-rid** ] command to configure the format of the automatically generated pure usernames of IPoE users.
     + Run the [**vlanpvc-to-username**](cmdqueryname=vlanpvc-to-username) **standard** **ignore-rid** command to configure the format of the automatically generated pure usernames of IPoE users.
  4. (Optional) Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The AAA domain view is displayed.
  5. (Optional) Run [**radius-server domain-annex**](cmdqueryname=radius-server+domain-annex) { **left** | **right** } *annex*
     
     
     
     The BRAS is configured to add a character string to the left or right of the domain name in a username when sending authentication and accounting request packets to the RADIUS server.
  6. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the AAA view.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a password generation mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**default-password**](cmdqueryname=default-password) [ **template** *template-name* ] { **cipher** *cipher-password* | **simple** *simple-password* | { **option60** | **vendor-class** } [ **cn** | [ **offset** *offset* ] { **length** *length* | **sub-option** *sub-option-code* [ **sub-offset** *sub-offset* ] [ **sub-length** *sub-length* ] } ] [ **md5-encryt** ] [ **support hex** ] | { **option77** | **user-class** | **mac-address** { **noseparator** | **separator** *separatorchar* } } }
     
     
     
     A password or password template is configured for an IPoE user.
     
     
     
     The differences between **cipher** and **simple** are as follows:
     
     If **cipher** is specified, you can enter an encrypted password. If **simple** is specified, you can enter only the original (non-encrypted) password. The **cipher** keyword supports longer passwords because encrypted passwords are longer than unencrypted ones.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The password must be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
     + For security purposes, you are advised to specify the ciphertext mode.
     + To ensure device security, change the password instead of using the preset one.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.