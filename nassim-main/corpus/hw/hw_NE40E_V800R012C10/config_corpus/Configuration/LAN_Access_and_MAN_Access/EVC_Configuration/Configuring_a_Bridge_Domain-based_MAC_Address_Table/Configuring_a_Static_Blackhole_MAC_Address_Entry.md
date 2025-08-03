Configuring a Static Blackhole MAC Address Entry
================================================

To prevent invalid MAC address entries (unauthorized users, for example) from using the MAC address table space and prevent hackers from attacking a device or network using forged MAC addresses, configure MAC addresses of untrusted users as blackhole MAC addresses. A device discards packets destined for static blackhole MAC addresses.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address blackhole**](cmdqueryname=mac-address+blackhole) *mac-address* **bridge-domain** *bd-id*
   
   
   
   A static blackhole MAC entry based on a bridge domain is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.