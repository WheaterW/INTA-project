(Optional) Configuring IGMP Querier Control Parameters
======================================================

IGMP querier control parameters include the interval at which General Query messages are sent, robustness variable, maximum response time of Query messages, keepalive time of other IGMP queriers, and interval at which IGMP last-member query messages are sent.

#### Context

An IGMP multicast Router can either be a querier or a non-querier. IGMP queriers are elected by the IGMP protocol. When receiving a Report message from a group member, a querier refreshes group memberships. If non-queriers have not received any general query message within the Keepalive time of other IGMP queriers, they consider the current IGMP querier faulty and trigger a new round of querier election automatically. You can adjust IGMP querier control parameters based on actual network conditions or whether hosts can quickly respond. IGMP querier control parameters supported by each IGMP version are as follows:

* IGMPv1 allows you to set only the interval at which General Query messages are sent and the robustness variable. Therefore, among the following steps for configuring IGMP querier control parameters, IGMPv1 supports only Steps 3 and 4.
* IGMPv2 and IGMPv3 allow you to configure all IGMP querier control parameters.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Interfaces that connect multicast devices to the same user network segment must have the same IGMP parameter configurations; otherwise, these multicast devices fail to communicate.

You can configure parameters of an IGMP querier either globally or on an interface.

* [Global configuration](#EN-US_TASK_0172366714__step_dc_vrp_multicast_cfg_225201): takes effect on all interfaces.
* [Interface-specific configuration](#EN-US_TASK_0172366714__step_dc_vrp_multicast_cfg_225202): takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

During the configuration, ensure that the interval for sending general query messages is greater than the maximum response time of Query messages but smaller than the keepalive time of other IGMP queriers.



#### Procedure

* Global configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**timer query**](cmdqueryname=timer+query) *interval*
     
     
     
     The interval at which the device sends general query messages is set.
  4. Run [**robust-count**](cmdqueryname=robust-count) *robust-value*
     
     
     
     An IGMP robustness variable is set.
     
     
     
     When a Router starts, the Router sends general query messages for the number of *robust-value* times. The sending interval is 1/4 of the interval for sending IGMP general query messages.
     
     After the Router receives a Leave message:
     
     + In IGMPv2, a Router sends group-specific query messages for the number of *robust-value* times. The sending interval is set using the **lastmember-queryinterval** command.
     + In IGMPv3, the Router sends group-specific or group-and-source-specific query messages for the number of *robust-value* times. The sending interval is set using the **lastmember-queryinterval query** command.
  5. Run [**max-response-time**](cmdqueryname=max-response-time) *interval*
     
     
     
     The maximum response time of IGMP Query messages is set.
  6. Run [**timer other-querier-present**](cmdqueryname=timer+other-querier-present) *interval*
     
     
     
     The keepalive time of other IGMP queriers is set.
  7. Run [**lastmember-queryinterval**](cmdqueryname=lastmember-queryinterval) *interval*
     
     
     
     The interval for sending IGMP last-member query messages is set.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Interface-specific configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp timer query**](cmdqueryname=igmp+timer+query) *interval*
     
     
     
     The interval at which the interface sends general query messages is set.
  4. Run [**igmp max-response-time**](cmdqueryname=igmp+max-response-time) *interval*
     
     
     
     The maximum response time of IGMP Query messages is set.
  5. Run [**igmp timer other-querier-present**](cmdqueryname=igmp+timer+other-querier-present) *interval*
     
     
     
     The keepalive time of other IGMP queriers is set.
  6. Run [**igmp robust-count**](cmdqueryname=igmp+robust-count) *robust-value*
     
     
     
     An IGMP robustness variable is set.
  7. Run [**igmp lastmember-queryinterval**](cmdqueryname=igmp+lastmember-queryinterval) *interval*
     
     
     
     The interval at which IGMP last-member query messages are sent is set.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.