Configuring an RD Filter
========================

Configuring an RD Filter

#### Context

An RD filter is used to filter BGP routes based on RDs contained in VPN routes. RDs are used to distinguish IPv4 or IPv6 prefixes within the same address segment in a VPN instance. RD-specific matching conditions can be configured in an RD filter.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an RD filter.
   
   
   ```
   [ip rd-filter](cmdqueryname=ip+rd-filter) rdfIndex [ index index-number ] matchMode rdStr &<1-10>
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ip rd-filter**](cmdqueryname=display+ip+rd-filter) [ *rd-filter-number* ] command to check information about the configured RD filter.