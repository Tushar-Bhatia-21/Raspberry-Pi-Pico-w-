👋 Hi, Welcome to Raspberry Pi Pico W devlopment using C/C++/ASM guide.

It is recommended to check out Starting Doc before following this guide.

This guide assumes that you are a beginner and will take extreme care to provide you the best experience of learning.

    Happy Coding😀

###############################################################

<b>For Windows.</b>
There are multiple options available for you to download the resources and SDK for the Pico/Pico W.

It is my recommendation to download pico-setup using the following link as it automates most of the setup process and saves a lot of time.

https://github.com/ndabas/pico-setup-windows/releases

Download the pico-setup-windowsx64 or x86 depending upon your system architecture. For Modern Windows systems, it is assumed that you have 64 bit architecture.
It can be easily checked by the following steps.
1. Open Start menu and click on Settings. 
2. Click on System-->About. See the architecture of your processor.
3. Download the Setup Accordingly. x32 bit means x86 setup is for you.

<b>Installation</b>

1.Click on Next.

![image](https://user-images.githubusercontent.com/113343003/210052856-d24dbbab-efb3-4050-bf1a-8219a72806c7.png)

2.All components are selected automatically, if you have any previously installed component it is recommend to Uncheck that component.

![image](https://user-images.githubusercontent.com/113343003/210052976-1f64528c-3413-4537-9d3f-b844123b655f.png)

3. Select location, it is recommended to install in default windows directory.

4. Click on Install and run VSCODE.

<b>VSCODE-SETUP</b>

All the required components are now installed on your system.

1. Press Ctrl+Shift+X. Extensions Market will now be opened on your system.
2. Search for C/C++ extension by microsoft and install if not installed.
3. Do the same for CMAKE extension, CMAKE tools extensions.
4. If each extension is installed <b>Congratulations</b>, now you can start devlopment.

<b>Now it is recommended to check out Build SDK using CMAKE</b>

<b>For MAC Systems</b>

To help us in devlopment and ease our installation process, we are going to download Homebrew.

1. Download and install Homebrew using the following command or by the following link.
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   https://brew.sh/
2. Copy the above command and open Terminal. To open terminal use the following link.
   https://support.apple.com/en-in/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac#:~:text=Terminal%20for%20me-,Open%20Terminal,%2C%20then%20double%2Dclick%20Terminal.
 
<b>Installing Toolchain</b>

    To install the toolchain write the following commmands in the terminal.
    $ brew install cmake
    $ brew tap ArmMbed/homebrew-formulae
    $ brew install arm-none-eabi-gcc

<b>If you are using Apple M1-based Mac you will need to install Rosetta 2 as the Arm compiler is still only compiled for x86 processors and does not have an Arm native version</b>

    To do the above, paste the following command in homebrew.
    $ /usr/sbin/softwareupdate --install-rosetta --agree-to-license

If you have followed the above steps, the toolchain is now installed.

<b>VSCODE SETUP</b>

1. Download and install Vscode using the following link.
```    https://code.visualstudio.com/download
```
2. 
