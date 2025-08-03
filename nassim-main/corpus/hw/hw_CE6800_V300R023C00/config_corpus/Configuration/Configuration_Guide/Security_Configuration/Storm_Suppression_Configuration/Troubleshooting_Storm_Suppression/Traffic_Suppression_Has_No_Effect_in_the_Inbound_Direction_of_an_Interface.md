Traffic Suppression Has No Effect in the Inbound Direction of an Interface
==========================================================================

Traffic Suppression Has No Effect in the Inbound Direction of an Interface

#### Fault Symptom

After traffic suppression for broadcast packets, unknown multicast packets, or unknown unicast packets is configured on an interface, broadcast storms caused by packets of the corresponding type still occur, interrupting the flow of traffic.


#### Possible Causes

* Traffic suppression is not configured for the corresponding type of packets on the interface or the configured traffic suppression threshold is high.
* Packets of the corresponding type are not discarded in the inbound direction of the interface.

#### Procedure

1. Check whether traffic suppression is correctly configured in the inbound direction of the interface.
   
   
   * Run the [**display storm suppression**](cmdqueryname=display+storm+suppression) { ****broadcast**** | ****multicast**** | ****unknown-unicast**** } [ **interface** *interface-type* *interface-number* ] command in any view to check traffic suppression information, or run the [**display this**](cmdqueryname=display+this) command in the interface view to check the traffic suppression configuration of the interface.
     1. Check whether traffic suppression is configured for the corresponding type of packets.
     2. Check whether the traffic suppression threshold is high.
        + If the traffic suppression threshold is high, run the [**storm suppression**](cmdqueryname=storm+suppression) { **broadcast** | **multicast** | **unknown-unicast** } { *percent-value* | **cir** *cir-value* [ **gbps** | **kbps** | **mbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] | ****packets**** **packets-per-second** } command in the interface view to modify traffic suppression parameters.
        + If the traffic suppression threshold is within a reasonable range, go to the next step.
2. Check whether packets are discarded in the inbound direction of the interface using either of the following methods:
   
   
   * Run the [**display interface**](cmdqueryname=display+interface) *interface-type interface-number* command in the user view to check whether the value of output bandwidth utilization changes significantly after traffic suppression is configured. Normally, after traffic suppression is configured, the bandwidth utilization on an interface decreases if the interface discards excess packets once the threshold is reached. If the bandwidth utilization does not change or changes only slightly, go to the next step.
   * Add another interface (interface B) to the same VLAN as the interface that is configured with traffic suppression (interface A). Then check whether the volume of the outgoing traffic on interface B is the same as the volume of the traffic on interface A. If they differ, packets are not discarded in the inbound direction of interface A. In this case, go to the next step.
3. Collect the following information and contact technical support personnel:
   
   
   * Results of the preceding troubleshooting procedure
   * Configuration, log, and trap information