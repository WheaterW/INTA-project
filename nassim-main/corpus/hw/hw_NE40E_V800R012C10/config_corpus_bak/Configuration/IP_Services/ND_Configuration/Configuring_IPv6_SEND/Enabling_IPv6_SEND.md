Enabling IPv6 SEND
==================

After a rate limit for the system to compute or verify the RSA signature in a specified period (1s), the key length allowed on an interface, and timestamp parameters in ND messages are set, the system considers the received ND messages that do not comply with these settings invalid.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ipv6 nd security rate-limit**](cmdqueryname=ipv6+nd+security+rate-limit) *ratelimit-value*
   
   
   
   A rate limit is set for the system to compute or verify the RSA signature in a specified period (1s).
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled.
5. (Optional) Run [**ipv6 nd security key-length**](cmdqueryname=ipv6+nd+security+key-length) { **minimum** *mini-keylen-value* | **maximum** *max-keylen-value* } \*
   
   
   
   The key length allowed on the interface is set.
6. (Optional) Run [**ipv6 nd security timestamp**](cmdqueryname=ipv6+nd+security+timestamp) { **fuzz-factor** *fuzz-value* | **delta** *delta-value* | **drift** *drift-value* } \*
   
   
   
   Timestamp parameters are set for ND messages.
7. Run [**ipv6 nd security strict**](cmdqueryname=ipv6+nd+security+strict)
   
   
   
   The strict security mode is enabled on the interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.