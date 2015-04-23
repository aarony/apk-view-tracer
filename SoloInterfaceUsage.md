#Usage of Solo Interface for Automation testing and Dynamic analysis.

# Introduction #

All functions of Solo Class.


# Details #

**class** **SoloInterface**

# _Constructor Method_

**init**(self, device\_name='emulator-5554', device\_port=5554, device\_address='127.0.0.1')


**appendEditTextById**(self, id, text)

**assertCurrentActivity**(self, expectedClassName)

**assertCurrentActivityNewInstance**(self, expectedClassName, oldHashCode)

**callDelete**(self, reDump=False)

**callDown**(self, reDump=False)

**callLeft**(self, reDump=False)

**callMenu**(self)

**callNotification**(self)

**callRight**(self, reDump=False)

**callUp**(self, reDump=False)

**clearAllNotifications**(self, reDump=False)

**clearEditTextById**(self, id)

**clickInPopupById**(self, id)

**clickInPopupByText**(self, text, partial\_matching=True)

**clickItemByIndex**(self, groupview\_id, index=0)

**clickItemByText**(self, groupview\_id, text, partial\_matching=True)

**clickMenuItemById**(self, id)

**clickMenuItemByText**(self, text, partial\_matching=True)

**clickNotificationItemByText**(self, text, partial\_matching=True)

**clickViewById**(self, id, ReDump=True)

**clickViewByText**(self, text, partial\_matching=True)

**close**(self)

**existViewByClassName**(self, class\_name)

**existViewById**(self, id)

**existViewByText**(self, text, partial\_matching=True)

**getCurrentProgress**(self)

**getCurrentViewClassName**(self)

**getItemsNumber**(self, groupview\_id, groupview\_classname=None)

**getProgressById**(self, id)

**getProgressByText**(self, text, partial\_matching=True)

**getTextById**(self, id)

**goBack**(self, ReDump=True)

**installPackage**(self, package\_name)

**isCheckedById**(self, id)

**isCheckedByText**(self, text, partial\_matching=True)

**isItemCheckedByIndex**(self, groupview\_id, index=0)

**isItemCheckedByText**(self, groupview\_id, text, partial\_matching=True)

**isViewType**(self, class\_name, view\_name\_list)

**isVisibleById**(self, id)

**longPressByText**(self, text, partial\_matching=True)

**longPressHome**(self)

**pressHome**(self)

**pullFile(self, device\_path, local\_path)**

**pushFile**(self, local\_path, device\_path)

**removePackage**(self, package\_name)

**searchForText**(self, text, partial\_matching=True)

**searchForViewClassName**(self, class\_name)

**searchForViewID**(self, id)

**selectInHorizontalPopupByText**(self, text, partial\_matching=True)

**selectInVerticalPopupByText**(self, text, partial\_matching=True)

**setEditTextById**(self, id, text)

**setUp**(self)

**shell**(self, command)

**shellForResult**(self, command)

**startActivity**(self, uri=None, action=None, data=None, mimetype=None, categories\_list=None, component=None, flags\_list=None, extras\_list=None)

**tearDown**(self)

**typeInPopupByIndex**(self, text, index=0)
