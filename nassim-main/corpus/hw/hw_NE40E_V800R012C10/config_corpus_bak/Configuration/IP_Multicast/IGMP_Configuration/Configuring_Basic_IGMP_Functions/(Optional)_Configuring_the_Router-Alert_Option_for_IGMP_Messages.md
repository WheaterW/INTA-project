(Optional) Configuring the Router-Alert Option for IGMP Messages
================================================================

You can configure a device to deny IGMP messages that do not contain the Router-Alert option and the device to send IGMP messages that do not contain the Router-Alert option. The two configurations are usually used together.

#### Context

Different from other IP packets, IGMP messages are sent to the routing protocol layer for processing, and the consistency between the destination addresses of the IGMP messages and the interface address is not checked. As a result, a large number of messages may be sent to the CPU, or security risks may exist. The Router-Alert option can solve such problems. After a multicast device receives an IGMP message:

* By default, the multicast device does not check the Router-Alert option and sends the IGMP message to the routing protocol layer, regardless of whether the IGMP message contains the Router-Alert option.
* If the multicast device is configured to check the Router-Alert option, the multicast device sends the IGMP message to the routing protocol layer only if the message contains the Router-Alert option.

IGMP message transmit and receive ends must have the same Router-Alert option configuration on the same network segment. If the two ends do not have the same Router-Alert option configuration, change the configuration on one end.

You can perform configurations either globally or on an interface.

* [Global configuration](#EN-US_TASK_0172366715__step_dc_vrp_multicast_cfg_225301): takes effect on all interfaces.
* [Interface-specific configuration](#EN-US_TASK_0172366715__step_dc_vrp_multicast_cfg_225302): takes precedence over the global configuration. If an interface-specific configuration is not available, the interface uses the global configuration.

#### Procedure

* Global configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
     
     
     
     The IGMP view is displayed.
  3. Run [**require-router-alert**](cmdqueryname=require-router-alert)
     
     
     
     The multicast device is configured to accept and process only IGMP messages with the Router-Alert option and discard those without the Router-Alert option.
  4. Run [**undo send-router-alert**](cmdqueryname=undo+send-router-alert)
     
     
     
     The device is configured to send IGMP messages without the Router-Alert option.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Interface-specific configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**igmp require-router-alert**](cmdqueryname=igmp+require-router-alert)
     
     
     
     The interface is configured to accept and process only IGMP messages with the Router-Alert option and discard those without the Router-Alert option.
  4. Run [**undo igmp send-router-alert**](cmdqueryname=undo+igmp+send-router-alert)
     
     
     
     The interface is configured to send IGMP messages without the Router-Alert option.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.