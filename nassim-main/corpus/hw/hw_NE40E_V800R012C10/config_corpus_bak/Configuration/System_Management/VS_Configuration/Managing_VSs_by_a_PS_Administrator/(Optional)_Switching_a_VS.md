(Optional) Switching a VS
=========================

A Physical System (PS) administrator can switch from one Virtual System (VS) to another.

#### Context

To facilitate user operations, you can run commands in the admin VS to switch to the VS system. In this way, you can perform operations on different VSs without switching the login window.

Furthermore, you can determine whether to enable login authentication when the user switches from the service admin VS to a service VS according to security requirements.


#### Pre-configuration Tasks

Ensure that the service VS to be switched to has been created.


#### Procedure

1. Run the [**switch virtual-system**](cmdqueryname=switch+virtual-system) *vs-name* command to switch the VS managed by the current user.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This configuration can be performed only on the admin VS. That is, only switching from the admin VS to a service VS is supported, and switching between service VSs is not supported.
2. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view of the service VS.
3. Run the [**virtual-system switch-authentication enable**](cmdqueryname=virtual-system+switch-authentication+enable) command to enable login authentication when the admin-VS is switched to a service VS.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Ensure that a valid user (AAA local user or remote user) has been configured for the service VS. Otherwise, the authentication fails and the user cannot log in to the service VS.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.