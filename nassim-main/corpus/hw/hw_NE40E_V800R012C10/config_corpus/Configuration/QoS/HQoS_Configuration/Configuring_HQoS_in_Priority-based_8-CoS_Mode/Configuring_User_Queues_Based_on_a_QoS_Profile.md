Configuring User Queues Based on a QoS Profile
==============================================

A QoS profile is the aggregate of QoS scheduling parameters. You can configure scheduling parameters and bandwidth values for user queues or bind an FQ profile.

#### Context

To achieve uniform scheduling of incoming traffic flows on multiple interfaces, you need to implement traffic management by user levels. Interface-based HQoS only supports classifying traffic flows on one interface into a user queue (SQ) for scheduling. It does not support uniform scheduling of traffic flows on multiple interfaces. Profile-based HQoS, by comparison, supports classifying traffic flows on multiple interfaces into an SQ for scheduling. It implements uniform scheduling of traffic flows on multiple interfaces by defining QoS profiles and applying the profiles to different interfaces.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can configure scheduling parameters in a common QoS profile or a time-based QoS profile. A maximum of two user queue configurations can be configured in a time-based QoS profile.

* The names of the common QoS profile and time-based QoS profile must be different.
* If you have configured one time-based user queue, configuring one more non-time-based user queue is recommended. Within the time range, the time-based user queue takes effect; at other time, the non-time-based user queue takes effect.
* If you need to configure two time-based user queues, configuring the two time ranges to cover the full day (24 hours) is recommended. If the two time ranges do not cover the full day (24 hours), the user queue does not take effect at the unspecified time.


#### Procedure

* Configure user-queue scheduling parameters for a QoS profile.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name*
     
     
     
     A QoS profile is defined and its view is displayed.
  3. (Optional) Run **[**description**](cmdqueryname=description)** **description-info**
     
     
     
     The description of the QoS profile is configured.
  4. Run **[**weight**](cmdqueryname=weight)** **weight-value** [ ****inbound**** | ****outbound**** ]
     
     
     
     A weight is set for user queues.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
* (Optional) Configure the bandwidth granularity and quantity in a channel profile.
  1. Run [**qos channel-profile**](cmdqueryname=qos+channel-profile) *channel-profile-name*
     
     
     
     A channel profile is created and its view is displayed.
  2. Run [**channel**](cmdqueryname=channel) *channel-id* ****bandwidth**** *bandwidth-value* ****quantity**** *quantity-value*
     
     
     
     A bandwidth granularity and quantity are configured for a specific channel.
     
     
     
     The bandwidth configured for user queues is a combination of a series of discrete bandwidths. Bandwidth granularity and quantity can be manually specified for each discrete bandwidth so that bandwidth can be properly allocated to services on the live network. If the default channel bandwidth is too small, the QoS resource specification requirements of PPP and MP services on low-speed cards cannot be met. Therefore, you need to run the [**display qos channel-profile**](cmdqueryname=display+qos+channel-profile) **slot** *slot-id* [ **verbose** ] command to check whether the current resources meet the specification requirements. If the current resources do not meet the requirements, you need to configure a static channel bandwidth.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.