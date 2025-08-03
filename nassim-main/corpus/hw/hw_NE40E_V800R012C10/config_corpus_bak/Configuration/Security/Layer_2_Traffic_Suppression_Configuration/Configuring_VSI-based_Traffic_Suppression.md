Configuring VSI-based Traffic Suppression
=========================================

This section describes how to configure VSI-based traffic suppression in order to reduce the traffic burden on a network.

#### Usage Scenario

In addition to user traffic management and bandwidth allocation, an Ethernet requires broadcast, multicast, and unknown unicast traffic to be suppressed to ensure the secure transmission of unicast traffic and properly utilize bandwidth resources.

Most networks require unicast traffic to be much heavier than broadcast traffic. If broadcast traffic is not suppressed, forwarding a large volume of such traffic consumes numerous bandwidth resources, reducing network performance and even causing a communication interruption.


#### Pre-configuration Tasks

Before configuring Layer 2 traffic suppression, complete the following task:

Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ]
   
   
   
   The VSI view is displayed.
3. Run [**suppression**](cmdqueryname=suppression) { **inbound** | **outbound** } **enable**
   
   
   
   Traffic suppression is enabled for the VSI.
4. Run [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   VSI AC-based broadcast traffic suppression is implemented.
5. Run [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   VSI AC-based multicast traffic suppression is implemented.
6. Run [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] { **uni-inbound** | **uni-outbound** }
   
   
   
   VSI AC-based unknown unicast traffic suppression is implemented.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, perform the following operation to verify the configuration:

Run the [**display traffic-statistics vsi**](cmdqueryname=display+traffic-statistics+vsi) *vsi-name* **suppression** **uni** command to check VSI-based traffic suppression statistics.