Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the **[**display cpu-defend policy**](cmdqueryname=display+cpu-defend+policy)** [ *policy-name* ] command to check the attack defense policy configuration.
* Run the [**display auto-defend attack-source**](cmdqueryname=display+auto-defend+attack-source) [ **slot** *slot-id* | **history** [ **slot** *slot-id* ] | **trace-type** { **source-mac** | **source-ip** | **source-portvlan** } [ **slot** *slot-id* ] ] command to check attack source information.
* Run the [**display auto-defend configuration**](cmdqueryname=display+auto-defend+configuration) [ **cpu-defend policy** *policy-name* | **slot** *slot-id* ] command to check the configuration of attack source tracing in the attack defense policy.
* Run the [**display auto-defend whitelist**](cmdqueryname=display+auto-defend+whitelist) **slot** *slot-id* command to check the whitelist information configured for attack source tracing.