Configuring Control Parameters for an IGMP Querier
==================================================

Configuring Control Parameters for an IGMP Querier

#### Context

Control parameters of an IGMP querier include the interval for sending IGMP General Query messages, robustness variable of the IGMP querier, maximum response time of IGMP General Query messages, keepalive period of other IGMP queriers, and interval for sending IGMP Group-Specific Query messages. When all these parameters are set to the default values, the IGMP querier can work normally. In addition, to promptly update and maintain group memberships and prevent network congestion caused by excessive packets, you can adjust the parameters of the IGMP querier through commands.

![](public_sys-resources/note_3.0-en-us.png) 

IGMPv1 supports only two parameters: the interval for sending General Query messages and the robustness variable of the IGMP querier.

Interfaces that connect multicast devices to the same user network segment must have the same IGMP parameter configurations; otherwise, these multicast devices fail to communicate.

In actual configuration, ensure that the interval for sending General Query messages is longer than the maximum response time of IGMP General Query messages and shorter than the keepalive period of other IGMP queriers.

The configuration can be performed in the IGMP or interface view, and takes effect based on the following rules:

* The configuration in the IGMP view is globally valid, whereas the configuration in the interface view takes effect only for the specified interface.
* If the same parameters are configured in both the interface and IGMP views, the configuration in the interface view takes effect. If the configuration is not performed on an interface, the interface uses the configuration in the IGMP view.
* If non-default values are configured in the IGMP view, the corresponding default values in the interface view do not take effect.


#### Procedure

* Configure global IGMP querier parameters.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the IGMP view.
     
     
     ```
     [igmp](cmdqueryname=igmp) [ vpn-instance vpn-instance-name ]
     ```
  3. Configure control parameters for the IGMP querier as required.
     
     
     
     **Table 1** Configuring control parameters for the IGMP querier
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure an interval at which General Query messages are sent. | [**timer query**](cmdqueryname=timer+query) *interval* | The default interval at which a querier sends General Query messages is 60 seconds, but the default interval defined in the corresponding protocol is 125 seconds. Currently, some vendor devices use the protocol-defined default interval of 125 seconds. To enable the querier to interwork with such devices, you must change the corresponding configuration to ensure that they send General Query messages at the same interval. |
     | Configure a robustness variable for the IGMP querier. | [**robust-count**](cmdqueryname=robust-count) *robust-value* | When a device starts, it sends *robust-value* General Query messages. The sending interval is 1/4 of the configured interval for sending IGMP General Query messages.  After the device receives a Leave message:  + In IGMPv2, the device sends *robust-value* Group-Specific Query messages. The sending interval is the configured interval for sending IGMP Group-Specific Query messages. + In IGMPv3, the device sends *robust-value* Group-Specific Query or Group-and-Source-Specific Query messages. The sending interval is the configured interval for sending IGMP Group-Specific Query or Group-and-Source-Specific Query messages. |
     | Configure the maximum response time of IGMP General Query messages. | [**max-response-time**](cmdqueryname=max-response-time) *interval* | By default, the maximum response time of IGMP General Query messages is 10 seconds. |
     | Configure the keepalive period of other IGMP queriers. | [**timer other-querier-present**](cmdqueryname=timer+other-querier-present) *interval* | By default, the keepalive period of other IGMP queriers is calculated using the following formula: Keepalive period of other IGMP queriers = Robustness variable x Interval for sending General Query messages + 1/2 x Maximum response time of General Query messages. If the robustness variable, interval for sending General Query messages, and maximum response time of General Query messages all use the default values, the keepalive period of other IGMP queriers is 125 seconds. |
     | Configure an interval for sending IGMP Group-Specific Query messages. | [**lastmember-queryinterval**](cmdqueryname=lastmember-queryinterval) *interval* | By default, the interval for sending IGMP Group-Specific Query messages is 1 second. The shorter the interval is, the more sensitive the querier is. |
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure IGMP querier parameters on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface connected to the user network segment.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Switch the interface working mode from Layer 2 to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Configure control parameters for the IGMP querier as required.
     
     
     
     **Table 2** Configuring control parameters for the IGMP querier
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure an interval at which General Query messages are sent. | [**igmp timer query**](cmdqueryname=igmp+timer+query) *interval* | The default interval at which a querier sends General Query messages is 60 seconds, but the default interval defined in the corresponding protocol is 125 seconds. Currently, some vendor devices use the protocol-defined default interval of 125 seconds. To enable the querier to interwork with such devices, you must change the corresponding configuration to ensure that they send General Query messages at the same interval. |
     | Configure a robustness variable for the IGMP querier. | [**igmp robust-count**](cmdqueryname=igmp+robust-count) *robust-value* | When a device starts, it sends *robust-value* General Query messages. The sending interval is 1/4 of the configured interval for sending IGMP General Query messages.  After the device receives a Leave message:  + In IGMPv2, the device sends *robust-value* Group-Specific Query messages. The sending interval is the configured interval for sending IGMP Group-Specific Query messages. + In IGMPv3, the device sends *robust-value* Group-Specific Query or Group-and-Source-Specific Query messages. The sending interval is the configured interval for sending IGMP Group-Specific Query or Group-and-Source-Specific Query messages. |
     | Configure the maximum response time of IGMP General Query messages. | [**igmp max-response-time**](cmdqueryname=igmp+max-response-time) *interval* | By default, the maximum response time of IGMP General Query messages is 10 seconds. |
     | Configure the keepalive period of other IGMP queriers. | [**igmp timer other-querier-present**](cmdqueryname=igmp+timer+other-querier-present) *interval* | By default, the keepalive period of other IGMP queriers is calculated using the following formula: Keepalive period of other IGMP queriers = Robustness variable x Interval for sending General Query messages + 1/2 x Maximum response time of General Query messages. If the robustness variable, interval for sending General Query messages, and maximum response time of General Query messages all use the default values, the keepalive period of other IGMP queriers is 125 seconds. |
     | Configure an interval for sending IGMP Group-Specific Query messages. | [**igmp lastmember-queryinterval**](cmdqueryname=igmp+lastmember-queryinterval) *interval* | By default, the interval for sending IGMP Group-Specific Query messages is 1 second. The shorter the interval is, the more sensitive the querier is. |
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```