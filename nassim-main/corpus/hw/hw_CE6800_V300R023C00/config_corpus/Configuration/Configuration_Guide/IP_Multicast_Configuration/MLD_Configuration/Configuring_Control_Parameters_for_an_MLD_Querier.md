Configuring Control Parameters for an MLD Querier
=================================================

Configuring Control Parameters for an MLD Querier

#### Context

An MLD querier's parameters include the interval at which General Query messages are sent, robustness variable, maximum response time of Query messages, keepalive period of the Other Querier Present timer, and interval at which last-member query messages are sent. When all these parameters are set to the default values, the MLD querier can work normally. In addition, to promptly update and maintain group memberships and prevent network congestion caused by excessive packets, you can adjust the parameters of the MLD querier through commands.

![](public_sys-resources/note_3.0-en-us.png) 

Interfaces that connect multicast devices to the same user network segment must have the same MLD parameter configurations; otherwise, these multicast devices fail to communicate.

During configuration, ensure that the interval for sending General Query messages is longer than the maximum response time of Query messages but shorter than the keepalive period of the Other Querier Present timer.

The configuration can be performed in the MLD or interface view, and takes effect based on the following rules:

* The configuration in the MLD view takes effect globally, whereas that in the interface view takes effect only for the specified interface.
* If the same parameters are configured in both the interface and MLD views, the configuration in the interface view takes effect. If the configuration is not performed on an interface, the configuration in the MLD view takes effect.
* If non-default values are configured in the MLD view, the corresponding default values in the interface view do not take effect.


#### Procedure

* Configure global MLD querier parameters.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the MLD view.
     
     
     ```
     [mld](cmdqueryname=mld)
     ```
  3. Configure control parameters for the MLD querier as required.
     
     
     
     **Table 1** Configuring control parameters for the MLD querier
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure an interval at which MLD General Query messages are sent. | [**timer query**](cmdqueryname=timer+query) *interval* | By default, the interval at which an MLD querier sends MLD General Query messages is 125s. |
     | Configure a robustness variable for the MLD querier. | [**robust-count**](cmdqueryname=robust-count) *robust-value* | By default, the robustness variable of MLD is 2. A larger robustness variable indicates a longer timeout period of a group membership.  When a device starts, it sends *robust-value* General Query messages. The sending interval is 1/4 of the configured interval for sending MLD General Query messages.  After the device receives a Multicast Listener Done message, it sends *robust-value* last-member query messages. The sending interval is the configured interval for sending last-member query messages. |
     | Configure the maximum response time of MLD General Query messages. | [**max-response-time**](cmdqueryname=max-response-time) *interval* | By default, the maximum response time of MLD General Query messages is 10s. |
     | Configure the keepalive period of the Other Querier Present timer. | [**timer other-querier-present**](cmdqueryname=timer+other-querier-present) *interval* | By default, the keepalive period of the Other Querier Present timer is calculated using the following formula:  Keepalive period of the Other Querier Present timer = Robustness variable x Interval for sending General Query messages + 1/2 x Maximum response time  If the robustness variable, interval for sending General Query messages, and maximum response time all use the default values, the keepalive period of the Other Querier Present timer is 255s. |
     | Configure an interval for sending last-member query messages. | [**lastlistener-queryinterval**](cmdqueryname=lastlistener-queryinterval) *interval* | By default, the interval for sending last-member query messages is 1s. The shorter the interval is, the more sensitive the querier is. |
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure MLD querier parameters on an interface.
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
  4. Configure control parameters for the MLD querier as required.
     
     
     
     **Table 2** Configuring control parameters for the MLD querier
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure an interval at which MLD General Query messages are sent. | [**mld timer query**](cmdqueryname=mld+timer+query) *interval* | By default, the interval at which an MLD querier sends MLD General Query messages is 125s. |
     | Configure a robustness variable for the MLD querier. | [**mld robust-count**](cmdqueryname=mld+robust-count) *robust-value* | By default, the robustness variable of MLD is 2. A larger robustness variable indicates a longer timeout period of a group membership.  When a device starts, it sends *robust-value* General Query messages. The sending interval is 1/4 of the configured interval for sending MLD General Query messages.  After the device receives a Multicast Listener Done message, it sends *robust-value* last-member query messages. The sending interval is the configured interval for sending last-member query messages. |
     | Configure the maximum response time of MLD General Query messages. | [**mld max-response-time**](cmdqueryname=mld+max-response-time) *interval* | By default, the maximum response time of MLD General Query messages is 10s. |
     | Configure the keepalive period of the Other Querier Present timer. | [**mld timer other-querier-present**](cmdqueryname=mld+timer+other-querier-present) *interval* | By default, the keepalive period of the Other Querier Present timer is calculated using the following formula:  Keepalive period of the Other Querier Present timer = Robustness variable x Interval for sending General Query messages + 1/2 x Maximum response time  If the robustness variable, interval for sending General Query messages, and maximum response time all use the default values, the keepalive period of the Other Querier Present timer is 255s. |
     | Configure an interval for sending last-member query messages. | [**mld lastlistener-queryinterval**](cmdqueryname=mld+lastlistener-queryinterval) *interval* | By default, the interval for sending last-member query messages is 1s. The shorter the interval is, the more sensitive the querier is. |
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```