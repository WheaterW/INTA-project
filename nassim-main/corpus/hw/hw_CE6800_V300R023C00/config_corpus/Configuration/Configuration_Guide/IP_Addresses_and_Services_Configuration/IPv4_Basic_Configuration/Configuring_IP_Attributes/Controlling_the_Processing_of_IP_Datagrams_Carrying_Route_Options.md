Controlling the Processing of IP Datagrams Carrying Route Options
=================================================================

Controlling the Processing of IP Datagrams Carrying Route Options

#### Context

IP datagrams can carry route options, including the Router Alert, Record Route, Source Route, and Timestamp options. Generally, these options are used for diagnosing network paths and temporarily transmitting special services. These options may also be used by attackers to ascertain the network structure and launch attacks. By default, devices process IP datagrams carrying route options. To prevent attacks from IP datagrams carrying route options, disable the system from processing such datagrams.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Perform the following operations for different route options in IP datagrams.
   
   
   
   **Table 1** Operations for different route options in IP datagrams
   | Operation | Command | Description |
   | --- | --- | --- |
   | Disable the system from processing IP datagrams carrying the Router Alert option. | [**ip option route-alert disable**](cmdqueryname=ip+option+route-alert+disable) | By default, devices process IP datagrams carrying the Router Alert option. To prevent attacks from IP datagrams carrying the Router Alert option, disable the system from processing such datagrams. |
   | Disable the system from processing IP datagrams carrying the Record Route option. | [**ip option route-record disable**](cmdqueryname=ip+option+route-record+disable) | By default, devices process IP datagrams carrying the Record Route option. To prevent attacks from IP datagrams carrying the Record Route option, disable the system from processing such datagrams. |
   | Disable the system from processing IP datagrams carrying the Source Route option. | [**ip option source-route disable**](cmdqueryname=ip+option+source-route+disable) | By default, devices process IP datagrams carrying the Source Route option. To prevent attacks from IP datagrams carrying the Source Route option, disable the system from processing such datagrams. |
   | Disable the system from processing IP datagrams carrying the Timestamp option. | [**ip option time-stamp disable**](cmdqueryname=ip+option+time-stamp+disable) | By default, devices process IP datagrams carrying the Timestamp option. To prevent attacks from IP datagrams carrying the Timestamp option, disable the system from processing such datagrams. |
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```