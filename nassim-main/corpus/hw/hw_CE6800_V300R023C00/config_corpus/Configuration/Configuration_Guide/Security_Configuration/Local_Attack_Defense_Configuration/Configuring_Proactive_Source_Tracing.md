Configuring Proactive Source Tracing
====================================

Configuring Proactive Source Tracing

#### Context

You can configure proactive source tracing to record attack traffic on a device, facilitating attack analysis and defense.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an attack defense policy and enter the attack defense policy view.
   
   
   ```
   [cpu-defend policy](cmdqueryname=cpu-defend+policy) policy-name
   ```
3. Enable proactive source tracing
   
   
   ```
   [auto-source-trace enable](cmdqueryname=auto-source-trace+enable)
   ```
   
   By default, proactive source tracing is enabled.
4. Configure the packet sampling ratio for proactive source tracing.
   
   
   ```
   [auto-source-trace sample](cmdqueryname=auto-source-trace+sample) sample-value
   ```
   
   By default, the packet sampling ratio for proactive source tracing is 16. That is, one packet is sampled in every 16 packets.
5. Configure the packet sampling interval for proactive source tracing.
   
   
   ```
   [auto-source-trace statistics interval](cmdqueryname=auto-source-trace+statistics+interval) interval-value
   ```
   
   By default, the packet sampling interval for proactive source tracing is 10 seconds.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Apply the attack defense policy.
   
   
   * Configure attack defense policies in batches.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name batch slot { start-slot [ to end-slot ] } &<1-12>
     ```
   * Configure an attack defense policy separately.
     ```
     [cpu-defend-policy](cmdqueryname=cpu-defend-policy) policy-name [ slot slot-id ]
     ```
   
   After an attack defense policy is created, you must apply the policy in the system view. Otherwise, the policy does not take effect.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display auto-source-trace record**](cmdqueryname=display+auto-source-trace+record) [ **packet** { **arp-request** | **arp-request-uc** | **arp-reply** | **nd** } ] [ **slot** *slot-id* ] command to check statistics about proactive source tracing.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL in low latency mode does not support nd.