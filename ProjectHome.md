<h1><b>Introduction</b></h1>

Apk-view-tracer is a trigger tool for Android Dynamic Analysis and it can be used in android anti-virus dynamic analysis.

Also it provides a group open-API for developer. It can trace Apk view without source code. <if you have source code, it must be work better>. So it also can be used in black-box testing of Android Development.

It is based on tracing apk view, and it implement two functions for Android development :

1. It provides apk automated testing interface.


2. It provides a event trigger tool for apk dynamic analysis.

<h1><b>Component</b></h1>

ApkViewTracer contains 5 components:

1. DeviceManagement

2. SystemComponent

3. ViewManagement

4. ViewController

5. SoloInterface

<h1><b>User Guide</b></h1>

a simple example as below:


_**import SoloInterface**_

_**solo = SoloInterface()**_

_**solo.setUp()**_

_**solo.clickViewById("btn\_login")**_

_**if solo.searchForText("Accept"):**_

> _**solo.clickViewByText("Accept")**_

_**solo.close()**_

<h1><b>Advantage</b></h1>

As you know, Robotium can provide API for testing, but it need that you have source code of the android application. If not, you can not do anything. And if the application has sign-protect, and you can not crack the protect, then it does not work any more.

Apk-view-tracer runs without source code and it can implement most requirements you want.

This project now is a python module. You can use it by importing the module named "SoloInterface". You can download the source code package from download page.


<h1><b>API Documents</b></h1>

see: <h3><a href='http://apk-view-tracer.googlecode.com/hg/SoloInterface.html'>API Document of Solo Interface for Automation testing and Dynamic analysis</a></h3>