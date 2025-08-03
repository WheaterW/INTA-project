Enabling LDP GR
===============

Enable LDP GR on both the GR Restarter and its neighboring nodes

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   LDP is enabled on the local LSR, and the MPLS-LDP view is displayed.
3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
   
   
   
   LDP GR is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * Enabling or disabling LDP GR causes an LDP session to be reestablished. If LDP sessions do not need to be reestablished when LDP GR is enabled or disabled, run the [**no-renegotiate session-parameter-change graceful-restart**](cmdqueryname=no-renegotiate+session-parameter-change+graceful-restart) command.
   * Enabling or disabling LDP GR causes an LDP session to be reestablished.
   * The [**undo mpls ldp**](cmdqueryname=undo+mpls+ldp) and [**reset mpls ldp**](cmdqueryname=reset+mpls+ldp) commands cannot be run during LDP GR.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configurations are committed.