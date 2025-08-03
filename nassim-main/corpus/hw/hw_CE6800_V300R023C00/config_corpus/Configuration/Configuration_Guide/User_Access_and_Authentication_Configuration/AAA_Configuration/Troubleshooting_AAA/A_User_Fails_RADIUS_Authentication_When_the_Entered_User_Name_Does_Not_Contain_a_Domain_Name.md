A User Fails RADIUS Authentication When the Entered User Name Does Not Contain a Domain Name
============================================================================================

A User Fails RADIUS Authentication When the Entered User Name Does Not Contain a Domain Name

#### Fault Symptom

When a user enters a user name that does not contain a domain name for RADIUS authentication, the user fails authentication.


#### Possible Causes

If a user is authenticated in the global default domain (in which RADIUS authentication is not configured) and enters a user name without the domain name, the user fails authentication.


#### Troubleshooting Procedure

Use one of the following methods to ensure that the domain used for RADIUS authentication is the same as the domain used for user authentication:

* As an administrator, configure the domain used for RADIUS authentication as the global default domain.
  + If the user who failed authentication is an administrator, run the [**domain**](cmdqueryname=domain) *domain-name* **admin** command in the system view to configure the domain used for RADIUS authentication as the global default domain.
* As an administrator, configure RADIUS authentication in the global default domain.
  + If the user who failed authentication is an administrator, configure RADIUS authentication in the global default domain named **default\_admin**.
* As an administrator or a common user, enter the user name containing the RADIUS authentication domain name.