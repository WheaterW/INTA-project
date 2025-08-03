Configuring Invalid-ND-Packet Attack Defense
============================================

Configuring Invalid-ND-Packet Attack Defense

#### Usage Scenario

Invalid-ND-packet attack defense is implemented by filtering out six types of invalid ND packets (NS/NA/RS/RA/Redirect/CPS) to protect the CPU.

In VS mode, this feature is supported only by the admin VS.


#### Prerequisites

None


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**set nd packet filter enable**](cmdqueryname=set+nd+packet+filter+enable) command to enable invalid-ND-packet attack defense.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display nd packet filter statistics**](cmdqueryname=display+nd+packet+filter+statistics) [ **slot** *slot-id* ] command to check statistics about invalid-ND-packet attack defense.