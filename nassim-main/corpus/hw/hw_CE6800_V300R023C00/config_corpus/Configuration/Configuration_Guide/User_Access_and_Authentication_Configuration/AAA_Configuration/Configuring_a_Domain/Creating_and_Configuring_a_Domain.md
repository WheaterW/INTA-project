Creating and Configuring a Domain
=================================

Creating and Configuring a Domain

#### Context

The device manages users based on domains. A user uses the AAA configuration in the domain to which the user belongs. The device determines the domain to which a user belongs based on the user name. Before performing authentication, authorization, and accounting for users, you need to create the domain to which the users belong.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create a domain and enter the domain view.
   
   
   ```
   [domain](cmdqueryname=domain) domain-name
   ```
4. (Optional) Configure the domain status.
   
   
   ```
   [state](cmdqueryname=state) { active | block [ time-range time-name &<1â4> ] }
   ```
   
   By default, a domain is active after being created. After the [**state**](cmdqueryname=state) **block** command is run to block a domain, online users in the domain are not affected, but offline users in the domain cannot log in again.
5. (Optional) Configure a domain name parsing scheme in the AAA view. The scheme takes effect for all the domains on the device.
   
   
   
   **Table 1** Configuring a domain name parsing scheme
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the domain name parsing direction. | [**domainname-parse-direction**](cmdqueryname=domainname-parse-direction) { **left-to-right** | **right-to-left** } | By default, a domain name is parsed from left to right. |
   | Configure a domain name delimiter. | [**domain-name-delimiter**](cmdqueryname=domain-name-delimiter) *delimiter* | By default, the domain name delimiter is @. |
   | Configure the domain name location. | [**domain-location**](cmdqueryname=domain-location) { **after-delimiter** | **before-delimiter** } | By default, a domain name is placed after a delimiter. |
6. (Optional) Enable the traffic statistics collection function for users in a domain.
   
   
   ```
   statistic enable
   ```
   
   By default, traffic statistics collection is disabled for users in a domain.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Only access users support this configuration.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```