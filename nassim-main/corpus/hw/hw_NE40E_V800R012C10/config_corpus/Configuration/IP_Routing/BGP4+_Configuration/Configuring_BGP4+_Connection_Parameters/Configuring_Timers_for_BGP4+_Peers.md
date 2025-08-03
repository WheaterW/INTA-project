Configuring Timers for BGP4+ Peers
==================================

Configuring timers properly improves network performance. Changing BGP4+ timer values, however, will interrupt peer relationships.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Changing timer values using the [**peer timer**](cmdqueryname=peer+timer) command will interrupt peer relationships between Routers. Therefore, exercise caution when changing the timeout period of a timer.

Perform the following steps on a BGP4+ device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run the [**peer**](cmdqueryname=peer+timer+keepalive+hold+min-holdtime) { *ipv6-address* | *group-name* } **timer** **keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ] command to configure the interval at which Keepalive messages are sent and the hold time for a peer or peer group. Alternatively, run the [**peer**](cmdqueryname=peer) *ipv6-address* [**timer**](cmdqueryname=timer+send-hold) **send-hold** *send-hold-time* command to configure the hold time during which a peer does not proactively disconnect from the peer end.
   
   
   
   The value of *hold-time* must be at least three times the value of *keepalive-time*.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to configure *hold-time* according to the total number of peers in all BGP address families. The more peers, the larger the recommended minimum hold time value. You can adjust the hold time based on [Table 1](dc_vrp_bgp_cfg_3047.html#EN-US_TASK_0172366221__table410763711163).
   
   
   
   **Table 1** Mapping between the total number of BGP peers in all address families and the recommended minimum hold time
   | Total Number of Peers | Recommended Minimum Hold Time |
   | --- | --- |
   | 0â100 | 20s |
   | 101â200 | 30s |
   | 201â300 | 45s |
   | 301â400 | 60s |
   | 401â500 | 75s |
   | Greater than or equal to 501 | 90s |
   
   Avoid the following situations when setting values for the three timers:
   
   * The values of *keepalive-time* and *hold-time* are both set to 0. In this case, the BGP timers become invalid, and BGP cannot detect link faults based on the timers.
   * The *hold-time* value is much greater than the *keepalive-time* value, for example, **timer keepalive 1 hold 65535** is configured. In this case, link faults cannot be detected in time.
   * The *keepalive-time* value is set to 0. In this case, the keepalive timer does not start. As a result, the *send-hold-time* function does not take effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.