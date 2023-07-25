#Python Dont Miss Live

Introduction

Dont Miss Live is a convenient command-line tool designed for users who are often away from their computers and need to access live game streams that offer in-game rewards (drops).
How it Works

Dont Miss Live allows you to specify a link and a scheduled time. When the scheduled time matches the local time of your computer, the link will automatically open in your default web browser. This enables you to log into game streams and claim any drops or rewards without needing to be  at your computer when the live starts.
##Usage

    Run the Python program and provide the link you want to open.
    Enter the scheduled time for the link to be opened.
    Optionally, specify your preferred web browser to open the link (leave blank for default).
    The program will continuously check the current time, and when the scheduled time is reached, it will open the link in the selected web browser.

Getting Started

To get started with Dont Miss Live, follow these steps:

    Download the repository.
    Open the terminal in the project directory:


```shell
$ git clone https://github.com/sartori96/dont_miss_live.git
$ cd dont_miss_live
```
##How to Install

Enter the following commands:

```shell

$ python -m venv venv
$ source venv/bin/activate  # For Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```
##How to Use

To use Dont Miss Live, run the following command:

```shell

$ python dont_miss_live.py
```
The program will prompt you to input the link and the scheduled time for the live stream. You can also specify your preferred web browser to open the link.

Example:

```shell

Enter the link you want to open: https://www.example.com/live-stream
Enter the time in format HH:MM (e.g., 09:30): 15:00
Enter the browser you want to use (leave blank for default): chrome
Link will open at 15:00. Don't miss the live stream!
```
Enjoy the convenience of automatically accessing game streams and claiming rewards without being physically present. Don't miss out on any exciting in-game rewards!