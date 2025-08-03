(Optional) Enabling Enhanced M-LAG Layer 3 Forwarding
=====================================================

(Optional) Enabling Enhanced M-LAG Layer 3 Forwarding

#### Context

To speed up convergence when an M-LAG member interface fails, you can enable enhanced M-LAG Layer 3 forwarding so that backup FRR resources are requested for all ARP and ND entries with M-LAG member interfaces as outbound interfaces, or enable enhanced M-LAG route convergence so that backup FRR resources are requested for all routing entries with M-LAG member interfaces as outbound interfaces. Active and standby paths are established for traffic forwarding on downlink outbound interfaces. If an M-LAG member interface fails, the outbound interface can be quickly changed to a peer-link interface.

For the CE6885-LL (low latency mode): IPv6-related configurations are not supported.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable enhanced M-LAG Layer 3 forwarding.
   
   
   
   For the CE6866, CE6860-SAN, CE6860-HAM, CE6866K, CE8851-32CQ8DQ-P, CE8850-SAN, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6885-SAN, CE6885-LL (low latency mode), CE6863E-48S8CQ:
   
   ```
   [undo m-lag forward layer-3](cmdqueryname=undo+m-lag+forward+layer-3) enhanced disable
   ```
   
   
   
   For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   
   
   ```
   [m-lag forward layer-3](cmdqueryname=m-lag+forward+layer-3) enhanced enable
   ```
3. (Optional) Enable enhanced M-LAG route convergence in IPv4 or IPv6 scenarios.
   
   
   ```
   [m-lag forward route convergence enhanced enable](cmdqueryname=m-lag+forward+route+convergence+enhanced+enable)
   ```
   
   Enhanced M-LAG route convergence is supported only by the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```