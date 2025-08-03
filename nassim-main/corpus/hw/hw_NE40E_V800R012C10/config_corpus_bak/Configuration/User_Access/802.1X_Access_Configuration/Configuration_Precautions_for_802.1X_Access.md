Configuration Precautions for 802.1X Access
===========================================

Configuration_Precautions_for_802.1X_Access

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Local authentication cannot be configured for MAC authentication users.  Configuring local authentication for MAC address authentication users is not recommended. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In 802.1X user access scenarios, if the user name contains a backslash (\), the part before the backslash (\) is parsed as the domain name, whereas that after the backslash (\) is parsed as the pure user name. The user name is re-encapsulated based on a domain name delimiter. For example, if the at sign (@) is specified as the domain name delimiter, the user name in the format of "a\b" is changed to "b@a" after the user goes online. Properly plan EAP user names. If a backslash (\) is required in a user name, ensure that the domain name is before the backslash and the pure user name is after the backslash. Otherwise, communication between EAP users and the RADIUS server is affected. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Among physical interfaces, 40GE interfaces (interface 40GE x/x/x or interface 40GE x/x/x/x) do not support BRAS access. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Among physical interfaces, 40GE interfaces (interface 40GE x/x/x or interface 40GE x/x/x/x) do not support BRAS access. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |