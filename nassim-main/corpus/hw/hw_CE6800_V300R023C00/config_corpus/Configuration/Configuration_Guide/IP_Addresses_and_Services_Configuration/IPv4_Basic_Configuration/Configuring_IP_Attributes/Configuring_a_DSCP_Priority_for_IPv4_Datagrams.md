Configuring a DSCP Priority for IPv4 Datagrams
==============================================

Configuring a DSCP Priority for IPv4 Datagrams

#### Context

The differentiated services code point (DSCP) is contained in the ToS field in an IP header. This field consists of six most significant bits and two currently unused bits, and the eight bits are used to form codes for marking priorities. The first three bits of the ToS field are defined as the IP precedence, which can be divided into eight priorities. This is sufficient in a scenario with a single service type and low service volume. However, in actual network deployment, the eight priorities are far from enough. Therefore, the ToS field is redefined. The first six bits are defined as the DSCP, and the last two bits are reserved. In this way, the DSCP priority ranges from 0 to 63. During network planning and deployment, if the DSCP priority of a device is determined, you can configure the device to send protocol datagrams carrying this DSCP priority. After the downstream device receives the protocol datagrams, it can schedule the datagrams into different queues based on the DSCP priorities in the datagrams. This allows datagrams sent from devices with higher DSCP priorities to be scheduled preferentially.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a DSCP priority for datagrams.
   
   
   ```
   [set priority dscp](cmdqueryname=set+priority+dscp) dscp-value
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```