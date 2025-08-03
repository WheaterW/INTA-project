Configuring the Last-Mile QoS Mode and Setting the Adjustment Value of the Size of Remote Packets
=================================================================================================

The device can adjust the link bandwidth based on the types of links between the user and DSLAM.

#### Context

The NE40E can implement last-mile QoS on two types of links.

Therefore, it selects the mode of last-mile QoS according to the type of the links on the two ends of the DSLAM If the user access mode is PPPoE, the mode of last-mile QoS should be **frame**.

The NE40E supports the configuration of the remote packet compensation value in both the interface view and the AAA domain view. The configuration in the AAA domain view takes effect for only the L2TP service.

Perform the following steps on the Router:


#### Procedure

* Configuring the last-mile QoS mode and setting the adjustment value of the size of remote packets in the interface view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**qos link-adjustment shaping-mode**](cmdqueryname=qos+link-adjustment+shaping-mode) { **frame** | **cell** }
     
     
     
     The last-mile QoS mode is configured.
  4. Run [**qos link-adjustment**](cmdqueryname=qos+link-adjustment) *adjust-value* **remote**
     
     
     
     The adjustment value of the size of remote packets is set.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring the last-mile QoS mode and setting the adjustment value of the size of remote packets in the AAA domain view
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**domain**](cmdqueryname=domain) *domain-name*
     
     
     
     The AAA domain view is displayed.
  4. Run [**qos link-adjustment shaping-mode**](cmdqueryname=qos+link-adjustment+shaping-mode) { **frame** | **cell** }
     
     
     
     The last-mile QoS mode is configured.
  5. Run [**qos link-adjustment**](cmdqueryname=qos+link-adjustment) *adjust-value* **remote**
     
     
     
     The adjustment value of the size of remote packets is set.
     
     
     
     The configuration in the AAA domain view takes effect for only the L2TP service. If the adjustment value is configured in both the interface view and the AAA domain view, the configuration in the AAA domain view takes effect.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.