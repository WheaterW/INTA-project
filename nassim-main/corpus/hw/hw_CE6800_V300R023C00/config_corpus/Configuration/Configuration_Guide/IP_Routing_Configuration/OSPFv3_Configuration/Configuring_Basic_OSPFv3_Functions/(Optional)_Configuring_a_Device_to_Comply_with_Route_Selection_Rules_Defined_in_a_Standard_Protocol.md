(Optional) Configuring a Device to Comply with Route Selection Rules Defined in a Standard Protocol
===================================================================================================

(Optional) Configuring a Device to Comply with Route Selection Rules Defined in a Standard Protocol

#### Context

RFC 5340 and RFC 1583 define route selection rules differently. After enabling OSPFv3 on a device, you can configure the device to comply with route selection rules defined in either standard protocol as required. By default, a device complies with the route selection rules defined in RFC 5340. If you want the device to comply with the other protocol, you need to configure the device to comply with the rules defined in RFC 1583. Such configurations ensure that all OSPFv3-enabled devices in an AS comply with the same route selection rules defined in the same standard protocol.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the OSPFv3 view.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) process-id [ vpn-instance vpn-instance-name ]
   ```
3. Configure the device to comply with the route selection rules defined in RFC 1583, rather than RFC 5340.
   
   
   ```
   [rfc1583 compatible](cmdqueryname=rfc1583+compatible)
   ```
   
   By default, a device complies with the route selection rules defined in RFC 5340.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```