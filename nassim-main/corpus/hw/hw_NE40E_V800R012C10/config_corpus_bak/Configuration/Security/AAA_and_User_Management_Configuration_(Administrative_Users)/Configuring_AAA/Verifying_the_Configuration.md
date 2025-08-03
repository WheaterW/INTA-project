Verifying the Configuration
===========================

After AAA is configured, you can view the configurations of authentication, authorization, and accounting schemes.

#### Prerequisites

AAA configurations are complete.


#### Procedure

* Run the [**display aaa configuration**](cmdqueryname=display+aaa+configuration) command to view brief AAA information.
* Run the [**display accounting-scheme**](cmdqueryname=display+accounting-scheme) command to check the accounting scheme configuration.
* Run the [**display authentication-scheme**](cmdqueryname=display+authentication-scheme) [ *authentication-scheme-name* ] command to check the authentication scheme configuration.
* Run the [**display authorization-scheme**](cmdqueryname=display+authorization-scheme) [ *authorization-scheme-name* ] command to check the authorization scheme configuration.
* Run the [**display domain**](cmdqueryname=display+domain) *domain-name* command to check the domain configuration.
* Run the [**display hwtacacs current-status**](cmdqueryname=display+hwtacacs+current-status) command to check the current HWTACACS status.
* Run the [**display hwtacacs-server template**](cmdqueryname=display+hwtacacs-server+template) command to check the HWTACACS server configuration.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **name** *attribute-name* | { **type** { **huawei** | **standard** } *attribute-id* } ] command to check the RADIUS attributes supported by the system.
* Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **group** *group-name* ] command to check the RADIUS server configuration.
* Run the [**display recording-scheme**](cmdqueryname=display+recording-scheme) command to check the recording scheme configuration.