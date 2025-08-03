AAA User Management
===================

AAA is short for authentication, authorization, and accounting. AAA provides the following functions, specifically:

Authentication: determines which users can access the network.

Authorization: authorizes users to access specific services.

Accounting: records network resource usage.

AAA is closely related to services and therefore its configuration is flexible.

#### Security Policy

* Remote authentication and authorization are supported. This is achieved by configuring user information (including the username, password, and attributes of a local user) on an authentication server. Remote authentication and authorization are implemented using Remote Authentication Dial-In User Service (RADIUS) or Huawei Terminal Access Controller Access Control System (HWTACACS). HWTACACS is an enhancement of the Terminal Access Controller Access Control System Plus (TACACS+) protocol (version v1.78).
* Remote command authentication is supported. You can set the command authentication mode to remote authentication for users of specified privilege levels. Information about users' command execution permissions is stored on a remote server. When a user runs a command, the server determines whether the user's privilege level permits the user to execute the command. Currently, only HWTACACS can be used for remote command authentication.
* The maximum number of consecutive authentication failures for local users and the interval for re-authentication can be configured to prevent unauthorized logins. Once a pre-defined number of consecutive authentication failures for local users is reached, a user account is locked for a pre-defined period of time to prevent unauthorized logins. This reduces the probability of successful probes and enhances device security.
* Local user passwords and authorization level upgrading passwords are securely stored in the system using advanced encryption algorithms.
* The none authentication mode (none) of management users is shielded.

#### Attack Methods

* Unauthorized users may attempt to obtain system administrators' login permissions by traversing key information (such as usernames and passwords).
* They may attack the remote server to obtain key information (such as usernames and passwords).
* Unauthorized users may attack the network between a user and a device to obtain key information such as entered passwords. Although user information is encrypted when being transmitted over a network to a server, an unauthorized user may still initiate a collision attack or traverse plaintext and ciphertext dictionaries to decrypt user information.

#### Configuration and Maintenance Methods

* Set user authentication and authorization modes to remote authentication and remote authorization. HWTACACS authentication and authorization are used as an example.
  
  # Create an HWTACACS template, configure the authentication and authorization servers, and configure the shared key.
  
  ```
  [~HUAWEI] hwtacacs-server template 1
  ```
  ```
  [*HUAWEI-hwtacacs-1] hwtacacs-server authentication 10.138.90.141
  ```
  ```
  [*HUAWEI-hwtacacs-1] hwtacacs-server authorization 10.138.90.141
  ```
  ```
  [*HUAWEI-hwtacacs-1] hwtacacs-server shared-key YsHsjx_202206
  ```
  ```
  [*HUAWEI-hwtacacs-1] commit
  ```
  
  # Set the authentication mode to HWTACACS authentication in the authentication scheme.
  
  ```
  [~HUAWEI] aaa
  ```
  ```
  [~HUAWEI-aaa] authentication-scheme 1
  ```
  ```
  [*HUAWEI-aaa-authen-1] authentication-mode hwtacacs
  ```
  ```
  [*HUAWEI-aaa-authen-1] commit
  ```
  
  # Set the authorization mode to HWTACACS authorization in the authorization scheme.
  
  ```
  [~HUAWEI-aaa] authorization-scheme 1
  ```
  ```
  [*HUAWEI-aaa-author-1] authorization-mode hwtacacs
  ```
  ```
  [*HUAWEI-aaa-author-1] commit
  ```
  
  # Bind the authentication scheme, authorization scheme, and HWTACACS template to the domain.
  
  ```
  [~HUAWEI-aaa] domain dom1
  ```
  ```
  [*HUAWEI-aaa-domain-dom1] authentication-scheme 1
  ```
  ```
  [*HUAWEI-aaa-domain-dom1] authorization-scheme 1
  ```
  ```
  [*HUAWEI-aaa-domain-dom1] hwtacacs-server 1
  ```
  ```
  [*HUAWEI-aaa-domain-dom1] commit
  ```
  
  # The authentication and authorization modes of users in domain **dom1** are remote HWTACACS authentication.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Note: RADIUS does not support separation of authentication and authorization. You only need to set the authentication mode to remote RADIUS authentication. The system automatically completes remote RADIUS authentication and authorization.
* Set the command authentication mode of users to remote authentication.
  
  # Set the authentication mode of level-3 users to remote authentication in the authorization scheme.
  
  ```
  [~HUAWEI] aaa
  ```
  ```
  [~HUAWEI-aaa] authorization-scheme 1
  ```
  ```
  [*HUAWEI-aaa-author-1] authorization-cmd 3 hwtacacs
  ```
  ```
  [*HUAWEI-aaa-author-1] commit
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  After remote authentication is configured, the system sends an authentication request to the remote server each time a user runs a command. The remote server determines whether the user has the permission to run the command. As such, the status of the network between the device and the server affects the response time of command execution.
* Configure the maximum number of consecutive authentication failures of local users.
  
  # Set the maximum number of consecutive authentication failures of a local user within 1 minute to 3:
  
  ```
  [~HUAWEI] aaa
  ```
  ```
  [~HUAWEI-aaa] user-block failed-times 3 period 1
  ```
  ```
  [*HUAWEI-aaa] commit
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If **failed-times** is set to 0, the number of consecutive authentication failures is not limited.
  
  # Configure the interval at which locked users are automatically unlocked. If a user is locked because the number of consecutive authentication failures exceeds the upper limit, the system automatically unlocks the user after the specified period of time.
  
  ```
  [~HUAWEI-aaa] user-block reactive 30
  ```
  ```
  [*HUAWEI-aaa] commit
  ```
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  If *reactive-time* is set to 0, the locked user cannot be automatically unlocked. Instead, the user can only be manually unlocked by the administrator. The value of *reactive-time* is in minutes.
  
  # Manually unlock a locked user.
  
  ```
  <HUAWEI> activate aaa local-user root
  ```
* Enable password complexity check.
  
  ```
  [~HUAWEI] user-security-policy enable
  ```
  ```
  [*HUAWEI-aaa] commit
  ```

#### Configuration and Maintenance Suggestions

If the system displays a message indicating that the password needs to be changed to reduce risks, change the password as prompted.


#### Verifying the Security Hardening Result

* Run the [**display authentication-scheme**](cmdqueryname=display+authentication-scheme) [ *authentication-scheme-name* ] command to check the authentication scheme configuration.
* Run the [**display accounting-scheme**](cmdqueryname=display+accounting-scheme) command to check the accounting scheme configuration.
* Run the [**display authorization-scheme**](cmdqueryname=display+authorization-scheme) [*authorization-scheme-name* ] command to check the authorization scheme configuration.
* Run the [**display domain**](cmdqueryname=display+domain) *domain-name* command to check the domain configuration.
* Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to view brief AAA information.