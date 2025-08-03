Configuring Probe Parameters for ND Entries in the PROBE State
==============================================================

Configuring Probe Parameters for ND Entries in the PROBE State

#### Context

If an ND entry is in the PROBE state, the reachability of a neighbor is unknown. In this case, the device sends unicast NS messages to detect the validity of the ND entry. Then, if a response is received from the neighbor, the ND entry enters the REACH state, indicating that the neighbor is known to have been reachable. However, if no response is received from the neighbor, the ND entry is deleted.

You are advised to set probe parameters to larger values for ND entries in the PROBE state in the following situations:

* The link reliability on the network is poor, and packet loss may occur during packet transmission.
* The peer device is busy processing services and cannot process NS messages in time.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure the maximum number of probe attempts for ND entries in the PROBE state.
   
   
   ```
   [ipv6 nd nud attempts](cmdqueryname=ipv6+nd+nud+attempts) attempts
   ```
6. Configure a probe interval for ND entries in the PROBE state.
   
   
   ```
   [ipv6 nd nud interval](cmdqueryname=ipv6+nd+nud+interval) interval
   ```
   
   
   By default:
   * If the [**ipv6 nd ns retrans-timer**](cmdqueryname=ipv6+nd+ns+retrans-timer) command has been run, the probe interval for ND entries in the PROBE state is the interval configured using this command.
   * If the [**ipv6 nd ns retrans-timer**](cmdqueryname=ipv6+nd+ns+retrans-timer) command is not run, the probe interval for ND entries in the PROBE state is 1000 ms.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```