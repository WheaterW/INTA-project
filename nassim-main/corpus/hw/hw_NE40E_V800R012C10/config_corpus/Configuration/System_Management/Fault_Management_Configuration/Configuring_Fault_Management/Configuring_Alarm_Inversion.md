Configuring Alarm Inversion
===========================

If you do not want an interface to generate loss alarms for services that have been deployed but not accessed, configure alarm inversion.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**reverse mode auto-resume**](cmdqueryname=reverse+mode+auto-resume) command to set the alarm inversion mode to automatic recovery.
4. Run the [**reverse**](cmdqueryname=reverse) command to enter the alarm inversion view.
5. Run the [**reverse interface**](cmdqueryname=reverse+interface) *interface-type* *interface-number* command to enable alarm inversion on an interface.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.