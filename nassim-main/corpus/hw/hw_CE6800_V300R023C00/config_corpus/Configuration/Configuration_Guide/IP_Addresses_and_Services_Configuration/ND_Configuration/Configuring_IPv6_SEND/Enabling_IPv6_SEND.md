Enabling IPv6 SEND
==================

Enabling IPv6 SEND

#### Context

After the following settings are configured, the system considers the received ND messages that do not comply with these settings as invalid:

* Rate limit for the system to compute or verify the RSA signature in a specified period (1s)
* Key length allowed on an interface
* Timestamp parameters in ND messages

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Set a rate limit for the system to compute or verify the RSA signature in a specified period (1s).
   
   
   ```
   [ipv6 nd security rate-limit](cmdqueryname=ipv6+nd+security+rate-limit) ratelimit-value
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
5. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. (Optional) Set the key length allowed on the interface.
   
   
   ```
   [ipv6 nd security key-length](cmdqueryname=ipv6+nd+security+key-length) { minimum mini-keylen-value | maximum max-keylen-value } *
   ```
7. (Optional) Set timestamp parameters for ND messages.
   
   
   ```
   [ipv6 nd security timestamp](cmdqueryname=ipv6+nd+security+timestamp) { delta delta-value | drift drift-value | fuzz-factor fuzz-value } *
   ```
8. Enable the strict security mode on the interface.
   
   
   ```
   [ipv6 nd security strict](cmdqueryname=ipv6+nd+security+strict)
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```