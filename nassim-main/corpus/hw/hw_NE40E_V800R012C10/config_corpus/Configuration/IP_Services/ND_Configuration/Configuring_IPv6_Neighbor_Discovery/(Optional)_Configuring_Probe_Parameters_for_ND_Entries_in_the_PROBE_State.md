(Optional) Configuring Probe Parameters for ND Entries in the PROBE State
=========================================================================

This section describes how to configure probe parameters for ND entries in the PROBE state to enhance probe reliability.

#### Context

If an ND entry is in the PROBE state, the reachability of a neighbor is unknown. In this case, the device sends unicast NS messages to detect the validity of the ND entry. Then, if a response is received from the neighbor, the ND entry enters the REACH state, indicating that the neighbor is known to have been reachable. However, if no response is received from the neighbor, the ND entry is deleted.

You are advised to set probe parameters to larger values for ND entries in the PROBE state in the following situations:

* The link reliability on the network is poor, and packet loss may occur during packet transmission.
* The peer device is busy processing services and cannot process NS messages in time.

This prevents ND entries from being mistakenly deleted, negatively affecting packet forwarding efficiency if no response is received from the neighbor within the specified period (calculated as Default number of probe retransmissions x Default interval of probe retransmissions).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled for the interface.
4. Run [**ipv6 nd nud attempts**](cmdqueryname=ipv6+nd+nud+attempts) *attempts*
   
   
   
   The number of probe retransmissions is set for ND entries in the PROBE state.
5. Run [**ipv6 nd nud interval**](cmdqueryname=ipv6+nd+nud+interval) *interval*
   
   
   
   A probe interval is set for ND entries in the PROBE state.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.