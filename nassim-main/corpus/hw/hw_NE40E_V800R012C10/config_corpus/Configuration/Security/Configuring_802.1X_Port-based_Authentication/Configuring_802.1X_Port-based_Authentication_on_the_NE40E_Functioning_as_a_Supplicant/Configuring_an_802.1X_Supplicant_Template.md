Configuring an 802.1X Supplicant Template
=========================================

When 802.1X supplicant authentication is used, the NE40E and the authenticator perform authentication negotiation
based on parameters defined in an 802.1X supplicant template.

#### Context

Perform the following steps on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dot1x-supplicant-template**](cmdqueryname=dot1x-supplicant-template) *dot1x-supplicant-template-number*
   
   
   
   An 802.1X supplicant template is created or the 802.1X
   supplicant template view is displayed.
   
   
   
   802.1X supplicant templates are identified by number. Only
   one 802.1X supplicant template can be configured on a device.
3. Run [**eap username**](cmdqueryname=eap+username) *username-string* **password cipher** *password-string*
   
   
   
   The EAP authentication
   user name and password for the 802.1X supplicant template are set.
4. (Optional) Run [**eap authentication-type pap**](cmdqueryname=eap+authentication-type+pap)
   
   
   
   An EAP authentication mode is configured for the
   802.1X supplicant template. Two EAP authentication modes (CHAP and
   PAP) are supported on the device. While PAP transmits passwords in
   plaintext with low security, CHAP transmits passwords in ciphertext
   with higher security.