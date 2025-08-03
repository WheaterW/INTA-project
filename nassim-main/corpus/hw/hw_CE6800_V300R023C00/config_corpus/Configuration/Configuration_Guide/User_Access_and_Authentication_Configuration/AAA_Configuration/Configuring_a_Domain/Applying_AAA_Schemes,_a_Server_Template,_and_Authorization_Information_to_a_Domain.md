Applying AAA Schemes, a Server Template, and Authorization Information to a Domain
==================================================================================

Applying AAA Schemes, a Server Template, and Authorization Information to a Domain

#### Context

The AAA schemes and server template in a domain are managed in a unified manner. Authorization information can also be configured in a domain. A user uses the AAA configuration in the domain to which the user belongs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Enter the domain view.
   
   
   ```
   [domain](cmdqueryname=domain) domain-name
   ```
4. Configure an authentication scheme to be applied to the domain.
   
   
   ```
   [authentication-scheme](cmdqueryname=authentication-scheme) authentication-scheme-name
   ```
5. Configure an authorization scheme to be applied to the domain. If RADIUS authentication is used, skip this step.
   
   
   ```
   authorization-scheme authorization-scheme-name
   ```
6. Configure an accounting scheme to be applied to the domain.
   
   
   ```
   [accounting-scheme](cmdqueryname=accounting-scheme) accounting-scheme-name
   ```
7. Configure a RADIUS server template to be applied to the domain. If RADIUS authentication is used, perform this step.
   
   
   ```
   [radius-server](cmdqueryname=radius-server) template-name
   ```
8. Configure an HWTACACS server template to be applied to the domain. If HWTACACS authentication is used, perform this step.
   
   
   ```
   [hwtacacs-server](cmdqueryname=hwtacacs-server) template-name
   ```
9. Configure an LDAP server template to be applied to the domain. If LDAP authentication is used, perform this step.
   
   
   ```
   [ldap-server](cmdqueryname=ldap-server) template-name
   ```
10. (Optional) Configure the device to deliver service scheme authorization to users in the domain.
    
    
    ```
    [service-scheme](cmdqueryname=service-scheme) service-scheme-name
    ```
11. (Optional) Enable the RADIUS accounting packet copy function and configure a RADIUS server template for level-2 accounting. This function is supported only when RADIUS authentication is used.
    
    
    ```
    [accounting-copy radius-server](cmdqueryname=accounting-copy+radius-server) template-name
    ```
    
    By default, the RADIUS accounting packet copy function is disabled.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the [**display domain**](cmdqueryname=display+domain) [ **name** *domain-name* ] command to check the domain configuration.