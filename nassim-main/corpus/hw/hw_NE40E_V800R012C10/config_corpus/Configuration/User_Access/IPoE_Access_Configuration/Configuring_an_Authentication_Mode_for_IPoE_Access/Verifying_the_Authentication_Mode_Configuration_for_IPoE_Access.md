Verifying the Authentication Mode Configuration for IPoE Access
===============================================================

After an authentication mode is configured, you can view the authentication mode by checking the domain configuration.

#### Procedure

* Run the [**display web-auth-server configuration**](cmdqueryname=display+web-auth-server+configuration) command to check the web authentication server configuration.
* Run the [**display domain**](cmdqueryname=display+domain) [*domain-name* ] command to check the domain configuration.
* Run the [**display aaa default-user-name**](cmdqueryname=display+aaa+default-user-name) [ **template** *template-name* | **global** ] command to check the mode in which pure IPoE usernames are generated.
* Run the [**display aaa default-password**](cmdqueryname=display+aaa+default-password) [ **template** *template-name* | **global** ] command to check the IPoE user password or the password generation mode.
* Run the [**display access https-redirect information**](cmdqueryname=display+access+https-redirect+information) command to check the information about the HTTPS redirection.
* Run the [**display access https-redirect blacklist**](cmdqueryname=display+access+https-redirect+blacklist) command to check the information about the blacklist generated during HTTPS redirection.
* Run the **display access https-redirect chasten-user slot** *slot-id* command to check HTTPS redirection information about a user on a specified slot.
* Run the [**display cpu-defend whitelist session-car web-auth-server statistics**](cmdqueryname=display+cpu-defend+whitelist+session-car+web-auth-server+statistics) **slot** *slot-id* command to check information about CAR for whitelisted portal sessions on a specified board.
* Run the [**display cpu-defend whitelist-v6 session-car web-auth-serverv6 statistics**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car+web-auth-serverv6+statistics) **slot** *slot-id* command to check information about CAR for whitelisted portalv6 sessions on a specified board.