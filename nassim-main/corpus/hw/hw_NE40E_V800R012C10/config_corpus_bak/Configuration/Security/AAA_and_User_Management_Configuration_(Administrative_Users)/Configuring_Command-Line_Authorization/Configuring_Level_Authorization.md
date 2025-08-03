Configuring Level Authorization
===============================

Configuring level authorization involves configuring the level authorization mode, adjusting the level of the user or command line, and configuring the user level promotion authentication mode.

#### Context

Configuring level authorization involves the following configurations:

* [Configuring the level authorization mode](#EN-US_TASK_0172371821__dc_vrp_aaa_cfg_101101)
  
  Level authorization is classified into local authorization and remote HWTACACS authorization.
* [Adjusting the level of the command line](#EN-US_TASK_0172371821__dc_vrp_aaa_cfg_101102)
  
  The user can customize the level of the command line.

#### Procedure

* Configure the level authorization mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
     
     
     
     The authorization scheme view is displayed.
  4. Run **authorization-cmd** [ *privilege-level* ] *mode1* [ *mode2* ]
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Adjust the level of the command line.
  
  
  
  For how to adjust the command line level, see Configuring Command Levels.