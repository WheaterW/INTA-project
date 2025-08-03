NTP Authentication Does Not Take Effect
=======================================

NTP Authentication Does Not Take Effect

#### Fault Symptom

The NTP authentication function does not take effect. Clock synchronization can be performed even when the server or client is invalid (for example, the keys on the server and client are inconsistent).


#### Possible Causes

NTP authentication is not configured before basic NTP functions are configured.


#### Procedure

1. Clear configurations of the basic NTP functions.
2. Enable NTP authentication.
3. Configure basic NTP functions.