Configuring the Command-Line Recording Scheme
=============================================

Before configuring the command-line recording scheme, you
must configure the HWTACACS server template.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**recording-scheme**](cmdqueryname=recording-scheme) *recording-scheme-name*
   
   
   
   The recording
   scheme is created, and the recording scheme view is displayed.
4. Run [**recording-mode**](cmdqueryname=recording-mode) **hwtacacs** *template-name*
   
   
   
   The HWTACACS server template associated with the recording
   scheme is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   The AAA view is displayed.
6. Run [**cmd recording-scheme**](cmdqueryname=cmd+recording-scheme) *recording-scheme-name*
   
   
   
   The command-line
   recording scheme is configured for the user.
7. Run [**system recording-scheme**](cmdqueryname=system+recording-scheme) *recording-scheme-name*
   
   
   
   The recording
   scheme sets are set on the device.
8. Run [**outbound recording-scheme**](cmdqueryname=outbound+recording-scheme) *recording-scheme-name*
   
   
   
   An outbound
   recording scheme in which the remote login operations of the device
   that functions as the client are recorded.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.