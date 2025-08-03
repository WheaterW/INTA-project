Dynamic Domain Name Resolution Cannot Be Implemented on a Device
================================================================

Dynamic Domain Name Resolution Cannot Be Implemented on a Device

#### Fault Symptom

The device functions as a DNS client that is configured with dynamic domain name resolution but is unable to resolve a domain name to a correct IP address.


#### Procedure

1. Run the [**display dns dynamic-host**](cmdqueryname=display+dns+dynamic-host) command check whether the specified domain name exists in the cache.
   
   
   * If the specified domain name does not exist, check whether the DNS client is communicating with the DNS server properly, whether the DNS server is running properly, and whether dynamic domain name resolution is enabled.
   * If the specified domain name exists but the IP address is incorrect, go to Step 2.
2. Run the [**display dns server**](cmdqueryname=display+dns+server) command to check whether the DNS server IP address configured on the DNS client is correct.
   
   
   
   If the DNS server IP address is incorrect, run the [**undo dns server**](cmdqueryname=undo+dns+server) *ip-address* command to delete the configured DNS server IP address, and run the [**dns server**](cmdqueryname=dns+server) *ip-address* command to reconfigure a correct one.