Configuring a Global Default Domain
===================================

Configuring a Global Default Domain

#### Context

The device determines the domain to which a user belongs based on the user name. If a user name does not contain a domain name and the device cannot determine the domain to which the user belongs, the device adds the user to a global default domain.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a global default domain for administrators.
   
   
   ```
   [domain](cmdqueryname=domain) domain-name admin
   ```
3. Configure a global default domain for access users.
   
   
   ```
   [domain](cmdqueryname=domain) domain-name access
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to check the currently configured global default domains. The **Administrator user default domain** field indicates the currently configured global default domain of administrators.