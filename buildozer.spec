[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Android API to target
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version to use
android.build_tools_version = 33.0.0

# (str) Permissions
android.permissions = INTERNET
