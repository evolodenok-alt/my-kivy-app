name: Build APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04
    timeout-minutes: 90
    env:
      JAVA_HOME: /usr/lib/jvm/java-17-openjdk-amd64
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev build-essential ccache
          pip install --upgrade pip
          pip install buildozer "cython<3" virtualenv

      - name: Build APK
        run: |
          export PATH=$JAVA_HOME/bin:$PATH
          java -version
          buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: app-debug-apk
          path: bin/*.apk
