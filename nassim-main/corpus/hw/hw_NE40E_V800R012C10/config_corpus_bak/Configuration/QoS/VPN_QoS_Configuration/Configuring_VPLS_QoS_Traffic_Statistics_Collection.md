Configuring VPLS QoS Traffic Statistics Collection
==================================================

The VPLS QoS traffic statistics collected in real time allow you to check whether the QoS requirements of VPLS services are met.

#### Usage Scenario

To monitor the network operating status and locate faults more easily on a VPLS network, configure traffic statistics collection.

After QoS is configured and traffic statistics collection is enabled, you can check whether the QoS requirements are met based on real-time traffic status.


#### Pre-configuration Tasks

VPLS QoS traffic statistics can be collected based on VSIs or VSI PWs. VSI-based QoS traffic statistics collection takes effect for all PWs in a VSI, whereas VSI PW-based QoS traffic statistics collection takes effect for a specified PW in an LDP VSI.

Before configuring QoS traffic statistics collection for a VPLS VSI, complete the following tasks:

* Configure a VPLS VSI.
* Configure VPLS QoS.

Before configuring VSI PW-based QoS traffic statistics collection for a VPLS network, complete the following tasks:

* Configure a VPLS VSI.
* Configure PWs for the VPLS VSI.
* Configure VPLS QoS.

#### Procedure

1. Configure VSI-based QoS traffic statistics collection for a VPLS network.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
   3. Run the [**qos cir**](cmdqueryname=qos+cir) *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] command to configure QoS parameters in the VSI view.
   4. Run the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) command to enable VPLS QoS traffic statistics collection in the VSI view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure VSI PW-based QoS traffic statistics collection for a VPLS network.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**vsi**](cmdqueryname=vsi) *vsi-name* command to create a VSI and enter its view.
   3. Run the [**pwsignal**](cmdqueryname=pwsignal) **ldp** command to create a VSI using LDP signaling and enter the VSI-LDP view.
   4. Run the [**traffic-statistics enable**](cmdqueryname=traffic-statistics+enable) command to enable VPLS QoS traffic statistics collection in the VSI-LDP view.
   5. Run the [**pw**](cmdqueryname=pw) *pw-name* command to create a PW and enter the VSI-LDP-PW view.
   6. Run the [**qos cir**](cmdqueryname=qos+cir) *cir-value* [ **pir** *pir-value* ] [ **qos-profile** *qos-profile-name* ] command to configure QoS parameters for the LDP PW.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring VPLS QoS traffic statistics collection, perform the following operation to check the configuration results:

* Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* **qos** [ **peer** *peer-address* [ **ldp129** | **negotiation-vc-id** *vc-id* | **remote-site** *remote-site-id* ] ] command to check VPLS QoS traffic statistics collection configurations.