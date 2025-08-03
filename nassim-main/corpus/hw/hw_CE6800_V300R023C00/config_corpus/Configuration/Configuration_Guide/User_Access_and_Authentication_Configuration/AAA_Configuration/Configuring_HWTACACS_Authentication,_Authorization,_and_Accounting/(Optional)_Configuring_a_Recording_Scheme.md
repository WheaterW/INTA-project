(Optional) Configuring a Recording Scheme
=========================================

(Optional) Configuring a Recording Scheme

#### Context

Incorrect operations performed during device configuration may result in network faults. When HWTACACS authentication and authorization are used, you can record related configuration information on the HWTACACS server. This information facilitates subsequent troubleshooting.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create a recording scheme and enter the recording scheme view.
   
   
   ```
   [recording-scheme](cmdqueryname=recording-scheme) recording-scheme-name
   ```
4. Associate the recording scheme with an HWTACACS server template.
   
   
   ```
   [recording-mode hwtacacs](cmdqueryname=recording-mode+hwtacacs) template-name
   ```
5. Return to the AAA view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Configure a recording policy for the recording scheme, and record the commands that have been executed on the device.
   
   
   
   **Table 1** Configuring a recording policy for the recording scheme
   | Operation | Command | Description |
   | --- | --- | --- |
   | Record the commands that have been executed on the device. | [**cmd recording-scheme**](cmdqueryname=cmd+recording-scheme) *recording-scheme-name* | By default, no recording policy is configured for a recording scheme. |
   | Record connection information. | [**outbound recording-scheme**](cmdqueryname=outbound+recording-scheme) *recording-scheme-name* |
   | Record system-level events. | [**system recording-scheme**](cmdqueryname=system+recording-scheme) *recording-scheme-name* |
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```