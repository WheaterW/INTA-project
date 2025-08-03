Configuring an MLD Querier
==========================

To configure an MLD querier, you can configure the MLD prompt leave function and set the following parameters: interval at which general query messages are sent, robustness variable, maximum response time of Query messages, keepalive time of other MLD queriers, and interval MLD last-listener query messages are sent.

#### Usage Scenario

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Interfaces that connect multicast devices to the same user network segment must have the same MLD parameter configurations; otherwise, these multicast devices fail to communicate.

An MLD querier is responsible for periodically sending MLD Query messages on a shared network segment to update group memberships. You can configure parameters of an MLD querier either globally or on an interface.

* Global configuration: takes effect on all interfaces.
* Interface-specific configuration: takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

During the configuration, ensure that the interval for sending general query messages is greater than the maximum response time of Query messages but smaller than the keepalive time of other MLD queriers.



#### Pre-configuration Tasks

Before configuring an MLD querier, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* [Configure basic MLD functions](dc_vrp_multicast_cfg_2073.html).

#### Procedure

* Configure an MLD querier globally.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mld**](cmdqueryname=mld)
     
     
     
     The MLD view is displayed.
  3. Run [**timer query**](cmdqueryname=timer+query) *interval*
     
     
     
     The interval at which the device sends general query messages is set.
  4. Run [**robust-count**](cmdqueryname=robust-count) *robust-value*
     
     
     
     An MLD robustness variable is set.
     
     
     
     When the Router starts, the Router sends general query messages for the number of *robust-value* times. The sending interval is 1/4 of the interval for sending MLD general query messages.
     
     After receiving a Done message, the Router sends last-listener query messages for the number of *robust-value* times. The sending interval is set by using the **lastlistener-query interval** command.
  5. Run [**max-response-time**](cmdqueryname=max-response-time) *interval*
     
     
     
     The maximum response time of MLD Query messages is set.
  6. Run [**timer other-querier-present**](cmdqueryname=timer+other-querier-present) *interval*
     
     
     
     The keepalive time of other MLD queriers is set.
  7. Run [**lastlistener-queryinterval**](cmdqueryname=lastlistener-queryinterval) *interval*
     
     
     
     The interval at which the device sends MLD last-listener query messages is set.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an MLD querier on an interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**mld timer query**](cmdqueryname=mld+timer+query) *interval*
     
     
     
     The interval at which the interface sends general query messages is set.
  4. Run [**mld max-response-time**](cmdqueryname=mld+max-response-time) *interval*
     
     
     
     The maximum response time of MLD Query messages is set.
  5. Run [**mld timer other-querier-present**](cmdqueryname=mld+timer+other-querier-present) *interval*
     
     
     
     The keepalive time of other MLD queriers is set.
  6. Run [**mld robust-count**](cmdqueryname=mld+robust-count) *robust-value*
     
     
     
     An MLD robustness variable is set.
  7. Run [**mld lastlistener-queryinterval**](cmdqueryname=mld+lastlistener-queryinterval) *interval*
     
     
     
     The interval at which the interface sends MLD last-listener query messages is set.
  8. Run [**mld prompt-leave**](cmdqueryname=mld+prompt-leave) [ **group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* } ]
     
     
     
     The MLD prompt leave function is configured on the interface.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Checking the Configurations

Run the [**display mld interface verbose**](cmdqueryname=display+mld+interface+verbose) command to view the configurations and operating status of MLD on an interface.